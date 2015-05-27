__author__ = 'Aymen'
from Libraries import challenges

# Global Variables
USERNAME = ""  # ringzer0team login                 *** DO NOT GIT TRACK **
PASSWORD = ""  # and password for authentication    *** DO NOT GIT TRACK **
if (USERNAME == "") or (PASSWORD == ""):
    exit("Username or Password field empty", -1)    # Put your email or password
DOMAIN = "http://ringzer0team.com"


if __name__ == '__main__':
    print(challenges.doAll())
