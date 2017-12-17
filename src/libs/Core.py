
from configparser import ConfigParser
from os import path
from Account_Manager import TwitterAccountManager

class TwitterCore:

    def __init__(self, confPath):
        self.account = None
        self.boot(confPath)

    # login to related account from parameters obtained from config file
    def boot(self, confPath):
        # Read config file
        parser = ConfigParser()
        parser.read(confPath)

        # Set application parameters
        consumerKey = parser.get('api', 'CONSUMERKEY')
        secretKey = parser.get('api', 'CONSUMERSECRET')
        accessKey = parser.get('api', 'ACCESSKEY')
        accessSecret = parser.get('api', 'ACCESSSECRET')

        self.ConnectToAccount(consumerKey, secretKey, accessKey, accessSecret)
        
    # Create AccountManager object and login to your account
    def ConnectToAccount(self, consumerKey, secretKey, accessKey, accessSecret):
        self.account = TwitterAccountManager(consumerKey, secretKey, accessKey, accessSecret)
        self.account.login()

    # Function To display Owner's Details
    def DisplayOwnerAccountInfo(self):
        print ("Your Account Information :")
        data = self.account.getMyUserInfo()
        for key, value in data.items():
            print (key, value)

    # Function to Display Followers
    def DisplayMyFollowers(self):
        print ("They are Following You:")
        print ("========================")
        for followers in self.account.getMyFollowers():
            print(followers.screen_name)
        print ("========================")

    # Function to List the users that you Follow
    def DisplayFollowingMe(self):
        print ("You are Following:")
        print ("========================")
        for following in self.account.getMyFollowings():
            print(following.screen_name)
        print ("========================")

    # Function To get other users Info
    def DisplayUserInfo(self, userName):
        print("Information of The User is:")
        print("===========================")
        info = self.account.getUserInfo(userName)
        for key, value in info.items():
            print (key, value)

    # Follow specefic user
    def Follow(self, userName):
        self.account.follow(userName)

    # Unfollow specefic user  
    def UnFollow(self, userName):
        self.account.follow(userName)

if __name__ == '__main__':
    pass
