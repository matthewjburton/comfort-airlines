# Meeting Minutes

## Meeting Information

**Date:** 3/21/24  
**Start Time:** 1:50pm  
**End Time:**  
**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Present Attendees:** Matt Burton, McHale Trotter, Justin Chen, Ryan Hirscher, Kevin Sampson  
**Absent Attendees:** Jeremy Maas  
**Scribe:** Matt  

## Sprint Recap

**Matt:**

- Created database class
- Created tests for database class
- Tested the airport class
- Refactored airport class and associated programs to use @property tags
- Discovered docstring for functions
- Created meeting agenda

**Ryan:**

- Functional specification document is done again
- Working on a unit test for flight duration

**Kevin:**

- Holding off on finishing flight duration file until we implement the new database class

**Justin:**

- Tested the great circle formula
- Started flight takeoff function

**McHale:**

- Finished the Gantt chart but needs to update it after checkiong this milestone
- Worked with Jerermy on creating modules and stubs for aircraft menu

**Jeremy:**

- Worked with McHale on creatint modules and stubs

## Agenda

- [X] Ask Oudshoorn questions
- [X] Fill in sprint recap
- [X] Check in on all documentation (especially the defect log)
- [ ] Handle outstanding pull requests
- [ ] Check in on testing progress
- [ ] Get Jira up to date
- [ ] Create new Jira issues
- [ ] Start new Jira sprint

## Synopsis and Discussion

- Requirements document needs to describe the functionality we didnt attempt and why but onyl by the final checkpoint
- Gantt chart needs to specify what the software should do at each milestone
- Gantt chart is a living document and needs to reflect the accurate past and updated future plan after each milestone
- Presentation needs to invlove everyone, ideally a live demo, potentially a video backup, discuss how we overcame adversity, and argue for why our team should win the contract
- Flight duration branch needs to clean up the multiple copies of the flight duration file
  - Theres a file for user input testing, generating every combination between airports, and the flight duration calculation
- Added Bug 6 to the defect log
- Discussed plan for final checkpoint: glue pieces of the codebase together, make  a presentation, and finalize the documents
- For our first implementation milestone we were supposed to be done with the modules and stubs and the view timetable feature, we are not done
  - Our plan to fix this is to get all of the stubs set up
- Our second implementation milestone is approaching this upcoming monday and we are expected to implement functionality for creating routes, searching routes, and editing the timetable
  - Given that we're behind we will be pushing these back
- Merged in the new functional specification document
- McHale and Justin ran into issues when running the test program because they didnt have python installed, Kevin had an issue with a missing module, but Ryan and Matt had no issues running the test
- Merged in the revised test plan that more accurately reflects our python testing approach over shell scripting
- Skipping over merging in just the database class because Matt opened a pull request including the new class and implementing it

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
