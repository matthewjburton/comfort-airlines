# Meeting Minutes

## Meeting Information

**Date:** 3/14/24  
**Start Time:** 1:45pm  
**End Time:** 2:50pm  
**Team Name:** Cloud Nine  
**Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher  
**Present Attendees:** Jeremy Maas, Matt Burton, McHale Trotter, Justin Chen, Ryan Hirscher, Kevin Sampson  
**Absent Attendees:** n/a  
**Scribe:** Matt  

## Sprint Recap

**Matt:**

- Rewrote requirements document
- Started work on main executable file and user menu design
- Updated clock, great circle, and turn around time to match new naming standards
- Reread entire project.pdf file and answers all outstanding questions with the client
- Created meeting agenda

**Ryan:**

- Finalized functional specification document and caught it up to our existing code

**Kevin:**

- Updated flight duration to meet naming standards

**Justin:**

- Inspection tested great circle formula

**McHale:**

- Remade the gantt chart by reviewing all the previous action items and schedulding future goals
- Unit tested the clock class
- Fixed populate flight template

**Jeremy:**

- Reformatted naming conventions for airport class, flight demand, and flight angle functions
- Revised the requirements document

## Agenda

- [X] Fill in sprint recap
- [X] Confirm with Oudshoorn that our documents are improvements
- [X] Handle outstanding pull requests
- [X] Confirm we updated to new naming standards
- [X] Determine which requirements document we want to go with
- [X] Check in on testing progress
- [X] Present user menu and main executable file
- [ ] Get Jira up to date
- [ ] Create new Jira issues
- [ ] Start new Jira sprint

## Synopsis and Discussion

- Make sure to move deliverable features out of the main user menu tree if we dont get around to implementing them and explain why we weren't able to implement them
- Add specifications on how we plan to implement the user interface using images and a description
- Functional specification document only needs to list the public functions
- Explain how using a database has been a trade off between implementing additional functionality to support the full scope of the project
- Add milestones that describe the functionality we expect from our software to the Gantt chart
- Functional spoecification can remove redundancy to reduce its length
- Populate flights template just needed a file header, added it, merged into main
- Merged in naming convention updates
- Merged in new requirements document
- McHale tested the clock but no one else was able to test anything until we updated the naming conventions
- User menu headed in the right direction

## Action Items

| **Assignee**        | **Task**                                          | **Due Date**  |
|---------------------|---------------------------------------------------|---------------|
Ryan Hirscher | Finally finalize the final version of the functional specification doc | Next Meeting
Ryan Hirscher | Test flight duration document | Next Meeting
McHale Trotter | Add milestones to the Gantt chart | Next meeting
Machale, Jeremy, and Matt | Start skeleton of modules and stubs | Next Meeting
Justin | Test the great circle function | Next Meeting
Justin | Aircraft take off function | Next Meeting
Kevin | Finalize flight duration file | Next Meeting
Kevin | Test flight angle | Next Meeting
Matt | Test the airport class | Next Meeting
