# tweeli = twitter + cli

A command line interface for Twitter with some cool features writing with python 3

## QuickStart

* First, enable Twitter apps for your account with the following link [Twitter Account Manager](https://apps.twitter.com).
* Then, write all neccessary information into config file which is located in `tweeli/config/config.ini`
* Install the required packages in requirements.txt:

```sh
$ pip3 install -r requirements.txt
```
* Run `main.py` program and press 'tab' to show all available commands. Then run your ideal command and enjoy it!

also you can use [PYPI](https://pypi.org/) to install tweeli:
```sh
$ pip3 install tweeli
```
Then import `tweeli` and use `tweeli.start()` for using it!

## Contribution

Bug reports and pull requests are welcome on GitHub at https://github.com/smmtaheri/tweeli .

Please fork it and raise a pull request for your contribution.

## To-Do:

1. Complete twitter core functions (list, direct, trends and ...)
2. Implement file system caching (handle twitter api limites and )
3. Add unfollow track (DB is required!)
