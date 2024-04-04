# Meeting Minutes

## Meeting Information

**Date:** 4/4/24  
**Start Time:** 1:40 pm  
**End Time:** 3:25 pm  
**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Present Attendees:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Absent Attendees:** n/a  
**Scribe:** Ryan  

## Sprint Recap

**Matt:**

- Fixed maintenance events
- Removed routes and flights_routes tables from the schema
- Renamed attributes in flights table
- Created view functionality for timetable airports and aircrafts
- Simplified arrival and departure times
- Reviewed some PRs
- Fixed Add airport
- Started simulation config

**Ryan:**

- Started on coding the algorithm to generate a random timetable
- Documented the criteria for the timetable
- Implementing most of the pseudocode, but will need more data/objects and discussion around it

**Kevin:**

- Did some slides on the presentation
- Worked on the timetable documentation

**Justin:**

- Looked at presentation
- Did the take off time function

**McHale:**

- Added input validation for airport menu
- Fixed naming conventions
- Worked on simulation configuration

**Jeremy:**

- Started on the timetable generation with Ryan
- Fixed some logic on flight demand
- Added inbound flights to airport class

## Agenda

- [X] Ask Oudshoorn questions
- [X] Fill in sprint recap
- [X] Defect log
- [ ] Handle outstanding pull requests
- [ ] Get Jira up to date
- [ ] Create new Jira issues
- [ ] Start new Jira sprint

## Synopsis and Discussion

- Discussed how to import airportList and how we should handle lists across different files
- We should not duplicate lists and update the same list across different files, there should be one instance of an airportList and aircraftList
- Can import a list like this: from .aircraft_objects import aircrafts
- Clock class will not be very useful for the timetable algorithm, instead it can better be used for the simulation
- Reviewing naming convention fixes
- Reviewing Simulate Maintenance: uses input from user to simulate event conflicts
- Reviewing Simplify and Update Schema: Renamed and organized flights table and triggers. Added view aircraft and airports as user menu options. Added airport validation, but not fully injection prevented - need to look into a way to sanitize the input making sure that they are in the appropriate range and not including malicious code.
- Added a function to get the number of aircrafts models for need be basis
- We decided to allow the client to add as many airports and hubs as they want
- Prevent the client from entering the same abbreviation as another airport
- Add cancel options for the menus and during input

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
Kevin | Finish presentation | Next Meeting
Jeremy Ryan | Continue timetable algorithm and place aircrafts | Next Meeting
McHale | Unit testing, Remove aircraft based on tailnumber, Enforce unique tailnumbers | Next Meeting
Justin | Work on presentation | Next Meeting
Matt | Validate airport input, Remove airports on abbreviation, enforce unique abbreviations, remove configure challenges, fix report frequency month calculation | Next Meeting
