# Meeting Minutes

## Meeting Information

**Date:** 3/28/24  
**Start Time:** 1:39pm  
**End Time:** 3:24pm  
**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Present Attendees:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Absent Attendees:** n/a  
**Scribe:** Matt  

## Sprint Recap

**Matt:**

- Created the simulation, event schedule, scheduled events, aircraft class, aircraft objects, flight objects, and airport objects
- Rewrote flight duration
- Organized fildes into folders
- Trimmed unusued functionality from the clock class
- Started the project presentation
- Created meeting agenda

**Ryan:**

- Generated pseudo code for timetable algorithm

**Kevin:**

- Worked on the presentation
- Discovered cant use docker on spock

**Justin:**

- Finished the aircraft takeoff function

**McHale:**

- Implemented the add remove and view functions for airport menu and aircraft menu

**Jeremy:**

- Started brainstorming with Kevin and Ryan about the timetable algorithm
- Corrected flight_demand.py naming conventions
- Started the simulation stubs

## Agenda

- [X] Ask Oudshoorn questions
- [X] Fill in sprint recap
- [X] Defect log
- [X] Handle outstanding pull requests
- [ ] Get Jira up to date
- [ ] Create new Jira issues
- [ ] Start new Jira sprint

## Synopsis and Discussion

- We dont need a makefile we just need to state that we dont
- Make user documents into PDFs before submitting
- Use the README to direct the user on installation, executation, and documentation
- Use pyinstaller to create an executable file
- Still no update on docker on spock
- Use the aircraft's maximum range to calculate burn rate
  - Add aircraft's maximum_range to aircraft table
- Remove the routes and flights_routes table
  - When the user wants to search for a route we can query the flights table to find route options when the starting ariport and ending airport
- Every time an aircraft lands at a hub we calculate the total time of all future flights for that aircraft until it returns to the hub, if the total time of future flights + the time since last maintenance exceed the minimum time to require a maintenance, then maintenance that aircraft and substitute another similar aircraft for that aircraft
- Merged in simulation branch
  - Need to fix maintenance time to 200 hours
  - Remove or comment out calculate total flight duration
  - potentially optimize postpone time
  - redefine how we determine a schedule conflict
- Merged in aircraft takeoff function
  - Needs to update imports to work with new file structure
  - Needs to update naming conventions in test_great_circle
  
## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
Jeremy | Finish flight demand | Next Meeting
Jeremy Ryan Kevin | timetable algorithm | Next Meeting
McHale | Simulation config | Next Meeting
Kevin | Investigate Docker issues | Next Meeting
Justin | Work on presentation | Next Meeting
Matt | Keep working on simulation | Next Meeting
