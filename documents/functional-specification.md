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
- Relationships identified (0, many, 1)
- Table names
- Table columns
- Column data types
- Null/not null
- Estimated number of rows
- Safe accessibility (update/insert/select)
- Departure airport must not equal destination airport

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
