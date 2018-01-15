
import tweepy
from configparser import ConfigParser
from os import path
import os
from sys import exit

CONFIG_PATH = 'config/twitter_account_manager.ini'

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
            print('[X] Config file does not exist or is invalid.')
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

    def getUser(self, userName):
        return self.__account.get_user(screen_name=userName)

    def getMyUser(self):
        return self.__account.me()

    def getTweet(self, tweetID):
        return self.__account.get_status(id=tweetID)

    def getFollowers(self, userName, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.followers, screen_name=userName).items()
        else:
            return tweepy.Cursor(self.__account.followers, screen_name=userName).items(count)

    def getFollowerIDs(self, userName, count=None):
        followers = self.getFollowers(userName) if count is None else self.getFollowers(userName, count)
        followerIDs = []
        for follower in followers:
            followerIDs.append(str(follower.id))
        return ','.join(followerIDs)

    def getFollowerUserNames(self, userName, count=None):
        followers = self.getFollowers(userName) if count is None else self.getFollowers(userName, count)
        followerUserNames = []
        for follower in followers:
            followerUserNames.append(follower.screen_name)
        return ','.join(followerUserNames)

    def getMyFollowers(self, count=None):
        myUserName = self.getMyUser().screen_name
        return self.getFollowers(myUserName) if count is None else self.getFollowers(myUserName, count)

    def getMyFollowerIDs(self, count=None):
        followers = self.getMyFollowers() if count is None else self.getMyFollowers(count)
        followerIDs = []
        for follower in followers:
            followerIDs.append(str(follower.id))
        return ','.join(followerIDs)

    def getMyFollowerUserNames(self, count=None):
        followers = self.getMyFollowers() if count is None else self.getMyFollowers(count)
        followerUserNames = []
        for follower in followers:
            followerUserNames.append(follower.screen_name)
        return ','.join(followerUserNames)

    def getFollowings(self, userName, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.friends, screen_name=userName).items()
        else:
            return tweepy.Cursor(self.__account.friends, screen_name=userName).items(count)

    def getFollowingIDs(self, userName, count=None):
        followings = self.getFollowings(userName) if count is None else self.getFollowings(userName, count)
        followingIDs = []
        for following in followings:
            followingIDs.append(str(following.id))
        return ','.join(followingIDs)

    def getFollowingUserNames(self, userName, count=None):
        followings = self.getFollowings(userName) if count is None else self.getFollowings(userName, count)
        followingUserNames = []
        for following in followings:
            followingUserNames.append(str(following.screen_name))
        return ','.join(followingUserNames)

    def getMyFollowings(self, count=None):
        myUserName = self.getMyUser().screen_name
        return self.getFollowings(myUserName) if count is None else self.getFollowings(myUserName, count)

    def getMyFollowingIDs(self, count=None):
        followings = self.getMyFollowings() if count is None else self.getMyFollowings(count)
        followingIDs = []
        for following in followings:
            followingIDs.append(str(following.id))
        return ','.join(followingIDs)

    def getMyFollowingUserNames(self, count=None):
        followings = self.getMyFollowings() if count is None else self.getMyFollowings(count)
        followingUserNames = []
        for following in followings:
            followingUserNames.append(following.screen_name)
        return ','.join(followingUserNames)

    def getFriends(self, userName, count=None):
        followings = [user for user in self.getFollowings(userName)]
        followersName = [user.screen_name for user in self.getFollowers(userName)]
        users = [user for user in followings if user.screen_name in followersName]
        return users[:count]

    def getFriendIDs(self, userName, count=None):
        followings = [user for user in self.getFollowings(userName)]
        followersName = [user.screen_name for user in self.getFollowers(userName)]
        users = [str(user.id) for user in followings if user.screen_name in followersName]
        return ','.join(users[:count])

    def getFriendUserNames(self, userName, count=None):
        followings = [user for user in self.getFollowings(userName)]
        followersName = [user.screen_name for user in self.getFollowers(userName)]
        users = [user.screen_name for user in followings if user.screen_name in followersName]
        return ','.join(users[:count])

    def getMyFriends(self, count=None):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [user for user in followings if user.screen_name in followersName]
        return users[:count]

    def getMyFriendIDs(self, count=None):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [str(user.id) for user in followings if user.screen_name in followersName]
        return ','.join(users[:count])

    def getMyFriendUserNames(self, count=None):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [user.screen_name for user in followings if user.screen_name in followersName]
        return ','.join(users[:count])

    def follow(self, userName):
        userObj = self.getUser(userName)
        userObj.follow()

    def unFollow(self, userName):
        userObj = self.getUser(userName)
        userObj.unfollow()

    def friendShip(self, userName1, userName2):
        'Return status of userName1 and userName2->[is_userName1_follow_userName2, is_userName2_follow_userName1]'
        result = self.__account.show_friendship(source_screen_name=userName1, target_screen_name=userName2)
        return [result[0].following, result[0].followed_by]

    def isFollow(self, userName1, userName2):
        'Return userName1 is followed userName2 or not.'
        return self.friendShip(userName1, userName2)[0]

    def isFriend(self, userName1, userName2):
        'Return both of userName1 and userName2 followed each other or not.'
        friendShip = self.friendShip(userName1, userName2)[0]
        return friendShip[0] and friendShip[1]

    def getHome(self, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.home_timeline).items()
        else:
            return tweepy.Cursor(self.__account.home_timeline).items(count)

    def getHomeTweetIDs(self, count=None):
        tweets = self.getHome() if count is None else self.getHome(count)
        tweetIDs = []
        for tweet in tweets:
            tweetIDs.append(str(tweet.id))
        return ','.join(tweetIDs)

    def getTimeline(self, userName, count=None):
        if count is None:
            return tweepy.Cursor(self.__account.user_timeline, screen_name=userName).items()
        else:
            return tweepy.Cursor(self.__account.user_timeline, screen_name=userName).items(count)

    def getTimelineTweetIDs(self, userName, count=None):
        tweets = self.getTimeline(userName) if count is None else self.getTimeline(userName, count)
        tweetIDs = []
        for tweet in tweets:
            tweetIDs.append(str(tweet.id))
        return ','.join(tweetIDs)

    def getMyTimeline(self, count=None):
        myUserName = self.getMyUser().screen_name
        if count is None:
            return tweepy.Cursor(self.__account.user_timeline, screen_name=myUserName).items()
        else:
            return tweepy.Cursor(self.__account.user_timeline, screen_name=myUserName).items(count)

    def getMyTimelineTweetIDs(self, count=None):
        tweets = self.getMyTimeline() if count is None else self.getMyTimeline(count)
        tweetIDs = []
        for tweet in tweets:
            tweetIDs.append(str(tweet.id))
        return ','.join(tweetIDs)

    def isMention(self, tweet):
        return tweet.in_reply_to_status_id is not None

    def fave(self, tweetID):
        self.__account.create_favorite(tweetID)

    def unFave(self, tweetID):
        self.__account.destroy_favorite(tweetID)

    def retweet(self, tweetID):
        self.__account.retweet(tweetID)

    def getNoBackUser(self, userName, count=None):
        User = self.getUser(userName)
        followings = self.getFollowings(userName)
        users = []
        for user in followings:
            if not self.isFollow(user.screen_name, User.screen_name):
                users.append(user)
        return users[:count]

    def getNoBackUserIDs(self, count=None):
        User = self.getUser(userName)
        followings = self.getFollowings(userName)
        users = []
        for user in followings:
            if not self.isFollow(user.screen_name, User.screen_name):
                users.append(str(user.id))
        return ','.join(users[:count])

    def getNoBackUserUserNames(self, count=None):
        User = self.getUser(userName)
        followings = self.getFollowings(userName)
        users = []
        for user in followings:
            if not self.isFollow(user.screen_name, User.screen_name):
                users.append(user.screen_name)
        return ','.join(users[:count])

    def getNoBackMe(self, count=None):
        'Return list of users that not followed back you.You follow them but they not follow you!'
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        # users = [user for user in followings if not self.isFollow(Me, user)]
        users = []
        for user in followings:
            if not self.isFollow(user.screen_name, Me.screen_name):
                users.append(user)
        return users[:count]
    
    def getNoBackMeIDs(self, count=None):
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        users = []
        for user in followings:
            if not self.isFollow(user.screen_name, Me.screen_name):
                users.append(str(user.id))
        return ','.join(users[:count])

    def getNoBackMeUserNames(self, count=None):
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        users = []
        for user in followings:
            if not self.isFollow(user.screen_name, Me.screen_name):
                users.append(user.screen_name)
        return ','.join(users[:count])

    def getUserNoBack(self, userName, count=None):
        followers = self.getFollowers(userName)
        User = self.getUser(userName)
        users = []
        for user in followers:
            if not self.isFollow(User.screen_name, user.screen_name):
                users.append(user)
        return users[:count]

    def getUserNoBackIDs(self, userName, count=None):
        followers = self.getFollowers(userName)
        User = self.getUser(userName)
        users = []
        for user in followers:
            if not self.isFollow(User.screen_name, user.screen_name):
                users.append(str(user.id))
        return ','.join(users[:count])

    def getUserNoBackUserNames(self, userName, count=None):
        followers = self.getFollowers(userName)
        User = self.getUser(userName)
        users = []
        for user in followers:
            if not self.isFollow(User.screen_name, user.screen_name):
                users.append(user.screen_name)
        return ','.join(users[:count])

    def getMeNoBack(self, count=None):
        followers = self.getMyFollowers()
        users = [user for user in followers if not user.following]
        return users[:count]

    def getMeNoBackIDs(self, count=None):
        followers = self.getMyFollowers()
        users = [str(user.id) for user in followers if not user.following]
        return ','.join(users[:count])

    def getMeNoBackUserNames(self, count=None):
        followers = self.getMyFollowers()
        users = [user.screen_name for user in followers if not user.following]
        return ','.join(users[:count])

if __name__ == '__main__':
    pass
