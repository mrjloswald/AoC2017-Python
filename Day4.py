inputFile = open( "Day4_input.txt", "r")
passphrases = 0
invalidPassphrases = 0
for line in inputFile:
    passphrases += 1
    wordsInLine = []
    for word in line.split():
        letters = sorted(list(word))
        word = ''.join(letters)
        if wordsInLine.count(word) > 0:
            invalidPassphrases += 1
            break
        else:
            wordsInLine.append(word)
inputFile.close()

print( passphrases-invalidPassphrases )
