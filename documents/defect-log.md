# Defect Log

- **Team Name:** Cloud Nine  
- **Team Members:** Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher

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

## Bug 5

- **Issue Description:** The sql trigger for the flight angle attribute in the flights table was only populating null values
- **Date Found:** 2/22/24
- **Action Plan:** Add a line to drop the trigger if it already exists, (the old trigger was still in place)
- **Assignee(s):** McHale
- **Date Fixed:** 2/23/24  
- **Solution:** Renamed the trigger from "calculate_flight_angle" to "calculate_flight_angle1" and added a line to drop the trigger if it exists already.

## Bug 6

- **Issue Description:** Miscalculated the flight demand by included the departure airport and airports within 150 miles
- **Date Found:** 3/1/24
- **Action Plan:** Reread the project.pdf and asked the client the specifics for this type of calculation
- **Assignee(s):** Jeremy
- **Date Fixed:** 3/2/24  
- **Solution:** Removed the departure airport and airports within 150 miles from the total population calculation

## Bug 7

- **Issue Description:** Adding and removing gates allowed for negative and more than total gate value
- **Date Found:** 3/18/24
- **Action Plan:** Add exception handling for when the program calls to add or remove a gate when it doesnt make sense
- **Assignee(s):** Matt
- **Date Fixed:** 3/18/24  
- **Solution:** Add exception handling for when the program calls to add or remove a gate when it doesnt make sense

## Bug 8

- **Issue Description:** error executing a query, error code 42000
- **Date Found:** 3/26/24
- **Action Plan:** Research sql syntax and error code 42000
- **Assignee(s):** McHale
- **Date Fixed:** 3/26/24  
- **Solution:** The variable was not being interpolated into the sql query correctly, so I used an f string

## Bug 9

- **Issue Description:** Error checking flights in the flight table because the truth value of the dataframe was ambigous
- **Date Found:** 3/27/24
- **Action Plan:** Reserach ambigous dataframes
- **Assignee(s):** McHale
- **Date Fixed:** 3/27/24  
- **Solution:** Use .empty to check that there was information in the dataframe

## Bug 10

- **Issue Description:** Flight angle doesnt account for bearing
- **Date Found:** 2/3/24
- **Action Plan:** Find a way to make it account for bearing
- **Assignee(s):** Jeremy
- **Date Fixed:** 2/3/24  
- **Solution:** Implemented a set of formulas found online for calculating bearing angle

## Bug 11

- **Issue Description:** Tried to use user input and database entried for the flight duration calculation
- **Date Found:** 2/10/24
- **Action Plan:** Tried to rework the database connection to get the information
- **Assignee(s):** Kevin
- **Date Fixed:** 2/10/24  
- **Solution:** Pass in aircraft and airport objects as parameters instead of taking input or querying the database

## Bug 12

- **Issue Description:** Variables out of reach for flight duration unit test
- **Date Found:** 3/20/24
- **Action Plan:** Use mock variables instead
- **Assignee(s):** Ryan
- **Date Fixed:** 3/20/24  
- **Solution:** Using mock variables solved the issue of variables out of reach

## Bug 13

- **Issue Description:** Ambigous naming between class variables and initializing variables when implenting @propety to airport
- **Date Found:** 3/20/24
- **Action Plan:** Rename private variables to something else
- **Assignee(s):** Matt
- **Date Fixed:** 3/20/24  
- **Solution:** private variables were renamed to use an underscore prefix to distinguish them from @propertys

## Bug 14

- **Issue Description:** Methods and stubs for timetable, aircraft, and airport menus weren't linked to the main menu
- **Date Found:** 3/22/24
- **Action Plan:** Link the stubs to the comfor_airlines.py main menu using imports
- **Assignee(s):** Matt
- **Date Fixed:** 3/22/24  
- **Solution:** Imported timetable, aircraft, and airport

## Bug 15
- **Issue Description:** The python interpreter couldn't find the module named 'utilities' when trying to import it in the 'aircraft_menu.py' script.
- **Date Found:** 3/27/24
- **Action Plan:** Find a way to execute the function from the comfort-airlines directory, where it can see all import folders.
- **Assignee(s):** McHale
- **Date Fixed:** 3/29/24  
- **Solution:** Created a test file in comfort-airlines which let me run these functions from the correct directory.

## Bug 16
- **Issue Description:** AirportMenu.view_airport() was printing out [48] and [49] instead of 0 and 1 for the 'is_hub' attribute.
- **Date Found:** 3/27/24
- **Action Plan:** Research a way to convert the form from ASCII to an integer before printing it to the terminal.
- **Assignee(s):** McHale
- **Date Fixed:** 3/29/24  
- **Solution:** Used the '.astype()' function to adjust the column before it's printed.
