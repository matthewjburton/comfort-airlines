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

### User Manual

- How client can make and run
- Clear concise manual on surface level goals, usage, and reveals
- How to read and understand what is happening in simulation
- How to generate a route from one airport to any other airport (without input complex queries)
- Application is simple and straightforward

### Database

- Well formed and Active ERD
    https://lucid.app/lucidchart/5309d00f-f70a-4fd5-8814-b1b4376db552/edit?invitationId=inv_474a4f67-407a-4268-8d16-66c24e7f123d&page=0_0#
- Relationships identified (0, many, 1)
- Table names
- Table columns
- Column data types
- Null/not null
- Estimated number of rows
- Protected or Unprotected (update/insert/select)

+---------------------+
| Tables_in_cloudnine |
+---------------------+
| aircraft            |
| airports            |
| flights             |
| flights_routes      |
| routes              |
+---------------------+

[ Aircraft Table - 55 rows - Protected - Hardcoded]
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| aircraft_id      | int(11)      | NO   | PRI | NULL    | auto_increment |
| tail_number      | varchar(20)  | YES  |     | NULL    |                |
| name             | varchar(255) | YES  |     | NULL    |                |
| model            | varchar(255) | YES  |     | NULL    |                |
| maximum_speed    | int(11)      | YES  |     | NULL    |                |
| maximum_capacity | int(11)      | YES  |     | NULL    |                |
| maximum_fuel     | int(11)      | YES  |     | NULL    |                |
| cargo_volume     | int(11)      | YES  |     | NULL    |                |
| leasing_cost     | int(11)      | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+

[ Airports Table - 31 rows - Protected - Hardcoded ]
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| airport_id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| name             | varchar(255) | YES  |     | NULL    |                |
| abbreviation     | varchar(3)   | YES  |     | NULL    |                |
| latitude         | float        | YES  |     | NULL    |                |
| longitude        | float        | YES  |     | NULL    |                |
| timezone_offset  | int(11)      | YES  |     | NULL    |                |
| metro_population | int(11)      | YES  |     | NULL    |                |
| total_gates      | int(11)      | YES  |     | NULL    |                |
| is_hub           | binary(1)    | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+

[ Flights Table - 100+ rows - Protected - Softcoded and updateable ]
+-------------------------+-------------+------+-----+---------+----------------+
| Field                   | Type        | Null | Key | Default | Extra          |
+-------------------------+-------------+------+-----+---------+----------------+
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
+-------------------------+-------------+------+-----+---------+----------------+

[ Flight Routes Table - 100+ rows - Protected - Softcoded and updateable ]
+--------------+---------+------+-----+---------+----------------+
| Field        | Type    | Null | Key | Default | Extra          |
+--------------+---------+------+-----+---------+----------------+
| route_leg_id | int(11) | NO   | PRI | NULL    | auto_increment |
| route_id     | int(11) | YES  | MUL | NULL    |                |
| flight_id    | int(11) | YES  | MUL | NULL    |                |
+--------------+---------+------+-----+---------+----------------+


[ Routes Table - 100+ rows - Protected - Softcoded and updateable ]
+------------------------+---------+------+-----+---------+----------------+
| Field                  | Type    | Null | Key | Default | Extra          |
+------------------------+---------+------+-----+---------+----------------+
| route_id               | int(11) | NO   | PRI | NULL    | auto_increment |
| starting_airport_id    | int(11) | YES  | MUL | NULL    |                |
| destination_airport_id | int(11) | YES  | MUL | NULL    |                |
+------------------------+---------+------+-----+---------+----------------+

### Docker

- Docker environment
- Container configurations
- README and instructions on how to use
- IDE integration with Github (user can commit, pull, merge, and branch)
- Must be able to run container with populated data from Github branch

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
