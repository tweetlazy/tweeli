
import tweepy
from configparser import ConfigParser
from os import path
import os
from sys import exit

CONFIG_PATH = '../config/twitter_account_manager.ini'

class TwitterCore:

    def __init__(self):
        self.__account = None

    def login(self):
        'Login to account that exist in config file'

        # Get params from config file
        parser = self.__initConfig()
        consumerKey, consumerSecret, accessKey, accessSecret, proxy = self.__getConfig(parser)

        # Login proccess
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessKey, accessSecret)
        if proxy is None:
            self.__account = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        else:
            self.__account = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, proxy=proxy)

    def __initConfig(self):
        'Return parser of config file'

        # Check config file is exist or not
        if not path.exists(CONFIG_PATH):
            print('[X] Config file does not exist or is invalid.|%s|%s'%(CONFIG_PATH, os.getcwd()))
            exit(1)

        # Read config file
        parser = ConfigParser()
        parser.read(CONFIG_PATH)
        return parser

    def __getConfig(self, parser):
        'Return config params from config file parser'

        # Get application parameters
        consumerKey = parser.get('api', 'CONSUMERKEY')
        consumerSecret = parser.get('api', 'CONSUMERSECRET')
        accessKey = parser.get('api', 'ACCESSKEY')
        accessSecret = parser.get('api', 'ACCESSSECRET')

        # Get proxy settings
        try:
            proxyURL = parser.get('proxy', 'PROXYURL')
            proxyPort = parser.get('proxy', 'PROXYPORT')
            proxy = proxyURL + ':' + proxyPort
        except:
            proxy = None

        return consumerKey, consumerSecret, accessKey, accessSecret, proxy

    def __showUserObj(self, userObj):
        'Convert user object of tweepy to dictionary'

        # Create a dictionary from neccessary informations of a user objec
        User = {'Name':userObj.name,
                'Username':userObj.screen_name,
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

    def showUser(self, userName):
        userObj = self.getUser(userName)
        return self.__showUserObj(userObj)

    def showMyUser(self):
        userObj = self.getMyUser()
        return self.__showUserObj(userObj)

    def getUser(self, userName):
        return self.__account.get_user(screen_name=userName)

    def getMyUser(self):
        return self.__account.me()

    def getFollowers(self, userName, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.followers, screen_name=userName).items()
        else:
            return tweepy.Cursor(self.__account.followers, screen_name=userName, count=count).items()

    def getMyFollowers(self, count=None):
        myUserName = self.getMyUser().screen_name
        if count is None:
            return tweepy.Cursor(self.__account.followers, screen_name=myUserName).items()
        else:
            return tweepy.Cursor(self.__account.followers, screen_name=myUserName, count=count).items()

    def getFollowings(self, userName, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.friends, screen_name=userName).items()
        else:
            return tweepy.Cursor(self.__account.friends, screen_name=userName, count=count).items()

    def getMyFollowings(self, count=None):
        myUserName = self.getMyUser().screen_name
        if count is None:
            return tweepy.Cursor(self.__account.friends, screen_name=myUserName).items()
        else:
            return tweepy.Cursor(self.__account.friends, screen_name=myUserName, count=count).items()

    def getFriends(self, userName, count=None):
        followings = [user for user in self.getFollowings(userName)]
        followersName = [user.screen_name for user in self.getFollowers(userName)]
        users = [user for user in followings if user.screen_name in followersName]
        return users[:count]

    def getMyFriends(self, count=None):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [user for user in followings if user.screen_name in followersName]
        return users[:count]

    def follow(self, userName):
        userObj = self.getUser(userName)
        userObj.follow()

    def unFollow(self, userName):
        userObj = self.getUser(userName)
        userObj.unfollow()

    def friendShip(self, userName1, userName2):
        'Return status of userName1 and userName2->[is_userName1_follow_userName2, is_userName2_follow_userName1]'
        result = self.__account.show_friendship(userName1, userName2)
        return [result['relationship']['target']['following'], result['relationship']['target']['followed_by']]

    def isFollow(self, userName1, userName2):
        'Return userName1 is followed userName2 or not.'
        return self.friendShip(userName1, userName2)[0]

    def getHome(self, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.home_timeline).items()
        else:
            return tweepy.Cursor(self.__account.home_timeline, count=count).items()

    def getTimeline(self, userName, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.user_timeline, screen_name = userName).items()
        else:
            return tweepy.Cursor(self.__account.user_timeline, screen_name = userName, count=count).items()

    def getMyTimeline(self, count=None):
        myUserName = self.getMyUser().screen_name
        if count is None:
            return tweepy.Cursor(self.__account.user_timeline, screen_name = myUserName).items()
        else:
            return tweepy.Cursor(self.__account.user_timeline, screen_name = myUserName, count=count).items()

    def isMention(self, tweet):
        return tweet.in_reply_to_status_id is not None

    def fave(self, tweetId):
        self.__account.create_favorite(tweetId)

    def unFave(self, tweetId):
        self.__account.destroy_favorite(tweetId)

    def faveAll(self, userName):
        tweets = self.getTimeline(userName)
        for tweet in tweets:
            if not self.isMention(tweet):
                try:
                    self.fave(tweet.id)
                except Exception as e:
                    print(e)

    def retweet(self, tweetId):
        self.__account.retweet(tweetId)

    def retweetAll(self, userName):
        tweets = self.getTimeline(userName)
        for tweet in tweets:
            if not self.isMention(tweet):
                try:
                    self.retweet(tweet.id)
                except Exception as e:
                    print(e)

    def getNoBack(self, userName, count=None):
        User = self.getUser(userName)
        followings = self.getFollowings(userName)
        users = [user for user in followings if not self.isFollow(user, User)]
        return users[:count]

    def getMyNoBack(self, count=None):
        'Return list of users that not followed back you.You follow them but they not follow you!'
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        users = [user for user in followings if not self.isFollow(Me, user)]
        return users[:count]

    def getNotBacked(self, userName, count=None):
        followers = self.getFollowers(userName)
        User = self.getUser(userName)
        users = [user for user in followers if not self.isFollow(User, user)]
        return users[:count]

    def getMyNotBacked(self, count=None):
        followers = self.getMyFollowers()
        users = [user for user in followers if not user.following]
        return users[:count]

if __name__ == '__main__':
    pass
