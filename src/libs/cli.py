
from cmd import Cmd
from sys import exit

from .cli_show import TwitterCLIShow
from .core import TwitterCore


class TwitterCLI(Cmd):

    MAIN_COMMANDS = ['show', 'follow' , 'unfollow', 'fave', 'unfave', 'retweet', 'me', 'user']
    SHOW_LEVEL_ONE = ['me', 'user', 'tweet']
    SHOW_LEVEL_TWO = ['timeline', 'follower', 'following', 'friend', 'home']
    SHOW_LEVEL_SHARE = ['noback']

    def start(self):
        self.__twitterCore = TwitterCore()
        self.__twitterCore.login()
        self.__CLIShow = TwitterCLIShow(self.__twitterCore)
        self.prompt =  'Twitter>>> '
        self.__output = None

    def do_show(self, line):
        if line.startswith('me'):
            if not self.__CLIShow.handleShowMe(line):
                self.error(line)
        elif line.startswith('user'):
            if not self.__CLIShow.handleShowUser(line):
                self.error(line)
        elif line.startswith('noback'):
            if not self.__CLIShow.handleNoback(line):
                self.error(line)
        elif line.startswith('tweet'):
            commandSegments = line.split()
            trueSyntax = False
            if len(commandSegments) == 2:
                tweetID = commandSegments[-1]
                if tweetID.isdigit():
                    try:
                        self.__CLIShow.displayTweet(tweetID)
                        trueSyntax = True
                    except Exception as e:
                        print("Error: %s"%str(e))
            if not trueSyntax:
                self.error(line)
        else:
            self.error(line)

    def complete_show(self, text, line, begidx, endidx):
        masterCommands = line.split('|')
        commandSegments = masterCommands[-1].split()
        completions = []
        if not text:
            if len(commandSegments) == 1:
                completions = self.SHOW_LEVEL_ONE[:] + self.SHOW_LEVEL_SHARE[:]
            elif len(commandSegments) == 2:
                if commandSegments[1] == 'noback':
                    completions = self.SHOW_LEVEL_ONE[:]
                elif commandSegments[1] == 'me':
                    completions = self.SHOW_LEVEL_TWO[:] + self.SHOW_LEVEL_SHARE[:]
            elif len(commandSegments) == 3:
                if commandSegments[1] == 'user':
                    completions = self.SHOW_LEVEL_TWO[:-1] + self.SHOW_LEVEL_SHARE[:]
        else:
            if len(commandSegments) == 2:
                completions = [f for f in self.SHOW_LEVEL_ONE + self.SHOW_LEVEL_SHARE if f.startswith(text)]
            elif len(commandSegments) == 3:
                if commandSegments[1] == 'noback':
                    completions = [f for f in self.SHOW_LEVEL_ONE if f.startswith(text)]
                elif commandSegments[1] == 'me':
                    completions = [f for f in self.SHOW_LEVEL_TWO + self.SHOW_LEVEL_SHARE if f.startswith(text)]
            elif len(commandSegments) == 4:
                if commandSegments[1] == 'user':
                    completions = [f for f in self.SHOW_LEVEL_TWO[:-1] + self.SHOW_LEVEL_SHARE if f.startswith(text)]
        return completions

    def do_follow(self, line):
        userNames = line.split(',')
        for userName in userNames:
            try:
                self.__twitterCore.follow(userName=userName)
            except Exception as e:
                print("Error: %s"%str(e))

    def do_unfollow(self, line):
        userNames = line.split(',')
        for userName in userNames:
            try:
                self.__twitterCore.unFollow(userName=userName)
            except Exception as e:
                print("Error: %s"%str(e))

    def do_fave(self, line):
        tweetIDs = line.split(',')
        for tweetID in tweetIDs:
            try:
                self.__twitterCore.fave(tweetID=tweetID)
            except Exception as e:
                print("Error: %s"%str(e))

    def do_unfave(self, line):
        tweetIDs = line.split(',')
        for tweetID in tweetIDs:
            try:
                self.__twitterCore.unFave(tweetID=tweetID)
            except Exception as e:
                print("Error: %s"%str(e))

    def do_retweet(self, line):
        tweetIDs = line.split(',')
        for tweetID in tweetIDs:
            try:
                self.__twitterCore.retweet(tweetID=tweetID)
            except Exception as e:
                print("Error: %s"%str(e))

    def do_me(self, line):
        commandSegments = line.split()
        trueSyntax = False
        if line == '':
            self.__output = self.__twitterCore.getMyUser().screen_name
            trueSyntax = True
        elif line.startswith('timeline'):
            if line == 'timeline':
                self.__output = self.__twitterCore.getMyTimelineTweetIDs()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getMyTimelineTweetIDs(count=int(count))
                    trueSyntax = True
        elif line.startswith('follower'):
            if line == 'follower':
                self.__output = self.__twitterCore.getMyFollowerUserNames()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getMyFollowerUserNames(count=int(count))
                    trueSyntax = True
        elif line.startswith('following'):
            if line == 'following':
                self.__output = self.__twitterCore.getMyFollowingUserNames()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getMyFollowingUserNames(count=int(count))
                    trueSyntax = True
        elif line.startswith('friend'):
            if line == 'friend':
                self.__output = self.__twitterCore.getMyFriendUserNames()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getMyFriendUserNames(count=int(count))
                    trueSyntax = True
        elif line.startswith('noback'):
            if line == 'noback':
                self.__output = self.__twitterCore.getMeNoBackUserNames()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getMeNoBackUserNames(count=int(count))
                    trueSyntax = True
        elif line.startswith('home'):
            if line == 'home':
                self.__output = self.__twitterCore.getHomeTweetIDs()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getHomeTweetIDs(count=int(count))
                    trueSyntax = True
        if not trueSyntax:
            self.error(line)
    
    def complete_me(self, text, line, begidx, endidx):
        masterCommands = line.split('|')
        commandSegments = masterCommands[-1].split()
        completions = []
        if not text:
            if len(commandSegments) == 1:
                completions = self.SHOW_LEVEL_TWO[:] + self.SHOW_LEVEL_SHARE[:]
        else:
            if len(commandSegments) == 2:
                completions = [f for f in self.SHOW_LEVEL_TWO + self.SHOW_LEVEL_SHARE if f.startswith(text)]
        return completions

    def do_user(self, line):
        commandSegments = line.split()
        trueSyntax = False
        if len(commandSegments) >= 1:
            userName = commandSegments[0]
            if len(commandSegments) == 1:
                self.__output = self.__twitterCore.getUser(userName=userName).screen_name
                trueSyntax = True
            elif commandSegments[1] == 'timeline':
                if len(commandSegments) == 2:
                    self.__output = self.__twitterCore.getTimelineTweetIDs(userName=userName)
                    trueSyntax = True
                elif len(commandSegments) == 3:
                    count = commandSegments[-1]
                    if count.isdigit():
                        self.__output = self.__twitterCore.getTimelineTweetIDs(userName=userName, count=int(count))
                        trueSyntax = True
            elif commandSegments[1] == 'follower':
                if len(commandSegments) == 2:
                    self.__output = self.__twitterCore.getFollowerUserNames(userName=userName)
                    trueSyntax = True
                elif len(commandSegments) == 3:
                    count = commandSegments[-1]
                    if count.isdigit():
                        self.__output = self.__twitterCore.getFollowerUserNames(userName=userName, count=int(count))
                        trueSyntax = True
            elif commandSegments[1] == 'following':
                if len(commandSegments) == 2:
                    self.__output = self.__twitterCore.getFollowingUserNames(userName=userName)
                    trueSyntax = True
                elif len(commandSegments) == 3:
                    count = commandSegments[-1]
                    if count.isdigit():
                        self.__output = self.__twitterCore.getFollowingUserNames(userName=userName, count=int(count))
                        trueSyntax = True
            elif commandSegments[1] == 'friend':
                if len(commandSegments) == 2:
                    self.__output = self.__twitterCore.getFriendUserNames(userName)
                    trueSyntax = True
                elif len(commandSegments) == 3:
                    count = commandSegments[-1]
                    if count.isdigit():
                        self.__output = self.__twitterCore.getFriendUserNames(userName=userName, count=int(count))
                        trueSyntax = True
            elif commandSegments[1] == 'noback':
                if len(commandSegments) == 2:
                    self.__output = self.__twitterCore.getUserNoBackUserNames(userName=userName)
                    trueSyntax = True
                elif len(commandSegments) == 3:
                    count = commandSegments[-1]
                    if count.isdigit():
                        self.__output = self.__twitterCore.getUserNoBackUserNames(userName=userName, count=int(count))
                        trueSyntax = True
        if not trueSyntax:
            self.error(line)

    def complete_user(self, text, line, begidx, endidx):
        masterCommands = line.split('|')
        commandSegments = masterCommands[-1].split()
        completions = []
        if not text:
            if len(commandSegments) == 0:
                completions = self.MAIN_COMMANDS[:]
            elif len(commandSegments) == 2:
                completions = self.SHOW_LEVEL_TWO[:] + self.SHOW_LEVEL_SHARE[:]
        else:
            if len(commandSegments) == 1:
                completions = [f for f in self.MAIN_COMMANDS if f.startswith(text)]
            elif len(commandSegments) == 3:
                completions = [f for f in self.SHOW_LEVEL_TWO[:-1] + self.SHOW_LEVEL_SHARE if f.startswith(text)]
        return completions

    def do_noback(self, line):
        commandSegments = line.split()
        trueSyntax = False
        if line.startswith('me'):
            if len(commandSegments) == 1:
                self.__output = self.__twitterCore.getNoBackMeUserNames()
                trueSyntax = True
            elif len(commandSegments) == 2:
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getNoBackMeUserNames(count=int(count))
                    trueSyntax = True
        elif line.startswith('user'):
            if len(commandSegments) == 2:
                userName = commandSegments[2]
                self.__output = self.__twitterCore.getNoBackUserUserNames(userName=userName)
                trueSyntax = True
            elif len(commandSegments) == 3:
                userName = commandSegments[2]
                count = commandSegments[-1]
                if count.isdigit():
                    self.__output = self.__twitterCore.getNoBackUserUserNames(userName=userName, count=int(count))
                    trueSyntax = True
        if not trueSyntax:
            self.error(line)

    def complete_noback(self, text, line, begidx, endidx):
        masterCommands = line.split('|')
        commandSegments = masterCommands[-1].split()
        completions = []
        if not text:
            if len(commandSegments) == 0:
                completions = self.MAIN_COMMANDS[:]
            elif len(commandSegments) == 1:
                completions = self.SHOW_LEVEL_ONE[:]
        else:
            if len(commandSegments) == 1:
                completions = [f for f in self.MAIN_COMMANDS if f.startswith(text)]
            elif len(commandSegments) == 2:
                completions = [f for f in self.SHOW_LEVEL_ONE if f.startswith(text)]
        return completions

    def do_pipe(self, args):
        buffer = None
        for arg in args:
            s = arg
            if buffer:
                s += ' ' + buffer
            self.onecmd(s)
            buffer = self.__output

    def complete_pipe(self, text, line, begidx, endidx):
        masterCommands = line.split('|')
        commandSegments = masterCommands[-1].split()
        completions = []
        if not text:
            if len(commandSegments) == 0:
                completions = self.MAIN_COMMANDS[:]
            elif commandSegments[0] in self.MAIN_COMMANDS:
                if hasattr(self, 'complete_' + commandSegments[0]):
                    method = getattr(self, 'complete_' + commandSegments[0])
                    return method(text, masterCommands[-1], begidx, endidx)
        else:
            if len(commandSegments) == 1:
                completions = [f for f in self.MAIN_COMMANDS if f.startswith(text)]
            elif commandSegments[0] in self.MAIN_COMMANDS:
                if hasattr(self, 'complete_' + commandSegments[0]):
                    method = getattr(self, 'complete_' + commandSegments[0])
                    return method(text, masterCommands[-1], begidx, endidx)
        return completions

    def postcmd(self, stop, line):
        if self.__output:
            print(self.__output)
            self.__output = None
        return stop

    def parseline(self, line):
        if '|' in line:
            return 'pipe', line.split('|'), line
        return Cmd.parseline(self, line)

    def error(self, line):
        self.__output = "*** Unknown syntax: %s"%line

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
