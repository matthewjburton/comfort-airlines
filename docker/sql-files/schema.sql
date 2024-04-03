/*
Removes all tables from the database and recreates them using the schema below
Also creates a trigger to calculate the total avaialable gates at each airport

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton and Ryan Hirscher

Execute: 
    1. Log into the database: docker exec -it <container name> mariadb -u <username> -p <database name>              
             
        docker exec -it mariadb-container mariadb -u admin -p cloudnine

    2. To execute the populate-aircraft-table.sql file: source <file/path/file_name.sql>
        
        source /docker-entrypoint.initdb.d/schema.sql
*/

-- Disable foreign key checks
SET FOREIGN_KEY_CHECKS = 0;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS flights_routes;
DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS aircraft;
DROP TABLE IF EXISTS airports;

-- Enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Create new tables
CREATE TABLE IF NOT EXISTS airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    abbreviation VARCHAR(3), 
    latitude FLOAT, -- coordinate position
    longitude FLOAT, -- coordinate position
    timezone_offset INT, -- difference in hours from 0 in UTC
    metro_population INT, -- amount of people
    total_gates INT, -- number of gates
    is_hub BINARY -- 1 for hub, 0 for normal airport
);

CREATE TABLE IF NOT EXISTS aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    tail_number VARCHAR(20),
    name VARCHAR(255),
    model VARCHAR(255),
    maximum_speed INT, -- miles per hour
    maximum_capacity INT, -- number of people
    maximum_fuel INT, -- amount in gallons
    cargo_volume INT, -- volume in cubic feet
    leasing_cost INT -- price in USD
);

CREATE TABLE IF NOT EXISTS flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20),
    aircraft_id INT,
    departure_airport_id INT,
    destination_airport_id INT,
    angle_of_flight FLOAT, -- angle from 0 to 360
    flight_duration INT, -- time in minutes
    departure_time INT,  -- time in UTC
    arrival_time INT,  -- time in UTC
    on_time_bin BINARY, -- 0 for on time, 1 for delayed
    gate_departure INT,
    gate_arrival INT,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id),
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id)
);

DELIMITER //
DROP TRIGGER IF EXISTS set_total_gates;
--  Trigger to calculate the total number of gates at each airport
CREATE TRIGGER IF NOT EXISTS set_total_gates
BEFORE INSERT ON airports
FOR EACH ROW
BEGIN
    IF NEW.total_gates IS NULL THEN        
        -- Calculate total gates based on the provided formula
        SET @gates = LEAST(ROUND(NEW.metro_population / 1000000), IF(NEW.is_hub, 11, 5));
        
        -- Set the calculated value to the total_gates column
        SET NEW.total_gates = @gates;
    END IF;
END;
//
DELIMITER ;

DELIMITER //
DROP TRIGGER IF EXISTS set_flight_angle;
-- Trigger to calculate the flight angle based on the departure and destination airports
CREATE TRIGGER IF NOT EXISTS set_flight_angle
BEFORE INSERT ON flights
FOR EACH ROW
BEGIN
    IF NEW.angle_of_flight IS NULL THEN
        SET @departure_lat = (SELECT latitude FROM airports WHERE airport_id = NEW.departure_airport_id);
        SET @departure_lon = (SELECT longitude FROM airports WHERE airport_id = NEW.departure_airport_id);
        SET @destination_lat = (SELECT latitude FROM airports WHERE airport_id = NEW.destination_airport_id);
        SET @destination_lon = (SELECT longitude FROM airports WHERE airport_id = NEW.destination_airport_id);
        SET @bearing_angle = DEGREES(ATAN2(SIN(RADIANS(@destination_lon - @departure_lon)) * COS(RADIANS(@destination_lat)), COS(RADIANS(@departure_lat)) * SIN(RADIANS(@destination_lat)) - SIN(RADIANS(@departure_lat)) * COS(RADIANS(@destination_lat)) * COS(RADIANS(@destination_lon - @departure_lon))));
        
        SET NEW.angle_of_flight = @bearing_angle;
    END IF;
END;
//
DELIMITER ;

