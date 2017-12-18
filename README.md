# Twitter-API-Account-Manager-Python3
## Python 3 script for managing your twitter account using twitter official api's

### Requirements

1. Create an Application with your Twitter account in [Twitter Account Manager](https://apps.twitter.com) to get API Access.
2. Rename "twitter_account_manager.ini_example" to "twitter_account_manager.ini"
3. Enter API keys in twitter_account_manager.ini file in config folder:

```sh

CONSUMERKEY = YOUR_CONSUMER_KEY

CONSUMERSECRET = YOUR_CONSUMER_SECRET

ACCESSKEY = YOUR_ACCESS_KEY

ACCESSSECRET = YOUR_ACCESS_SECRET
```

4. Install the required packages in requirements.txt:

```sh
$pip3 install tweepy
$pip3 install configparser
```
5. Edit and Add functions in main.py and run it!

## Contribution

Bug reports and pull requests are welcome on GitHub at https://github.com/smmtaheri/Twitter-API-Account-Manager-Python .

Please fork it and raise a pull request for your contribution.

## Next Steps:

1. Improve *cli* and adopt existing *cli* modules
2. Add fave method in *Account_manager.py*
3. Add "get list of following not followd you" method in *Account_Manager.py*
4. Implement file system caching
