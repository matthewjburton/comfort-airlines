-- Purpose: Removes all entries from the airports table
--          then inserts all of the airports in the list below
-- Author:  Matt Burton
-- Execute: 1. Move to the /comfort-airlines directory
--          2. Copy this file from the repository into the docker using: docker cp <local_file_path> <container_name_or_id>:<container_path>
--              
--              docker cp populate-airports-table.sql mariadb-container:/tmp/
--
--          3. Log into the database: docker exec -it <container name> mariadb -u <username> -p <database name>              
--              
--              docker exec -it mariadb-container mariadb -u admin -p cloudnine
--
--          4. To execute the populate-airports-table.sql file: source <file_name.sql>
--              
--              source /tmp/populate-airports-table.sql

-- Clear the airports table
DELETE FROM airports;

-- Insert airport entries into the table
INSERT INTO airports (name, abbreviation, latitude, longitude, timezone_offset, metro_population, is_hub)
VALUES
    ('John F. Kennedy International Airport', 'JFK', 40.641766, -73.780968, -5, 19034000, 1),
    ('Newark Liberty International Airport', 'EWR', 40.6895314, -74.1744624, -5, 19034000, 1),
    ('LaGuardia Airport', 'LGA', 40.7769, -73.874, -5, 19034000, 1),
    ('Los Angeles International Airport', 'LAX', 33.9416, -118.4085, -8, 12598000, 1),
    ('O''Hare International Airport', 'ORD', 41.978611, -87.904724, -6, 8984000, 0),
    ('Chicago Midway International Airport', 'MDW', 41.7868, -87.7522, -6, 8984000, 0),
    ('Dallas/Fort Worth International Airport', 'DFW', 32.89748, -97.040443, -6, 6655000, 0),
    ('George Bush Intercontinental Airport', 'IAH', 29.9902, -95.3368, -6, 6802000, 0),
    ('Ronald Reagan Washington National Airport', 'DCA', 38.8512, -77.0402, -5, 5545000, 0),
    ('Washington Dulles International Airport', 'IAD', 38.9531, -77.4565, -5, 5545000, 0),
    ('Fort Lauderdale–Hollywood International Airport', 'FLL', 26.0742, -80.1506, -5, 6317000, 0),
    ('Miami International Airport', 'MIA', 25.7959, -80.287, -5, 6317000, 0),
    ('Hartsfield-Jackson Atlanta International Airport', 'ATL', 33.640411, -84.419853, -5, 6193000, 0),
    ('Philadelphia International Airport', 'PHL', 39.8729, -75.2437, -5, 5821000, 0),
    ('Phoenix Sky Harbor International Airport', 'PHX', 33.435, -122, -7, 4777000, 0),
    ('Logan International Airport', 'BOS', 42.3656, -71.0096, -5, 4367000, 0),
    ('San Francisco International Airport', 'SFO', 37.6213129, -122.3789554, -8, 3343000, 0),
    ('Detroit Metropolitan Wayne County Airport', 'DTW', 42.2124, -83.3534, -5, 3528000, 0),
    ('Tacoma International Airport', 'SEA', 47.4502, -122.3088, -8, 3549000, 0),
    ('Minneapolis–Saint Paul International Airport', 'MSP', 44.8819, -93.2218, -6, 3014000, 0),
    ('San Diego International Airport', 'SAN', 32.7338, -117.1933, -8, 3345000, 0),
    ('Tampa International Airport', 'TPA', 27.9755, -82.5332, -5, 3009000, 0),
    ('Denver International Airport', 'DEN', 39.8561, -104.6737, -7, 2963000, 0),
    ('Baltimore/Washington International Thurgood Marshall Airport', 'BWI', 39.1774, -76.6684, -5, 2370000, 0),
    ('Orlando International Airport', 'MCO', 28.4312, -81.308, -5, 2101000, 0),
    ('Charlotte Douglas International Airport', 'CLT', 35.21308, -81.308, -5, 2321000, 0),
    ('Harry Reid International Airport', 'LAS', 36.06601, -115.153969, -8, 2953000, 0),
    ('Austin-Bergstrom International Airport', 'AUS', 30.1945, -97.6699, -6, 2274000, 0),
    ('Nashville International Airport', 'BNA', 36.1263, -86.6774, -6, 1333000, 0),
    ('Salt Lake City International Airport', 'SLC', 40.7899, -111.9791, -7, 1214000, 0),
    ('Paris Charles de Gaulle Airport', 'CDG', 49.0079, 2.5508, 1, 11277000, 0);
