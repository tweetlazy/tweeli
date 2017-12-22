
# import readline
import sys
from os import path

from libs.CLI import TwitterCLI

def main():
    # if path.exists('./.CLI_history'):
    #     readline.read_history_file('./.CLI_history')
    # confPath = "config/twitter_account_manager.ini"
    TwCLI = TwitterCLI()
    TwCLI.start()
    if len(sys.argv) > 1:
        TwCLI.onecmd(' '.join(sys.argv[1:]))
    else:
        TwCLI.cmdloop()
    # readline.write_history_file('./.CLI_history')
main()