
"""
Twitter in CLI mode
"""
name = "tweeli"

__version__ = '1.0.1'
__author__ = 'Mohammad Taheri'
__license__ = 'MIT'

from tweeli.core import TwitterCore
from tweeli.cli import TwitterCLI
from tweeli.cli_show import TwitterCLIShow
from tweeli.main import start