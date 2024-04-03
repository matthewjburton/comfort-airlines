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
INSERT INTO flights (flight_number, aircraft_id, departure_airport_id, destination_airport_id, departure_time)
VALUES
    ('ABC123', 1, 4, 5, 10);
--    ('DEF456', 2, 2, 3, 10),
--    ('GHI789', 3, 3, 4, 10),
--    ('JKL123', 4, 4, 5, 12),
--    ('MNO456', 5, 5, 6, 14),
--    ('PQR789', 6, 6, 7, 240, 20),
--    ('STU123', 7, 7, 8, 18),
--    ('VWX456', 8, 8, 9, 20),
--    ('YZA789', 9, 9, 10, 21),
--    ('BCD123', 10, 10, 11, 0),
--    ('EFG456', 11, 11, 12, 2),
--    ('HIJ789', 12, 12, 13, 4),
--    ('KLM123', 13, 13, 14, 6),
--    ('NOP456', 14, 14, 15, 8),
--    ('QRS789', 15, 15, 16, 10),
--    ('TUV123', 16, 16, 17, 12),
--    ('VWX495', 17, 17, 18, 14),
--    ('YZA934', 18, 18, 19, 16),
--    ('BCD853', 19, 19, 20, 18),
--    ('EFG185', 20, 20, 21, 20),
--    ('HIJ927', 21, 21, 22, 22),
--    ('KLM903', 22, 22, 23, 0),
--    ('NOP094', 23, 23, 24, 2),
--    ('QRS345', 24, 24, 25, 4),
--    ('TUV834', 25, 25, 26, 6),
--    ('VWX174', 26, 26, 27, 8),
--    ('YZA643', 27, 27, 28, 10),
--    ('BCD628', 28, 28, 29, 12);