
# import readline
import sys
from multiprocessing import Process
from os import path

from libs.api import runServer
from libs.cli import TwitterCLI


def runAPIServer():
    runServer()

def main():
    # if path.exists('./.CLI_history'):
    #     readline.read_history_file('./.CLI_history')
    # confPath = "config/twitter_account_manager.ini"
    TwCLI = TwitterCLI()
    Process(target=runAPIServer).start()
    TwCLI.start()
    if len(sys.argv)>1:
        TwCLI.onecmd(' '.join(sys.argv[1:]))
    else:
        TwCLI.cmdloop()
    # readline.write_history_file('./.CLI_history')

if __name__ == "__main__":
    main()
