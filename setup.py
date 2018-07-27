#!/usr/bin/env python

import re
from setuptools import setup, find_packages

VERSIONFILE = "tweeli/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="tweeli",
      version=version,
      description="You can using Twitter in CLI mode",
      license="MIT",
      author="Mohammad Taheri",
      author_email="admirer135@yahoo.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="http://github.com/smmtaheri/tweeli",
      packages=find_packages(),
      install_requires=[
          "tweepy>=3.0.0",
      ],
      keywords="twitter CLI library",
      python_requires='>=2.7',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      zip_safe=True)