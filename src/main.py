
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

#Function To get user's timeline
def FollowingsNotFollowing():
    names = myAccount.noBackFollowings()
    for name in names:
        print (name)

#Function To get user's home timeline
def DisplayHomeTimeline():
    tweets = myAccount.getHomeTimeline()
    for tweet in tweets:
        print("id : "+ str(tweet.id))
        print (tweet.user.screen_name + " tweeted :")
        print(tweet.text)
        print("===========================")

#Function to get user's get Timeline
def DisplayMyTimeline():
    tweets = myAccount.getMyTimeline()
    for tweet in tweets:
        print("id : "+ str(tweet.id))
        print (tweet.user.screen_name + " tweeted :")
        print(tweet.text)
        print("===========================")

#Function to get user's get Timeline
def DisplayUserTimeline(screenName):
    tweets = myAccount.getTimeline(screenName)
    for tweet in tweets:
        print("id : "+ str(tweet.id))
        print (tweet.user.screen_name + " tweeted :")
        print(tweet.text)
        print("===========================")

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
  print("""Enter "followingsnotfollowing" to see who doesnt follow you back """)
  print("""Enter "timeline" to see someone`s timeline """)
  print("""Enter "mytimeline" to see your timeline """)
  print("""Enter "home" to see home timeline """)
  print("""Enter "fave" to fave a tweet """)
  print("""Enter "unfave" to unfave a tweet """)
  print("""Enter "retweet" to retweet a tweet """)

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
    elif command =="followingsnotfollowing":
      FollowingsNotFollowing()
    elif command == "timeline":
      print(">>>Enter User Name: ", end="")
      username = input()
      DisplayUserTimeline(username)
    elif command == "mytimeline":
      DisplayMyTimeline()
    elif command == "home":
      DisplayHomeTimeline()
    elif command == "fave":
      print(">>>Enter Tweet Id: ", end="")
      tweetId = input()
      try:
        myAccount.fave(tweetId)
      except Exception as e:
        print(e)
    elif command == "unfave":
      print(">>>Enter Tweet Id: ", end="")
      tweetId = input()
      try:
        myAccount.unfave(tweetId)
      except Exception as e:
        print(e)
    elif command =="retweet":
      print(">>>Enter Tweet Id: ", end="")
      tweetId = input()
      try:
        myAccount.retweet(tweetId)
      except Exception as e:
        print(e)
    print(">>> ", end='')
    command = input()

main()
