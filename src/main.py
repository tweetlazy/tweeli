

import readline
from os import path

from libs.Command_Line_Interface import TwitterCLI
from libs.Core import TwitterCore

def main():
    if path.exists('./.CLI_history'):
        readline.read_history_file('./.CLI_history')
    confPath = "config/twitter_account_manager.ini"

    if not path.exists(confPath):
        print("[X] Config file does not exist or is invalid.")
        exit(1)
    TwCore = TwitterCore(confPath)
    TwCmd = TwitterCLI()
    TwCmd.init(TwCore)
    TwCmd.prompt='Twitter>>> '
    TwCmd.cmdloop(TwCore)
    readline.write_history_file('./.CLI_history')

main()

