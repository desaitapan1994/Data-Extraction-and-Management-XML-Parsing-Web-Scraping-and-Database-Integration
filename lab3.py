
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Enter Twitter API Keys
access_token = "1312877331703361536-gt1C0Zto3Rven1QLNR4HvE5skEkVmc"
access_token_secret = "CjN1xs2AsiAU77ACZ1T5FNduAQr6i1XbDCo2VH99Kf5v7"
consumer_key = "OKr6dwJ0Tb7nJf2vgE63ya6Pv"
consumer_secret = "o9vbI8154bKJRpnykgS2u4i0Jwvd1sPVWN8T5iUzFMpeBN9OeT"

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
      
    def on_data(self, data):   
        print(data)
        return True
        

    def on_error(self, status):
        print(status)


if __name__ == '__main__':  
# Handle Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter("#iphone12","#iphone")