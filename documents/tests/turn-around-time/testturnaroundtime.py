import turn_around_time

#Testing 4 cases:
#   Two correct assertions, one for refueling, one without
#   Two incorrect assertions, one for refueling, one without
#   Results, assertions correctly captured valid output. Function's arithmetic works successfully

def testfuncRefuelCorrect():
    assert turn_around_time.turn_around_time(True) == 50

def testfuncNoRefuelCorrect():
    assert turn_around_time.turn_around_time(False) == 40

def testfuncRefuelIncorrect():
    assert turn_around_time.turn_around_time(True) == 100

#def testfuncNoRefuelIncorrect():
    #assert turn_around_time.turn_around_time(False) == 100

testfuncRefuelCorrect()

testfuncNoRefuelCorrect()

#testfuncNoRefuelIncorrect()

testfuncRefuelIncorrect()