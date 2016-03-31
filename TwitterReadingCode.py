from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey= '4Nb42wFU3j24Ih519IBvrSxMw'
csecret= '7Dh6W7TDZcpbNB6o2KbzGorzSZxQs3yzBLc8drOM0mgxJKxqVK'
atoken= '2718944394-EblILqMDkrSyHUWmmttXTruLd590AQloLhN8Q20'
asecret= '8mzN8H1AUkxNMVaJ9iKXkA3557FQOivKasFqAD0RcVWME'

class listener(StreamListener):
	def on_data(self, data):
		try:
			#print data
			tweet=data.split(',"text":"')[1].split(',"source"')[0]
			print tweet
			saveThis=tweet
			saveFile=open('twitDB3.txt','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True	
		except BaseException,e:
			print 'failed on data',str(e)
			time.sleep(5)	
	
	def on_error(self, status):
		print status

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["car"])