/*
DELIMITER //
DROP FUNCTION IF EXISTS calculate_percentage;
CREATE FUNCTION IF NOT EXISTS calculate_percentage(
    @departureLat FLOAT,
    @departureLon FLOAT,
    @destinationLat FLOAT,
    @destinationLon FLOAT
)
RETURNS FLOAT
BEGIN
    DECLARE wind FLOAT DEFAULT 0.45;
    DECLARE dif FLOAT;
    DECLARE degrees FLOAT;
    DECLARE percentValue FLOAT;

    SET dif = @destinationLon - @departureLon;

    -- Edge case: Flight is perfectly vertical, wind has no effect
    IF (dif = 0) THEN
        RETURN 1;
    END IF;

    -- Edge case: Flight is perfectly horizontal, wind has full effect
    IF (@departureLat = @destinationLat) THEN
        IF (dif < 0) THEN
            RETURN 1 + wind; -- East to West, Time added
        ELSE
            RETURN 1 - wind; -- West to East, Time saved
        END IF;
    END IF;

    -- Math to determine the bearing angle: will yield value between -180 to 180
    DECLARE firstPart FLOAT;
    DECLARE secondPart FLOAT;
    
    SET firstPart = COS(RADIANS(@destinationLat)) * SIN(RADIANS(dif));
    SET secondPart = COS(RADIANS(@departureLat)) * SIN(RADIANS(@destinationLat)) - SIN(RADIANS(@departureLat)) * COS(RADIANS(@destinationLat)) * COS(RADIANS(dif));
    SET degrees = DEGREES(ATAN2(firstPart, secondPart));

    IF (degrees < 0) THEN -- Flight direction is : East to West
        SET percentValue = degrees / 90; -- Gets percentage of 90(Full wind speed) that the flight angle contains
        IF (percentValue < -1) THEN -- If it is below negative one, need to do additional calculations to get correct %
            SET percentValue = -1 * (percentValue + 2);
        END IF;

        SET percentValue = 1 + (percentValue * -1 * wind); -- Since negative number indicates % increase in flight time, change % to positive, multiply by wind, and add one to find % of base flight time this flight will have
    ELSE -- Flight direction is: West to East
        SET percentValue = degrees / 90; -- Gets percentage of 90(Full wind speed) that the flight angle contains
        IF (percentValue > 1) THEN -- If it is above one, need to do additional calculations to get correct %
            SET percentValue = (1 - percentValue) + 1;
        END IF;

        SET percentValue = 1 - (percentValue * wind); -- Since % number indicates % decrease in flight time, multiply % by wind, and subtract from 1 to get % time of base flight time this flight will have
    END IF;

    RETURN percentValue; -- Multiply this result by flight time to get actual flight time accounting for wind
END;
//
DELIMITER ;

-- Function to calculate the distance between two sets of coordinates
DELIMITER //
DROP FUNCTION IF EXISTS great_circle;
CREATE FUNCTION IF NOT EXISTS great_circle(
    @departureLat FLOAT,
    @departureLon FLOAT,
    @destinationLat FLOAT,
    @destinationLon FLOAT
)
RETURNS FLOAT
BEGIN
    DECLARE RADIUS FLOAT DEFAULT 3958.8;
    DECLARE distance FLOAT;
    DECLARE deltaLatitude FLOAT;
    DECLARE deltaLongitude FLOAT;
    DECLARE intermediateTerm FLOAT;
    DECLARE haversineTerm FLOAT;
    
    -- Calculate coordinate deltas
    SET deltaLatitude = RADIANS(@destinationLat) - RADIANS(@departureLat);
    SET deltaLongitude = RADIANS(@destinationLon) - RADIANS(@departureLon);

    -- Intermediate calculations for Haversine formula
    SET intermediateTerm = SIN(deltaLatitude / 2) * SIN(deltaLatitude / 2) + COS(RADIANS(@departureLat)) * COS(RADIANS(@destinationLat)) * SIN(deltaLongitude / 2) * SIN(deltaLongitude / 2);
    SET haversineTerm = 2 * ATAN2(sqrt(intermediateTerm), sqrt(1 - intermediateTerm));

    -- Final distance calculation
    SET distance = RADIUS * haversineTerm;
    
    RETURN distance;
END;
//
DELIMITER ;

-- Function to calculate the flight duration between two airports given an aircraft
DELIMITER //
DROP FUNCTION IF EXISTS calculate_flight_duration;
CREATE FUNCTION IF NOT EXISTS calculate_flight_duration(
    maximumSpeed INT,
    @departureLat FLOAT,
    @departureLon FLOAT,
    @destinationLat FLOAT,
    @destinationLon FLOAT
)
RETURNS INT
BEGIN
    DECLARE PERCENT_OF_MAX_SPEED FLOAT DEFAULT 0.9;

    DECLARE reducedSpeed FLOAT;
    DECLARE distance FLOAT;
    DECLARE angleFactor FLOAT;
    DECLARE flightSpeed FLOAT;
    DECLARE flightDuration FLOAT;
    DECLARE flightDurationInMinutes INT;

    SET reducedSpeed = maximumSpeed * PERCENT_OF_MAX_SPEED;

    SET distance = great_circle(@departureLat, @departureLon, @destinationLat, @destinationLon);

    SET angleFactor = calculate_percentage(@departureLat, @departureLon, @destinationLat, @destinationLon);

    SET flightSpeed = reducedSpeed * angleFactor;

    SET flightDuration = distance / flightSpeed;
    SET flightDurationInMinutes = ROUND(flightDuration * 60);
    return flightDurationInMinutes;
END
//
DELIMITER ;

DELIMITER //
DROP TRIGGER IF EXISTS set_flight_duration;
-- Trigger to calculate the duration of a flight between two airports given a certain aircraft model
CREATE TRIGGER IF NOT EXISTS set_flight_duration
BEFORE INSERT ON flights
FOR EACH ROW
BEGIN
    IF NEW.flight_duration IS NULL THEN
        DECLARE maximumSpeed INT;
        DECLARE @departureLat FLOAT;
        DECLARE @departureLon FLOAT;
        DECLARE @destinationLat FLOAT;
        DECLARE @destinationLon FLOAT;

        -- Get aircraft speed
        SELECT maximum_speed INTO maximumSpeed FROM aircraft WHERE aircraft_id = NEW.aircraft_id;

        -- Get departure airport coordinates
        SELECT latitude, longitude INTO @departureLat, @departureLon FROM airports WHERE airport_id = NEW.departure_airport_id;

        -- Get destination airport coordinates
        SELECT latitude, longitude INTO @destinationLat, @destinationLon FROM airports WHERE airport_id = NEW.destination_airport_id;

        -- Calculate flight duration in minutes
        SET NEW.flight_duration = calculate_flight_duration(maximumSpeed, @departureLat, @departureLon, @destinationLat, @destinationLon);
    END IF;
END;
//
DELIMITER ;
*/