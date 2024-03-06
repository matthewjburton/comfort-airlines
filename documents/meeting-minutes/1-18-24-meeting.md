# Meeting Minutes

## Meeting Information

- **Date:** 1/18/24
- **Start Time:** 1:35 pm
- **End Time:** 3:15 pm
- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
- **Present Attendees:** Matt, Ryan, Kevin, Justin
- **Absent Attendees:** McHale, Jeremy
- **Scribe:** Matt

## Sprint Recap

- **McHale:**
  - Great circle formula
- **Kevin:**
  - Airport information document
  - Convert airport distances into a spreadsheet
  - List the metro population for each airport
  - List the demand for each airport
- **Matt:**
  - Created a front-end mockup
  - Researched strengths and weaknesses of C#
  - Created a meeting agenda

## Agenda

- [X] Decide on programming language
- [X] Decide on how to manage the database
- [X] Decide on what our main goals are for our presentation
- [X] Talk about setting up Dockers
- [ ] Decide the Hubs
- [ ] Make sure everyone reads over the code standards before writing any code
- [ ] Established goals for part one

## Synopsis

- We tentatively decided on the C# language as the ASP.NET framework and the Entity Framework support web development and database integration. Additionally, MAUI allows for cross-platform development.
- Shifted our design strategy from class objects to database tables.
- Added the ERD diagram as an issue in Jira.
- Decided to focus our presentation on the simulation part over the timetable or a GUI.
- Reminded everyone to read over the coding standards before writing any code.
- Established goals for part one including:
  - Create a timetable
  - Assign aircraft to initial airports
  - Create a schedule so passengers can get from one airport to any other
  - Assign flight numbers
  - Maintain the timetable in a database
  - Indicate departure time, arrival time, the airports involved, and the passenger capacity
  - Printed version of the timetable
  - An interface for users to look up flights from airport A to airport B
    - If it is possible to get from A to B, show all flight options for that day
      - Departure/arrival times
      - Airports involved
      - Layover time(s)
      - Cost of the trip

## Notes from Oudshoorn

- Routes are made up of one or more flights using one or more airport
- If a plane doesn't return to the same airport by the end of the day then that airport must have another plane end its day at the airport so early morning flights have a plane on standby
- If a small amount of people want to take an undesirable unique flight we can route them through a hub to increase profits and maximize capacity
- Use universal time (UTC), add timezones to the airports
- Design for someone who can make a timetable
- Dont design for the passengers

## Action Items

| Assignee          | Task                                                                       | Due Date  |
|-------------------|----------------------------------------------------------------------------|-----------|
| All team members | Come prepared to defend a list of hubs with strong reasons                 | 1/25/24   |
| All team members | Practice creating a docker with a MariaDB container                        | 1/25/24   |
