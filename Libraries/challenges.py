__author__ = 'Aymen'
from Coding import hash_me_please

challenges = {13 : hash_me_please.hash_me_please,
             }

def challenge(value):
    return challenges[value].__name__ + " ---> " + challenges[value]() + '\n'

def doAll():
    output = ""
    for key, _ in challenges.iteritems():
        output += challenge(key)
    return output