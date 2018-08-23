import tweepy


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return False


def main():

    # Authenticate with Twitter
    credentials = {}
    with open('./secrets.txt', 'r') as infile:
        for line in infile.readlines():
            if ":" in line:
                key_val = line.split(': ',1)
                credentials[key_val[0]] = key_val[1].strip()

    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth)

    # Stream Tweets
    # myStreamListener = MyStreamListener()
    myStreamListener = StdOutListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    myStream.filter(track=['NIKEiD', 'nike', 'nike custom OR customized'], async=False)

if __name__ == "__main__":
    main()
