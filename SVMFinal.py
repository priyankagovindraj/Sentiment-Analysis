import re
import svm
from svmutil import *

def getSVMFeatureVectorAndLabels(tweets, featureList):
    sortedFeatures = sorted(featureList)
    map = {}
    feature_vector = []
    labels = []
    for t in tweets:
        label = 0
        map = {}
        for w in sortedFeatures:
            map[w] = 0

        tweet_words = t[0]
        tweet_opinion = 'positive'
        for word in tweet_words:
            word = replaceTwoOrMore(word)
            word = word.strip('\'"?,.')
            if word in map:
                map[word] = 1
        values = map.values()
        feature_vector.append(values)
        if(tweet_opinion == 'positive'):
            label = 0
        elif(tweet_opinion == 'negative'):
            label = 1
        elif(tweet_opinion == 'neutral'):
            label = 2
        labels.append(label)
    return {'feature_vector' : feature_vector, 'labels': labels}

def replaceTwoOrMore(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

labels = [0, 1, 1, 2]
samples = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 0, 0]]

TwF = open("PreProcessStage2Result.txt",'r')
FL  = open("FeatureVector.txt","r")
words = []
tweets = []
featureList = []

for lines in TwF:
    line = lines.split()
    for words in line:
        tweets.append(words)
featureList = (FL.readline().split())
TwF.close()
FL.close()

result = getSVMFeatureVectorAndLabels(tweets, featureList)
problem = svm_problem(labels,samples)
param = svm_parameter('-q')
param.kernel_type = LINEAR
classifier = svm_train(problem, param)
svm_save_model('model_file', classifier)
test_data = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
#test_feature_vector = getSVMFeatureVector(test_tweets, featureList)
p_labels, p_accs, p_vals = svm_predict([0] * len(test_data),test_data, classifier)
print p_labels
