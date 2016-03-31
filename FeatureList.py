import re

stopWords = []

def replaceTwoOrMore(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

def getStopWordList(stopWordListFileName):
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords

def getFeatureVector(tweet):
    featureVector = []
    words = tweet.split()
    for w in words:
        w = replaceTwoOrMore(w)
        w = w.strip('\'"?,.')
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector

fp1 = open('PreProcessStage2Result.txt', 'r')
line = fp1.readline()

stopWords = getStopWordList('StopWord.txt')

FV = open('FeatureVector.txt', 'w')

while line:
    featureVector = getFeatureVector(line)
    for words in featureVector:
        FV.write(words + ' ')        
    line = fp1.readline()
    
fp1.close()
FV.close()
