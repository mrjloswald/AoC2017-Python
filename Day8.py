def compare( a, b, operator ):
    #print( a, operator, b )
    if operator == ">":
        return a > b
    elif operator == ">=":
        return a >= b
    elif operator == "<":
        return a < b
    elif operator == "<=":
        return  a <= b
    elif operator == "==":
        return a == b
    else:
        return a != b

registers = {}
maxValue = 0
for line in open("Day8_input.txt","r"):
    tokens = line.split()
    register = tokens[0]
    direction = 1 if tokens[1] == "inc" else -1
    value = direction * int(tokens[2])
    if compare( registers.get(tokens[4],0), int(tokens[6]), tokens[5] ):
        #print( "update register " + register + " with " + str(value) )
        registers[register] = registers.get( register, 0 ) + value
        if registers[register] > maxValue:
            maxValue = registers[register]
print( registers )
print( max(registers.values()) )
print( maxValue )
