inputFile = open( "Day6_input.txt", "r")
line = inputFile.read().splitlines()[0]
banks = [int(value) for value in line.split()]
#banks = [0,2,7,0]
currentState = "-".join(str(n) for n in banks)
states = []
stateCounters = []
cycles = 0
while( states.count(currentState) == 0 ):
    states.append( currentState )
    stateCounters.append(0)
    # find largest
    maxValue = banks[0]
    maxIndex = 0
    for i in range(0,len(banks)):
        if banks[i] > maxValue:
            maxIndex = i
            maxValue = banks[i]
    # redistribution
    cycles += 1
    stateCounters = map(lambda x: x + 1, stateCounters)
    banks[maxIndex] = 0
    index = maxIndex + 1
    while maxValue > 0:
        if index >= len( banks ):
            index = 0
        banks[index] += 1
        maxValue -= 1
        index += 1
    # store new state
    currentState = "-".join(str(n) for n in banks)

print( stateCounters[states.index( currentState )] )
