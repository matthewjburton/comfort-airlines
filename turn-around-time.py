def TurnAroundTime(refueling):
    # time breakdown
    timeToDisembarkPassengers = 15
    timeToCleanAircraftAndChangeCrew = 10
    timeToBoardPassengers = 15
    timeToRefuel = 10

    # time calculation
    totalTurnAroundTime = timeToDisembarkPassengers + timeToCleanAircraftAndChangeCrew + timeToBoardPassengers
    if refueling:
        totalTurnAroundTime += timeToRefuel

    return totalTurnAroundTime