
import tweepy

class TwitterAccountManager:

    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        self.__consumerKey = consumer_key
        self.__consumerSecret = consumer_secret
        self.__accessKey = access_key
        self.__accessSecret = access_secret
        self.__api = None

# Twitter API has a limited rate : https://developer.twitter.com/en/docs/basics/rate-limiting
# Added wait_on_rate_limit to true to automatically wait for rate limits tor eplenish
# Added wait_on_rate_limit_notify to true since it will print a notification when Tweepy is waiting for rate limits to replenish
    def login(self, proxy=None):
        auth = tweepy.OAuthHandler(self.__consumerKey, self.__consumerSecret)
        auth.set_access_token(self.__accessKey, self.__accessSecret)
        if proxy is None:
            self.__api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        else:
            self.__api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, proxy=proxy)

    def showUser(self, userObj):
        User = {'Name':userObj.name,
                'Screen Name':userObj.screen_name,
                'Bio':userObj.description,
                'ID':userObj.id,
                'Protected':userObj.protected,
                'Location':userObj.location,
                'Creation Date':userObj.created_at,
                'Verified':userObj.verified,
                'Language':userObj.lang,
                'Followers Count':userObj.followers_count,
                'Followings Count':userObj.friends_count,
                'Favourites Count':userObj.favourites_count,
                'Tweets Count':userObj.statuses_count,
                'Lists Count':userObj.listed_count
                }
        return User

    def getUser(self, screenName):
        return self.__api.get_user(screen_name=screenName)

    def getMyUser(self):
        return self.__api.me()

    def getUserInfo(self, screenName):
        userObj = self.getUser(screenName)
        return self.showUser(userObj)

    def getMyUserInfo(self):
        userObj = self.getMyUser()
        return self.showUser(userObj)

    def getFollowers(self, screenName, count=None):
        if count is None:
            return tweepy.Cursor(self.__api.followers, screen_name=screenName).items()
        else:
            return tweepy.Cursor(self.__api.followers, screen_name=screenName, count=count).items()

    def getMyFollowers(self, count=None):
        myScreenName = self.getMyUserInfo()['Screen Name']
        if count is None:
            return tweepy.Cursor(self.__api.followers, screen_name=myScreenName).items()
        else:
            return tweepy.Cursor(self.__api.followers, screen_name=myScreenName, count=count).items()

    def getFollowings(self, screenName, count=None):
        if count is None:
            return tweepy.Cursor(self.__api.friends, screen_name=screenName).items()
        else:
            return tweepy.Cursor(self.__api.friends, screen_name=screenName, count=count).items()

    def getMyFollowings(self, count=None):
        myScreenName = self.getMyUserInfo()['Screen Name']
        if count is None:
            return tweepy.Cursor(self.__api.friends, screen_name=myScreenName).items()
        else:
            return tweepy.Cursor(self.__api.friends, screen_name=myScreenName, count=count).items()

    def follow(self, screenName):
        userObj = self.getUser(screenName)
        userObj.follow()

    def unfollow(self, screenName):
        userObj = self.getUser(screenName)
        userObj.unfollow()

    def getHomeTimeline(self, count=None):
        if count is None:
            return tweepy.Cursor(self.__api.home_timeline).items()
        else:
            return tweepy.Cursor(self.__api.home_timeline, count=count).items()

    def getTimeline(self, screenName, count=None):
        if count is None:
            return tweepy.Cursor(self.__api.user_timeline, screen_name = screenName).items()
        else:
            return tweepy.Cursor(self.__api.user_timeline, screen_name = screenName, count=count).items()

    def getMyTimeline(self, count=None):
        myScreenName = self.getMyUserInfo()['Screen Name']
        if count is None:
            return tweepy.Cursor(self.__api.user_timeline, screen_name = myScreenName).items()
        else:
            return tweepy.Cursor(self.__api.user_timeline, screen_name = myScreenName, count=count).items()

    def isMention(self, tweet):
        return tweet.in_reply_to_status_id is not None

    def fave(self, tweetId):
        self.__api.create_favorite(tweetId)

    def unfave(self, tweetId):
        self.__api.destroy_favorite(tweetId)

    def faveAll(self, screenName):
        tweets = self.getTimeline(screenName)
        for tweet in tweets:
            if not self.isMention(tweet):
                try:
                    self.fave(tweet.id)
                except Exception as e:
                    print(e)

    def retweet(self, tweetId):
        self.__api.retweet(tweetId)


    def retweetAll(self, screenName):
        tweets = self.getTimeline(screenName)
        for tweet in tweets:
            if not self.isMention(tweet):
                try:
                    self.retweet(tweet.id)
                except Exception as e:
                    print(e)

    def noBackFollowings(self):
        userObj = self.getMyUser()
        myFollowings = [f.screen_name for f in self.getMyFollowings()]
        myFollowers = [f.screen_name for f in self.getMyFollowers()]
        nBack = [user for user in myFollowings if not user in myFollowers]
        return nBack

if __name__ == '__main__':
    pass
