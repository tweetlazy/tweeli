# Twitter-API-Account-Manager-Python3
Python 3 script for managing of your twitter account using twitter official api's

Requirements
1. First of all you must create an application with your twitter account.
Go to link below and create your application with personal data (you have to logged in to your account before it):

https://apps.twitter.com/

So you need four things for login with your account in this application. CONSUMERKEY, CONSUMERSECRET, ACCESSKEY, ACCESSSECRET

Enter data in twitter_account_manager.ini file in config folder:

CONSUMERKEY = YOUR_CONSUMER_KEY

CONSUMERSECRET = YOUR_CONSUMER_SECRET

ACCESSKEY = YOUR_ACCESS_KEY

ACCESSSECRET = YOUR_ACCESS_SECRET

2. After that you need install the requirements packages in requirements.txt:

pip3 install tweepy
pip3 install configparser

3. edit functions in main.py and run it!

ToDo

. convert main.py to cli mode

. add fave method in Account_Manager.py

. add "get list of following not followd you" method in Account_Manager.py

. add "unfollow notification" method in Account_Manager.py
