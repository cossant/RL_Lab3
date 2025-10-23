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

def memoize(f):
  cache = {}
  def helper(*args):
    if args not in cache:
      cache[args] = f(*args)
    return cache[args]
  return helper

@memoize
def _poisson_pmf(n, process_name):
    match process_name:
        case "RENT_A":
            return RENT_A_probabilities[n]
        case "RENT_B":
            return RENT_B_probabilities[n]
        case "RETURN_A":
            return RETURN_A_probabilities[n]
        case "RETURN_B":
            return RETURN_B_probabilities[n]
        case _:
            raise ImportError("Poisson invoked for unknown process")

@memoize
def poisson_pmf(n, n_max, process_name):
  if n > n_max:
    return 0
  if n == n_max:
    return 1-sum([_poisson_pmf(n,process_name) for n in range(n_max)]) # Т.к. перебирает не все комбинации, то последней возможной в таком случае комбинации присваивается сумма всех оставшихся вероятностей.
  return _poisson_pmf(n, process_name)