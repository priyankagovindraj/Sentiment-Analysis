import re
import string

def processTweet(tweet):
    tweet = tweet.lower()
    tweet = tweet.replace('(www\.[^\s]+)','URL')
   
    tweet = tweet.replace('http:\/\/t.co\/','URL')
    tweet = tweet.replace('\u [a-z0-9]*',' ')
    tweet = tweet.replace('http:\/','URL')  
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = re.sub('/n',' ', tweet)  
    tweet = tweet.strip('http')
    f = open('twitDB3.txt','r')
    line = f.readline()
    line.replace('"',' ')
    return tweet

fp = open('twitDB3.txt', 'r')
saveFile = open('PreProcessStage1Result.txt','a')
line = fp.readline()

while line:
    processedTweet = processTweet(line)
    #print processedTweet
    saveFile.write(processedTweet)
    saveFile.write('\n')
    line = fp.readline()

fp.close()
saveFile.close()
