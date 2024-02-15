# Defect Log

## Bug 1

- **Issue Description:** The docker was constantly restarting and we couldnt log into the database  
- **Date Found:** 2/13/24  
- **Action Plan:** Research the errors found in the docker log
- **Assignee(s):** Matt and Kevin
- **Date Fixed:** 2/14/24  
- **Solution:** Deleted the maradb-data volume and recomposed the docker to recreated the volume

## Bug 2

- **Issue Description:** The schema file tried to implement ararys to handle the list of flights which isnt supported by sql
- **Date Found:** 2/9/24
- **Action Plan:** Create a separate table to manage the routes and flights relationships
- **Assignee(s):** Matt, Jeremy, and Ryan
- **Date Fixed:** 2/14/24  
- **Solution:** We created a separate table to manage the connection between flights and routes

## Bug 3

- **Issue Description:** The number of attributes in the populate-aircraft-table.sql didnt match the schema nor did the names of the attributes
- **Date Found:** 2/10/24
- **Action Plan:** Get with Justin and confirm aircraft attributes and ERD attributes
- **Assignee(s):** Matt and Justin
- **Date Fixed:** 2/12/24  
- **Solution:** Ensuring the aircraft attributes matched the ERD and that the ERD was functional

## Bug 4

- **Issue Description:** Pushing the meeting minutes to the documentation branch resulted in a divergent branch issue
- **Date Found:** 2/15/24
- **Action Plan:** Rebase the branch
- **Assignee(s):** Matt
- **Date Fixed:** 2/15/24  
- **Solution:** Ran git rebase
