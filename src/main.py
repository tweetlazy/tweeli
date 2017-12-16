
from configparser import ConfigParser
from libs.Account_Manager import AccountManager

# Read config file
parser = ConfigParser()
parser.read("config/twitter_account_manager.ini")

# Set application parameters
CONSUMERKEY = parser.get('api', 'CONSUMERKEY')
CONSUMERSECRET = parser.get('api', 'CONSUMERSECRET')
ACCESSKEY = parser.get('api', 'ACCESSKEY')
ACCESSSECRET = parser.get('api', 'ACCESSSECRET')

# Create AccountManager object and login to your account
myAccount = AccountManager(CONSUMERKEY, CONSUMERSECRET, ACCESSKEY, ACCESSSECRET)
myAccount.login()


# Function To display Owner's Details
def DisplayOwnerAccountInfo():
  print ("Your Account Information :")
  data = myAccount.getMyUserInfo()
  for key, value in data.items():
      print (key,value)

# DisplayOwnerAccountInfo()

# Function to Display Followers
def DisplayMyFollowers():
    print ("They are Following You:")
    print ("========================")
    for followers in myAccount.getMyFollowers():
      print(followers.screen_name)
    print ("========================")

# DisplayMyFollowers()

# Function to List the users that you Follow
def DisplayFollowingMe():
  print ("You are Following:")
  print ("========================")
  for following in myAccount.getMyFollowings():
    print(following.screen_name)
  print ("========================")

# DisplayFollowingMe()

# To Follow and Unfollow we need to uncomment following:
# myAccount.follow('smm_taheri')
# myAccount.unfollow('smm_taheri')

def helpCommand():
  print("""Enter "myaccountinfo" to show the information of your account""")
  print("""Enter "myfollowers" to show your followers""")
  print("""Enter "myfollowings" to show your followings""")

def main():
  print("***Welcome to CLI mode***")
  print("""Enter "help" to show list of commands or Enter "exit" to exit the cli mode!""")
  print(">>> ", end="")
  command = input()
  while str(command) != "exit":
    if command == "help":
      helpCommand()
    elif command == "myaccountinfo":
      DisplayOwnerAccountInfo()
    elif command == "myfollowers":
      DisplayMyFollowers()
    elif command == "myfollowings":
      DisplayFollowingMe()
    print(">>> ", end='')
    command = input()

main()