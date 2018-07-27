
# import readline
import sys
# from os import path

from .cli import TwitterCLI

def start(configPath="./config/config.ini"):
    print("""
    This module need config file in default path ./config/config.ini
    read more in https://github.com/smmtaheri/tweeli
    if you want to put login parameteres in console press 'y' else press 'n': """, end='')
    consoleLogin = input()
    TwCLI = TwitterCLI()
    if consoleLogin.lower() == "y":
        consumerKey = input("Enter consumerkey: ")
        consumerSecret = input("Enter consumersecret: ")
        accessKey = input("Enter accesskey: ")
        accessSecret = input("Enter accesssecret: ")
        TwCLI.start(consumerKey=consumerKey,
                    consumerSecret=consumerSecret,
                    accessKey=accessKey,
                    accessSecret=accessSecret,
                    configPath=configPath)
    else:
        TwCLI.start(configPath=configPath)
    # if path.exists('./.CLI_history'):
    #     readline.read_history_file('./.CLI_history')
    # confPath = "config/config.ini"
    if len(sys.argv)>1:
        TwCLI.onecmd(' '.join(sys.argv[1:]))
    else:
        TwCLI.cmdloop()
    # readline.write_history_file('./.CLI_history')

if __name__ == "__main__":
    start()
