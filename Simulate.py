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
    events  = ["BUSY", "AVAILABLE", "UNAVAILABLE"]
    probabilities = [PROB_BUSY, PROB_AVAILABLE, PROB_UNAVAILABLE]

    while not successful and unsuccessfulCounter < 4:
        event = random.choices(events, probabilities)[0]
        if event == "BUSY":
            W += Busy()
            W += End()
            unsuccessfulCounter += 1
        elif event == "AVAILABLE":
            W += Available()
            W += End()
            successful = True
        elif event == "UNAVAILABLE":
            W += Unavailable()
            W += End()
            unsuccessfulCounter += 1
    return W


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
    '''
    Time taken is # X ~ Exponential(1/12)
    :return: X
    '''
    lambdaValue = 1/12
    return random.expovariate(lambdaValue)
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

