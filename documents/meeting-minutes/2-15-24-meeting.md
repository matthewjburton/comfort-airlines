# Meeting Minutes

## Meeting Information

- **Date:** 2/15/24
- **Start Time:** 1:40 pm
- **End Time:** 2:50 pm
- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
- **Present Attendees:** Matt, Ryan, Kevin, Justin, Jeremy, McHale
- **Absent Attendees:** n/a
- **Scribe:** Matt

## Sprint Recap

- **Matt:**
  - Worked with Justin to create popualte-aircraft-table.sql file
  - Fixed issues with arrays in the database schema
  - Refined attributes in ERD
  - Solved docker restarting issue
  - Translated documentation to the repository
  - Experimented with querying from Python
- **Ryan:**
  - ERD
  - Simulation documents
  - Started Python bootcamp
- **Kevin:**
  - Debugging docker issues
- **Justin:**
  - Worked on the popualte-aircraft-table.sql file
  - Helped with the ERD
- **McHale:**
  - Started populate flights file template
- **Jeremy:**
  - ERD
  - Updated requirements documentation
  - Started flight angle function

## Agenda

- [X] Confirm ERD  
- [X] Prepare for checkpoint 2  
- [X] Confirm docker works again
- [ ] Review open pull requests
- [X] Get Jira tasks up to date
- [X] Set up Jira sprint for next week
- [ ] Review checkpoint 1 feedback
- [X] Start defect log

## Synopsis and Discussion

- ERD is up to date with our current requirements document and runs in the docker
- Modernized the requirements document with the new ERD and specified document requirements
- Matt, Kevin, Ryan, and Justin all confirmed the docker restarting issue has been resolved. The cause was a corrupted volume storing the mariadb-data, so by removing it and recomposing the docker that volume was recreated, fixing the corruption issue.
- We decided that we are going to focus on getting our timetable version one created by hand.
- Merged the new database schema and populate aircraft table into main
- We decided to move our documentation away from Google Drive and into the repository because then we can leverage source control to track our changes
- Our first ERD experimented with a separate time table but later realized that the timetable is really just the flights tables so we removed the redundant table
- We wanted to create a routes table algorithmically but realized this would require a large time investment, so we decided on hand crafting the routes so we can focus on getting to the simulation
- Our original routes table in the ERD has arrays to list the flights and layover times between each flights which we later learned are not supported by sql so we created a separate route_flights table to handle the list of flights in each route. The layover time between flights can be calculated by querying the flights with the same route id in the flights_routes table, ordering the flights based on takeoff time, and calculating the difference between the deparature and arrival time of back to back flights

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
| Kevin Sampson       | Flight Duration Function          | Next Meeting  |
| All Team Members    | Create a first version of the time table | Next Meeting  |
| Jeremy         | Flight angle function                            | Next Meeting  |
| Jeremy     | Creating airport class ORM with database        | Next Meeting  |
| Justin         | Flight takeoff function | Next Meeting  |
