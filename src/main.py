
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

# do some functions
print(myAccount.getUserInfo('smm_taheri'))
print(myAccount.getMyUserInfo())
res = myAccount.getFollowers('smm_taheri')
res = myAccount.getMyFollowers()
res = myAccount.getFollowings('smm_taheri')
res = myAccount.getMyFollowings()
while True:
    try:
        user = AccountManager.showUser(res.next())
        print(user.items())
        print(dir(res.next()))
        break
    except StopIteration:
        break
# myAccount.follow('smm_taheri')
myAccount.unfollow('smm_taheri')