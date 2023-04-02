#import Simulate.py
from Simulate import simulate

NUM_SIMULATIONS = 1000
## Simulation:
wArray = []

for i in range(NUM_SIMULATIONS):
    print("Simulation: ", i+1)
    W = simulate()
    wArray.append(W)

## Analysis:
print("Average Time: ", sum(wArray)/len(wArray))
print("Median Time: ", sorted(wArray)[len(wArray)//2])
print("First Quartile Time: ", sorted(wArray)[len(wArray)//4])
print("Third Quartile Time: ", sorted(wArray)[3*len(wArray)//4]) #TODO: Double Check
print("P[W<=15] = ", len([w for w in wArray if w <= 15])/len(wArray)) #TODO: Double Check
print("P[W<=20] = ", len([w for w in wArray if w <= 20])/len(wArray)) #TODO: Double Check
print("P[W<=30] = ", len([w for w in wArray if w <= 30])/len(wArray)) #TODO: Double Check
print("P[W>40] = ", len([w for w in wArray if w > 40])/len(wArray)) #TODO: Double Check

# W > w5 W > w6 W > w7
# TODO Write print statements for these
#  depict well the right tail of the cumulative distribution function of 𝑊.

















