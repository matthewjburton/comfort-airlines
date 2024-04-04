"""
Generates reports about the simulation

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
import logging

MINUTES_IN_A_DAY = 1440
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24
DAYS_IN_A_WEEK = 7
DAYS_IN_A_YEAR = 365
MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Report:
    @staticmethod
    def handle_report(config, minutes):
        try:
            if minutes <= 0:
                raise ValueError("Minutes must be a positive value")
            if Report.should_generate_report(config, minutes):
                Report.generate_report()
        except ValueError as ve:
            logging.error(f"Invalid input: {ve}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    @staticmethod
    def should_generate_report(config, minutes):
        reportFrequency = config['reportFrequency']

        if reportFrequency == 'daily' and Report.is_start_of_day(minutes):
            return True
        elif reportFrequency == 'weekly' and Report.is_start_of_week(minutes):
            return True
        elif reportFrequency == 'monthly' and Report.is_start_of_month(minutes):
            return True
        elif reportFrequency == 'yearly' and Report.is_start_of_year(minutes):
            return True
        elif reportFrequency == 'final' and Report.is_end_of_simulation(config, minutes):
            return True
        else:
            return False
        
    @staticmethod
    def generate_report():
        print('Executing generate_report()')

    @staticmethod
    def is_start_of_day(minutes):
        return minutes % MINUTES_IN_A_DAY == 0

    @staticmethod
    def is_start_of_week(minutes):
        return minutes % (DAYS_IN_A_WEEK * MINUTES_IN_A_DAY) == 0

    @staticmethod
    def is_start_of_month(minutes):
        simulationDay = (minutes / MINUTES_IN_A_DAY) % DAYS_IN_A_YEAR
        
        for monthLength in MONTH_LENGTHS:
            if simulationDay == monthLength or simulationDay == 1:
                return True
            simulationDay -= monthLength

        return False

    @staticmethod
    def is_start_of_year(minutes):
        return minutes % (DAYS_IN_A_YEAR * MINUTES_IN_A_DAY) == 0
    
    @staticmethod
    def is_end_of_simulation(config, minutes):
        simulationDuration = config['startDate'] + config['duration']
        return minutes == simulationDuration * MINUTES_IN_A_DAY