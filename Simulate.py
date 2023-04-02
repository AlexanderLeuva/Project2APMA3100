import random


def simulate():
    '''
    Simulate the system for one customer.
    :return: W, the total time spent by representative for one customer.
    '''
    # Variables/Flags
    unsuccessfulCounter = 0
    successful = False
    W = 0

    # Constants
    PROB_BUSY = 0.2
    PROB_AVAILABLE = 0.5
    PROB_UNAVAILABLE = 0.3
    events  = ["Busy", "Available", "Unavailable"]
    probabilities = [PROB_BUSY, PROB_AVAILABLE, PROB_UNAVAILABLE]

    event = random.choices(events, probabilities)
    print(event)

    #while (successful != True) or (unsuccessfulCounter != 4):


def Start():
    '''
    Takes 6 seconds to start
    :return: 6
    '''
    return 6
def Busy():
    '''
    Takes 3 seconds to return Busy Call
    :return: 3
    '''
    return 3
def Available():
    print("Available")
    # TODO Implement
def Unavailable():
    '''
    Takes 25 additional seconds to wait for 5 rings and conclude that no one will answer
    :return: 25
    '''
    return 25
def End():
    '''
    Takes 1 second to end the call
    :return: 1
    '''
    return 1

