# Functional Specification

- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher


## Table of Contents

- [Introduction](#introduction)
    - [Naming Conventions](#naming-conventions)
- [Files Information Template](#files-information-template)
    - [airport](#airportpy)
    - [flight_duration](#flight_durationpy)
    - [flight_demand](#flight_demandpy)
    - [turn_around_time](#turn_around_timepy)
    - [flight_angle](#flight_anglepy)
    - [clock](#clockpy)
- [SQL Template](#sql-template)
    - [schema](#schemasql)
    - [populate_airports_table](#populate_airports_tablesql)
    - [populate_aircraft_table](#populate_aircraft_tablesql)
- [Database Template](#database-template)
    - [tables](#tables)
    - [aircraft](#aircraft---55-rows---protected---hardcoded)
    - [airport](#airports---31-rows---protected---hardcoded)
    - [flights](#flights---100-rows---protected---softcoded-and-updateable)
    - [flights_routes](#flights_routes---100-rows---protected---softcoded-and-updateable)
    - [routes](#routes---100-rows---protected---softcoded-and-updateable)
- [Docker Template](#docker-template)
- [User Manual Template](#user-manual-template)
- [Simulation Template](#simulation-template)

## Introduction

  This document serves as a detailed introduction to the codebase highlighting the purpose and use of files, functions, schemas, and conditions involved in each. The overall codebase is coded in Python as the choice of language. Defects should be logged in defect-log.md and implementation shall be updated here making this a living document. Testing for the functions can be found in tests directory.

##### Naming Conventions

- Functions/Methods: this_function_name
- Classes: ThisClassName
- File: this_file_name.py
- @Properties: property_name
- Private variables: _underscorePrefixed
- Attributes: attribute_name_convention
- Variables: VariableNames
- Constants: CONSTANT_NAME
  - Note: constants must go at the top of the file

### Files Information Template

- Filename
- { Functions/classes list | Purpose, Returns, Parameters, Tests }
- Function call
- Purpose
- Author
- Current testing
- Preconditions
- Postconditions
- Parameters
- Returns
- Execution steps

##### airport.py
- { class: Airport }
- Class purpose: Pull airport information from the database into python class objects allowing easier access.
```python
# Author/Editors: Jeremy
# Purpose: Import and create an instance of an airport 
# Returns: The airport instance instantiated
# Parameters: The abbreviation for the airport
# Precondition: Airport object not created and instantiated
# Postcondition: Airport object created and instantiated
# Test cases: Make sure that expected values are stored in a given airport instantiation
import airport
JFK = airport.Airport("JFK")
```
- {get method list}
```python
# Author/Editors: Jeremy
# Purpose: Able to retreive airport information with get methods
# Returns: The information stored in the database
# Parameters: None
# Precondition: None
# Postcondition: Airport information of that instance is returned
# Test: Expected information is returned for different instances
# Airport Methods:
JFK.get_airport_id()
JFK.get_airport_name()
JFK.get_airport_abbreviation()
JFK.get_airport_latitude()
JFK.get_airport_longitude()
JFK.get_airport_timezone_offset()
JFK.get_metro_population()
JFK.get_total_gates()
JFK.get_available_gates()
JFK.get_is_hub()
```
- { Modifying Functions }
```python
# Author/Editors: Jeremy
# Purpose: Adjust gate values to ensure consistency
# Parameters: None
# Returns: None
# Precondition: A gate becomes available or taken up
# Postcondition: Gate availability is consistent and up to date
# Test: Take and free gates up until an expected value
# Modifying Functions:
remote_gate()
add_gate()
```
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 airport.py

#####  flight_duration.py 
- { function: calculate_flight_time }
```python
# Author/Editors: Kevin
# Purpose: Ensures that destination airport does not equal starting airport, ensures that destination airport is not within 150 miles of the departing airport. Flight time is calculated is found meeting these criteria.
# Returns: Flight time
# Parameters: Database configuration in key value pairs of user, password, host, and dbname
# Precondition: 
# Postcondition: 
# Test cases:
calculate_flight_time(db_config)
```
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 flight_duration.py

##### flight_demand.py 
- { function: individual_demand }
```python
# Author/Editors: Jeremy
# Purpose: Calculate the number of people flying from A to B
# Returns: Integer number of people
# Parameters: starting airport, destination airport
# Precondition: Passengers for a flight unknown
# Postcondition: Passengers for a flight known
# Test cases: calculate by hand and add a test case for a given flight
individual_demand(JFK, LAX)
```
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 flight_demand.py

##### turn_around_time.py 
- { function: turn_around_time }
```python
# Author/Editors: Matt
# Purpose: Return the amount of time in minutes that an aircraft must wait before take off
# Returns: Total minimum turn around time for an aircraft
# Parameters: Refueling binary value
# Precondition: A plane is at the gate
# Postcondition: The turn around time is calculated
# Test cases: 0 and 1
# 0: No extra time needed for refueling
# 1: Extra time needed for refueling
turn_around_time(0)
```
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 turn_around_time.py

##### flight_angle.py 
- { function: calculate_percentage }
```python
# Author/Editors: Jeremy
# Purpose: Returns the percentage of base flight time that a flight will take based on the wind and bearing angle
# Returns: A float to multiply with flight time to find the actual time the flight will take
# Parameter: startAirport, endAirport, wind
# Precondition: % of flight time is not accoutned for
# Postcondition: % of flight time is returned
# Test cases: 0 and 1
# 0: One of any airport for start and end, wind default is 0.045
# 1: Crosscheck flight angle percentages against well known values found online for current flights
calculate_percentage(JFK, LAX, 0.045)
```
- Execute:
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 flight_angle.py

##### clock.py 
- { class: Clock }
- Class purpose: Track the current simulation time and manage incrementing time minute by minute
- { method: reset_clock }
```python
# Author/Editors: Matt
# Purpose: Reset to day 1 at 0 hours and 0 minutes
# Returns: none
# Parameter: none
# Precondition: Time is some value
# Postcondition: Time is set to 1, 0, 0
# Test cases: At any time the clock will be reset to 1, 0, 0
reset_clock()
```
- { method: increment_clock }
```python
# Author/Editors: Matt
# Purpose: Increment the clock by 1 minute and check for hour increment and day increment
# Return: none
# Parameter: none
# Precondition: Time is some value
# Postcondition: Minute is incremented by 1, if 60 minutes the hour will be incremented 
#                and minutes set to 0, if 24 hours set both to zero and increment day
# Test cases: At any time the clock will be incremented by one minute, the hour is 
#             incremented at 60 minutes and the minutes are set to 0, at 24 hours the 
#             day is incremented and the hours and minutes are set to 0
# 0: Increment the length of a day in minutes and examine the time
increment_clock()
```

- { method: print_time}
```python
# Author/Editor: Matt
# Purpose: Output the current time of the clock to the terminal
# Return: none
# Parameter: none
# Precondition: Time not printed but available
# Postcondition: Time printed to terminal
# Test cases: The time printed must match the time when printed
print_time()
```
- Execute: 
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 clock.py

 great_circle.py 
- { class: Airport }
- Author: Matt
- Purpose: Initialize airports for testing
- { function: great_circle }
```python
# Author/Editors: Matt
# Purpose: Return the distance between the two airports
# Return: Distance float value in miles
# Paramter: departure airport, and arrival airport
# Precondition: Distance between two airports is not calculated
# Postcondition: Distance is calculated and returned
# Test cases: Airport values passed to the function which returns the distance. Tested against real values through Haversine formula.
great_circle(JFK, LAX)
```
- Execute: 
    1. Move to the comfort-airlines/ directory
    2. Execute the file using the following command in the terminal:
-       python3 great_circle.py

### SQL Template

- Author/Editor
- Purpose
- Precondition
- Postcondition
- { trigger }
    - Purpose
- Test
- Execute steps

##### schema.sql
- Author/Editors: Matt and Ryan
- Purpose: Removes all tables from the database and recreates them using the schema
- Precondition: Old database volume or structure
- Postcondition: Baseline infrastructure created
- { trigger: calculate_total_gates }
- This SQL trigger populates gates at a given airport. 5 per airport and 11 per hub up until the population limit.
- Test: periodically compose down and up the container. Connect to mariadb then to the database and show tables.
- Execute: 
    1. Log into the database:  docker exec -it &lt;container name&gt; mariadb -u &lt;username&gt; -p &lt;database name&gt;                         
-      docker exec -it mariadb-container mariadb -u admin -p cloudnine
    2. To execute the populate-aircraft-table.sql file: source &lt;file/path/file_name.sql&gt;
-       source /docker-entrypoint.initdb.d/schema.sql

##### populate_airports_table.sql 
- Purpose: Removes all entries from the airports table then inserts all of the airports in the list
- Author:  Matt Burton
- Precondition: Airports table is created but unpopulated or populated with old data
- Postcondition: Airports table is populated with new data
- Test: periodically compose down and up the container. Connect to mariadb then to the database and show tables.
- Execute:
    1. Log into the database: docker exec -it &lt;container name&gt; mariadb -u &lt;username&gt; -p &lt;database name&gt;
-       docker exec -it mariadb-container mariadb -u admin -p cloudnine
    2. To execute the populate-airport-table.sql file: source &lt;file/path/file_name.sql&gt;
-       source /docker-entrypoint.initdb.d/populate_airport_table.sql

##### populate_aircraft_table.sql 
- Purpose: Removes all entries from the aircraft table then inserts all of the aircraft in the list below
- Author:  Justin Chen and Matt Burton
- Precondition: Aircrafts table is created but unpopulated or populated with old data
- Postcondition: Aircrafts table is populated with new data
- Test: periodically compose down and up the container. Connect to mariadb then to the database and show tables.
- Execute: 
    1. Log into the database: docker exec -it &lt;container name&gt; mariadb -u &lt;username&gt; -p &lt;database name&gt;             
-       docker exec -it mariadb-container mariadb -u admin -p cloudnine
    2. To execute the populate-aircraft-table.sql file: source &lt;file/path/file_name.sql&gt;
-       source /docker-entrypoint.initdb.d/populate_aircraft_table.sql

### Database Template

- Table name - row estimate - protected/unprotected - hard/softcoded 
- Table description of Field, Type, Null, Key, Null, Extra information

##### Tables

| Tables_in_cloudnine |
|---------------------|
| aircraft            |
| airports            |
| flights             |
| flights_routes      |
| routes              |



##### aircraft - 55 rows - Protected - Hardcoded
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

##### airports - 31 rows - Protected - Hardcoded
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

##### flights - 100+ rows - Protected - Softcoded and updateable
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

##### flights_routes - 100+ rows - Protected - Softcoded and updateable
| Field        | Type    | Null | Key | Default | Extra          |
|--------------|---------|------|-----|---------|----------------|
| route_leg_id | int(11) | NO   | PRI | NULL    | auto_increment |
| route_id     | int(11) | YES  | MUL | NULL    |                |
| flight_id    | int(11) | YES  | MUL | NULL    |                |

##### routes - 100+ rows - Protected - Softcoded and updateable
| Field                  | Type    | Null | Key | Default | Extra          |
|------------------------|---------|------|-----|---------|----------------|
| route_id               | int(11) | NO   | PRI | NULL    | auto_increment |
| starting_airport_id    | int(11) | YES  | MUL | NULL    |                |
| destination_airport_id | int(11) | YES  | MUL | NULL    |                |

### Docker Template

- Filename
- Purpose
- Execution

##### docker_compose.yaml
- Purpose: Configurations for docker are listed in here which are parsed when to composing up an instance with key value pairs. This specifies the volumes to mount for SQL files and MariaDB data, environment values like database name and password prompt, and GUI for database.
- Compose command: docker compose up mariadb -d

### User Manual Template

- Filename
- { Functions/classes list | Purpose, Returns, Parameters, Tests }
- Function call
- Purpose
- Author
- Current testing
- Preconditions
- Postconditions
- Parameters
- Returns
- Execution steps

### Simulation Template

- Filename
- { Functions/classes list | Purpose, Returns, Parameters, Tests }
- Function call
- Purpose
- Author
- Current testing
- Preconditions
- Postconditions
- Parameters
- Returns
- Execution steps
