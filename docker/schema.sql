CREATE TABLE airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    abbreviation VARCHAR(3),
    latitude FLOAT,
    longitude FLOAT,
    timezone_offset INT,
    metro_population INT,
    city VARCHAR(255),
    state VARCHAR(255)
);

CREATE TABLE aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    tail_number VARCHAR(20),
    model VARCHAR(255),
    maximum_speed INT,
    maximum_capacity INT,
    maximum_fuel INT,
    leasing_cost INT
);

CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    departure_airport_id INT,
    destination_airport_id INT,
    direction_of_flight FLOAT,
    flight_duration_minutes INT,
    departure_time INT,
    arrival_time INT,
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id)
);

CREATE TABLE routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    layover_times JSON
);

CREATE TABLE flights_routes (
    flight_id INT,
    route_id INT,
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),
    FOREIGN KEY (route_id) REFERENCES routes(route_id),
    PRIMARY KEY (flight_id, route_id)
);