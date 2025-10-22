from scipy.stats import poisson
from GLOBAL_CONSTANTS import M_RENT_A, M_RENT_B, M_RETURN_A, M_RETURN_B, MAX_CARS_PER_STATION

RENT_A_probabilities = []
RENT_B_probabilities = []
RETURN_A_probabilities = []
RETURN_B_probabilities = []

def generateEventProbabilities():
    for cars_count in range(MAX_CARS_PER_STATION + 1):
        RENT_A_probabilities.append(poisson.pmf(cars_count, M_RENT_A))
        RENT_B_probabilities.append(poisson.pmf(cars_count, M_RENT_B))
        RETURN_A_probabilities.append(poisson.pmf(cars_count, M_RETURN_A))
        RETURN_B_probabilities.append(poisson.pmf(cars_count, M_RETURN_B))