
from cmd import Cmd
from sys import exit

from .Core import TwitterCore
from .CLI_Show import TwitterCLIShow

class TwitterCLI(Cmd):

    SHOW_USERS = ['me', 'user']
    SHOW_COMMANDS = ['timeline', 'follower', 'following', 'friend', 'noback', 'notbacked', 'home']

    def start(self):
        self.__twitterCore = TwitterCore()
        self.__twitterCore.login()
        self.__CLIShow = TwitterCLIShow(self.__twitterCore)
        self.prompt='Twitter>>> '

    def do_show(self, line):
        if line == 'me':
            self.__CLIShow.displayOwnerAccount()
        elif line == 'me timeline':
            self.__CLIShow.displayOwnerTimeline()
        elif line == 'me follower':
            self.__CLIShow.displayOwnerFollowers()
        elif line == 'me following':
            self.__CLIShow.displayOwnerFollowings()
        elif line == 'me friend':
            self.__CLIShow.displayOwnerFriends()
        elif line == 'me noback':
            self.__CLIShow.displayOwnerNoBack()
        elif line == 'me notbacked':
            self.__CLIShow.displayOwnerNotBacked()
        elif line == 'me home':
            self.__CLIShow.displayOwnerHome()
        elif 'user ' and ' timeline' in line:
            userName = line.split()[1]
            self.__CLIShow.displayTimeline(userName)
        elif 'user ' and ' follower' in line:
            userName = line.split()[1]
            self.__CLIShow.displayFollowers(userName)
        elif 'user ' and ' following' in line:
            userName = line.split()[1]
            self.__CLIShow.displayFollowings(userName)
        elif 'user ' and ' friend' in line:
            userName = line.split()[1]
            self.__CLIShow.displayFriends(userName)
        elif 'user ' and ' noback' in line:
            userName = line.split()[1]
            self.__CLIShow.displayNoBack(userName)
        elif 'user ' and ' notbacked' in line:
            userName = line.split()[1]
            self.__CLIShow.displayNotBacked(userName)
        elif 'user ' in line:
            userName = line.split()[1]
            self.__CLIShow.displayAccount(userName)
        else:
            print("*** Unknown syntax: %s"%line)

    def complete_show(self, text, line, begidx, endidx):
        commands = line.split()
        if not text:
            if len(commands) == 1:
                completions = self.SHOW_USERS[:]
            elif len(commands) == 2 and 'me' in line:
                completions = self.SHOW_COMMANDS[:]
            elif len(commands) == 3:
                completions = self.SHOW_COMMANDS[:]
        else:
            if len(commands) == 2:
                completions = [f for f in self.SHOW_USERS if f.startswith(text)]
            elif len(commands) == 3 and 'me' in line:
                completions = [f for f in self.SHOW_COMMANDS if f.startswith(text)]
            elif len(commands) == 4:
                completions = [f for f in self.SHOW_COMMANDS if f.startswith(text)]
        return completions

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
