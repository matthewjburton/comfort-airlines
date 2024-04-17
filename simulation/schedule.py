"""
Stores a list of all events and at what times they occur. Also, resolves conlficts between invalid event addtions

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

"""
Comment out recheduling events since its not working as intended and we dont have time to fix it
POSTPONE_TIME = 3
"""

class Schedule:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Schedule()
        return cls._instance

    def __init__(self):
        self._schedule = {}

    def clear_schedule(self):
        self._schedule = {}

    def add_event(self, event):
        """
        Add an event to the scheduler.
        """
        minute = event._time  # Assuming event.time represents minutes
        if minute not in self._schedule:
            self._schedule[minute] = []  # Create a list for events at this minute if it doesn't exist
        
        """
        Comment out recheduling events since its not working as intended and we dont have time to fix it
        self.reschedule_conflicts(minute, event) # Determine if the new events is scheduled to occur at the same time and airport as another sscheduled event
        """

        self._schedule[minute].append(event)  # Add the event to the list for this minute

    def get_events_for_minute(self, minute):
        """
        Retrieve events scheduled for a given minute.
        """
        return self._schedule.get(minute, [])  # Return the list of events for the given minute, or an empty list if no events
    
    """
    Comment out recheduling events since its not working as intended and we dont have time to fix it
    def reschedule_conflicts(self, minute, event):
        """"""
        Find existing events that would conflict with a new event and resechule the new event
        """"""
        eventConflict = False
        for scheduledEvent in self._schedule[minute]:
            # If the event type for both the scheduled event and the new event are either a departure or arrival event for both events reschedule
            if scheduledEvent._airport == event._airport and (scheduledEvent._event_type in ['Departure', 'Arrival']) and (event._event_type in ['Departure', 'Arrival']):
                eventConflict = True

        if eventConflict:
            event._time += POSTPONE_TIME
            self.add_event(event)
    """
