'''
Created on May 31, 2013

# REST PROXY between IVR & Refugee United REST APIs
@author: Mohamed El Ersh

'''
import urllib2
import json
import logging

logging.getLogger().setLevel(logging.DEBUG)

def Call_API(inputStr):
    "Utility function for calling REST APIs from Refugee United Servers."
    #  Fetch json
    # = '/search.json?name=Ali'
    #RESTCall ='/partner.json'
    logging.log(logging.INFO, "call_api");
    # URL String Creation.
    URL = 'http://api.ru.istykker.dk' + inputStr;
    logging.log (logging.INFO, "URL REST ---> #" + URL+"#");
    # REST API Configurations.
    Realm    = 'api.ru.istykker.dk';
    Username = 'hackathon';
    Password = '473ba3ff6162c6064479825bcefa7de95e2ef266';
    #Call API and log the return values.
    authhandler = urllib2.HTTPDigestAuthHandler();
    authhandler.add_password(Realm, URL, Username, Password);
    opener = urllib2.build_opener(authhandler);
    urllib2.install_opener(opener);
    page_content = urllib2.urlopen(URL);
    response = json.loads(page_content.read());
    logging.log(logging.INFO, "REST Return Result ");
    logging.log(logging.INFO, response)
    return response;

def getOwningVolunteer(refugeeID):
    "This returns ID of owning volunteer associated with passed Refugee ID"
    X = Call_API("/profile/" + str(refugeeID)+".json");
    logging.log(logging.INFO, X.get("profile").get("genderId"))
    return;

''''
Functions::

createRefugeeProfile
createNewVolunteer
addNewMissing
addNewMemo
reportMatchByRefugee
reportMatchByVolunteer
search
editRefugeeProfile
editVolanteerProfile
getOwningVolunteer

.....
Admin Panel

'''
'''
#  Fetch json
RESTCall = '/search.json?name=Ali'
#RESTCall ='/partner.json'
URL = 'http://api.ru.istykker.dk' + RESTCall  #URL      = 'http://api.ru.istykker.dk/topcountries.json'
Realm    = 'api.ru.istykker.dk'
Username = 'hackathon'
Password = '473ba3ff6162c6064479825bcefa7de95e2ef266'

authhandler = urllib2.HTTPDigestAuthHandler()
authhandler.add_password(Realm, URL, Username, Password)
opener = urllib2.build_opener(authhandler)
urllib2.install_opener(opener)
page_content = urllib2.urlopen(URL)

response = json.loads(page_content.read())
print response['count']

def search():
    print "XXXXXX"
    return 0;

'''

#print ("start here")
getOwningVolunteer("354544")
