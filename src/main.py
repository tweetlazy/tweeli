
from configparser import ConfigParser
from os import path
from sys import exit
from libs.Account_Manager import AccountManager

# Read config file
conf_path = "config/twitter_account_manager.ini"
parser = ConfigParser()

if not path.exists(conf_path):
  print("[X] Config file does not exist or is invalid.")
  exit(1)

parser.read(conf_path)

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

# Function to Display Followers
def DisplayMyFollowers():
    print ("They are Following You:")
    print ("========================")
    for followers in myAccount.getMyFollowers():
      print(followers.screen_name)
    print ("========================")

# Function to List the users that you Follow
def DisplayFollowingMe():
  print ("You are Following:")
  print ("========================")
  for following in myAccount.getMyFollowings():
    print(following.screen_name)
  print ("========================")

#Function To get other users Info
def DisplayUserInfo(user_name):
    print("Information of The User is:")
    print("===========================")
    info = myAccount.getUserInfo(user_name)
    for key, value in info.items():
        print (key, value)

# To Follow and Unfollow we need to uncomment following:
# myAccount.follow('smm_taheri')
# myAccount.unfollow('smm_taheri')

def helpCommand():
  print("""Enter "myaccountinfo" to show the information of your account""")
  print("""Enter "myfollowers" to show your followers""")
  print("""Enter "myfollowings" to show your followings""")
  print("""Enter "userinfo" to see the information of the user """)
  print("""Enter "follow" to following new users""")
  print("""Enter "unfollow" to unfollow someone """)

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
    elif command =="userinfo":
      print(">>> Enter User Name: ", end="")
      username = input()
      DisplayUserInfo(username)
    elif command =="follow":
      print(">>>Enter User Name: ", end="")
      username = input()
      myAccount.follow(username)
    elif command =="unfollow":
      print(">>>Enter User Name: ", end="")
      username = input()
      print(">>>Are you sure you want to Unfollow " + username + " ? y/n")
      answer = input()
      if answer == "y":
        myAccount.unfollow(username)
      elif answer == "n":
        print("Good Decision")

    print(">>> ", end='')
    command = input()

main()
