__author__ = 'Aymen'
from ringzer0team import hash_me_please, hash_me_reloaded

challenges = {13 : hash_me_please.hash_me_please,
              14 : hash_me_reloaded.hash_me_reloaded
             }

def challenge(value):
    return challenges[value].__name__ + " ---> " + challenges[value]() + '\n'

def doAll():
    output = ""
    for key in challenges.keys():
        output += challenge(key)
    return output