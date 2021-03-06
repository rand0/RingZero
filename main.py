__author__ = 'Aymen'
from Libraries import challenges, usefulLibrary
from termcolor import colored
from colorama import init
import getpass

init() # Initialize the color fonction

# Global Variables
global input
try: input = raw_input
except NameError: pass

DOMAIN = "http://ringzer0team.com"
CHALLENGES = "RingZeroTeam"


class colors:
    HEADER = '\033[97m'  #white
    OKBLUE = '\033[94m'
    CREDS = '\033[91m'
    WARNING = '\033[91m' #red
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    FLAG = '\033[1m'
    UNDERLINE = '\033[4m'


def populateCreds(creds):
    cryptedLogins = usefulLibrary.readFile(creds)
    if cryptedLogins == "":
        return "FAIL"
    decryptedLogins = usefulLibrary.decryptData(cryptedLogins)
    return "SUCCESS"

def createCreds(creds):
    usefulLibrary.createFile(creds)
    print colored('WARNING:', 'red'), colored('Your credentials file: ', 'green'), colored(creds, 'white') + colored(' was not found ! \n', 'green')
    print colored('--------------------------------------------------------------------------', 'white')
    USERNAME = input(colors.CREDS +  "Username: ")
    PASSWORD = getpass.getpass("Password: ")
    print colored('--------------------------------------------------------------------------\n', 'white')
    print ('{:^100}'.format(colors.HEADER+ '** ' +colors.OKBLUE + 'Welcome ' + colors.CREDS + USERNAME + colors.HEADER+ ' **' '\n\n'))
    usefulLibrary.createFile(creds)
    cryptedLogins = usefulLibrary.encryptData(USERNAME, PASSWORD)
    usefulLibrary.appendToFile(creds, cryptedLogins)

if __name__ == '__main__':
    creds = CHALLENGES+".credentials"
    if usefulLibrary.fileExist(creds):
        if populateCreds(creds) == "FAIL":
            createCreds(creds)
    else:
        createCreds(creds)
    print(challenges.doAll())