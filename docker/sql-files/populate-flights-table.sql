/*
Removes all entries from the flights table, then inserts all of the flights in the list below.
__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter

    Execute: 1. Log into the database: docker exec -it <container name> mariadb -u <username> -p <database name>       
       
        docker exec -it mariadb-container mariadb -u admin -p cloudnine
            
            2. To execute the populate-flights-table.sql file: source <file/path/file_name.sql>

        source /docker-entrypoint-initdb.d/populate-flights-table.sql
*/

-- Clears the flights table.
DELETE FROM flights;

-- Sets the auto increment back to 1.
ALTER TABLE flights AUTO_INCREMENT = 1;

-- Inserts 28 flight entries into the table
INSERT INTO flights (flight_number, aircraft_id, departure_airport_id, destination_airport_id, local_departure_time, local_arrival_time, on_time_bin, gate_departure, gate_arrival)
VALUES
    ('ABC123', 1, 4, 5, 10, 12, 1, 1, 2);
--    ('DEF456', 2, 2, 3, 10, 13, 1, 3, 1),
--    ('GHI789', 3, 3, 4, 10, 12, 0, 2, 3),
--    ('JKL123', 4, 4, 5, 12, 15, 1, 4, 5),
--    ('MNO456', 5, 5, 6, 14, 16, 1, 2, 1),
--    ('PQR789', 6, 6, 7, 240, 16, 20, 1, 3, 1),
--    ('STU123', 7, 7, 8, 18, 20, 0, 2, 1),
--    ('VWX456', 8, 8, 9, 20, 22, 1, 2, 3),
--    ('YZA789', 9, 9, 10, 21, 24, 1, 1, 3),
--    ('BCD123', 10, 10, 11, 0, 2, 1, 2, 1),
--    ('EFG456', 11, 11, 12, 2, 4, 1, 2, 3),
--    ('HIJ789', 12, 12, 13, 4, 6, 0, 1, 4),
--    ('KLM123', 13, 13, 14, 6, 9, 1, 2, 1),
--    ('NOP456', 14, 14, 15, 8, 10, 1, 3, 2),
--    ('QRS789', 15, 15, 16, 10, 12, 1, 1, 3),
--    ('TUV123', 16, 16, 17, 12, 14, 1, 1, 2),
--    ('VWX495', 17, 17, 18, 14, 16, 0, 2, 3),
--    ('YZA934', 18, 18, 19, 16, 19, 1, 3, 1),
--    ('BCD853', 19, 19, 20, 18, 20, 1, 2, 1),
--    ('EFG185', 20, 20, 21, 20, 22, 0, 2, 2),
--    ('HIJ927', 21, 21, 22, 22, 24, 1, 1, 1),
--    ('KLM903', 22, 22, 23, 0, 3, 1, 3, 2),
--    ('NOP094', 23, 23, 24, 2, 4, 0, 2, 3),
--    ('QRS345', 24, 24, 25, 4, 6, 1, 2, 1),
--    ('TUV834', 25, 25, 26, 6, 8, 1, 1, 1),
--    ('VWX174', 26, 26, 27, 8, 10, 0, 3, 2),
--    ('YZA643', 27, 27, 28, 10, 13, 1, 3, 2),
--    ('BCD628', 28, 28, 29, 12, 14, 0, 3, 1);