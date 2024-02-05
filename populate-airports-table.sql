-- Purpose: Removes all entries from the airports table
--          then inserts all of the airports in the list below
-- Author:  Matt Burton
-- Notes:   The list does not include paris
--          Populations should be changed from the number in millions to the actual value
-- Execute: 1. Move to the comfort-airlines/ directory
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
INSERT INTO airports (name, abbreviation, latitude, longitude, timezone_offset, metro_population, city, state)
VALUES
    ('John F. Kennedy International Airport', 'JFK', 40.641766, -73.780968, -5, 20.1, 'New York City', 'New York'),
    ('Newark Liberty International Airport', 'EWR', 40.6895314, -74.1744624, -5, 20.1, 'Newark', 'New Jersey'),
    ('LaGuardia Airport', 'LGA', 40.7769, -73.874, -5, 20.1, 'New York City', 'New York'),
    ('Los Angeles International Airport', 'LAX', 33.9416, -118.4085, -8, 13.2, 'Los Angeles', 'California'),
    ('O''Hare International Airport', 'ORD', 41.978611, -87.904724, -6, 9.5, 'Chicago', 'Illinois'),
    ('Chicago Midway International Airport', 'MDW', 41.7868, -87.7522, -6, 9.5, 'Chicago', 'Illinois'),
    ('Dallas/Fort Worth International Airport', 'DFW', 32.89748, -97.040443, -6, 7.76, 'Dallas', 'Texas'),
    ('George Bush Intercontinental Airport', 'IAH', 29.9902, -95.3368, -6, 7.1, 'Houston', 'Texas'),
    ('Ronald Reagan Washington National Airport', 'DCA', 38.8512, -77.0402, -5, 6.3, 'Arlington', 'Virginia'),
    ('Washington Dulles International Airport', 'IAD', 38.9531, -77.4565, -5, 6.3, 'Dulles', 'Virginia'),
    ('Fort Lauderdale–Hollywood International Airport', 'FLL', 26.0742, -80.1506, -5, 6.2, 'Fort Lauderdale', 'Florida'),
    ('Miami International Airport', 'MIA', 25.7959, -80.287, -5, 6.2, 'Miami', 'Florida'),
    ('Hartsfield-Jackson Atlanta International Airport', 'ATL', 33.640411, -84.419853, -5, 6.1, 'Atlanta', 'Georgia'),
    ('Philadelphia International Airport', 'PHL', 39.8729, -75.2437, -5, 6.1, 'Philadelphia', 'Pennsylvania'),
    ('Phoenix Sky Harbor International Airport', 'PHX', 33.435, -122, -7, 4.9, 'Phoenix', 'Arizona'),
    ('Logan International Airport', 'BOS', 42.3656, -71.0096, -5, 4.9, 'Boston', 'Massachusetts'),
    ('San Francisco International Airport', 'SFO', 37.6213129, -122.3789554, -8, 4.7, 'San Francisco', 'California'),
    ('Detroit Metropolitan Wayne County Airport', 'DTW', 42.2124, -83.3534, -5, 4.3, 'Detroit', 'Michigan'),
    ('Tacoma International Airport', 'SEA', 47.4502, -122.3088, -8, 3.9, 'Seattle', 'Washington'),
    ('Minneapolis–Saint Paul International Airport', 'MSP', 44.8819, -93.2218, -6, 3.6, 'Minneapolis', 'Minnesota'),
    ('San Diego International Airport', 'SAN', 32.7338, -117.1933, -8, 3.3, 'San Diego', 'California'),
    ('Tampa International Airport', 'TPA', 27.9755, -82.5332, -5, 3.1, 'Tampa', 'Florida'),
    ('Denver International Airport', 'DEN', 39.8561, -104.6737, -7, 2.9, 'Denver', 'Colorado'),
    ('Baltimore/Washington International Thurgood Marshall Airport', 'BWI', 39.1774, -76.6684, -5, 2.8, 'Baltimore', 'Maryland'),
    ('Orlando International Airport', 'MCO', 28.4312, -81.308, -5, 2.6, 'Orlando', 'Florida'),
    ('Charlotte Douglas International Airport', 'CLT', 35.21308, -81.308, -5, 2.6, 'Charlotte', 'North Carolina'),
    ('Harry Reid International Airport', 'LAS', 36.06601, -115.153969, -8, 2.3, 'Las Vegas', 'Nevada'),
    ('Austin-Bergstrom International Airport', 'AUS', 30.1945, -97.6699, -6, 2.3, 'Austin', 'Texas'),
    ('Nashville International Airport', 'BNA', 36.1263, -86.6774, -6, 2, 'Nashville', 'Tennessee'),
    ('Salt Lake City International Airport', 'SLC', 40.7899, -111.9791, -7, 1.2, 'Salt Lake City', 'Utah'),
    ('Paris Charles de Gaulle Airport', 'CDG', 49.0079, 2.5508, 1, 11277000, 'Paris', 'France');
