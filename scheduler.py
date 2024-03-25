from clock import Clock  # Import the Clock class

class Scheduler:
    def __init__(self, clock):
        self._clock = clock  # Initialize the clock
        self._schedule = {}  # Initialize schedule as a dictionary

    def add_event(self, event):
        """
        Add an event to the scheduler.
        """
        minute = event.time  # Assuming event.time represents minutes
        if minute not in self._schedule:
            self._schedule[minute] = []  # Create a list for events at this minute if it doesn't exist
        self._schedule[minute].append(event)  # Add the event to the list for this minute

    def get_events_for_minute(self, minute):
        """
        Retrieve events scheduled for a given minute.
        """
        return self._schedule.get(minute, [])  # Return the list of events for the given minute, or an empty list if no events
