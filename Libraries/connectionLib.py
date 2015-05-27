__author__ = 'Aymen'
import requests, os
from ringzer0team import DOMAIN, USERNAME, PASSWORD

# authentificating
def connect(url):
    if url.find("ringzer0team") > -1:
        credentials = {'username': USERNAME, 'password': PASSWORD}
        session = requests.Session()
        session.post(DOMAIN+"/login", data=credentials)
        return session
    else:
        exit("Only accept " + DOMAIN + " domain for now")

# Getting the webpage
def getWebpage(session, url):
    challenge = session.get(url)
    page_source = challenge.text  # Page_source contains all the web page source in a single sting
    return page_source

def getPayload(page_source, beg_message, end_message, beg_padding=0, end_padding=0, reverse = False):  # To do : implement regex

    if beg_message == '':
        beg = 0
    elif not reverse:
        beg = page_source.find(beg_message, 0, len(page_source))
    else:
        beg = page_source.rfind(beg_message, 0, len(page_source))
    if beg == -1:
        return ""
    else:
        beg += len(beg_message) + beg_padding

    if end_message == '':
        end = len(page_source)
    elif not reverse:
        end = page_source.find(end_message, beg, len(page_source))
    else:
        end = page_source.rfind(end_message, beg, len(page_source))
    if end == -1:
        return ""
    else:
        end -= end_padding

    payload = ""
    payload += page_source[beg:end]
    return payload

# Send payload flag
def submitPayload(payload, session, url):
    connectTo = url + "/" + payload
    return getWebpage(session, connectTo)

def getChallengeName(session, challengeID):
    relativePath = '<a href="/challenges/'+challengeID+' ">'
    url = DOMAIN + "/challenges"
    page_source = getWebpage(session, url)
    name = getPayload(page_source, relativePath, "</a>")
    return name

def getChallengeCategorie(session, challengeID):
    relativePath = '<a href="/challenges/'+challengeID+' ">'
    url = DOMAIN + "/challenges"
    page_source = getWebpage(session, url)

    categorie = getPayload(page_source, '', relativePath)
    categorie = getPayload(categorie, '<h4 class="title_hover" data-id=', '', 0, 0, True)
    categorie = getPayload(categorie, '">', ' (<')
    return categorie

# Send flag
def submitFlag(flag, session, url):
    # Lets save the flag in the flag file !
    # we create prepare the file
    SAVE_FILE = "RingZeroFlags.csv"
    if not os.path.exists("RingZeroFlags.csv"):
        f = open(SAVE_FILE, 'w')
        f.write("Flag;Category;Name;ID;URL\n")
        f.close()

    # format flag
    challengeID = url.split('/')[-1]
    challengeName = getChallengeName(session, challengeID)
    challengeCat = getChallengeCategorie(session, challengeID)
    flagID = flag + ";" + challengeCat + ';' + challengeName + ';' + challengeID + ';' + url + '\n'

    # Check if flag exist already
    f = open(SAVE_FILE, "r")
    f.seek(0)
    flagExist = False
    for line in f:
        if line == flagID:
            flagExist = True
    f.close()
    if not flagExist:
        f = open(SAVE_FILE, 'a')
        f.write(flagID)
        f.close()

    # And now send the flag to the server
    credentials = {'flag': flag}
    status = session.post(url, data=credentials)

    return status  # useless here