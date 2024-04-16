# Cloud Nine Requirements

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

## <ins>Deliverables</ins>

Cloud Nine will provide Comfort Airlines with software to manage a timetable, gather profitability data, and evaluate customer satisfaction by simulating their business plan.

## <ins>Expectations</ins>

Cloud Nine recognizes the ambitious scope of this feature list and as such have decided to focus on our fundamental deliverables first. We plan to provide a simple timetable, a simple simulation, and a user interface to operate these two features. Additional functionality and accuracy will be implemented once the core functionality has been developed and tested.

## <ins>How to Access Features</ins>

**NOTE:** Features not implemented will be denoted with ***NYI*** and will be available to view under the **Non-Implemented Features Descriptions and Implementation Criteria** section along with an explanation as to why they were not implemented.

Run the comfort_airlines.py executable file. You then should be provided with a user menu displaying different options. All options are prompted in the terminal, to access a specific menu option, type and enter the corresponding number in the terminal.

```bash
Enter the number of your choice:
```

These options include:

- [ ] Timetable
  - [X] View timetable
  - [ ] Search routes(**NYI**)
    - [ ] Sort by cost(**NYI**)
    - [ ] Sort by number of stops(**NYI**)
    - [ ] Sort by departure time(**NYI**)
  - [ ] Edit timetable(**NYI**)
    - [ ] Add route(**NYI**)
    - [ ] Remove route(**NYI**)
    - [ ] Upload timetable(**NYI**)
  - [ ] Download timetable(**NYI**)
- [ ] Simulation
  - [X] Run simulation
  - [X] Configure simulation
    - [X] Set start date
    - [X] Define duration
    - [X] Specify report frequency
    - [X] Adjust costs
  - [ ] Analyze simulation results(**NYI**)
    - [ ] Track aircraft(**NYI**)
    - [ ] Download reports(**NYI**)
- [X] Airports
  - [X] View airports
  - [X] Edit airports
    - [X] Add airport
    - [X] Remove airport
- [X] Aircraft
  - [X] View aircraft
  - [X] Edit aircraft
    - [X] Add aircraft
    - [X] Remove aircraft

Detailed descriptions of each feature along with how to leverage them are present in the descriptions below.

## <ins>Implemented Features Descriptions</ins>

### Timetable

- #### View timetable

Allows user to viewing the timetable lists every flight and route available to potential flyers by selecting this option's corresponding number. This list will detail which aircraft are scheduled to fly between which airports and at what times.

### Simulation

- #### Run Simulation

Allows user to simulate the flights on the timetable by selecting this option's corresponding number. Reports will be generated to estimate the profitability of your business model and customer satisfaction.

### Airports

- #### View airports

Allows user to list every airport in the simulation and all of their details. Details include: name, abbreviation, lattitude, longitude, time zone offset from UTC, metro population, number of available gates, and whether its a hub or not.

- #### Edit airports

The user can add or remove airports to our database, via prompting of an airport abbreviation.

- **Add airport**: Add an airport to the database.

- **Remove airport**: Remove an airport from the database. An airport cannot be removed if timetable uses that airport.

### Aircrafts

- #### View aircraft

Lists every aircraft in the simulation all of their details. Details include: tail number, name, model, maximum speed, maximum capacity, maximum fuel, cargo volume, and leasing cost.

- #### Edit aircraft

The user can add or remove aircrafts to our database.

- **Add aircraft**: Add an aircraft to the simulation.

- **Remove aircraft**: Remove an aircraft from the simulation. An aircraft cannot be removed from the simulation if the timetable uses that aircraft.

## <ins>Non-Implemented Features Descriptions and Implementation Criteria</ins>

### Timetable

- #### Search routes

  This option would have the capability to search between routes. Due to time constraints, we were unable to implement this functionality by the deadline, although it's implementation is in future plans. The search criteria not implemented for the above reason are below:

- **Sort by cost**: Sorts routes from least expensive to most expensive.

- **Sort by number of stops**: Sorts routes from direct flights to most stops.

- **Sort by departure time**: Sorts routes from earliest departure time to latest.

- #### Edit timetable

  This option would allow you to add or remove routes and to upload your own timetable, overriding the current one. This would give flexibility to choose any routes you specifically desire if our algorithm did not generate them. Time restriction was our main obstacle here, as we prioritized proof-of-concept timetable generation. This would be relatively easy to implement, and do not expect it to take long.

- **Add route**: Adds a new route to the timetable with user defined details. This process will fail if the aircraft in unavailable or the flight is invalid.

- **Remove route**: Removes a route from the time table. Cannot remove individual flights.

- **Upload timetable**: Upload a .csv file to override the existing timetable.

- #### Download timetable

  This would download a .csv file listing all flights and routes. Time restrictions came into effect here, but would be extremely easy to implement, requiring only a few lines of code.

- #### French Timetable Translation

  Due to time restrictions, we were focusing more on the functionality and accuracy of our timetable generation. A simple translation to French would be a rather easy task.

### Simulation

- #### Configure Simulation

  This would provide options for simulation configuration. The user would be able to select criteria such as start date, duration, report frequency, and cost adjustment. Additionally, the user would be able to add delays, weather conditions, or any other incidents that may impact flight times such as maintenance and rescheduling conflicts.

- **Set start date**: Set the start date of the simulation. By default the simulation would start on day one.

- **Define duration**: Define the duration of the simulation in days.

- **Specify report frequency**: Specify how often the simulation generates reports. Options include daily, weekly, monthly, yearly, and final. By default the report frequency is set to final. Final produces one report at the end of the simulation.

- **Adjust costs**: Adjust the cost of fuel, takeoffs, landing, and gate fees.

- #### Analyze simulation results

  This option would allow the user to view an aicraft's flight path during a simulation as well as downloading the reports based on report frequency.

- **Track aircraft**: Select an aircraft to view its travel history.

- **Download reports**: Download a copy of every report from the previous simulation.
