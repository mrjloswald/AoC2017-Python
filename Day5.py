inputFile = open( "Day5_input.txt", "r")
tape = [int(line.strip()) for line in inputFile]
#tape = [0,3,0,1,-3]
index = 0
steps = 0
while( index < len(tape) and tape[index] + index < len(tape) ):
    nextIndex = tape[index] + index
    if tape[index] >= 3:
        tape[index] -= 1
    else:
        tape[index] += 1
    index = nextIndex
    steps += 1
print( steps + 1)
