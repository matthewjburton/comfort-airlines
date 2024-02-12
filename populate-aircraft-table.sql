-- Purpose: Removes all entries from the aircraft table
--          then inserts all of the aircraft in the list below
-- Author:  Justin Chen
-- Execute: 1. Move to the /comfort-airlines directory
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
INSERT INTO aircraft (tail_number, name, model, maximum_speed, maximum_capacity, maximum_fuel, cargo_volume, leasing_cost)
VALUES
    -- Boeing 737-600
    ('N100C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N101C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N102C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N103C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N104C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N105C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N106C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N107C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N108C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N109C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N110C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N111C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N112C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N113C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    ('N114C9', 'Boeing', '737-600', 588, 130, 6875, 756, 245000),
    -- Boeing 737-800
    ('N200C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N201C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N202C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N203C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N204C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N205C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N206C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N207C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N208C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N209C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N210C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N211C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N212C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N213C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    ('N214C9', 'Boeing', '737-800', 588, 184, 6875, 1591, 270000),
    -- Airbus A200-100
    ('N300C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N301C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N302C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N303C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N304C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N305C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N306C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N307C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N308C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N309C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N310C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    ('N311C9', 'Airbus', 'A200-100', 515, 135, 5790, 724, 192000),
    -- Airbus A200-300
    ('N400C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N401C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N402C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N403C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N404C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N405C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N406C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N407C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N408C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N409C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N410C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N411C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000),
    ('N412C9', 'Airbus', 'A220-300', 521, 160, 5790, 989, 228000);
  