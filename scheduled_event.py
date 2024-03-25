"""
Handle various event types, storing references to the associated information

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from database import Database
class ScheduledEvent:
    def __init__(self, eventType, time):
        self.event_type = eventType
        self.time = time

    def execute(self):
        # Implement the specific behavior of the event
        pass

class DepartureEvent(ScheduledEvent):
    def __init__(self, aircraftID, airportID, departureTime):
        super().__init__('Departure', departureTime)
        self.aircraftID = aircraftID
        self.airportID = airportID

    def execute(self):
        # Implement behavior for departure event
        db = Database()
        query = f'SELECT * FROM aircraft WHERE aircraft_id = {self.aircraftID}'
        dataframe = db.execute_query_to_dataframe(query)

        # Check if any aircraft is found with the given ID
        if dataframe.empty:
            print(f"No aircraft found with ID {self.aircraftID}")
            return
        
        aircraft_tail_number = dataframe['tail_number'].iloc[0]
        
        query = f'SELECT * FROM airports WHERE airport_id = {self.airportID}'
        dataframe = db.execute_query_to_dataframe(query)

        # Check if any aircraft is found with the given ID
        if dataframe.empty:
            print(f"No airport found with ID {self.airportID}")
            return
        
        airport_abbreviation = dataframe['abbreviation'].iloc[0]
        return f"Aircraft {aircraft_tail_number} departing from Airport {airport_abbreviation}"        

class ArrivalEvent(ScheduledEvent):
    def __init__(self, aircraftID, airportID, arrivalTime):
        super().__init__('Arrival', arrivalTime)
        self.aircraftID = aircraftID
        self.airportID = airportID

    def execute(self):
        db = Database()
        query = f'SELECT * FROM aircraft WHERE aircraft_id = {self.aircraftID}'
        dataframe = db.execute_query_to_dataframe(query)

        # Check if any aircraft is found with the given ID
        if dataframe.empty:
            print(f"No aircraft found with ID {self.aircraftID}")
            return
        
        aircraft_tail_number = dataframe['tail_number'].iloc[0]
        
        query = f'SELECT * FROM airports WHERE airport_id = {self.airportID}'
        dataframe = db.execute_query_to_dataframe(query)

        # Check if any aircraft is found with the given ID
        if dataframe.empty:
            print(f"No airport found with ID {self.airportID}")
            return
        
        airport_abbreviation = dataframe['abbreviation'].iloc[0]
        return f"Aircraft {aircraft_tail_number} arriving at Airport {airport_abbreviation}"   
