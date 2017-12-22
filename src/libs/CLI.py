
from cmd import Cmd
from sys import exit

from .Core import TwitterCore
from .CLI_Show import TwitterCLIShow

class TwitterCLI(Cmd):

    def preloop(self):
        Cmd.preloop(self)

    def start(self):
        self.__twitterCore = TwitterCore()
        self.__twitterCore.login()
        self.__CLIShow = TwitterCLIShow(self.__twitterCore)
        self.prompt='Twitter>>> '

    def do_show(self, line):
        params = line.split()
        if params[0] == 'me':
            if len(params) == 1:
               self.__CLIShow.displayOwnerAccount()
            else:
                command = params[1]
                if command == 'timeline':
                   self.__CLIShow.displayOwnerTimeline()
                elif command == 'follower':
                   self.__CLIShow.displayOwnerFollowers()
                elif command == 'following':
                   self.__CLIShow.displayOwnerFollowings()
                elif command == 'friend':
                   self.__CLIShow.displayOwnerFriends()
                elif command == 'noback':
                   self.__CLIShow.displayOwnerNoBack()
                elif command == 'notbacked':
                   self.__CLIShow.displayOwnerNotBacked()
                elif command == 'home':
                   self.__CLIShow.displayOwnerHome()
        elif params[0] == 'user':
            if len(params) == 2:
                userName = params[1]
                self.__CLIShow.displayAccount(userName)
            else:
                userName = params[1]
                command = params[2]
                if command == 'timeline':
                   self.__CLIShow.displayTimeline(userName)
                elif command == 'follower':
                   self.__CLIShow.displayFollowers(userName)
                elif command == 'following':
                   self.__CLIShow.displayFollowings(userName)
                elif command == 'friend':
                   self.__CLIShow.displayFriends(userName)
                elif command == 'noback':
                   self.__CLIShow.displayNoBack(userName)
                elif command == 'notbacked':
                   self.__CLIShow.displayNotBacked(userName)
        elif params[0] == 'help':
            self.__CLIShow.displayHelp()

    def do_follow(self, line):
        userName = line
        try:
            self.__twitterCore.follow(userName)
        except Exception as e:
                print("Error: %s"%str(e))

    def do_unfollow(self, line):
        userName = line
        try:
            self.__twitterCore.unFollow(userName)
        except Exception as e:
                print("Error: %s"%str(e))

    def do_fave(self, line):
        tweetId = line
        try:
            self.__twitterCore.fave(tweetId)
        except Exception as e:
                print("Error: %s"%str(e))

    def do_unfave(self, line):
        tweetId = line
        try:
            self.__twitterCore.unFave(tweetId)
        except Exception as e:
                print("Error: %s"%str(e))

    def do_retweet(self, line):
        tweetId = line
        try:
            self.__twitterCore.retweet(tweetId)
        except Exception as e:
                print("Error: %s"%str(e))

    def do_exit(self, line):
        exit(1)

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
