# Meeting Minutes

## Meeting Information

- **Date:** 2/22/24
- **Start Time:** 2:01 pm
- **End Time:** 3:40 pm
- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
- **Present Attendees:** Matt, Ryan, Kevin, Justin, Jeremy, McHale
- **Absent Attendees:** n/a
- **Scribe:** Matt

## Sprint Recap

- **Matt:**
  - Reviewed Ryan's pull request for functional specification updates
  - Shared Checkpoint 2 feedback with the team
  - Worked with Ryan to create a map with all the airports and hubs
  - Created meeting agenda
  - Attempted to make a timetable using the map
- **Ryan:**
  - Worked with Matt to make a map with all the airports and hubs
  - Functional specification updates
- **Kevin:**
  - Working on flight duration function
  - Tried making a time table
  - Tried to allocate an aircraft at each airport
- **Justin:**
  - n/a
- **McHale:**
  - Finished populate flights table
  - Created a trigger that calculates the flight angle
  - Attempted to make a timetable using Python
- **Jeremy:**
  - Finished flight angle function
  - Airports class

## Agenda

- [X] Fill in sprint recap
- [X] Review feedback from checkpoint 2
- [X] Discuss each member's proposed timetable
- [X] Start new Jira sprint

## Synopsis and Discussion

- Tracked everyone's previous contributions in the sprint recap
- We are going to add our group name and member names at the top of every file as per the feedback on checkpoint 2
- Documentation needs updates to focus more on the actual requirements that we need to deliver a sufficient product as opposed to us listing the structure we need to  store our data
- We plan to revisit the fucntional specification document to use code blocks to list the public methods, their parameters, and a descriptions of each method
- We created Jira issues for starting the test plan and user manual documents
- Timetable discussion
  - Matt: Considered starting most flights from satalittle airports (not hubs) so we can travel through hubs in longer routes
  - Ryan: has a plane going from every hub going to every other airport except for one. Planned mostly 8am flights
  - Kevin: putting an aircraft at each airport, maximize aircraft at hubs, majority of 737 based models start in the west because they have longer travel distances
  - McHale: Attempted a Python program to produce a timetable function using the flight table data from the populate-flight-table.sql file
  - Jeremy: Suggested creating the simplest timetable that sends all aircraft on an outbound and inbound flight to and from the same airport just so we have a timetable to start working on the simulation
  - This was way too hard to do by hand, we need to find a better way to create a time table
  - We need a function to calculate the demand of people flying out of each airport
  - Down the road start to determine the best flights to generate based on the profit a potential flight would generate
- We will definitely need to use less gates than the maximum avaiable to save money
- How do we keep track of avaiable gates
- Create temporary classes and method stubs
- For the timetable set up each route as a closed loop that interacts with at least one hub
- Update flights to  only care about the model of the aircraft not the aircraft id
- Must leave a 2 minute gap between using a runway
- None of the planes can actually make it to Paris so we either need to lease a bigger plane or not fly to Paris

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
| Matt Burton| Update functional specification document | Next meeting |
