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

- **Issue Description:** Aircraft can be maintenanced at airports that arent hubs
- **Date Found:** 3/28/24
- **Action Plan:** Convert the is_hub value in the dataframe to an integer
- **Assignee(s):** Matt
- **Date Fixed:** 4/2/24  
- **Solution:** Cast the is_hub value to an integer when creating airport objects

## Bug 16

- **Issue Description:** Running back to back simulations increases the number of events
- **Date Found:** 4/2/24
- **Action Plan:** Reset the schedule before running each simulation
- **Assignee(s):** Matt
- **Date Fixed:** 4/2/24  
- **Solution:** Clear the schedule before each simulation run

## Bug 17

- **Issue Description:** Selecting the run option from the simulation menu runs the simulation but also says invalid choice
- **Date Found:** 4/2/24
- **Action Plan:** Invesstigate when invalid choice is displayed
- **Assignee(s):** Matt
- **Date Fixed:** 4/2/24  
- **Solution:** Added a try/except block around the event.execute() part of the simulation loop to handle raised exceptions

## Bug 18

- **Issue Description:** When adding an event to the schedule all events occuring at the same airport at the same time resulted in a conflict
- **Date Found:** 4/2/24
- **Action Plan:** Compare the event types to determine if the events are truly conflicting
- **Assignee(s):** Matt
- **Date Fixed:** 4/2/24  
- **Solution:** Modified the condition to ensure that the events are either departure or arrival events at the same airport before rescheduling the new event

## Bug 19

- **Issue Description:** When starting the simulation on a later date the simulation doesnt run any flight
- **Date Found:** 4/11/24
- **Action Plan:** Loop the timetable every day
- **Assignee(s):** Matt
- **Date Fixed:** 4/15/24  
- **Solution:** Clear and repopulate the schedule at the start of every day. Handle events for each minute into the day not total minutes into the simulation.  
- **Date Fixed:**  
- **Solution:**  

## Bug 20

- **Issue Description:** Timetable generation exceeds the length of the day because the home is too far and we choose to go home at the wrong itme
- **Date Found:** 4/9/24
- **Action Plan:** Must determine when an aircraft should fly to the nearest home
- **Assignee(s):** Ryan
- **Date Fixed:**  4/9/24
- **Solution:**  Created a dictionary on airport objects that tracks where each plane starts and thus where each model should end. Nearest_home function finds the shortest distance among the 30 airports that accepts the same model type and then removes one entry of that type from the destination airport. Lowered the limit to 1100 ensuring that aircrafts arrive on time more frequently.

## Bug 21

- **Issue Description:** Condition error when checking when to fly home
- **Date Found:** 4/9/24
- **Action Plan:** There should be 2 major sections: flying to the next leg or flying home. Decide the conditions on when to do which.
- **Assignee(s):** Ryan
- **Date Fixed:** 4/9/24
- **Solution:**  If the time to the next leg and the time to the next home exceed the time in the day, then fly to the current nearest home instead.

## Bug 22

- **Issue Description:** While iterating through the aircrafts, a simple decrement and increment of gates does not let other aircrafts know when a gate becomes unavailable making it possible for aircrafts to land at the same time at the same gate.
- **Date Found:** 4/12/24
- **Action Plan:** Create a way to timestamp gates for when they should not be available, count the number of gates to exclude and compare with the the total number of gates
- **Assignee(s):** Ryan
- **Date Fixed:**  4/13/24
- **Solution:**  Created a funciton of airport class to reserve a gate which creates an entry in a dictionary of a time window of when a plane reserves to land and takeoff. A second function checks the availability of gates at an airport where it counts the number of overlaps that a plane is trying to reserve a time slot for. This prevents aircrafts from exceeding the gate limit.

## Bug 23

- **Issue Description:** Each aircraft should visit a hub at least once, which it is not.
- **Date Found:** 4/11/24
- **Action Plan:** Choose a leg of the flight path to fly to a hub
- **Assignee(s):** Ryan
- **Date Fixed:**  4/11/24
- **Solution:**  Added a leg counter and randomly choose between the first leg and second leg to go to a hub, if all the gates are unavailable at the hubs, then keep trying after each flight

## Bug 24

- **Issue Description:** Paris aircraft must only fly between JFK and paris. Meaning, JFK should be a hub. Changing the hub introduced some hardcoding errors
- **Date Found:** 4/15/24
- **Action Plan:** Change the way that the hubs are indexed in choose_airport so that we can make adjustments to the database without changing code
- **Assignee(s):** Ryan
- **Date Fixed:**  4/15/24
- **Solution:**  (quick fix to fix the hardcoding), refactored the code

## Bug 25

- **Issue Description:** Aircrafts often visit their previous airports, this should not happen. However, this will lead to infinite recursion if the last flight must fly to a home that is in the flight history
- **Date Found:** 4/13/24
- **Action Plan:** Add a list flight_history to keep track of the previous airports. Choosing a home to fly to should ignore the flight history restraint
- **Assignee(s):** Ryan
- **Date Fixed:**  4/13/24
- **Solution:**  Created a property of flight objects which tracks the list of airports it has been to. Added a method to flights object that searches the history list for the airport in question. This prevents the aircraft from choosing an airport in its history as long as it is not on its last flight home.
