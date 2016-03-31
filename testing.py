#fp = open("PreProcessStage2Result.txt",'r')
#words = []
#tweet = []

#for lines in fp:
#    line = lines.split()
#    for words in line:
#        tweet.append(words)

#fp.close()
#print tweet

fp = open("FeatureVector.txt",'r')
featureList = []
featureList = (fp.readline().split())
print featureList
fp.close()
