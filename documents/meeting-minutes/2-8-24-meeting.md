# Meeting Minutes

## Meeting Information

- **Date:** 2/8/24
- **Start Time:** 1:35 pm
- **End Time:** 3:15 pm
- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
- **Present Attendees:** Matt, Ryan, Kevin, Justin, Jeremy
- **Absent Attendees:** McHale
- **Scribe:** Ryan

## Sprint Recap

- **Matt:**
  - Added Paris to the airports table
  - Updated population values to a consistent source
  - Rewrote the great circle formula in Python
  - Created meeting agenda
  - Started first sprint on Jira
- **Ryan:**
  - ERD reviewing/editing
  - Documentation for input and configuration file on simulation
  - Learning Python
- **Kevin:** n/a
- **Justin:**
  - Populated aircraft table
  - Researched aircraft tail number format
- **McHale:**
  - Decided aircraft initial locations for the timetable
- **Jeremy:**
  - ERD rework
  - Installed project tools on VM to work around local machine issues
  - Provided Python Libraries/helpful tools
  - Flight angle function logic

## Agenda

- [X] Discuss Gantt chart
- [X] Review new ERD
- [X] Assign small tasks to generate our timetable
- [X] Consider getting the simulation working to evaluate timetable options
- [X] Finish the first sprint on Jira and plan next week’s sprint

## Synopsis and Discussion

- Discussing Gantt chart adjusting more time for database review during the timetable.
- Discussing ERD and structure. Timetable is the same as the Flights table and the Route table. How we define a route will determine how much focus there will be on the timetable. Should we  
    A. programmatically calculate the shortest path algorithm from one airport to any other  
    or  
    B. By hand map out predetermined routes that cycle every other day.  
    Solution B is going to be approached initially because we do not want to waste time on the NP-complete problem. ERD will need to be changed to match Solution B. Conceptual Timetable attributes need to be mapped to the Flights table and a boarding pass is generated (routes from origin to final destination) from the routes table which is connected to flights and aircraft. Must print out all information from that Foreign Key in the other tables for that information.
- Timetable discussion: We need to discuss what planes should start where. We also need to figure out how to decide on what model plane needs to end each day at or second day at. For example, we may need the same plane type at the starting location for the next day or the day after. We will want to start the aircraft servicing Paris in New York so we can use the extra time that day for another trip in the US.
- Finished ERD for now - Need to update database schema.
- Assigning Story points on JIRA items.

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
| Jeremy Maas         | Flight Angle Function - Testing verified          | Next Meeting  |
| Matt Burton         | Test query database via code and react appropriately | Next Meeting  |
| Matt Burton         | Simulation event queue                            | Next Meeting  |
| McHale & Jeremy     | Designating Starting Airports on aircrafts        | Next Meeting  |
| Ryan/Jeremy         | Bring Database up to date with ERD, Redo the schema file (Branch CA - 45) | Next Meeting  |
