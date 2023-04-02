#import Simulate.py
from Simulate import simulate

NUM_SIMULATIONS = 1000
## Simulation:

for i in range(NUM_SIMULATIONS):
    print("Simulation: ", i+1)
    W = simulate()
    print("W: ", W)

















