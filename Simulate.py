


def simulate():
    '''
    Simulate the system for one customer.
    :return: W, the total time spent by representative for one customer.
    '''
    # Variables/Flags
    unsuccessfulCounter = 0
    successfulCounter = 0

    # Constants
    PROB_BUSY = 0.2
    PROB_AVAILABLE = 0.5
    PROB_UNAVAILABLE = 0.3
    # TODO: Implement Simulation.