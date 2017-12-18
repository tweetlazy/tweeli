import cmd
import sys
# import readline
# import os

class TwitterCLI(cmd.Cmd):

    def preloop(self):
        cmd.Cmd.preloop(self)

    def init(self, twitterCore):
        self.twitterCore = twitterCore

    def do_myaccountinfo(self, line):
        self.twitterCore.DisplayOwnerAccountInfo()

    def do_myfollowers(self, line):
        self.twitterCore.DisplayMyFollowers()

    def do_myfollowings(self, line):
        self.twitterCore.DisplayFollowingMe()

    def do_userinfo(self, line):
        userName = line
        self.twitterCore.DisplayUserInfo(userName)

    def do_follow(self, line):
        userName = line
        self.twitterCore.Follow(userName)

    def do_unfollow(self, line):
        userName = line
        self.twitterCore.UnFollow(userName)

    def do_fave(self, line):
        tweetId = line
        self.twitterCore.Fave(tweetId)

    def do_unfave(self, line):
        tweetId = line
        self.twitterCore.UnFave(tweetId)

    def do_retweet(self, line):
        tweetId = line
        self.twitterCore.Retweet(tweetId)

    def do_home(self, line):
        self.twitterCore.DisplayHomeTimeline()

    def do_mytimeline(self, line):
        self.twitterCore.DisplayMyTimeline()

    def do_timeline(self, line):
        userName = line
        self.twitterCore.DisplayUserTimeline(userName)

    def do_followingsnotfollowing(self, line):
        self.twitterCore.FollowingsNotFollowing()

    def do_help(self, line):
        print("These shell commands are defined internally!\n\n")
        print("myaccountinfo           show the information of your account")
        print("myfollowers             show your followers")
        print("myfollowings            show your followings")
        print("userinfo                show the information of the user ")
        print("follow                  following new users")
        print("unfollow                unfollow someone ")
        print("followingsnotfollowing  to see who doesnt follow you back ")
        print("timeline                user`s timeline ")
        print("mytimeline              your timeline ")
        print("home                    home timeline ")
        print("fave                    fave a tweet ")
        print("unfave                  unfave a tweet ")
        print("retweet                 retweet a tweet ")

    def do_exit(self, line):
        sys.exit()

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
