from GLOBAL_CONSTANTS import MAX_CARS_PER_STATION

def generateEqualProbabilityPolicy(actions_count):
    probability = float(1) / actions_count
    actions_probability = [probability for _ in range(actions_count)]
    probability_arr = [[None for _ in range(MAX_CARS_PER_STATION)] for _ in range(MAX_CARS_PER_STATION)]
    for i in range(MAX_CARS_PER_STATION):
        for j in range(MAX_CARS_PER_STATION):
            probability_arr[i][j] = actions_probability
    return probability_arr


