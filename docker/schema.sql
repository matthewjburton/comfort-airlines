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

-- Delete entities from existing tables to remove data
DELETE FROM layovers;
DELETE FROM route_legs;
DELETE FROM flights;
DELETE FROM aircraft;
DELETE FROM routes;
DELETE FROM airports;

-- Enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS layovers;
DROP TABLE IF EXISTS route_legs;
DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS aircraft;
DROP TABLE IF EXISTS airports;

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
    aircraft_id VARCHAR(20),
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

CREATE TABLE IF NOT EXISTS route_legs (
    route_leg_id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT,
    flight_id INT,
    FOREIGN KEY (route_id) REFERENCES routes(route_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE IF NOT EXISTS layovers (
    layover_id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT,
    layover_time INT,
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
);
