# Functional Specification

## Language of choice: Python

### Files

- General organization
- Structural organization/path
- List functions at the top of files
- Pre/post conditions at the top of functions
- Reasoning and criteria for a file/function
- Tested/untested files/functions
- Functional drivers (critical/fragile code identified)
- Private/public data structures and why
- READMEs talking about use cases and functionality

[ turn-around-time.py ]
- { function: TurnAroundTime }
- Purpose:  Return the minimum amount of time in minutes that an
            aircraft must wait before taking off for its next flight
- Author:   Matt Burton
- Notes:    This function will be in the simulation immediately after a flight lands
            Consider moving this function to an event scheduler or the aircraft class
- test: Call to refuel and not refuel
- Precondition: A plane is at the gate
- Postcondition: The turn around time is calculated
- Parameters: refueling is a boolean where if true, it must add refueling time to the total turnaround time.
- Returns: totalTurnAroundTime which is the minimum sum of time to disembark, 
           time to clean the aircraft and change the crew, and board the passengers
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 turn-around-time.py

[ flight-angle.py ]
- { function: calculatePercentage }
- Purpose: Returns % of base flight time that a flight will take based on wind and bearing angle
- Author:  Jeremy Maas
- Notes:   Airport class is temporary
- Precondition: % of flight angle is not accounted for in flight time
- Postcondition: % of flight angle is returned
- Parameters: Source airport and destination ariport for a single leg flight 
              and wind speed which is default set to 0.045
- Returns: Z, the % of the flight angle
- test: Crosscheck flight angle percentages against well known values found online for current flights
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 flight-angle.py

[ clock.py ]
- { class: Clock }
- Purpose:  Track the current simulation time and manage incrementing time minute by minute
- Author:   Matt Burton
- Notes:    Currently, no support for daylight savings time. This class is not meant to be 
            a stand-alone class, instead it will be used by the main simulation
- { method: __init__(self) }
- Set time to day 1 at 0 hours and 0 minutes
- { method: ResetClock }
- Reset time to day 1 at 0 hours and 0 minutes
- { method: IncrementClock }
- Increment 1 minute, at 60 minutes add one hour and reset minutes. At 24 hours increment day and reset hours and minutes
- Precondition: Time is not set or incrementing
- Postcondition: Time is set at 1.0.0 and is incrementing
- Parameters: current time in day, hour, minute
- test: Loop one day of iterations and see if 1 day with 0 hours and 0 minutes
- Execute: 
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 clock.py

[ great-circle.py ]
- { function: GreatCircle }
- Purpose:  Return the distance in miles between two airports
- Author:   Matt Burton
- Notes:    The Airport class is entirely temporary from within this file.
- Precondition: Distance between two airports is not calculated
- Postcondition: Distance is calculated and returned
- Return Value: distance float in miles
- test: hardcoded airport values passed to the function which returns the distance. Tested against real values through Haversine formula.
- Execute: 
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 great-circle.py

[ schema.sql ]
- Purpose: Removes all tables from the database and recreates them using the schema
- Authors: Matt Burton
- Editor: Ryan Hirscher
- Notes: The tables are created and foreign keys are identified
- Precondition: Old database volume or structure
- Postcondition: Baseline infrastructure created
- { trigger: calculate_total_gates }
- This SQL trigger populates gates at a given airport. 5 per airport and 11 per hub up until the population limit.
- test: periodically compose down and up the container. Connect to mariadb then to the database and show tables.
- Execute: 
    1. Log into the database:  docker exec -it &lt;container name&gt; mariadb -u &lt;username&gt; -p &lt;database name&gt;                         
-      docker exec -it mariadb-container mariadb -u admin -p cloudnine
    2. To execute the populate-aircraft-table.sql file: source &lt;file/path/file_name.sql&gt;
-       source /docker-entrypoint.initdb.d/schema.sql

[ populate-airports-table.sql ]
- Purpose: Removes all entries from the airports table then inserts all of the airports in the list
- Author:  Matt Burton
- Precondition: Airports table is created but unpopulated or populated with old data
- Postcondition: Airports table is populated with new data
- test: periodically compose down and up the container. Connect to mariadb then to the database and show tables.
- Execute:
    1. Log into the database: docker exec -it &lt;container name&gt; mariadb -u &lt;username&gt; -p &lt;database name&gt;              
-       docker exec -it mariadb-container mariadb -u admin -p cloudnine
    2. To execute the populate-airport-table.sql file: source &lt;file/path/file_name.sql&gt;
-       source /docker-entrypoint.initdb.d/populate-airport-table.sql


[ populate-aircraft-table.sql ]
- Purpose: Removes all entries from the aircraft table then inserts all of the aircraft in the list below
- Author:  Justin Chen and Matt Burton
- Precondition: Aircrafts table is created but unpopulated or populated with old data
- Postcondition: Aircrafts table is populated with new data
- test: periodically compose down and up the container. Connect to mariadb then to the database and show tables.
- Execute: 
    1. Log into the database: docker exec -it &lt;container name&gt; mariadb -u &lt;username&gt; -p &lt;database name&gt;             
-       docker exec -it mariadb-container mariadb -u admin -p cloudnine
    2. To execute the populate-aircraft-table.sql file: source &lt;file/path/file_name.sql&gt;
-       source /docker-entrypoint.initdb.d/populate-aircraft-table.sql


### User Manual

- How client can make and run
- Clear concise manual on surface level goals, usage, and reveals
- How to read and understand what is happening in simulation
- How to lookup a route from one airport to any other airport (without input complex queries)
- Application is simple and straightforward

