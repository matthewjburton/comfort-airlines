-- Purpose: Removes all entries from the flights table, then inserts all of the flights in the list below.
-- Author:  McHale Trotter
-- Execute: 1. Log into the database: docker exec -it <container name> mariadb -u <username> -p <database name>              
--              
--              docker exec -it mariadb-container mariadb -u admin -p cloudnine
--
--          2. To execute the populate-flights-table.sql file: source <file/path/file_name.sql>
--              
--              source /docker-entrypoint.initdb.d/populate-aircraft-table.sql


-- Clears the flights table.
DELETE FROM flights;

-- Sets the auto increment back to 1.
ALTER TABLE flights AUTO_INCREMENT = 1;

-- Inserts 28 flight entries into the table
INSERT INTO flights (flight_number, aircraft_id, departure_airport_id, destination_airport_id, angle_of_flight, flight_duration_minutes, local_departure_time, local_arrival_time, on_time_bin, gate_departure, gate_arrival)
VALUES
    ('ABC123', 1, 1, 2, 45.0, 120, 10, 12, 1, 1, 2),
    ('DEF456', 2, 2, 3, 30.5, 180, 10, 13, 1, 3, 1),
    ('GHI789', 3, 3, 4, 60.0, 120, 10, 12, 0, 2, 3),
    ('JKL123', 4, 4, 5, 90.0, 180, 12, 15, 1, 4, 5),
    ('MNO456', 5, 5, 6, 45.0, 120, 14, 16, 1, 2, 1),
    ('PQR789', 6, 6, 7, 30.5, 240, 16, 20, 1, 3, 1),
    ('STU123', 7, 7, 8, 60.0, 120, 18, 20, 0, 2, 1),
    ('VWX456', 8, 8, 9, 45.0, 120, 20, 22, 1, 2, 3),
    ('YZA789', 9, 9, 10, 30.5, 180, 21, 24, 1, 1, 3),
    ('BCD123', 10, 10, 11, 60.0, 120, 0, 2, 1, 2, 1),
    ('EFG456', 11, 11, 12, 45.0, 120, 2, 4, 1, 2, 3),
    ('HIJ789', 12, 12, 13, 30.5, 120, 4, 6, 0, 1, 4),
    ('KLM123', 13, 13, 14, 90.0, 180, 6, 9, 1, 2, 1),
    ('NOP456', 14, 14, 15, 45.0, 120, 8, 10, 1, 3, 2),
    ('QRS789', 15, 15, 16, 30.5, 120, 10, 12, 1, 1, 3),
    ('TUV123', 16, 16, 17, 60.0, 120, 12, 14, 1, 1, 2),
    ('VWX456', 17, 17, 18, 45.0, 120, 14, 16, 0, 2, 3),
    ('YZA789', 18, 18, 19, 30.5, 180, 16, 19, 1, 3, 1),
    ('BCD123', 19, 19, 20, 60.0, 120, 18, 20, 1, 2, 1),
    ('EFG456', 20, 20, 21, 45.0, 120, 20, 22, 0, 2, 2),
    ('HIJ789', 21, 21, 22, 30.5, 120, 22, 24, 1, 1, 1),
    ('KLM123', 22, 22, 23, 90.0, 180, 0, 3, 1, 3, 2),
    ('NOP456', 23, 23, 24, 45.0, 120, 2, 4, 0, 2, 3),
    ('QRS789', 24, 24, 25, 30.5, 120, 4, 6, 1, 2, 1),
    ('TUV123', 25, 25, 26, 60.0, 120, 6, 8, 1, 1, 1),
    ('VWX456', 26, 26, 27, 45.0, 120, 8, 10, 0, 3, 2),
    ('YZA789', 27, 27, 28, 30.5, 180, 10, 13, 1, 3, 2),
    ('BCD123', 28, 28, 29, 60.0, 120, 12, 14, 0, 3, 1);