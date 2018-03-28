from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import NLTKTut as tut

def sentiment(text):
    feats = tut.find_features(text)
    return tut.voted_classifier.classify(feats),tut.voted_classifier.confidence(feats)

#consumer key, consumer secret, access token, access secret.
consumer_key = "B5JUDcuhR8SdSLGDtNXWpkVes"
consumer_secret = "479X4KVe8Hz49RDSdUeUQZgwKLlnzAA4FmF9icUKqasXvaM49q"
access_token = "3115213074-Kc6NBqQ3Gtuu4PMCoSxEZIPtMQfy0yBWd9aVYpG"
access_secret = "CVKInuwtxA5DKbqltdBvfkXi32WfwYTY9yy2ion3URY26"

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = sentiment(tweet)
#		print(tweet, sentiment_value, confidence)
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True
    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])