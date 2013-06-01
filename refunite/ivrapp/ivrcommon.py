from refunite.ivrapp import app
from flask import request, redirect, session
import logging
import twilio.twiml
import twilio
from messages import ivrtext

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+201001036588": "Mohamed Abdellatif"
}


@app.route("/", methods=['GET', 'POST'])
def hello():
        # Get the caller's phone number from the incoming Twilio request
        from_number = request.values.get('From', None)
        session['from_number'] = from_number
        logging.log(logging.INFO, "Received a call from: " + str(from_number));
        
        resp = twilio.twiml.Response()

        # if the caller is someone we know:
        if from_number in callers:
            # Greet the caller by name
            resp.say("Hello " + callers[from_number])
        else:
            resp.say("Hello!")
        
        resp.say("Welcome to Refugees United!")
     
        with resp.gather(numDigits=1, action="/handle-lang", method="POST", timeout=5) as g:
                g.say("For English press 1", voice=twilio.twiml.Say.WOMAN)
                g.say("Pour francis appuez 2", voice=twilio.twiml.Say.WOMAN, language=twilio.twiml.Say.FRENCH)
        resp.say("Sorry, couldn't get your choice", voice=twilio.twiml.Say.WOMAN)
        return str(resp)
    
@app.route('/handle-lang', methods=['GET', 'POST'])
def lang():
        digit_pressed = request.values.get('Digits', None)
        logging.info("Language choice: " + str(digit_pressed))
        logging.info("Session[from_number]: " + str(session.get('from_number', '0')))
        if digit_pressed=="2":
            lang = twilio.twiml.Say.FRENCH
        else:
            lang = twilio.twiml.Say.ENGLISH
        
        session['lang'] = lang
        
        msgs = ivrtext.get(lang)
        resp = twilio.twiml.Response()
        resp.say(msgs.get('welcome'), language=lang, voice=twilio.twiml.Say.WOMAN)
        with resp.gather(numDigits=1, action="/handle-option", method="POST", timeout=5) as g:
            g.say(msgs.get('askRegisterOrSearch'), voice=twilio.twiml.Say.WOMAN, language=lang)
        resp.say(msgs.get('sorry'), language=lang)
        return str(resp)

from ivrsearch import doivrsearch
from ivrregister import doivrregister

@app.route('/handle-option', methods=['GET', 'POST'])
def registerOrSearch():
        digit_pressed = request.values.get('Digits', None)
        logging.info("Option choice: " + str(digit_pressed))
        if str(digit_pressed)=='1':
            return doivrsearch()
        else:
            return doivrregister()
            

