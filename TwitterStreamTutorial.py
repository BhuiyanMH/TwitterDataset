from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumerKey = 'PUT YOUR DATA HERE'
consumerSecret = 'PUT YOUR DATA HERE'
accessToken = 'PUT YOUR DATA HERE'
accessSecret = 'PUT YOUR DATA HERE'
#anger, disgust, fear, guilt, interest, joy, sadness, shame and surprise
class listener(StreamListener):
    def on_data(self, data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]#[1] indicate the right side of the split
            print tweet
            saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitDBAnger.csv', 'a')
            #saveFile.write(data)
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'Failed on data',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["angry"])
#twitterStream.filter(locations=[-180,-90,180,90])
#twitterStream.sample()
