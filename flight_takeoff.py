import math
import airport


def calculate_taxi_time(population, is_hub=False):
    if is_hub:
        if population <= 9000000:
            taxi_time = 15
        else:
            taxi_time = 15 + ((population - 9000000) // 2000000)
        return min(taxi_time, 20)
    else:
        taxi_time = min(13, population * 0.00075)
        return min(taxi_time, 13)

def calculate_takeoff_time():
    return 1

def calculate_landing_time():
    return 2

def calculate_acceleration_time(cruising_altitude, max_speed):
    time_to_cruise_altitude = (cruising_altitude - 10000) / 280  # time to ascend to cruising altitude
    time_to_max_speed = (max_speed * 0.8 - 280) / 25  # time to accelerate to 80% of max speed
    return time_to_cruise_altitude + time_to_max_speed

def calculate_descent_time(distance):
    descent_rate = 1000 / 3  # descent rate in feet per nautical mile
    if distance >= 1500:
        cruising_altitude = 35000
    elif distance >= 350:
        cruising_altitude = 30000
    elif distance >= 200:
        cruising_altitude = 25000
    else:
        cruising_altitude = 20000
    time_to_cruise_altitude = (cruising_altitude - 10000) / 250  # time to descend to cruising altitude
    time_to_land = (distance * 1.852) / 200  # time to descend at 200 knots
    return time_to_cruise_altitude + time_to_land

# Example usage:
population = 5000000  # Example metro area population
is_hub = False  # Example airport type
distance = 1000  # Example flight distance in nautical miles
max_speed = 600  # Example maximum speed of the aircraft in knots

taxi_time = calculate_taxi_time(population, is_hub)
takeoff_time = calculate_takeoff_time()
landing_time = calculate_landing_time()
acceleration_time = calculate_acceleration_time(38000, max_speed)  # Example cruising altitude for international flight
descent_time = calculate_descent_time(distance)

total_flight_time = taxi_time + takeoff_time + landing_time + acceleration_time + descent_time
print(f"Total flight time: {total_flight_time} minutes")