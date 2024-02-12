-- Purpose: Removes all tables frim the database and recreates
--          them using the schema below
-- Authors: Matt Burton and Ryan Hirscher 
-- Execute: 1. Move to the /comfort-airlines/docker directory
--          2. Copy this file from the repository into the docker using: docker cp <local_file_path> <container_name_or_id>:<container_path>
--              
--              docker cp schema.sql mariadb-container:/tmp/
--
--          3. Log into the database: docker exec -it <container name> mariadb -u <username> -p <database name>              
--              
--              docker exec -it mariadb-container mariadb -u admin -p cloudnine
--
--          4. To execute the schema.sql file: source <file_name.sql>
--              
--              source /tmp/schema.sql

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
    latitude FLOAT,
    longitude FLOAT,
    timezone_offset INT,
    metro_population INT,
    total_gates INT,
    is_hub BINARY
);

CREATE TABLE IF NOT EXISTS aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    tail_number VARCHAR(20),
    name VARCHAR(255),
    model VARCHAR(255),
    maximum_speed INT,
    maximum_capacity INT,
    maximum_fuel INT,
    cargo_volume INT,
    leasing_cost INT
);

CREATE TABLE IF NOT EXISTS flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    departure_airport_id INT,
    destination_airport_id INT,
    angle_of_flight FLOAT,
    flight_duration_minutes INT,
    local_departure_time INT,
    local_arrival_time INT,
    aircraft_id INT,
    flight_number INT,
    available_seats INT,
    on_time_bin BINARY,
    gate_departure INT,
    gate_arrival INT,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id),
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id)
);

CREATE TABLE IF NOT EXISTS routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    starting_airport_id INT,
    destination_airport_id INT,
    FOREIGN KEY (starting_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id)
);

CREATE TABLE IF NOT EXISTS flights_routes (
    route_leg_id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT,
    flight_id INT,
    FOREIGN KEY (route_id) REFERENCES routes(route_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

-- Set delimiter to define the trigger
DELIMITER //

--  Trigger to calculate the total number of gates at each airport
CREATE TRIGGER calculate_total_gates
BEFORE INSERT ON airports
FOR EACH ROW
BEGIN
    DECLARE gates INT;
    
    -- Calculate total gates based on the provided formula
    SET gates = LEAST(ROUND(NEW.metro_population / 1000000), IF(NEW.is_hub, 11, 5));
    
    -- Set the calculated value to the total_gates column
    SET NEW.total_gates = gates;
END;
//

-- Reset the delimeter
DELIMITER ;