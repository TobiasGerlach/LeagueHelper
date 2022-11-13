import os
import setuptools
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read() 
setuptools.setup(
    name = "LeagueHelper",
    version = "0.0.0",
    author = "Tobias Gerlach",
    author_email = "me@tobias-gerlach.de",
    description = ("Helper tool for League of Legends. DO NOT USE INGAME. Just for demonstartion purposes."),
    license = "I dont know or care, do what you like with the code",
    keywords = "league of legends helper tool",
    url = "",
    package_dir = {"LeagueHelper.AI": "src.AI"},
    packages=setuptools.find_packages(),
    long_description=read('README.md'),
)