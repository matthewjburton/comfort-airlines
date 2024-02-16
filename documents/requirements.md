# Cloud Nine Functional Requirements

## Timetable

Table containing all flight information for a specific day, including starting and ending airports, plane tail number, flight number, (any layovers), flight times, and passenger capacity, price

## Database-Related

### Airport specifications

- Airport ID(uuid) - Primary Key
- Airport Name - String
- Airport Abbreviation - String
- Latitude - Float
- Longitude - Float
- Timezone Offset - Int
- Metro Population - Int
- Is_Hub - Binary/Boolean

### Aircraft specifications

- Aircraft ID(uuid) - Primary Key
- Name - String
- Tail Number - String
- Model - String
- Maximum Speed - Int
- Maximum Capacity - Int
- Maximum Fuel - Int
- Cargo Volume - Int
- Leasing Cost - Int

### Flights

- UUID - Primary Key
- Flight Number - String
- Departure Airport - Foreign Key
- Destination Airport - Foreign Key
- Angle of Flight - Float
- Flight Duration - Date/String
- Departure Time - Date/String
- Arrival Time - Date/String
- Available Seats - Int
- On Time - Binary/Boolean
- Gate Departure - Int
- Gate Arrival - Int

### Airport hubs/maps

- Determined Los Angeles, Newark, Chicago, and Dallas to be our 4 hubs. Attempting to maximize the population and distance covered by our hubs

### ERD

- Contain database tables, relationships, and datatypes
- (Safely) update/select from tables with proper access
- Leverage Python library to be able to update Database tables via Pandas

## Functions/Code-Related

### Great Circle Function

- Function takes two Airport Objects as inputs, and returns the distance in miles accounting for the Earth's curvature

### Flight Turnaround Time Function

- Function used to calculate how long a flight takes, takes into account flight % gain/loss, plane speed, account for events, and distance between airports
- Leverages Clock

### Flight Angle Function

- Calculates bearing angle between two airports
- Then leverages the angle and given wind percentage to find the percentage time saved or gained based on the angle

### Flight Class pulling from timetable

### Clock

- Allows us to track flight time, track DST, and determine turnaround time

### Event scheduler

- Leverages clock to determine takeoff times(if a plane can take off)
- Optional Parameters for delays, weather, wind increases, anything that will affect travel time

### Graphical Interface Flight Map

## Non-Functional Requirements

- Requirements document
  - This document
  - Contains all the functional and non functional requirements for our project, is updated when new requirements are needed
- Create the Functional Specification document
  - Contains function specific documentation, such as input, what the function does, and output
- Meeting Minutes
  - Group notes that summarize our discussions, planning, and accomplishments during a meeting
- Gantt Chart/PERT Chart
  - Outlines our timeline for completing different aspects of the project such as planning, implementing, debugging, and testing
- Test Plan
  - Document detailing how we will go about testing our product
- Defect Logs - track bugs
  - Document detailing a chronological order to bugs as we encountered them
- User manual
  - Document outlining how to use/run our simulation
- Properly Commented Code
  - Easy to read, understand, and modify code through concise commenting
- Reflective Essay (individual)
- Journaling

## Non-Attempted Functionality

- N/A currently
- Will populate once we start heavily implementing code
