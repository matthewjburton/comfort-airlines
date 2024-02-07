-- Purpose: Removes all entries from the aircraft table
--          then inserts all of the aircraft in the list below
-- Author:  Justin Chen
-- Notes:   
-- Execute: 1. Move to the comfort-airlines/ directory
--          2. Copy this file from the repository into the docker using: docker cp <local_file_path> <container_name_or_id>:<container_path>
--              
--              docker cp populate-aircraft-table.sql mariadb-container:/tmp/
--
--          3. Log into the database: docker exec -it <container name> mariadb -u <username> -p <database name>              
--              
--              docker exec -it mariadb-container mariadb -u admin -p cloudnine
--
--          4. To execute the populate-aircraft-table.sql file: source <file_name.sql>
--              
--              source /tmp/populate-aircraft-table.sql

-- Clear the aircraft table
DELETE FROM aircraft;

-- Insert airport entries into the table
INSERT INTO aircraft (name, tail_number, maximum_speed, maximum_capacity, maximum_fuel, leasing_cost)
VALUES
    -- Boeing 737-600
    ('Boeing 737-600', 'N100C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N101C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N102C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N103C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N104C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N105C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N106C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N107C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N108C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N109C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N110C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N111C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N112C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N113C9', 588, '108/130', 6875, 245000),
    ('Boeing 737-600', 'N114C9', 588, '108/130', 6875, 245000),
    -- Boeing 737-800
    ('Boeing 737-800', 'N200C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N201C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N202C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N203C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N204C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N205C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N206C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N207C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N208C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N209C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N210C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N211C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N212C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N213C9', 588, '160/184', 6875, 270000),
    ('Boeing 737-800', 'N214C9', 588, '160/184', 6875, 270000),
    -- Airbus A200-100
    ('Airbus A200-100', 'N300C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N301C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N302C9', 515, '116/135', 5790, 192000), 
    ('Airbus A200-100', 'N303C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N304C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N305C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N306C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N307C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N308C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N309C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N310C9', 515, '116/135', 5790, 192000),
    ('Airbus A200-100', 'N311C9', 515, '116/135', 5790, 192000),
    -- Airbus A200-300
    ('Airbus A220-300', 'N400C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N401C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N402C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N403C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N404C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N405C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N406C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N407C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N408C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N409C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N410C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N411C9', 521, '141/160', 5790, 228000),
    ('Airbus A220-300', 'N412C9', 521, '141/160', 5790, 228000);
  