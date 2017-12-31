
class TwitterCLIShow:

    def __init__(self, account):
        self.__account = account

    def displayOwnerAccount(self):
        "Show owner account details"
        print("\nYour Account Details :")
        print("==============================")
        data = self.__account.showMyUser()
        for key, value in data.items():
            print (key, value)
        print("==============================")

    def displayAccount(self, userName):
        "Show account details"
        print("\nUser %s Account Details :"%userName)
        print("==============================")
        info = self.__account.showUser(userName)
        for key, value in info.items():
            print(key, value)
        print("==============================")

    def displayOwnerTimeline(self, count=None):
        "Show owner tweets in timeline"
        tweets = self.__account.getMyTimeline() if count is None else self.__account.getMyTimeline(count)
        print("\nYour Timeline:")
        for tweet in tweets:
            try:
                print("==============================")
                print("Tweet id : " + str(tweet.id))
                print (tweet.user.screen_name + " tweeted :")
                print(tweet.text)
                print("==============================")
            except Exception as e:
                print("Error: %s"%str(e))

    def displayTimeline(self, userName, count=None):
        "Show tweets in timeline"
        tweets = self.__account.getTimeline(userName) if count is None else self.__account.getTimeline(userName, count)
        print("\nUser %s Timeline:"%userName)
        for tweet in tweets:
            try:
                print("==============================")
                print("Tweet id : " + str(tweet.id))
                print (tweet.user.screen_name + " tweeted :")
                print(tweet.text)
                print("==============================")
            except Exception as e:
                print("Error: %s"%str(e))

    def displayOwnerFollowers(self, count=None):
        "Show owner followers"
        followers = self.__account.getMyFollowers() if count is None else self.__account.getMyFollowers(count)
        print("\nThey Are Following You:")
        print("==============================")
        for follower in followers:
            try:
                print(follower.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayFollowers(self, userName, count=None):
        "Show followers"
        followers = self.__account.getFollowers(userName) if count is None else self.__account.getFollowers(userName, count)
        print("\nThey Are Following User %s:"%userName)
        print("==============================")
        for follower in followers:
            try:
                print(follower.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayOwnerFollowings(self, count=None):
        "Show owner followings"
        followings = self.__account.getMyFollowings() if count is None else self.__account.getMyFollowings(count)
        print("\nYou Are Following:")
        print("==============================")
        for following in followings:
            try:
                print(following.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayFollowings(self, userName, count=None):
        "Show followings"
        followings = self.__account.getFollowings(userName) if count is None else self.__account.getFollowings(userName, count)
        print("\nUser %s Are Following:"%userName)
        print("==============================")
        for following in followings:
            try:
                print(following.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayOwnerFriends(self, count=None):
        "Show owner users both you and them followed each other"
        users = self.__account.getMyFriends() if count is None else self.__account.getMyFriends(count)
        print("\nYour Friends:")
        print("==============================")
        for user in users:
            try:
                print(user.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayFriends(self, userName, count=None):
        "Show users both hi/she and them followed each other"
        users = self.__account.getFriends(userName) if count is None else self.__account.getFriends(userName, count)
        print("\nUser %s Friends:"%userName)
        print("==============================")
        for user in users:
            try:
                print(user.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayOwnerNoBack(self, count=None):
        "Show owner users not follow back you"
        users = self.__account.getMyNoBack() if count is None else self.__account.getMyNoBack(count)
        print("\nThey Did Not Followed Back You:")
        print("==============================")
        for user in users:
            try:
                print(user.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayNoBack(self, userName, count=None):
        "Show users not follow back user"
        users = self.__account.getNoBack(userName) if count is None else self.__account.getNoBack(userName, count)
        print("\nThey Did Not Followed Back User %s:"%userName)
        print("==============================")
        for user in users:
            try:
                print(user.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayOwnerNotBacked(self, count=None):
        "Show owner users not followed back by you"
        users = self.__account.getMyNotBacked() if count is None else self.__account.getMyNotBacked(count)
        print("\nYou Did Not Followed Back:")
        print("==============================")
        for user in users:
            try:
                print(user.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayNotBacked(self, userName, count=None):
        "Show users not followed back by user"
        users = self.__account.getNotBacked(userName) if count is None else self.__account.getNotBacked(userName, count)
        print("\nUser %s Did Not Followed Back:"%userName)
        print("==============================")
        for user in users:
            try:
                print(user.screen_name)
            except Exception as e:
                print("Error: %s"%str(e))
        print("==============================")

    def displayOwnerHome(self, count=None):
        "Show owner tweets in home"
        tweets = self.__account.getHome() if count is None else self.__account.getHome(count)
        print("\nYour Home:")
        print("==============================")
        for tweet in tweets:
            try:
                print("===========================")
                print("Tweet id : " + str(tweet.id))
                print(tweet.user.screen_name + " tweeted :")
                print(tweet.text)
                print("===========================")
            except Exception as e:
                print("Error: %s"%str(e))
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
