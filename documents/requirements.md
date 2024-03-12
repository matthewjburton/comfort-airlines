# Cloud Nine Requirements

**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

## Deliverables

Cloud Nine will provide Comfort Airlines with software to manage a timetable and gather profibility data by simulating their business plan.

## Features

The software provided by Cloud Nine to Comfort Airlines will support the following features:

Timetable  

- [ ] View
- [ ] Search routes
  - [ ] Sort by cost
  - [ ] Sort by number of stops
  - [ ] Sort by departure time
- [ ] Edit
  - [ ] Add
  - [ ] Remove
  - [ ] Upload
- [ ] Download

Simulation  

- [ ] Run
- [ ] Configure
  - [ ] Start date
  - [ ] Duration
  - [ ] Report frequency
  - [ ] Costs
    - [ ] Fuel
    - [ ] Gate
    - [ ] Takeoff
    - [ ] Landing
    - [ ] Aircraft
  - [ ] Challenges
    - [ ] View
    - [ ] Edit
- [ ] Analyze
  - [ ] Follow aircraft
  - [ ] Download report(s)

Airports

- [ ] View
- [ ] Edit
  - [ ] Add
  - [ ] Remove

Aircraft

- [ ] View
- [ ] Edit
  - [ ] Add
  - [ ] Remove

## Feature Descriptions

### Timetable

#### View

Viewing the timetable allows the user to see every flight avaiable to potential flyers. This list will detail which aircraft are scheduled to fly between which airports and at what times.

#### Search routes

Searching for routes allows the user to find flights and routes between departure and destination airports.

##### Sort by cost

Routes returned from the search can be sorted by cost from either high to low or low to high.

##### Sort by number of stops

Routes returned from the search can be sorted from the most connecting flights to the least or least to most.

##### Sort by departure time

Routes returned from the search can be sorted from the earliest departure time to the latest departure time or latest to earliest.

#### Edit

##### Add

The user can add a new route to the timetable assuming there is at least one aircraft in the system available to fly that route.

##### Remove

The user can remove a route from the time table to free up an aircraft.

##### Upload

The user can upload a .csv file that overrides the existing timetable with the newly uploaded timetable.

#### Download

The user can download a .csv file that details the entire list of flights and routes avaialable under the current timetable.

### Simulation

#### Run

The user can run a simulation that will use the timetable to govern the flights of each aircraft. After the simulation has finished a report will be generated with information detailing the number of people who got to their destination and the profitability of the business model.

##### Configure

The user can modify the specifications of the simulation as offered in subsequent menu options.

###### Start date

The user can set the start date of the simulation. By default the simulation starts on day one.

###### Duration

The user can set the duration that the simulation will run for in days.

###### Report frequency

The user can set how often the simulation generates reports. The options include daily, weekly, monthly, yearly, and final. Final will produce only one report once the simulation is complete.

###### Costs

The user can redefine the cost values for the following submenu options.
