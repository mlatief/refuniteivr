'''
Created on May 31, 2013

# REST PROXY between IVR & Refugee United REST APIs
@author: Mohamed El Ersh

'''
import urllib2
import urllib
import json
import logging

logging.getLogger().setLevel(logging.DEBUG)

def createProfile (genderID,name,tribe,birthCountryID,MSISDN):
    "Create New Refugee Profile."
#    Call_API('/profile.json');    
    query_args= {'genderId':genderID,'givenName':name,'tribe':tribe,'birthCountryId':birthCountryID,'cellPhone':MSISDN};
    result = post_API('/profile', query_args);
    newProfileId = result['profile']['id'];
    return newProfileId; 

def post_API(inputStr, args):
    "Calls Refugee United Get "
    logging.log(logging.INFO, "Post API");
    URL = 'http://api.ru.istykker.dk' + inputStr + '.json';

    Realm    = 'api.ru.istykker.dk';
    Username = 'hackathon';
    Password = '473ba3ff6162c6064479825bcefa7de95e2ef266';
    
    logging.log(logging.INFO, URL);
    
    #Call API and log the return values.
    authhandler = urllib2.HTTPDigestAuthHandler();
    authhandler.add_password(Realm, URL, Username, Password);
    opener = urllib2.build_opener(authhandler);
    urllib2.install_opener(opener);
    #params = urllib.urlencode(args);
    
    logging.log(logging.INFO, args);
    
    req = urllib2.Request(URL, str(args));
    resp = urllib2.urlopen(req);
    resp_json = json.loads(resp.read());
    logging.log(logging.INFO, "REST Return Result ");
    logging.log(logging.INFO, resp_json)
    return resp_json;


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
    X = Call_API("/profile/" + str(refugeeID));
    logging.log(logging.INFO, X.get("profile").get("genderId"))
    logging.log(logging.INFO, X.get("profile").get("genderId"))
    return;

def search(name, genderId, countryOfBirthId):
    "Calls search REST API with Parameters passed."
    logMeIn = "Search for -- > name:" + name + ",genderID:" + genderId + ",Refugee Country:" + countryOfBirthId+".";    
    logging.log(logging.INFO, logMeIn);  
    xxx = "/search.json?name=" + name+ "&countryOfBirthId="+countryOfBirthId+"&genderId="+genderId;
    returnAPI = Call_API(xxx);
    #  results, surName,profileid
    # result['profile']['id']
    
    X=[]
    for row in returnAPI['results']:
        M = { row['profileid'], row['givenName'], row['age'], row['surName']};
        X.append(M);        
    
    return X; 


#IVR MAPPING

#1 50
#2 173
#3 189
#4  68
#5 197
#6 36




### Test Call for functions
search("Mohamed","3","189")
XX = createProfile ("2","Mohamed","XXX",'168',"0212001311");

#createProfile (genderID,name,tribe,birthCountryID,MSISDN);