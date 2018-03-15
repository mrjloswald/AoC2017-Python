f = open("Day9_test1_input.txt","r")
line = f.readline()

score = 0
depth = 0
garbage = False
ignoringNext = False
for ch in line:
    if garbage:
        if ignoringNext:
            ignoringNext = False
        elif ch == "!":
            ignoringNext = True
        elif ch == ">":
            garbage = False
    else:
        if ch == "{":
            depth += 1
        elif ch == "}":
            score += depth
            depth -= 1
        elif ch == "<":
            garbage = True

print( score )
