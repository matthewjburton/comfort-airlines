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
    duration INT, -- time in minutes
    departure_time INT,  -- time in minutes
    arrival_time INT,  -- time in minutes
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