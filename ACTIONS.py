from GLOBAL_CONSTANTS import MAX_MOVES, MAX_CARS_PER_STATION

ALL_ACTIONS_COUNT = 2 * MAX_MOVES + 1
ACTIONS = { # A (+)--> B
    0 : -5,
    1 : -4,
    2 : -3,
    3 : -2,
    4 : -1,
    5 : 0,
    6 : +1,
    7 : +2,
    8 : +3,
    9 : +4,
    10 :+5,
}

def applyAction(action_index, station_a_cars, station_b_cars):
    action_operation = ACTIONS[action_index]
    station_a_cars -= action_operation
    station_b_cars += action_operation
    return cropValue(station_a_cars), cropValue(station_b_cars)

def cropValue(value, lower_crop = 0, upper_crop = MAX_CARS_PER_STATION):
    if value < lower_crop:
        value = lower_crop
    if value > upper_crop:
        value = upper_crop
    return value
