
from cmd import Cmd
from sys import exit

from .Core import TwitterCore
from .CLI_Show import TwitterCLIShow

class TwitterCLI(Cmd):

    SHOW_LEVEL_ONE = ['me', 'user']
    SHOW_LEVEL_TWO = ['timeline', 'follower', 'following', 'friend', 'home']
    SHOW_LEVEL_SHARE = ['noback']

    def start(self):
        self.__twitterCore = TwitterCore()
        self.__twitterCore.login()
        self.__CLIShow = TwitterCLIShow(self.__twitterCore)
        self.prompt='Twitter>>> '

    def handleShowMe(self, line):
        commandSegments = line.split()
        if line == 'me':
            self.__CLIShow.displayOwnerAccount()
            return True
        elif line.startswith('me timeline'):
            if line == 'me timeline':
                self.__CLIShow.displayOwnerTimeline()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerTimeline(int(count))
                    return True
        elif line.startswith('me follower'):
            if line == 'me follower':
                self.__CLIShow.displayOwnerFollowers()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerFollowers(int(count))
                    return True
        elif line.startswith('me following'):
            if line == 'me following':
                self.__CLIShow.displayOwnerFollowings()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerFollowings(int(count))
                    return True
        elif line.startswith('me friend'):
            if line == 'me friend':
                self.__CLIShow.displayOwnerFriends()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerFriends(int(count))
                    return True
        elif line.startswith('me noback'):
            if line == 'me noback':
                self.__CLIShow.displayOwnerNotBacked()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerNotBacked(int(count))
                    return True
        elif line.startswith('me home'):
            if line == 'me home':
                self.__CLIShow.displayOwnerHome()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerHome(int(count))
                    return True
        self.showError(line)
        return False

    def handleShowUser(self, line):
        commandSegments = line.split()
        if len(commandSegments) < 1:
            self.showError(line)
            return False
        userName = commandSegments[1]
        if len(commandSegments) == 2:
            self.__CLIShow.displayTimeline(userName)
            return True
        elif commandSegments[2] == 'timeline':
            if len(commandSegments) == 3:
                self.__CLIShow.displayTimeline(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayTimeline(userName, int(count))
                    return True
        elif commandSegments[2] == 'follower':
            if len(commandSegments) == 3:
                self.__CLIShow.displayFollowers(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayFollowers(userName, int(count))
                    return True
        elif commandSegments[2] == 'following':
            if len(commandSegments) == 3:
                self.__CLIShow.displayFollowings(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayFollowings(userName, int(count))
                    return True
        elif commandSegments[2] == 'friend':
            if len(commandSegments) == 3:
                self.__CLIShow.displayFriends(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayFriends(userName, int(count))
                    return True
        elif commandSegments[2] == 'noback':
            if len(commandSegments) == 3:
                self.__CLIShow.displayNotBacked(userName)
                return True
            elif len(commandSegments) == 4:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayNotBacked(userName, int(count))
                    return True
        self.showError(line)
        return False

    def handleNoback(self, line):
        commandSegments = line.split()
        if line.startswith('noback me'):
            if line == 'noback me':
                self.__CLIShow.displayOwnerNoBack()
                return True
            elif len(commandSegments) == 3:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayOwnerNoBack(int(count))
                    return True
        elif line.startswith('noback user'):
            if len(commandSegments) == 3:
                userName = commandSegments[2]
                self.__CLIShow.displayNoBack(userName)
                return True
            elif len(commandSegments) == 4:
                userName = commandSegments[2]
                count = commandSegments[-1]
                if count.isdigit():
                    self.__CLIShow.displayNoBack(userName, int(count))
                    return True

    def showError(self, line):
        print("*** Unknown syntax: %s"%line)

    def do_show(self, line):
        commandFrags = line.split()
        showCommandFlag = False
        if line.startswith('me'):
            self.handleShowMe(line)
        elif line.startswith('user'):
            self.handleShowUser(line)
        elif line.startswith('noback'):
            self.handleNoback(line)

    def complete_show(self, text, line, begidx, endidx):
        commands = line.split()
        if not text:
            if len(commands) == 1:
                completions = self.SHOW_LEVEL_ONE[:] + self.SHOW_LEVEL_SHARE[:]
            elif len(commands) == 2:
                if commands[1] == 'noback':
                    completions = self.SHOW_LEVEL_ONE[:]
                elif commands[1] == 'me':
                    completions = self.SHOW_LEVEL_TWO[:] + self.SHOW_LEVEL_SHARE[:]
            elif len(commands) == 3:
                if commands[1] == 'user':
                    completions = self.SHOW_LEVEL_TWO[:-1] + self.SHOW_LEVEL_SHARE[:]
        else:
            if len(commands) == 2:
                completions = [f for f in self.SHOW_LEVEL_ONE + self.SHOW_LEVEL_SHARE if f.startswith(text)]
            elif len(commands) == 3:
                if commands[1] == 'noback':
                    completions = [f for f in self.SHOW_LEVEL_ONE if f.startswith(text)]
                elif commands[1] == 'me':
                    completions = [f for f in self.SHOW_LEVEL_TWO + self.SHOW_LEVEL_SHARE if f.startswith(text)]
            elif len(commands) == 4:
                if commands[1] == 'user':
                    completions = [f for f in self.SHOW_LEVEL_TWO[:-1] + self.SHOW_LEVEL_SHARE if f.startswith(text)]
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
