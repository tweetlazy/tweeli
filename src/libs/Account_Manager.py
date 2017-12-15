
import tweepy

class AccountManager:

    def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
        self.__consumerKey = consumer_key
        self.__consumerSecret = consumer_secret
        self.__accessKey = access_key
        self.__accessSecret = access_secret
        self.__api = None

    def login(self, proxy=None):
        auth = tweepy.OAuthHandler(self.__consumerKey, self.__consumerSecret)
        auth.set_access_token(self.__accessKey, self.__accessSecret)
        if proxy is None:
            self.__api = tweepy.API(auth)
        else:
            self.__api = tweepy.API(auth, proxy=proxy)

    def showUser(userObj):
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

    def getUserInfo(self, screenName):
        res = self.__api.get_user(screen_name=screenName)
        User = {'Name':res.name,
                'Screen Name':res.screen_name,
                'Bio':res.description,
                'ID':res.id,
                'Protected':res.protected,
                'Location':res.location,
                'Creation Date':res.created_at,
                'Verified':res.verified,
                'Language':res.lang,
                'Followers Count':res.followers_count,
                'Followings Count':res.friends_count,
                'Favourites Count':res.favourites_count,
                'Tweets Count':res.statuses_count,
                'Lists Count':res.listed_count
                }
        return User

    def getMyUserInfo(self):
        res = self.__api.me()
        User = {'Name':res.name,
                'Screen Name':res.screen_name,
                'Bio':res.description,
                'ID':res.id,
                'Protected':res.protected,
                'Location':res.location,
                'Creation Date':res.created_at,
                'Verified':res.verified,
                'Language':res.lang,
                'Followers Count':res.followers_count,
                'Followings Count':res.friends_count,
                'Favourites Count':res.favourites_count,
                'Tweets Count':res.statuses_count,
                'Lists Count':res.listed_count
                }
        return User

    def getFollowers(self, screenName, count=None):
        if count is None:
            return tweepy.Cursor(self.__api.followers, screen_name=screenName).items()
        else:
            return tweepy.Cursor(self.__api.followers, screen_name=screenName, count=count)  .items()          

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

if __name__ == '__main__':
    CONSUMERKEY = ''
    CONSUMERSECRET = ''
    ACCESSKEY = ''
    ACCESSSECRET = ''

    myAccount = AccountManager(CONSUMERKEY, CONSUMERSECRET, ACCESSKEY, ACCESSSECRET)
    myAccount.login()
    # print(myAccount.getUserInfo('smm_taheri'))
    # print(myAccount.getMyUserInfo())
    # res = myAccount.getFollowers('smm_taheri')
    # res = myAccount.getMyFollowers()
    # res = myAccount.getFollowings('smm_taheri')
    res = myAccount.getMyFollowings()
    while True:
        try:
            user = AccountManager.showUser(res.next())
            print(user.items())
            break
        except StopIteration:
            break