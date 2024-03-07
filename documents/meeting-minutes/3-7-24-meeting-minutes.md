# Meeting Minutes

## Meeting Information

**Date:** 3/7/24  
**Start Time:** 1:38pm  
**End Time:** 3:10pm  
**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Present Attendees:** Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Absent Attendees:** Jeremy Maas  
**Scribe:** Matt  

## Sprint Recap

**Matt:**

- Created Test Plan document
- Documented dependencies and created a list of dependencies to streamline pip install process
- Created meeting agenda

**Ryan:**

- Rewrote functional specification document  
- Experiemented with timetable mapping  

**Kevin:**

- Flight duration function is ready for review
- Compiled a spreadsheet distances and durations between every airport for each aircraft
- Wrote a script to automate testing the flight duration program

**Justin:**

- Reviewed the test plan document
- Investigated how we can use an algorithm to make a time table

**McHale:**

- Corresponded with Oudshoorn about time management plan  
- Pushed flights template to populate flights for review  

**Jeremy:**

- Wrote the airport class  
- Implemented new airport class into older programs using temporary classes
- Wrote the flight demand program to generate the number of people that need to fly between any two airports in a given day  

## Agenda

- [X] Fill in sprint recap
- [X] Discuss Justin's research on an algorithm for generating a time table
- [X] Review requirements documentation
- [X] Review functional specification document
- [X] Review test plan
- [X] Handle outstanding pull requests
- [X] Discuss naming standards
- [ ] Get Jira up to date
- [ ] Create new Jira issues
- [ ] Start new Jira sprint

## Synopsis and Discussion

- Considering using Djikstra's or Wilshem's algorithm to generate a time table
- Jeremy is revising the requirements document during this meeting and we will review it at the end of the meeting
- Functional specification document needs to be fleshed out to include every module we will need to meet the requirements outlined in the requirements document
- Each module must list the available methods, their return types, a description of what they do, and a list of their parameters
- Test plan looks good but we need to go back and formally test our existing code  
- Each team member is responsible for testing one module that they didnt write before next Thursday so we are caught up
- Requirements document has been updated to move away from the design oriented description and instead outline our deliverables
- Merged in the flight demands program that calculates how many people need to travel between two airports each day
- Merged in the test plan documentation
- Postponed merging in the functional specification document until its met the standards outlined above
- Merged in an sql script to generate a single test flight and also adds a trigger to populate the flight angle attribute for flights
- Update requirements document to separate implemented features and potential features for both the timetable and the simulation
- Validate the simulation accuracy by listing the factors we take into account during the simulation
- We need a main program that prompts the user with a menu of options like:
  - [1] Lookup flights
  - [2] View time table
  - [3] Simulate flights
- For naming standards we've decided to use:
  - underscores for file names
    - so we can implement them (the dash character isnt allowed in file imports in python)
  - underscores for function names
  - camel case for variable names

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
Kevin | Test flight angle | Next Meeting
McHale | Test Clock class | Next Meeting
Justin | Test Great Circle formula | Next Meeting
Jeremy | Test  Flight turn around time | Next Meeting
Ryan | Test flight duration | Next Meeting
Matt | Test Airport class | Next Meeting
McHale | Revise Gantt Chart | Next Meeting
Ryan | revising the functional specification document| Next Meeting
Jeremy | revising the requirements documentation | Next Meeting
All Authors | standardize naming conventions | 3-11-24
