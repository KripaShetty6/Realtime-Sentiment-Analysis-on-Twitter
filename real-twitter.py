from twython import TwythonStreamer
print ("########################################Started")
class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print (data['text'].encode('utf-8'))

    def on_error(self, status_code, data):
        print (status_code)
        self.disconnect()


# replace these with the details from your Twitter Application
consumer_key = 'zzKX9uyqxb7O7RMnwF5cAZtqI'
consumer_secret = 'zS62gAmSoHKhne4mziFFNJsWHHeReuWqMTrUYYwYdzqhjZWigK'
access_token = '3257507474-1Twt7HuhS2Q1OIgiKU161DTEnEjRZuthWh4VYbs'
access_token_secret = 'pNRIJAYwFoQHXuHtCgrkNEz08P3K9TM66K8j0p2UaKs9d'

streamer = TweetStreamer(consumer_key, consumer_secret,
                         access_token, access_token_secret)

streamer.statuses.filter(track = 'india')