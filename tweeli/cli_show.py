
class TwitterCLIShow:

    def __init__(self, account):
        self.__account = account

    def __userObjDict(self, userObj):
        'Convert user object of tweepy to dictionary'

        # Create a dictionary from neccessary informations of a user object
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

    def __tweetObjDict(self, tweetObj):
        'Convert tweet object of tweepy to dictionary'

        # Create a dictionary from neccessary informations of a tweet object
        Tweet = {'Author Name':tweetObj.author.name,
                'Author UserName':tweetObj.author.screen_name,
                'ID':tweetObj.id,
                'Text':tweetObj.text,
                'HashTags':' '.join([f['text'] for f in tweetObj.entities['hashtags']]),
                'Location':tweetObj.place,
                'Creation Date':tweetObj.created_at,
                'Is Quote':tweetObj.is_quote_status,
                'Is Faved By You':tweetObj.favorited,
                'Is Reted By You':tweetObj.retweeted,
                'Language':tweetObj.lang,
                'Favorites Count':tweetObj.favorite_count,
                'Retweets Count':tweetObj.retweet_count
                }
        return Tweet

    def userDict(self, userName):
        userObj = self.__account.getUser(userName=userName)
        return self.__userObjDict(userObj)

    def myUserDict(self):
        userObj = self.__account.getMyUser()
        return self.__userObjDict(userObj)

    def tweetDict(self, tweetID):
        tweetObj = self.__account.getTweet(tweetID=tweetID)
        return self.__tweetObjDict(tweetObj)

    def handleShowMe(self, line):
        commandSegments = line.split()
        if line == 'me':
            self.displayOwnerAccount()
            return True
        elif line.startswith('me timeline'):
            if line == 'me timeline':
                self.displayOwnerTimeline()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayOwnerTimeline(int(count))
                    return True
        elif line.startswith('me follower'):
            if line == 'me follower':
                self.displayOwnerFollowers()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayOwnerFollowers(int(count))
                    return True
        elif line.startswith('me following'):
            if line == 'me following':
                self.displayOwnerFollowings()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayOwnerFollowings(int(count))
                    return True
        elif line.startswith('me friend'):
            if line == 'me friend':
                self.displayOwnerFriends()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayOwnerFriends(int(count))
                    return True
        elif line.startswith('me noback'):
            if line == 'me noback':
                self.displayOwnerNoBack()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayOwnerNoBack(int(count))
                    return True
        elif line.startswith('me home'):
            if line == 'me home':
                self.displayOwnerHome()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayOwnerHome(int(count))
                    return True
        return False

    def handleShowUser(self, line):
        commandSegments = line.split()
        if len(commandSegments) < 1:
            return False
        userName = commandSegments[1]
        if len(commandSegments) == 2:
            self.displayAccount(userName)
            return True
        elif commandSegments[2] == 'timeline':
            if len(commandSegments) == 3:
                self.displayTimeline(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayTimeline(userName, int(count))
                    return True
        elif commandSegments[2] == 'follower':
            if len(commandSegments) == 3:
                self.displayFollowers(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayFollowers(userName, int(count))
                    return True
        elif commandSegments[2] == 'following':
            if len(commandSegments) == 3:
                self.displayFollowings(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayFollowings(userName, int(count))
                    return True
        elif commandSegments[2] == 'friend':
            if len(commandSegments) == 3:
                self.displayFriends(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayFriends(userName, int(count))
                    return True
        elif commandSegments[2] == 'noback':
            if len(commandSegments) == 3:
                self.displayUserNoBack(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayUserNoBack(userName, int(count))
                    return True
        return False

    def handleNoback(self, line):
        commandSegments = line.split()
        if line.startswith('noback me'):
            if line == 'noback me':
                self.displayNoBackOwner()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayNoBackOwner(int(count))
                    return True
        elif line.startswith('noback user'):
            if len(commandSegments) == 3:
                userName = commandSegments[2]
                self.displayNoBackUser(userName)
                return True
            elif len(commandSegments) == 4:
                userName = commandSegments[2]
                count = commandSegments[-1]
                if count.isdigit():
                    self.displayNoBackUser(userName, int(count))
                    return True

    def displayOwnerAccount(self):
        "Show owner account details"
        print("\nYour Account Details:")
        print("==============================")
        data = self.myUserDict()
        for key, value in data.items():
            print (key, value)
        print("==============================")

    def displayAccount(self, userName):
        "Show account details"
        print("\nUser %s Account Details:"%userName)
        print("==============================")
        info = self.userDict(userName)
        for key, value in info.items():
            print(key, value)
        print("==============================")

    def displayTweet(self, tweetID):
        "Show tweet details"
        print("\nTweet %s Details:"%tweetID)
        print("==============================")
        info = self.tweetDict(tweetID)
        for key, value in info.items():
            print(key, value)
        print("==============================")

    def displayOwnerTimeline(self, count=None):
        "Show owner tweets in timeline"
        tweets = self.__account.getMyTimeline(count=count)
        print("\nYour Timeline:")
        print("==============================")
        print("=========================")
        for tweet in tweets:
            try:
                data = self.__tweetObjDict(tweet)
                for key, value in data.items():
                    print (key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")            
        print("==============================")

    def displayTimeline(self, userName, count=None):
        "Show tweets in timeline"
        tweets = self.__account.getTimeline(userName=userName, count=count)
        print("\nUser %s Timeline:"%userName)
        print("==============================")
        print("=========================")        
        for tweet in tweets:
            try:
                data = self.__tweetObjDict(tweet)
                for key, value in data.items():
                    print (key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayOwnerFollowers(self, count=None):
        "Show owner followers"
        followers = self.__account.getMyFollowers(count=count)
        print("\nThey Are Following You:")
        print("==============================")
        print("=========================")
        for follower in followers:
            try:
                info = self.__userObjDict(follower)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayFollowers(self, userName, count=None):
        "Show followers"
        followers = self.__account.getFollowers(userName=userName, count=count)
        print("\nThey Are Following User %s:"%userName)
        print("==============================")
        print("=========================")
        for follower in followers:
            try:
                info = self.__userObjDict(follower)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayOwnerFollowings(self, count=None):
        "Show owner followings"
        followings = self.__account.getMyFollowings(count=count)
        print("\nYou Are Following:")
        print("==============================")
        print("=========================")
        for following in followings:
            try:
                info = self.__userObjDict(following)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayFollowings(self, userName, count=None):
        "Show followings"
        followings = self.__account.getFollowings(userName=userName, count=count)
        print("\nUser %s Are Following:"%userName)
        print("==============================")
        print("=========================")
        for following in followings:
            try:
                info = self.__userObjDict(following)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayOwnerFriends(self, count=None):
        "Show owner users both you and them followed each other"
        friends = self.__account.getMyFriends(count=count)
        print("\nYour Friends:")
        print("==============================")
        print("=========================")
        for friend in friends:
            try:
                info = self.__userObjDict(friend)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayFriends(self, userName, count=None):
        "Show users both hi/she and them followed each other"
        friends = self.__account.getFriends(userName, count=count)
        print("\nUser %s Friends:"%userName)
        print("==============================")
        print("=========================")
        for friend in friends:
            try:
                info = self.__userObjDict(friend)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayNoBackOwner(self, count=None):
        "Show owner users not follow back you"
        users = self.__account.getNoBackMe(count=count)
        print("\nThey Did Not Followed Back You:")
        print("==============================")
        print("=========================")
        for user in users:
            try:
                info = self.__userObjDict(user)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayNoBackUser(self, userName, count=None):
        "Show users not follow back user"
        users = self.__account.getNoBackUser(userName=userName, count=count)
        print("\nThey Did Not Followed Back User %s:"%userName)
        print("==============================")
        print("=========================")
        for user in users:
            try:
                info = self.__userObjDict(user)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayOwnerNoBack(self, count=None):
        "Show owner users not followed back by you"
        users = self.__account.getMeNoBack(count=count)
        print("\nYou Did Not Followed Back:")
        print("==============================")
        print("=========================")
        for user in users:
            try:
                info = self.__userObjDict(user)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayUserNoBack(self, userName, count=None):
        "Show users not followed back by user"
        users = self.__account.getUserNoBack(userName=userName, count=count)
        print("\nUser %s Did Not Followed Back:"%userName)
        print("==============================")
        print("=========================")
        for user in users:
            try:
                info = self.__userObjDict(user)
                for key, value in info.items():
                    print(key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayOwnerHome(self, count=None):
        "Show owner tweets in home"
        tweets = self.__account.getHome(count=count)
        print("\nYour Home:")
        print("==============================")
        print("=========================")
        for tweet in tweets:
            try:
                data = self.__tweetObjDict(tweet)
                for key, value in data.items():
                    print (key, value)
            except Exception as e:
                print("Error: %s"%str(e))
            print("=========================")
        print("==============================")

    def displayHelp(self):
        print("\nThese shell commands are defined internally!\n\n")
        print("show me                                   Show your account details. ")
        print("show me follower                          Show your followers. ")
        print("show me following                         Show your followings. ")
        print("show me friend                            Show your friends.You and them both followed each other. ")
        print("show me noback                            Show users that not followed back you. ")
        print("show me notbacked                         Show users that you not followed back them. ")
        print("show me timeline                          Show your timeline tweets. ")
        print("show me home                              Show your home tweets. ")
        print("show user [username]                      Show user [X] account details. ")
        print("show user [username] follower             Show user [X] followers. ")
        print("show user [username] following            Show user [X] followings. ")
        print("show user [username] friend               Show user [X] friends.You and them both followed each other. ")
        print("show user [username] noback               Show users that not followed back user [X]. ")
        print("show user [username] notbacked            Show users that user [X] not followed back them. ")
        print("show user [username] timeline             Show user [X] timeline tweets. ")
        print("follow [username]                         Follow user [X]")
        print("unfollow [username]                       UnFollow user [X]")
        print("fave [tweetid]                            Favorite tweet [X]")
        print("unfave [tweetid]                          Unfavorite tweet [X]")
        print("retweet [tweetid]                         Retweet tweet [X]")


if __name__ == '__main__':
    # from Core import TwitterCore
    # if os.path.exists('./.CLI_history'):
    #     readline.read_history_file('./.CLI_history')
    # TCore = TwitterCore('../config/twitter_account_manager.ini')
    # myCmd = TwitterCLI()
    # myCmd.init(TCore)
    # myCmd.prompt='Twitter>>> '
    # myCmd.cmdloop(TCore)
    # readline.write_history_file('./.CLI_history')
    pass
