-- Drop existing tables if they exist
DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS aircraft;
DROP TABLE IF EXISTS airports;

-- Create new tables
CREATE TABLE airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    abbreviation VARCHAR(3),
    latitude FLOAT,
    longitude FLOAT,
    timezone_offset INT,
    metro_population INT,
    total_gates INT
);

CREATE TABLE aircraft (
    tail_number VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255),
    model VARCHAR(255),
    maximum_speed INT,
    maximum_capacity INT,
    maximum_fuel INT,
    cargo_volume INT,
    leasing_cost INT
);

CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    departure_airport_id INT,
    destination_airport_id INT,
    direction_of_flight FLOAT,
    flight_duration_minutes INT,
    local_departure_time INT,
    local_arrival_time INT,
    plane VARCHAR(20),
    flight_number INT,
    available_seats INT,
    on_time_bin BINARY,
    gate_arrival_bin BINARY,
    gate_destination_bin BINARY,
    gate_departure INT,
    gate_arrival INT,
    FOREIGN KEY (aircraft) REFERENCES aircraft(tail_number),
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id)
);

CREATE TABLE routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    layover_time INT[],
    starting_airport INT,
    destination_airport INT,
    flight_legs INT[],
    FOREIGN KEY (starting_airport) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport) REFERENCES airports(airport_id),
    FOREIGN KEY (flight_legs) REFERENCES flights(flight_id)
);
