# Functional Specification

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  

## Table of Contents

- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Module Information](#module-information)
  - [populate-aircraft-table.sql](#populate-aircraft-tablesql)
  - [populate-airports-table.sql](#populate-airports-tablesql)
  - [populate-flights-table.sql](#populate-flights-tablesql)
  - [schema.sql](#schemasql)

  - [maintenance_exception.py](#maintenance_exceptionpy)
  - [aircraft_menu.py](#aircraft_menupy)
  - [airport_menu.py](#airport_menupy)
  - [configuration_menu.py](#configuration_menupy)
  - [cost_menu.py](#cost_menupy)
  - [simulation_menu.py](#simulation_menupy)
  - [timetable_menu.py](#timetable_menupy)

  - [aircraft.py](#aircraftpy)
  - [airport.py](#airportpy)
  - [flight.py](#flightpy)

  - [aircraft_objects.py](#aircraft_objectspy)
  - [airport_objects.py](#airport_objectspy)
  - [report.py](#reportpy)
  - [schedule.py](#schedulepy)
  - [scheduled_event.py](#scheduled_eventpy)
  - [simulation_config.json](#simulation_configjson)
  - [simulation.py](#simulationpy)

  - [timetable.py](#timetablepy)

  - [clock.py](#clockpy)
  - [database.py](#databasepy)
  - [display_menu.py](#display_menupy)
  - [flight_angle.py](#flight_anglepy)
  - [flight_demand.py](#flight_demandpy)
  - [flight_duration.py](#flight_durationpy)
  - [flight_takeoff.py](#flight_takeoffpy)
  - [great_circle.py](#great_circlepy)
  - [turn_around_time.py](#turn_around_timepy)

  - [comfort_airlines.py](#comfort_airlinespy)

- [Directory Structure](#directory-structure)
- [Docker Template](#docker-template)
- [User Manual Template](#user-manual-template)
- [Simulation Template](#simulation-template)

## Introduction

  This document serves as a detailed introduction to the codebase highlighting the purpose and use of files, functions, schemas, and conditions involved in each. The overall codebase is written in Python, and the database in SQL.

## Naming Conventions

| Type                | Example                    |
|---------------------|----------------------------|
| Files               | `this_file_name.py`        |
| Functions/Methods   | `this_function_name`       |
| Classes             | `ThisClassName`            |
| @Properties         | `property_name`            |
| Local variables     | `variableNames`            |
| Private variables   | `_underscorePrefixed`      |
| Constants           | `CONSTANT_NAME`            |
|                     | *(Note: constants must go at the top of the file)* |
| Attributes          | `attribute_name_convention`|

## Module Information

### populate-aircraft-table.sql

**Location:** comfort-airlines/docker/sql-files/populate-aircraft-table.sql  
**Purpose:** Replaces the entities in the aircraft table with the hardcoded list of aircraft in this file.  
**Execution:** Once inside the cloudnine database, ensure that the schema has been initialized, then run:  

```sql
source /docker-entrypoint-initdb.d/populate-aircraft-table.sql
```

### populate-airports-table.sql

**Location:** comfort-airlines/docker/sql-files/populate-airports-table.sql  
**Purpose:** Replaces the entities in the airports table with the hardcoded list of airports in this file.  
**Execution:** Once inside the cloudnine database, ensure that the schema has been initialized, then run:  

```sql
source /docker-entrypoint-initdb.d/populate-airports-table.sql
```

### populate-flights-table.sql

**Location:** comfort-airlines/docker/sql-files/populate-flights-table.sql  
**Purpose:** Replaces the entities in the flights table with the hardcoded list of flights in this file.  
**Execution:** Once inside the cloudnine database, ensure that the schema has been initialized, then run:  

```sql
source /docker-entrypoint-initdb.d/populate-flights-table.sql
```

### schema.sql

**Location:** comfort-airlines/docker/sql-files/schema.sql  
**Purpose:** Empties and replaces the existing tables with the database schema as defined in this file.  
**Execution:** Once inside the cloudnine database, initialize the schema by running:  

```sql
source /docker-entrypoint-initdb.d/schema.sql
```

### maintenance_exception.py

**Location:** comfort-airlines/exceptions/maintenance_exception.py  
**Purpose:** Handles error logging for invalid maintenance calls  

### aircraft_menu.py

**Location:** comfort-airlines/menus/aircraft_menu.py  
**Purpose:** Responsible for implementing the menu options under the aircraft menu option  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|
| `view_aircraft()` | Prints the aircraft entities from the aircraft table | None | None |
| `print_aircrafts_header()` | Formats and prints the column headers for all aircraft attributes | None | None |
| `print_aircraft(aircraft)` | Formats and prints the information of the aircraft object passed in | `aircraft`: dataframe row | None |
| `edit_aircraft()` | Displays the list of editing options | None | None |
| `add_aircraft()` | Adds an aircraft to the database from user input | None | None |
| `remove_aircraft()` | Prints the aircraft table and then allows user to remove an aircraft by tail_number | None | None |
| `get_valid_tail_number()` | Returns valid tail_number from user input or 'quit' if the user cancels | None | `str` or `'quit'`|
| `get_valid_name_or_model(input_type)` | Returns valid string from user input or 'quit' if the user cancels | `input_type`: str | `str` or `'quit'` |
| `get_int_value(input_type)` | Returns valid integer value from user input or 'quit' if the user cancels | `input_type`: str | `int` or `'quit'` |

### airport_menu.py

**Location:** comfort-airlines/menus/airport_menu.py  
**Purpose:** Responsible for implementing the menu options under the airport menu option  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|
| `view_airports()` | Queries the database for the airports table and prints the entities | None | None |
| `print_airports_header()` | Formats and prints the column headers for all airport attributes | None | None |
| `print_airport(airport)` | Formats and prints the information of the airport object passed in| `airport`: dataframe row| None  |
| `edit_airport()` | Displays the list of editing options | None | None |
| `add_airport()` | Adds an airport to the database from user input | None | None |
| `remove_airport()` | Prints the airport table and then allows user to remove an airport by abbreviation | None | None |
| `get_valid_name()` | Returns valid airport name from user input or 'quit' if the user cancels | None  | `str` or `'quit'` |
| `get_valid_abbreviation(removingAirport)`| Returns valid airport abbreviation from user input or 'quit' if the user cancels. If removingAirport is True, checks if abbreviation exists in the database | `removingAirport`: bool | `str` or `'quit'` |
| `get_valid_latitude()` | Returns valid latitude from user input or 'quit' if the user cancels | None | `float` or `'quit'` |
| `get_valid_longitude()` | Returns valid longitude from user input or 'quit' if the user cancels | None | `float` or `'quit'` |
| `get_valid_timezone_offset()` | Returns valid timezone offset from user input or 'quit' if the user cancels | None | `int` or `'quit'` |
| `get_valid_metro_population()` | Returns valid metro population from user input or 'quit' if the user cancels | None | `int` or `'quit'` |
| `get_valid_is_hub()` | Returns valid is_hub value from user input or 'quit' if the user cancels | None | `int` or `'quit'` |
| `get_valid_total_gates(metroPopulation, isHub)` | Returns valid total gates value from user input or 'quit' if the user cancels. Calculates maximum possible gates based on metroPopulation and isHub values | `metroPopulation`: int, `isHub`: int | `int` or `'quit'` |

### configuration_menu.py

**Location:** comfort-airlines/menus/configuration_menu.py  
**Purpose:** Responsible for implementing the menu options under the configure simulation menu option  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|
| `read_config()` | Reads the simulation configuration from the JSON file | None | `dict` |
| `write_config(config)` | Writes the simulation configuration to the JSON file| `config`: dict | None |
| `configure_start_date()` | Configures the start date of the simulation | None | None |
| `configure_duration()` | Configures the duration of the simulation| None | None |
| `configure_report_frequency()` | Configures the report frequency of the simulation | None  | None |
| `get_report_frequency_options(duration)`| Determines the available report frequency options based on the duration of the simulation | `duration`: int | `list` |
| `format_options_for_print(options)` | Formats the report frequency options for display | `options`: list | `str` |
| `ensure_valid_report_frequency(config, duration)`| Ensures that the selected report frequency is valid based on the duration of the simulation | `config`: dict, `duration`: int | `str` |
| `configure_costs()` | Displays the costs submenu | None | None |

### cost_menu.py

**Location:** comfort-airlines/menus/cost_menu.py  
**Purpose:** Responsible for implementing the menu options under the configure costs menu option  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|
| `read_config()` | Reads the simulation configuration from the JSON file | None | `dict` |
| `write_config(config)` | Writes the simulation configuration to the JSON file| `config`: dict | None |
| `configure_fuel_cost()`| Configures the fuel cost for the simulation | None | None |
| `configure_takeoff_cost()` | Configures the takeoff cost for the simulation | None | None |
| `configure_landing_cost()` | Configures the landing cost for the simulation | None | None |
| `configure_leasing_costs()` | Configures the leasing costs for different aircraft models | None| None |
| `retrieve_aircraft_models_and_costs()` | Retrieves the aircraft models and their leasing costs from the database | None | `dataframe` |
| `display_aircraft_models_and_costs(dataframe)` | Displays the current leasing costs for each aircraft model | `dataframe`: dataframe | None |
| `handle_model_input(leasingCosts)` | Handles user input for selecting an aircraft model| `leasingCosts`: dict | `str` |
| `handle_leasing_cost_input(model, leasingCosts, config)`| Handles user input for updating the leasing cost of an aircraft model | `model`: str, `leasingCosts`: dict, `config`: dict | None |
| `update_leasing_costs_in_database(leasingCosts)` | Updates the leasing costs of aircraft models in the database| `leasingCosts`: dict | None |
| `is_valid_dollar_value(inputString)`| Checks if the input string represents a valid dollar value | `inputString`: str | `bool` |

### simulation_menu.py

**Location:** comfort-airlines/menus/simulation_menu.py  
**Purpose:** Responsible for implementing the menu options under the simulation menu option  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|
| `run_simulation()` | Runs the simulation | None | None |
| `configure_simulation()` | Displays the menu for configuring simulation options | None | None |
| `analyze_simulation()` | Displays the analyze simulation submenu | None | None |
| `analyze_follow_aircraft()` | Prints 'executing analyze_follow_aircraft()' | None | None |
| `analyze_download_reports()` | Prints 'executing analyze_download_reports()' | None | None |

### timetable_menu.py

**Location:** comfort-airlines/menus/timetable_menu.py  
**Purpose:** Responsible for implementing the menu options under the timetable main menu option  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|
| `view_timetable()` | Displays the timetable | None | None |
| `search_routes()` | Prints 'executing search_routes()' | None | None |
| `edit_timetable()` | Displays the edit timetable submenu | None | None |
| `download_timetable()` | Prints 'executing download_timetable()' | None | None |
| `sort_by_cost()` | Prints 'executing sort_by_cost()' | None | None |
| `sort_by_number_of_stops()` | Prints 'executing sort_by_number_of_stops()' | None | None |
| `sort_by_departure_time()` | Prints 'executing sort_by_departure_time()' | None | None |
| `add_flight()` | Prints 'executing add_flight()' | None | None |
| `remove_flight()` | Prints 'executing remove_flight()' | None | None |
| `upload_timetable()` | Prints 'executing upload_timetable()' | None | None |

### aircraft.py

**Location:** comfort-airlines/objects/aircraft.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### airport.py

**Location:** comfort-airlines/objects/airport.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### flight.py

**Location:** comfort-airlines/objects/flight.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### aircraft_objects.py

**Location:** comfort-airlines/simulation/aircraft_objects.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### airport_objects.py

**Location:** comfort-airlines/simulation/airport_objects.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### report.py

**Location:** comfort-airlines/simulation/report.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### schedule.py

**Location:** comfort-airlines/simulation/schedule.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### scheduled_event.py

**Location:** comfort-airlines/simulation/scheduled_event.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### simulation_config.json

**Location:** comfort-airlines/simulation/simulation_config.json  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### simulation.py

**Location:** comfort-airlines/simulation/simulation.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### timetable.py

**Location:** comfort-airlines/timetable/timetable.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### clock.py

**Location:** comfort-airlines/utilities/clock.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### database.py

**Location:** comfort-airlines/utilities/database.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### display_menu.py

**Location:** comfort-airlines/utilities/display_menu.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### flight_angle.py

**Location:** comfort-airlines/utilities/flight_angle.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### flight_demand.py

**Location:** comfort-airlines/utilities/flight_demand.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### flight_duration.py

**Location:** comfort-airlines/utilities/flight_duration.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### flight_takeoff.py

**Location:** comfort-airlines/utilities/flight_takeoff.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### great_circle.py

**Location:** comfort-airlines/utilities/great_circle.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### turn_around_time.py

**Location:** comfort-airlines/utilities/turn_around_time.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

### comfort_airlines.py

**Location:** comfort-airlines/comfort_airlines.py  
**Purpose:**  

| Method Name | Purpose | Parameters | Return Values |
|-------------|---------|------------|---------------|

##### flight_duration.py

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
#   and minutes set to 0, if 24 hours set both to zero and increment day
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

## Directory Structure

### docker/sql-files/

This directory is a volume connected to the docker so users can execute these files in the cloudnine database. These files are copied in into the *docker-entrypoint-initdb.d/* directory within the docker.

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
