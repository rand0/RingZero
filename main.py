__author__ = 'Aymen'
from Libraries import challenges, usefulLibrary

# Global Variables
global input
try: input = raw_input
except NameError: pass

DOMAIN = "http://ringzer0team.com"
CHALLENGES = "RingZeroTeam"

def populateCreds(creds):
    cryptedLogins = usefulLibrary.readFile(creds)
    if cryptedLogins == "":
        return "FAIL"
    decryptedLogins = usefulLibrary.decryptData(cryptedLogins)
    return "SUCCESS"

def createCreds(creds):
    usefulLibrary.createFile(creds)
    print("WARNING: Your credentials file '" + creds + "' was not found !")
    USERNAME = input("Please enter your username: ")
    PASSWORD = input("Please enter your password: ")
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
