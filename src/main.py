
from configparser import ConfigParser
from libs.Account_Manager import AccountManager

# read config file
parser = ConfigParser()
parser.read("config/twitter_account_manager.ini")

# set application parameters
CONSUMERKEY = parser.get('api', 'CONSUMERKEY')
CONSUMERSECRET = parser.get('api', 'CONSUMERSECRET')
ACCESSKEY = parser.get('api', 'ACCESSKEY')
ACCESSSECRET = parser.get('api', 'ACCESSSECRET')

# create accountmanager object and login to your account
myAccount = AccountManager(CONSUMERKEY, CONSUMERSECRET, ACCESSKEY, ACCESSSECRET)
myAccount.login()

#def main():
# Define Command Line here in main

# Function To display Owner's Details
def DisplayOwnerAccountInfo ():
    print ("Your Account Information :")
    data = myAccount.getMyUserInfo()
    for key, value in data.items():
        print (key,value)

DisplayOwnerAccountInfo()

# Function to Display Followers
def DisplayMyFollowers():
    print ("They are Following You:")
    print ("========================")
    for followers in myAccount.getMyFollowers():
      print(followers.screen_name)
    print ("========================")
DisplayMyFollowers()

# Function to List the users that you Follow
def DisplayFollowingMe():
  print ("You are Following:")
  print ("========================")
  for following in myAccount.getMyFollowing():
    print(following.screen_name)
  print ("========================")
DisplayFollowingMe()

# To Follow and Unfollow we need to uncomment following:
# myAccount.follow('smm_taheri')
#myAccount.unfollow('smm_taheri')
