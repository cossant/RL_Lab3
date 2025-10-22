import PolicyEvaluator
import PolicyHelpers
from PuassonGen import *
from GLOBAL_CONSTANTS import MAX_CARS_PER_STATION, STARTING_STATES_WEIGHT
from ACTIONS import *
from Visualisations import *
from PolicyEvaluator import *

# Modules init
generateEventProbabilities()

# Evaluation init
currStateWeights = [[STARTING_STATES_WEIGHT for _ in range(MAX_CARS_PER_STATION + 1)] for _ in range(MAX_CARS_PER_STATION + 1)]
currPolicy = PolicyHelpers.generateEqualProbabilityPolicy(ALL_ACTIONS_COUNT)

# Tests

for testRun in range(1):
    currStateWeights, recieved_delta = PolicyEvaluator._calculateStateWeights(currStateWeights, currPolicy)

print(recieved_delta)
printCurrStateWeights(currStateWeights)

