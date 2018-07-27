
import json
from configparser import ConfigParser
from os import path

# third-party imports
import tweepy

DEFAULT_CONFIG_PATH = 'config/config.ini'

class TwitterCore:

    def __init__(self):
        self.__account = None

    def login(self, **kwargs):
        'Login to account'

        if kwargs == {}:
            # Get params from config file
            parser = self.__initConfig(DEFAULT_CONFIG_PATH)
            consumerKey, consumerSecret, accessKey, accessSecret, proxy = self.__getConfig(parser)
        elif "configPath" in kwargs:
            # Get params from config file
            configPath = kwargs["configPath"]
            parser = self.__initConfig(configPath)
            consumerKey, consumerSecret, accessKey, accessSecret, proxy = self.__getConfig(parser)
        else:
            if "consumerKey" in kwargs:
                consumerKey = kwargs["consumerKey"]
            else:
                return {'status_code':'400', 'description':'Param consumerKey Is Not Exist!'}
            if "consumerSecret" in kwargs:
                consumerSecret = kwargs["consumerSecret"]
            else:
                return {'status_code':'400', 'description':'Param consumerSecret Is Not Exist!'}
            if "accessKey" in kwargs:
                accessKey = kwargs["accessKey"]
            else:
                return {'status_code':'400', 'description':'Param accessKey Is Not Exist!'}
            if "accessSecret" in kwargs:
                accessSecret = kwargs["accessSecret"]
            else:
                return {'status_code':'400', 'description':'Param accessSecret Is Not Exist!'}
            if "proxy" in kwargs:
                proxy = kwargs["proxy"]
            else:
                proxy = None
        # Login proccess
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessKey, accessSecret)
        if proxy is None:
            self.__account = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        else:
            self.__account = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, proxy=proxy)
        return True

    def __initConfig(self, configPath):
        'Return parser of config file'

        # Check config file is exist or not
        if not path.exists(configPath):
            print('[X] Config file is not exist or is invalid.')
            exit(1)

        # Read config file
        parser = ConfigParser()
        parser.read(configPath)
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

    def getUser(self, **kwargs):
        if "userName" in kwargs:
            userName = kwargs["userName"]
            response = self.__account.get_user(screen_name=userName)
            return response
        else:
            raise ValueError('Param userName is not exist!')

    def getMyUser(self, **kwargs):
        return self.__account.me()

    def getTweet(self, **kwargs):
        if "tweetID" in kwargs:
            tweetID = kwargs["tweetID"]
            return self.__account.get_status(id=tweetID)
        else:
            raise ValueError('Param tweetID is not exist!')

    def getFollowers(self, **kwargs):
        if "userName" in kwargs:
            userName = kwargs["userName"]
            if "count" in kwargs:
                count = int(kwargs["count"])
                if count is not None:
                    return tweepy.Cursor(self.__account.followers, screen_name=userName).items(count)
            return tweepy.Cursor(self.__account.followers, screen_name=userName).items()
        else:
            raise ValueError('Param userName is not exist!')

    def getFollowerIDs(self, **kwargs):
        followers = self.getFollowers(**kwargs)
        followerIDs = ''
        for follower in followers:
            followerIDs += ',' + (str(follower.id))
        return followerIDs[1:]

    def getFollowerUserNames(self, **kwargs):
        followers = self.getFollowers(**kwargs)
        followerUserNames = ''
        for follower in followers:
            followerUserNames += ',' + (follower.screen_name)
        return followerUserNames[1:]

    def getMyFollowers(self, **kwargs):
        myUserName = self.getMyUser().screen_name
        kwargs["userName"] = myUserName
        return self.getFollowers(**kwargs)

    def getMyFollowerIDs(self, **kwargs):
        followers = self.getMyFollowers(**kwargs)
        followerIDs = ''
        for follower in followers:
            followerIDs += ',' + (str(follower.id))
        return followerIDs[1:]

    def getMyFollowerUserNames(self, **kwargs):
        followers = self.getMyFollowers(**kwargs)
        followerUserNames = ''
        for follower in followers:
            followerUserNames += ',' + (follower.screen_name)
        return followerUserNames[1:]

    def getFollowings(self, **kwargs):
        if "userName" in kwargs:
            userName = kwargs["userName"]
            if "count" in kwargs:
                count = int(kwargs["count"])
                if count is not None:
                    return tweepy.Cursor(self.__account.friends, screen_name=userName).items(count)
            return tweepy.Cursor(self.__account.friends, screen_name=userName).items()
        else:
            raise ValueError('Param userName is not exist!')

    def getFollowingIDs(self, **kwargs):
        followings = self.getFollowings(**kwargs)
        followingIDs = ''
        for following in followings:
            followingIDs += ',' + (str(following.id))
        return followingIDs[1:]

    def getFollowingUserNames(self, **kwargs):
        followings = self.getFollowings(**kwargs)
        followingUserNames = ''
        for following in followings:
            followingUserNames += ',' + (str(following.screen_name))
        return followingUserNames[1:]

    def getMyFollowings(self, **kwargs):
        myUserName = self.getMyUser().screen_name
        kwargs["userName"] = myUserName
        return self.getFollowings(**kwargs)

    def getMyFollowingIDs(self, **kwargs):
        followings = self.getMyFollowings(**kwargs)
        followingIDs = ''
        for following in followings:
            followingIDs += ',' + (str(following.id))
        return followingIDs[1:]

    def getMyFollowingUserNames(self, **kwargs):
        followings = self.getMyFollowings(**kwargs)
        followingUserNames = ''
        for following in followings:
            followingUserNames += ',' + (following.screen_name)
        return followingUserNames[1:]

    def getFriends(self, **kwargs):
        followings = [user for user in self.getFollowings(**kwargs)]
        followersName = [user.screen_name for user in self.getFollowers(**kwargs)]
        users = [user for user in followings if user.screen_name in followersName]
        count = int(kwargs["count"])
        return users[:count]

    def getFriendIDs(self, **kwargs):
        followings = [user for user in self.getFollowings(**kwargs)]
        followersName = [user.screen_name for user in self.getFollowers(**kwargs)]
        users = [str(user.id) for user in followings if user.screen_name in followersName]
        count = int(kwargs["count"])
        return ','.join(users[:count])

    def getFriendUserNames(self, **kwargs):
        followings = [user for user in self.getFollowings(**kwargs)]
        followersName = [user.screen_name for user in self.getFollowers(**kwargs)]
        users = [user.screen_name for user in followings if user.screen_name in followersName]
        count = int(kwargs["count"])
        return ','.join(users[:count])

    def getMyFriends(self, **kwargs):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [user for user in followings if user.screen_name in followersName]
        count = int(kwargs["count"])
        return users[:count]

    def getMyFriendIDs(self, **kwargs):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [str(user.id) for user in followings if user.screen_name in followersName]
        count = int(kwargs["count"])
        return ','.join(users[:count])

    def getMyFriendUserNames(self, **kwargs):
        followings = [user for user in self.getMyFollowings()]
        followersName = [user.screen_name for user in self.getMyFollowers()]
        users = [user.screen_name for user in followings if user.screen_name in followersName]
        count = int(kwargs["count"])
        return ','.join(users[:count])

    def follow(self, **kwargs):
        userObj = self.getUser(**kwargs)
        userObj.follow()

    def unFollow(self, **kwargs):
        userObj = self.getUser(**kwargs)
        userObj.unfollow()

    def friendShip(self, **kwargs):
        'Return status of userName1 and userName2->[is_srcUserName_follow_dstUserName, is_dstUserName_follow_srcUserName]'
        if "srcUserName" in kwargs:
            srcUserName = kwargs["srcUserName"]
        else:
            raise ValueError('Param srcUserName is not exist!')
        if "dstUserName" in kwargs:
            dstUserName = kwargs["dstUserName"]
        else:
            raise ValueError('Param dstUserName is not exist!')
        result = self.__account.show_friendship(source_screen_name=srcUserName, target_screen_name=dstUserName)
        return [result[0].following, result[0].followed_by]

    def isFollow(self, **kwargs):
        'Return srcUserName is followed dstUserName or not.'
        return self.friendShip(**kwargs)[0]

    def isFriend(self, **kwargs):
        'Return both of srcUserName and dstUserName followed each other or not.'
        friendShip = self.friendShip(**kwargs)[0]
        return friendShip[0] and friendShip[1]

    def getHome(self, **kwargs):
        if "count" in kwargs:
            count = int(kwargs["count"])
            if count is not None:
                return tweepy.Cursor(self.__account.home_timeline).items(count)
        return tweepy.Cursor(self.__account.home_timeline).items()

    def getHomeTweetIDs(self, **kwargs):
        tweets = self.getHome(**kwargs)
        tweetIDs = ''
        for tweet in tweets:
            tweetIDs += ',' + (str(tweet.id))
        return tweetIDs[1:]

    def getTimeline(self, **kwargs):
        if "userName" in kwargs:
            userName = kwargs["userName"]
            if "count" in kwargs:
                count = int(kwargs["count"])
                if count is not None:
                    return tweepy.Cursor(self.__account.user_timeline, screen_name=userName).items(count)
            return tweepy.Cursor(self.__account.user_timeline, screen_name=userName).items()
        else:
            raise ValueError('Param userName is not exist!')

    def getTimelineTweetIDs(self, **kwargs):
        tweets = self.getTimeline(**kwargs)
        tweetIDs = ''
        for tweet in tweets:
            tweetIDs += ',' + (str(tweet.id))
        return tweetIDs[1:]

    def getMyTimeline(self, **kwargs):
        myUserName = self.getMyUser().screen_name
        if "count" in kwargs:
            count = int(kwargs["count"])
            if count is not None:
                return tweepy.Cursor(self.__account.user_timeline, screen_name=myUserName).items(count)
        return tweepy.Cursor(self.__account.user_timeline, screen_name=myUserName).items()

    def getMyTimelineTweetIDs(self, **kwargs):
        tweets = self.getMyTimeline(**kwargs)
        tweetIDs = ''
        for tweet in tweets:
            tweetIDs += ',' + (str(tweet.id))
        return tweetIDs[1:]

    def isMention(self, **kwargs):
        tweet = self.getTweet(**kwargs)
        return tweet.in_reply_to_status_id is not None

    def fave(self, **kwargs):
        if "tweetID" in kwargs:
            tweetID = kwargs["tweetID"]
            self.__account.create_favorite(tweetID)
        else:
            raise ValueError('Param tweetID is not exist!')

    def unFave(self, **kwargs):
        if "tweetID" in kwargs:
            tweetID = kwargs["tweetID"]
            self.__account.destroy_favorite(tweetID)
        else:
            raise ValueError('Param tweetID is not exist!')

    def retweet(self, **kwargs):
        if "tweetID" in kwargs:
            tweetID = kwargs["tweetID"]
            self.__account.retweet(tweetID)
        else:
            raise ValueError('Param tweetID is not exist!')

    def getNoBackUser(self, **kwargs):
        User = self.getUser(**kwargs)
        followings = self.getFollowings(**kwargs)
        users = []
        for user in followings:
            if not self.isFollow(srcUserName=user.screen_name, dstUserName=User.screen_name):
                users.append(user)
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return users[:count]

    def getNoBackUserIDs(self, **kwargs):
        User = self.getUser(**kwargs)
        followings = self.getFollowings(**kwargs)
        users = []
        for user in followings:
            if not self.isFollow(srcUserName=user.screen_name, dstUserName=User.screen_name):
                users.append(str(user.id))
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getNoBackUserUserNames(self, **kwargs):
        User = self.getUser(**kwargs)
        followings = self.getFollowings(**kwargs)
        users = []
        for user in followings:
            if not self.isFollow(srcUserName=user.screen_name, dstUserName=User.screen_name):
                users.append(user.screen_name)
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getNoBackMe(self, **kwargs):
        'Return list of users that not followed back you.You follow them but they not follow you!'
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        # users = [user for user in followings if not self.isFollow(Me, user)]
        users = []
        for user in followings:
            if not self.isFollow(srcUserName=user.screen_name, dstUserName=Me.screen_name):
                users.append(user)
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return users[:count]
    
    def getNoBackMeIDs(self, **kwargs):
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        users = []
        for user in followings:
            if not self.isFollow(srcUserName=user.screen_name, dstUserName=Me.screen_name):
                users.append(str(user.id))
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getNoBackMeUserNames(self, **kwargs):
        followings = self.getMyFollowings()
        Me = self.getMyUser()
        users = []
        for user in followings:
            if not self.isFollow(srcUserName=user.screen_name, dstUserName=Me.screen_name):
                users.append(user.screen_name)
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getUserNoBack(self, **kwargs):
        followers = self.getFollowers(**kwargs)
        User = self.getUser(**kwargs)
        users = []
        for user in followers:
            if not self.isFollow(srcUserName=User.screen_name, dstUserName=user.screen_name):
                users.append(user)
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return users[:count]

    def getUserNoBackIDs(self, **kwargs):
        followers = self.getFollowers(**kwargs)
        User = self.getUser(**kwargs)
        users = []
        for user in followers:
            if not self.isFollow(srcUserName=User.screen_name, dstUserName=user.screen_name):
                users.append(str(user.id))
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getUserNoBackUserNames(self, **kwargs):
        followers = self.getFollowers(**kwargs)
        User = self.getUser(**kwargs)
        users = []
        for user in followers:
            if not self.isFollow(srcUserName=User.screen_name, dstUserName=user.screen_name):
                users.append(user.screen_name)
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getMeNoBack(self, **kwargs):
        followers = self.getMyFollowers()
        users = [user for user in followers if not user.following]
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return users[:count]

    def getMeNoBackIDs(self, **kwargs):
        followers = self.getMyFollowers()
        users = [str(user.id) for user in followers if not user.following]
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getMeNoBackUserNames(self, **kwargs):
        followers = self.getMyFollowers()
        users = [user.screen_name for user in followers if not user.following]
        if "count" in kwargs:
            count = int(kwargs["count"])
        else:
            count = None
        return ','.join(users[:count])

    def getMeFaves(self):
        pass

    def getUserFaves(self, **kwargs):
        pass

    def getFavesMe(self):
        pass

    def getFavesUser(self, **kwargs):
        pass

    def getMeRetweets(self):
        pass

    def getUserRetweets(self, **kwargs):
        pass

    def getRetweetsMe(self):
        pass

    def getRetweetsUser(self, **kwargs):
        pass

    def getMeTweetWithMentions(self):
        pass

    def getUserTweetWihtMentions(self, **kwargs):
        pass

    def getMeTweetWithNoMentions(self):
        pass

    def getUserTweetWithNoMentions(self):
        pass

    def getMeList(self):
        pass

    def getUserList(self, **kwargs):
        pass

    def getMeReplies(self):
        pass

    def getUserReplies(self, **kwargs):
        pass

    def getLastMeActivity(self):
        pass

    def getLastUserActivity(self, **kwargs):
        pass

    def getMePinTweet(self):
        pass

    def getUserPinTweet(self, **kwargs):
        pass

    def getTweetFaves(self, **kwargs):
        pass

    def getTweetRetweets(self, **kwargs):
        pass

    def getTweetReplies(self, **kwargs):
        pass

    def getTweetReplires(self, **kwargs):
        pass

    def getUserMentions(self, **kwargs):
        pass

    def getMeMentions(self, **kwargs):
        pass

    def fetchMeState(self):
        pass

    def fetchUserState(self, **kwargs):
        pass

    def updateMeDB(self):
        pass

    def updateUserDB(self, **kwargs):
        pass

if __name__ == '__main__':
    pass
