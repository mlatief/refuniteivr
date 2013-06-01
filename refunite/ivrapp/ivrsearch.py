from refunite.ivrapp import app
from flask import request, session, redirect, url_for
import logging
import twilio.twiml
from messages import ivrtext, searchtext

def doivrsearch():
    lang = session['lang']
    msgs = ivrtext.get(lang)
    resp = twilio.twiml.Response()
    with resp.gather(numDigits=1, action="/search-gender", method="POST", timeout=5) as g:
        g.say(msgs.get('askGender'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.say(msgs.get('sorry'), language=lang)
    return str(resp)

@app.route("/search-gender", methods=['GET', 'POST'])
def searchGender():
    gender = request.values.get('Digits', None)
    logging.log(logging.INFO, "Gender choice: " + str(gender))
    session['gender'] = str(gender)
    lang = session['lang']
    msgs = ivrtext.get(lang)

    resp = twilio.twiml.Response()
    resp.say(msgs.get('askName').format('her' if str(gender)=='1' else 'his'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.record(maxLength="10", action="/search-name")
    return str(resp)

@app.route("/search-name", methods=['GET', 'POST'])
def searchName():
    name_url = request.values.get('RecordingUrl', None)
    logging.log(logging.INFO, "Name recording: " + str(name_url))
    session['name_url'] = name_url
    gender = session['gender'] 
    
    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    resp = twilio.twiml.Response()
    with resp.gather(numDigits=1, action="/search-country", method="POST", timeout=5) as g:
        g.say(msgs.get('askCountry').format('her' if gender=='1' else 'his'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.say(msgs.get('sorry'), language=lang)
    return str(resp)


@app.route("/search-country", methods=['GET', 'POST'])
def searchCountry():
    country_choice = request.values.get('Digits', None)
    logging.log(logging.INFO, "Country choice: " + str(country_choice))
    session['country_choice'] = country_choice
    
    lang = session['lang']
    msgs = ivrtext.get(lang)
    
    resp = twilio.twiml.Response()
    resp.say(msgs.get('pleaseWaitSearching'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.redirect("/search-start")
    return str(resp)

@app.route("/search-start", methods=['GET', 'POST'])
def searchStart():
    session_obj = {"gender": session['gender'], "country": session['country_choice'], "name_url":session['name_url']}
    logging.info(session_obj)

    search_results = [{'profileId':'1234','givenName':'Ali Samir', 'age':'25'},{'profileId':'4567','givenName':'Samir Sami', 'age':'35'}]
    
    session['idx']=0;
    session['results'] = search_results
    
    return searchLoop()

def find_voice(idx):
    return False

@app.route("/search-loop", methods=['GET', 'POST'])
def searchLoop():
    idx = session['idx']
    results = session['results']
    lang = session['lang']
    
    msgs = searchtext.get(lang)
    resp = twilio.twiml.Response()

    loop_choice = str(request.values.get('Digits', None))
    logging.log(logging.INFO, "Loop choice: " + str(loop_choice))
    if loop_choice:
        if loop_choice=='2':
            idx = idx - 1
        elif loop_choice=='3':
            redirect(url_for('/search-match'))
        else:
            idx = idx + 1
        
        session['idx'] = idx
    
    if idx <0 : 
        idx = 0
    elif idx >= len(results):
        idx = len(results) - 1
        
    if idx==0:
        count = len(results)
        resp.say(msgs.get('resultCount').format(count), voice=twilio.twiml.Say.WOMAN, language=lang)
        resp.say(msgs.get('firstMatch'), voice=twilio.twiml.Say.WOMAN, language=lang)
    
    #Speech the result
    resp.say(results[idx].get('givenName'), voice=twilio.twiml.Say.WOMAN, language=lang)
    age_str = str(results[idx].get('age')) + msgs.get('years') 
    resp.say(age_str, voice=twilio.twiml.Say.WOMAN, language=lang)
    
    profile_id = results[idx].get('profileId')
    voice_mp3 = find_voice(profile_id) 
    if voice_mp3:
        resp.say(msgs.get('voiceMemo'), voice=twilio.twiml.Say.WOMAN, language=lang)
        resp.play(voice_mp3)
        
    with resp.gather(numDigits=1, action="/search-loop", method="POST", timeout=5) as g:
        if idx<len(results):
            g.say(msgs.get('nextMatch'), voice=twilio.twiml.Say.WOMAN, language=lang)
        g.say(msgs.get('selectMatch'), voice=twilio.twiml.Say.WOMAN, language=lang)
        if idx>1:
            g.say(msgs.get('previousMatch'), voice=twilio.twiml.Say.WOMAN, language=lang)
    resp.redirect("/search-loop?Digits=1")
    return str(resp)
