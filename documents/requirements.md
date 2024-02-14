# Cloud Nine Functional Requirements

## Timetable

Table containing all flight information for a specific day, including starting and ending airports, plane tail number, flight number, (any layovers), flight times, and passenger capacity, price

## Database-Related

### Airport specifications

- Airport ID
- Airport Name
- Airport Abbreviation
- Latitude
- Longitude
- Timezone Offset
- Metro Population
- City
- State

### Aircraft specifications

- Aircraft ID
- Name
- Tail Number
- Model
- Maximum Speed
- Maximum Capacity
- Maximum Fuel
- Leasing Cost

### Flights

- Flight ID
- Departure Airport
- Destination Airport
- Direction of Flight
- Flight Duration
- Departure Time
- Arrival Time
- Price (Route)
- TBD whether or not this will be generated on demand or be stored in a table

### Airport hubs/maps

- Determined Los Angeles, Newark, Chicago, and Dallas to be our 4 hubs

### ERD

- Plan out all database tables, relationships, and datatypes
- (Safely) update/select from tables with proper access
- Leverage Python library to be able to update Database tables
- Pandas

## Functions/Code-Related

### Great Circle Function

- Function should calculate proper distance between two airports using latitude and longitude

### Flight Turnaround Time Function

- Function used to calculate how long a flight takes, takes into account flight % gain/loss, plane speed, account for events, and distance between airports
- Leverages Clock

### Flight Direction Function

- Calculates % gain or loss on flight based on direction, Leverages given % values for east/west and updates percentage based on latitude changes

### Flight Class pulling from timetable

### Clock

- Allows us to track flight time, track DST, and determine turnaround time

### Event scheduler

- Leverages clock to determine takeoff times(if a plane can take off)
- Optional Parameters for delays, weather, wind increases, anything that will affect travel time

### Graphical Interface Flight Map

## Non-Functional Requirements

- Requirements document
- Create the Functional Specification document
- Meeting Minutes
- Gantt Chart/PERT Chart
- Test Plan
- Defect Logs - track bugs
- User manual
- Properly Commented Code
- Reflective Essay (individual)
- Journaling

## Non-Attempted Functionality

- N/A currently
- Will populate once we start heavily implementing code
