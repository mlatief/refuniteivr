import twilio.twiml


ivrtext = {twilio.twiml.Say.ENGLISH: {'welcome': 'Refugees United offers a free service where you can search for missing family member',
                 'askRegisterOrSearch': 'if you are looking for missing relative press 1, if you want to register as a refugee press 2',
                 'askGender': 'If you are looking for a female refugee, press 1. If you are looking for a male refugee, press 2',
                 'askName': 'Please say {0} name after the tone and press hash',
                 'askCountry': 'What is {0} country of origin? For Congo press 1, for Ruwanda press 2, for Somalia press 3, for Ethiopia press 4, for Sudan press 5, for Burundi press 6',
                 'askTribe': 'Please say the name of your tribe after the tone, then press hash',
                 'askMemo': 'Please record a voice memo to your relatives',
                 'pleaseWaitSearching': 'Please wait while looking for matches',
                 'pleaseWaitRegistering': 'Please wait while registering',
                 'sorry':'Sorry can not understand your choice', 
                 'thanks':'Thank you for using our service' 
                 },
           twilio.twiml.Say.FRENCH: {'welcome': 'Refugees United vous offre un service gratuit pour pouvoir retrouver vos proches disparus',
                 'askRegisterOrSearch': 'Si vous cherchez un proche disparu, appuez sur 1, Si vous voulez vous enregistrer comme refuge appuez sur 2',
                 'askGender': 'Si vous cherchez une proche, appuez sur 1. Si vous cherchez un proche, appuez sur 2',
                 'askName': 'Apres la tonalitee, dite son nom et appyez sur carre',
                 'askCountry': "Quel est son pays d'origine? Pour le Congo appuez sur 1, pour le Rouwanda appuez sur 2, pour le Somalia appuez sur 3, pour Ethiopia appuez sur 4, pour Sudan appuez sur 5, pour Burundi appuez sur 6",
                 'askTribe': 'Veuillez prononcer le nom de votre tribue apres la tonalite et appuez sur carre',
                 'askMemo': "S'il vous plait enregistrer un memo vocal a vos proches",
                 'pleaseWaitSearching': u"S'il vous plait patienter pendant que la recherche de proche",
                 'pleaseWaitRegistering': u"S'il vous plait patienter pendant que enregistrer comme refuge",
                 'sorry':'Desole, vous avez effectuez une mauvaise operation',
                 'thanks':'Merci, au revoir'
            }}

searchtext = {twilio.twiml.Say.ENGLISH: {'resultCount': "Your search resulted in {0} matches.",
                'firstMatch': "Your first match",
                'years': "years",
                'voiceMemo': "and have recorded this memo",
                'nextMatch': "To listen to the next match, press 1",
                'previousMatch':"To go to the previous match, press 2",
                'selectMatch': "To report this match, press 3",
                'leaveMessage': "Please leave {0} a message"
                },
              twilio.twiml.Say.FRENCH: {'resultCount': "Votre recherche a retourne {0} selection",
                'firstMatch': "Votre premiere selection",
                'years': "ans",
                'voiceMemo': "et a enregistre cette note",
                'nextMatch': "Pour entndre la prochaine selection, appuez sur 1",
                'previousMatch': "Pour entendre la selection precedente, appuez sur 2",
                'selectMatch': "Si vous choisisez cette selection, appuez sur 3",
                'leaveMessage': "lui laisser un message s'il vous plait"
                }}
