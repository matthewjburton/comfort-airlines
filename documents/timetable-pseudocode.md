Criteria to Generate a Random Timetable

This makes the assumption that aircrafts are strategically placed for takeoffs at 8 AM which is 1-2 aircrafts at non-hub airports and 7-11 aircrafts at hubs. The RNG timetable will generate a cyclic timetable for one day which is then repeated daily. 

Flight Path generation:
An aircraft may not fly to the same airport
An aircraft may not fly to an airport within 150 miles
An airport must end the day with the same aircraft type
The algorithm will generate a flight path for a given plane
An aircraft must fly to airport within its operating hours
The destination airport is chosen by RNG
A non-hub airport should not have more than 2 aircrafts flying to it within 1.5 hours of another flight
A hub airport should not have more than 5 aircrafts flying to it within 1.5 hours of another flight
When an aircraft lands, it should have a layover of at least 1.5 hours for unforeseen delays and turnaround time
Each hub must have at least 1 plane in reserve for maintenance swaps
Each aircraft flight path must go through a hub
When at the hub, calculate if it should do maintenance for 1.5 days, if so, swap out a plane in reserve and finish the flight path (edit the original plane type to the reserved type)

Post Generation:
A passenger must be able to go from one airport to any other over the span of a day across multiple flights
This can be tested with queries for routes during the generation
We can write dozens to hundreds of queries to test routes to decide whether or not to re-generate flight paths and add it into the algorithm (this will make it take longer to run the algorithm)
Integrate into the algorithm to make this decision automatically


Initialize everything (pull for db)
Get objects
For each aircraft in aircrafts:
   Time_to_home = Nearst_Home(current_airport) //Time to go to nearest acceptable airport
   Current_time = 0;
   While (Time_to_home + current_time > home operating hours - the time it takes to fly home) // MUST identify when to make the last flight
      Chosen_airport = Choose_airport() Choose random airport that is not itself and greater than 150 miles away and flights inbound less than 2 if nonhub and less than 5 if hub
     Print ( chosen_airport + “=>” )
      Timestamp and log inbound flight EX: +1 flight at 8:45 AM
      Wait 1.5 hours
      Time_to_home = Nearst_home(current_airport) //Time to get to nearest acceptable airport
      Decrement inbound flights for that airport
      Decrement available gates for that airport
      Current_time adjust by flight duration
   Fly_Home //Assume here that the aircraft must make a decision on where to make its last flight
   New aircraft
      
def choose_airport(airportOne):
	randomAirport = airportList[random.randint(0,31)]
	if (great_circle.great_circle(airportOne, randomAirport) <= 150 or randomAirport.gatesAvailable - randomAirport.inboundFlights <= 1):
		choose_airport(airportOne)
	return randomAirport



Next steps:

An aircraft can end the day at the closest airport that accepts the same model within operating hours and not saturated with another plane or two planes (decide on how many is saturated)
An aircraft should fly to this location if it cannot make it to the next leg and home.
What can a flight do at the end of the day? Where is the nearest acceptable airport?
Have an aircraft path through a hub once a day
Which models should start where?
Add paris flight into model (and create french translated timetable)



