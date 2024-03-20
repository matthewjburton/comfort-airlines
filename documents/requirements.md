# Cloud Nine Requirements

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

## Deliverables

Cloud Nine will provide Comfort Airlines with software to manage a timetable, gather profitability data, and evaluate customer satisfaction by simulating their business plan.

## Features

The software provided by Cloud Nine to Comfort Airlines will support the following features:

- [ ] Timetable
  - [ ] View timetable
  - [ ] Search routes
    - [ ] Sort by cost
    - [ ] Sort by number of stops
    - [ ] Sort by departure time
  - [ ] Edit timetable
    - [ ] Add route
    - [ ] Remove route
    - [ ] Upload timetable
  - [ ] Download timetable
- [ ] Simulation
  - [ ] Run simulation
  - [ ] Configure simulation
    - [ ] Set start date
    - [ ] Define duration
    - [ ] Specify report frequency
    - [ ] Adjust costs
  - [ ] Analyze simulation results
    - [ ] Track aircraft
    - [ ] Download reports
- [ ] Airports
  - [ ] View airports
  - [ ] Edit airports
    - [ ] Add airport
    - [ ] Remove airport
- [ ] Aircraft
  - [ ] View aircraft
  - [ ] Edit aircraft
    - [ ] Add aircraft
    - [ ] Remove aircraft

## Feature Descriptions

### Timetable

#### View timetable

Viewing the timetable lists every flight and route available to potential flyers. This list will detail which aircraft are scheduled to fly between which airports and at what times.

#### Search routes

Searching for routes finds routes between two airports.

- **Sort by cost**: Sorts routes from least expensive to most expensive.

- **Sort by number of stops**: Sorts routes from direct flights to most stops.

- **Sort by departure time**: Sorts routes from earliest departure time to latest.

#### Edit timetable

- **Add route**: Adds a new route to the timetable with user defined details. This process will fail if the aircraft in unavailable or the flight is invalid.

- **Remove route**: Removes a route from the time table. Cannot remove individual flights.

- **Upload timetable**: Upload a .csv file to override the existing timetable.

#### Download timetable

Download a .csv file listing all flights and routes.

### Simulation

#### Run Simulation

Simulate the flights on the timetable and recovers from predefined challenges. Reports will be generated to estimate the profitability of your business model and customer satisfaction.

#### Configure Simulation

- **Set start date**: Set the start date of the simulation. By default the simulation starts on day one.

- **Define duration**: Define the duration of the simulation in days.

- **Specify report frequency**: Specify how often the simulation generates reports. Options include daily, weekly, monthly, yearly, and final. By default the report frequency is set to final. Final produces one report at the end of the simulation.

- **Adjust costs**: Adjust the cost of fuel, takeoffs, landing, and gate fees.

#### Analyze simulation results

- **Track aircraft**: Select an aircraft to view its travel history.

- **Download reports**: Download a copy of every report from the previous simulation.

### Airports

#### View airports

List every airport in the simulation and all of their details. Details include: name, abbreviation, lattitude, longitude, time zone offset from UTC, metro population, number of available gates, and whether its a hub or not.

#### Edit airports

- **Add airport**: Add an airport to the simulation.

- **Remove airport**: Remove an airport from the simulation. An airport cannot be removed if timetable uses that airport.

### Aircraft

#### View aircraft

Lists every aircraft in the simulation all of their details. Details include: tail number, name, model, maximum speed, maximum capacity, maximum fuel, cargo volume, and leasing cost.

#### Edit aircraft

- **Add aircraft**: Add an aircraft to the simulation.

- **Remove aircraft**: Remove an aircraft from the simulation. An aircraft cannot be removed from the simulation if the timetable uses that aircraft.

## Expectations

Cloud Nine recognizes the ambitious scope of this feature list and as such have decided to focus on our fundamental deliverables first. We plan to provide a simple timetable, a simple simulation, and a user interface to operate these two features. Additional functionality and accuracy will be implemented once the core functionality has been developed and tested.
