__author__ = 'Aymen'
from Libraries import challenges

# Global Variables
USERNAME = ""  # ringzer0team login
PASSWORD = ""    # and password for authentification
if ((USERNAME == "") or (PASSWORD == "")):
    exit("Username or Password field empty", -1)   #Put your email or password
DOMAIN = "http://ringzer0team.com"


if __name__ == '__main__':
    print challenges.doAll()
