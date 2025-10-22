from GLOBAL_CONSTANTS import MAX_CARS_PER_STATION, R_MOVE, COEFF_OF_FORGET
from ACTIONS import ALL_ACTIONS_COUNT, applyAction, ACTIONS

def acquireGreedyPolicy(state_weights):
    greedy_policy = [[[0 for action_probability in range(ALL_ACTIONS_COUNT)] \
                         for cars_count_in_b in range(MAX_CARS_PER_STATION)] \
                         for cars_count_in_a in range(MAX_CARS_PER_STATION)] # Actions * Cars * Cars = Actions * States
    for cars_count_in_a in range(MAX_CARS_PER_STATION):
        for cars_count_in_b in range(MAX_CARS_PER_STATION):
            greedy_actions_indexes = _getGreedyActionIndex(_calculateActionWeights(state_weights, (cars_count_in_a, cars_count_in_b)))
            partial_probability = float(1) / len(greedy_actions_indexes)
            for index in greedy_actions_indexes:
                greedy_policy[cars_count_in_a][cars_count_in_b][index] = partial_probability

def convergeWeights(start_weights, policy, desired_delta):
    new_weights = None
    while True:
        new_weights, delta = _calculateStateWeights(start_weights, policy)
        if delta <= desired_delta:
            break
    return new_weights

def _calculateStateWeights(previous_state_weights, current_policy):
    CARS_RANGE = range(MAX_CARS_PER_STATION)
    new_state_weights = [[None for cars_count_in_b in CARS_RANGE] for cars_count_in_a in CARS_RANGE]
    actions_probability = []
    actions_weight = []
    max_delta = 0

    # Foreach state
    for cars_count_in_a in CARS_RANGE:
        for cars_count_in_b in CARS_RANGE:
            #Foreach probabilities
            for cars_rent_a in CARS_RANGE:
                for cars_rent_b in CARS_RANGE:
                    for cars_returned_a in CARS_RANGE:
                        for cars_returned_b in CARS_RANGE:
                            # Foreach actions
                            actions_probability = current_policy[cars_count_in_a][cars_count_in_b]
                            actions_weight = _calculateActionWeights(previous_state_weights, (cars_count_in_a, cars_count_in_b))
                            state_weight = 0
                            for action_index in range(ALL_ACTIONS_COUNT):
                                state_weight += actions_weight[action_index] * actions_probability[action_index]
                            new_state_weights[cars_count_in_a][cars_count_in_b] = state_weight
    state_delta = abs(state_weight - previous_state_weights[cars_count_in_a][cars_count_in_b])
    if state_delta > max_delta:
        max_delta = state_delta
    return new_state_weights, max_delta


def _calculateActionWeights(state_weights, current_state : tuple[int, int]):
    weights = []
    for action_index in range(ALL_ACTIONS_COUNT):
        weights.append(_calculateActionWeight(action_index, current_state, state_weights))
    return weights

def _calculateActionWeight(action_index, current_state : tuple[int, int], state_weights):
    cars_in_a, cars_in_b = current_state
    applyAction(action_index, cars_in_a, cars_in_b)
    reward = abs(ACTIONS[action_index]) * R_MOVE
    new_state_weight = state_weights[cars_in_a][cars_in_b]
    action_weight = reward + COEFF_OF_FORGET * new_state_weight
    return action_weight

def _getGreedyActionIndex(action_weights_array):
    max_weight = action_weights_array[0]
    max_weight_indexes = [0]
    for i in range(len(action_weights_array)):
        if action_weights_array[i] > max_weight:
            max_weight_indexes = [i]
        if action_weights_array[i] == max_weight:
            max_weight_indexes.append(i)
    return max_weight_indexes