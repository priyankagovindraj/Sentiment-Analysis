UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def loadDictionary():
    dictionaryFile = open("dictionary.txt","r")
    englishWords = set(line.strip() for line in open('dictionary.txt'))
    dictionaryFile.close()
    return englishWords



f  = open("PreProcessStage1Result.txt","r")
f2 = open("PreProcessStage2Result.txt","a")
ENGLISH_WORDS = loadDictionary()

for lines in f:
    x = lines
    y = removeNonLetters(x)
    z = y.split()

    for i in z:
        if i in ENGLISH_WORDS:
            f2.write(i)
            f2.write(' ')
    f2.write('\n')
   
f.close()
f2.close()
