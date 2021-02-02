import tweepy
consumerKey = 'ldbZte7f6sWNjil4nRvr2KqfK'
consumerSecret = 'J2TMLInVqvKx4fncBB3db1oc9KbRch2jj2UoMASRrikLJh3v2P'
accessToken = '1354446685670264836-yxFzwreEscrqRVgVmNO29wbNHVN5j6'
accessTokenSecret = 'FmAnUvYHONF9RRbfJ59AM0ImAuZr9M1b9m6dOtNawk0We'

class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''
    def on_status(self, status):
        print(status.id)
        print(status.user.name)
        print(status.text)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True 

listener = TwitterStreamListener()
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
stream = tweepy.streaming.Stream(auth, listener)
stream.filter(track=['#Tesla'])