### Database

- Well formed and Active ERD
- https://lucid.app/lucidchart/5309d00f-f70a-4fd5-8814-b1b4376db552/edit?invitationId=inv_474a4f67-407a-4268-8d16-66c24e7f123d&page=0_0#
- Relationships identified (0, many, 1)
- Table names
- Table columns
- Column data types
- Null/not null
- Estimated number of rows
- Protected or Unprotected (update/insert/select)

| Tables_in_cloudnine |
|---------------------|
| aircraft            |
| airports            |
| flights             |
| flights_routes      |
| routes              |


[ Aircraft Table - 55 rows - Protected - Hardcoded ]
| Field            | Type         | Null | Key | Default | Extra          |
|------------------|--------------|------|-----|---------|----------------|
| aircraft_id      | int(11)      | NO   | PRI | NULL    | auto_increment |
| tail_number      | varchar(20)  | YES  |     | NULL    |                |
| name             | varchar(255) | YES  |     | NULL    |                |
| model            | varchar(255) | YES  |     | NULL    |                |
| maximum_speed    | int(11)      | YES  |     | NULL    |                |
| maximum_capacity | int(11)      | YES  |     | NULL    |                |
| maximum_fuel     | int(11)      | YES  |     | NULL    |                |
| cargo_volume     | int(11)      | YES  |     | NULL    |                |
| leasing_cost     | int(11)      | YES  |     | NULL    |                |


[ Airports Table - 31 rows - Protected - Hardcoded ]
| Field            | Type         | Null | Key | Default | Extra          |
|------------------|--------------|------|-----|---------|----------------|
| airport_id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| name             | varchar(255) | YES  |     | NULL    |                |
| abbreviation     | varchar(3)   | YES  |     | NULL    |                |
| latitude         | float        | YES  |     | NULL    |                |
| longitude        | float        | YES  |     | NULL    |                |
| timezone_offset  | int(11)      | YES  |     | NULL    |                |
| metro_population | int(11)      | YES  |     | NULL    |                |
| total_gates      | int(11)      | YES  |     | NULL    |                |
| is_hub           | binary(1)    | YES  |     | NULL    |                |


[ Flights Table - 100+ rows - Protected - Softcoded and updateable ]
| Field                   | Type        | Null | Key | Default | Extra          |
|-------------------------|-------------|------|-----|---------|----------------|
| flight_id               | int(11)     | NO   | PRI | NULL    | auto_increment |
| flight_number           | varchar(20) | YES  |     | NULL    |                |
| aircraft_id             | int(11)     | YES  | MUL | NULL    |                |
| departure_airport_id    | int(11)     | YES  | MUL | NULL    |                |
| destination_airport_id  | int(11)     | YES  | MUL | NULL    |                |
| angle_of_flight         | float       | YES  |     | NULL    |                |
| flight_duration_minutes | int(11)     | YES  |     | NULL    |                |
| local_departure_time    | int(11)     | YES  |     | NULL    |                |
| local_arrival_time      | int(11)     | YES  |     | NULL    |                |
| on_time_bin             | binary(1)   | YES  |     | NULL    |                |
| gate_departure          | int(11)     | YES  |     | NULL    |                |
| gate_arrival            | int(11)     | YES  |     | NULL    |                |


[ Flight Routes Table - 100+ rows - Protected - Softcoded and updateable ]
| Field        | Type    | Null | Key | Default | Extra          |
|--------------|---------|------|-----|---------|----------------|
| route_leg_id | int(11) | NO   | PRI | NULL    | auto_increment |
| route_id     | int(11) | YES  | MUL | NULL    |                |
| flight_id    | int(11) | YES  | MUL | NULL    |                |



[ Routes Table - 100+ rows - Protected - Softcoded and updateable ]
| Field                  | Type    | Null | Key | Default | Extra          |
|------------------------|---------|------|-----|---------|----------------|
| route_id               | int(11) | NO   | PRI | NULL    | auto_increment |
| starting_airport_id    | int(11) | YES  | MUL | NULL    |                |
| destination_airport_id | int(11) | YES  | MUL | NULL    |                |


### Docker

- Docker environment
- Container configurations
- README and instructions on how to use
- IDE integration with Github (user can commit, pull, merge, and branch)
- Must be able to run container with populated data from Github branch

[ docker-compose.yaml ]
- Configurations for docker are listed in here which are parsed when to composing up an instance with key value pairs. This specifies the volumes to mount for SQL files and MariaDB data, environment values like database name and password prompt, and GUI for database.

- Compose command: docker compose up mariadb -d

### Simulation

- Anything can happen on any given day (up to n times)
- Simulates 2 weeks based on an input file describing what happens
- Proper recovery from an event
- Way to test individual events and integrated events
- Proper margin of error for time
- Track profit/loss
- Virtualize people, keep track of capacity, keep track of people per plane
- Track planes
- Measure downtime or wait time for planes with unavailable gates
- Measure optimization of gates, gates should not be idle for long.
- Clock by minute

### Time table

- One table
- Meets previous database functional requirements
- Algorithm to map a flight from any two airports
- Can join with itself to create routes on a needed basis
- Account for layover at given nodes and account into shortest path algorithm (create a buffer for planes landing)
- Minimize idle planes
- Departure/Arrival airports
- Actual Flight Durations
- Estimated Flight Durations
- Local Arrival Time Estimates
- Local Departure Time Estimates
- Track Gate availability
- Tail Numbers
- Flight Numbers
- Availability (capacity)
