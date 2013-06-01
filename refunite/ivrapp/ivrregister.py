from refunite.ivrapp import app
from flask import request, session
import logging
import twilio.twiml
from messages import ivrtext

def doivrregister():
    lang = session['lang']
    msgs = ivrtext.get(lang)
    resp = twilio.twiml.Response()
    with resp.gather(numDigits=1, action="/register-gender", method="POST", timeout=5) as g:
        g.say(msgs.get('askGender'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.say(msgs.get('sorry'), language=lang)
    return str(resp)

@app.route("/register-gender", methods=['GET', 'POST'])
def registerGender():
    gender = request.values.get('Digits', None)
    logging.log(logging.INFO, "Gender choice: " + str(gender))
    session['gender'] = str(gender)
    lang = session['lang']
    msgs = ivrtext.get(lang)

    resp = twilio.twiml.Response()
    resp.say(msgs.get('askName').format('your'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.record(maxLength="10", action="/register-name")
    return str(resp)

@app.route("/register-name", methods=['GET', 'POST'])
def registerName():
    name_url = request.values.get('RecordingUrl', None)
    logging.log(logging.INFO, "Name recording: " + str(name_url))
    session['name_url'] = name_url
    
    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    resp = twilio.twiml.Response()
    with resp.gather(numDigits=1, action="/register-country", method="POST", timeout=5) as g:
        g.say(msgs.get('askCountry').format('your'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.say(msgs.get('sorry'), language=lang)
    return str(resp)


@app.route("/register-country", methods=['GET', 'POST'])
def registerCountry():
    country_choice = request.values.get('Digits', None)
    logging.log(logging.INFO, "Country choice: " + str(country_choice))
    session['country_choice'] = country_choice

    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    resp = twilio.twiml.Response()
    resp.say(msgs.get('askTribe').format('your'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.record(maxLength="10", action="/register-tribe")
    return str(resp)

@app.route("/register-tribe", methods=['GET', 'POST'])
def registerTribe():
    tribe_url = request.values.get('RecordingUrl', None)
    logging.log(logging.INFO, "Tribe name recording: " + str(tribe_url))
    session['tribe_url'] = tribe_url
    
    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    resp = twilio.twiml.Response()
    resp.say(msgs.get('askMemo'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.record(maxLength="10", action="/register-memo")
    return str(resp)

@app.route("/register-memo", methods=['GET', 'POST'])
def registerMemo():
    memo_url = request.values.get('RecordingUrl', None)
    logging.log(logging.INFO, "Memo recording: " + str(memo_url))
    session['memo_url'] = memo_url
    
    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    resp = twilio.twiml.Response()
    resp.say(msgs.get('pleaseWaitRegistering'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.redirect("/register-start")
    return str(resp)

@app.route("/register-start", methods=['GET', 'POST'])
def registerStart():
    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    session_obj = {"gender": session['gender'], "country": session['country_choice'], "name_url":session['name_url'], "tribe_url": session['tribe_url'], "memo_url":session['memo_url']}
    logging.info(session_obj)
    resp = twilio.twiml.Response()
    resp.say(msgs.get('thanks'), language=lang,  voice=twilio.twiml.Say.WOMAN)
    return str(resp)
