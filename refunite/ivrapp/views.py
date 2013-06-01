from refunite.ivrapp import app
from flask import request, redirect, session
import logging
import twilio.twiml

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
        resp = twilio.twiml.Response()
        logging.log(logging.INFO, "Received a call from: " + from_number);
        # if the caller is someone we know:
        if from_number in callers:
            # Greet the caller by name
            resp.say("Hello " + callers[from_number])
        else:
            resp.say("Hello!")
        
        resp.say("Welcome to Refugee United Mobile Services")
     
        with resp.gather(numDigits=1, action="/handle-lang", method="POST", timeout=5) as g:
                g.say("Please choose your language. For English press 1, for French press 2, for Spanish press 3.")
        resp.say("Sorry, couldn't get your choice")
        resp.redirect("http://refuniteivr.appspot.com/")
        return str(resp)
    
@app.route('/handle-lang', methods=['GET', 'POST'])
def lang():
        resp = twilio.twiml.Response()
        digit_pressed = request.values.get('Digits')
        logging.log(logging.INFO, digit_pressed)
        if digit_pressed=="2":
            resp.say("enregistrer votre voix", language=twilio.twiml.Say.FRENCH)
        elif digit_pressed=="3":
            resp.say("grabar su voz", language=twilio.twiml.Say.SPANISH)
        else:
            resp.say("Please record your voice")
        
        resp.record(maxLength="10", action="/handle-recording", finishOnKey="#")
        resp.say("Sorry nothing recorded!")
        return str(resp)

@app.route('/handle-recording', methods=['GET', 'POST'])
def recording():
        resp = twilio.twiml.Response()
        recording_url = request.values.get("RecordingUrl")
        resp.say("Thanks for recording")
        resp.play(recording_url)
        resp.say("Goodbye.")        
        return str(resp)    