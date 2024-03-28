# Meeting Minutes

## Meeting Information

**Date:** 3/28/24  
**Start Time:** 1:39pm  
**End Time:**
**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Present Attendees:**  
**Absent Attendees:**  
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
- [ ] Handle outstanding pull requests
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
- Reviewed simulation branch, looks good
  - Need to fix maintenance time to 200 hours
  - Remove or comment out calculate total flight duration
  - potentially optimize postpone time
  - redefine how we determine a schedule conflict

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
Justin | Finish testing great circle | Next Meeting
Justin | Finish aircraft takeoff function | Next Meeting
McHale | Clarify milestones  on the Gantt chart | Next Meeting
Jeremy | Finish testing flight turn around function | 3/22/24
Kevin | Finish the  flight duration function | Next Meeting
Ryan | Ensure flight duration tests still work after Kevin's changes | Next Meeting
Ryan and Matt | Start presentation | Next Meeting
McHale and Jeremy | Continue working on modules and stubs | Next Meeting
Matt | Connect everything into a rudimentary simulation | Next Meeting
