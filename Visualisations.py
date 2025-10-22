def printCurrStateWeights(state_weights):
    for line in state_weights:
        for element in line:
            print(round(element, 4), end=' ')
        print()