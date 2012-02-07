#!/usr/bin/python
# -*- coding: utf-8 -*-
#by Joh Gerna

from plugin import *

import random

class smalltalk(Plugin):
    
    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)")
    @register("fr-FR", "(.*Bonjour.*)|(.*Salut.*)")
    def st_hello(self, speech, language):
        if language == 'de-DE':
            self.say("Hallo.")
        if language == 'fr-FR':
            self.say("Bonjour!")
        else:
            self.say("Hello")
        self.complete_request()

    @register("de-DE", ".*Dein Name.*")
    @register("fr-FR", u"(.*ton nom.*)|(.*ton pr\u00E9nom.*)|Comment t'appelles-tu.*")
    @register("en-US", ".*your name.*")
    def st_name(self, speech, language):
        if language == 'de-DE':
            self.say("Siri.")
        if language == 'fr-FR':
            self.say("Je m'appelle Siri.")
        else:
            self.say("Siri.")
        self.complete_request()

    @register("de-DE", "Wie geht es dir?")
    @register("fr-FR", u"(Comment vas-tu?)|(Comment \u00E7a va?)")
    @register("en-US", "How are you?")
    def st_howareyou(self, speech, language):
        if language == 'de-DE':
            self.say("Gut danke der Nachfrage.")
        if language == 'fr-FR':
            self.say("Bien, merci.")
        else:
            self.say("Fine, thanks for asking!")
        self.complete_request()
        
    @register("de-DE", ".*Danke.*")
    @register("fr-FR", ".*Merci.*")
    @register("en-US", ".*Thank.*you.*")
    def st_thank_you(self, speech, language):
        if language == 'de-DE':
            self.say("Bitte.")
            self.say("Kein Ding.")
        if language == 'fr-FR':
            self.say("De rien.")
            self.say("Je ne fais que mon travail.")
        else:
            self.say("You are welcome.")
            self.say("This is my job.")
        self.complete_request()     
    
    @register("de-DE", "(.*möchtest.*heiraten.*)|(.*willst.*heiraten.*)")
    @register("fr-FR", u"(.*veux-tu m'\u00E9pouser*)|(.*veux tu m'\u00E9pouser*)|(.*\u00E9pouse-moi.*)|(.*\u00E9pouse moi.*)|(.*marions nous.*)")
    @register("en-US", ".*Want.*marry*")
    def st_marry_me(self, speech, language):
        if language == 'de-DE':
            self.say("Nein Danke, ich stehe auf das schwarze iPhone von Deinem Kollegen.")     
        if language == 'fr-FR':
              self.say("Non merci, je suis amoureux de l'iPhone blanc de votre ami.") 
        else:
            self.say("No thank you, I'm in love with the black iPhone from you friend.")
        self.complete_request()

    @register("de-DE", ".*erzähl.*Witz.*")
    @register("fr-FR", ".*raconte.*blague*")
    @register("en-US", ".*tell.*joke*")
    def st_tell_joke(self, speech, language):
        if language == 'de-DE':
            self.say("Zwei iPhones stehen an der Bar ... den Rest habe ich vergessen.") 
        if language == 'fr-FR':
            self.say("C'est l'histoire d'un pingouin qui respire par le cul. Il s'asseoit et il meurt.")
        else:
            self.say("Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()

    @register("de-DE", ".*erzähl.*Geschichte.*")
    @register("fr-FR", ".*raconte.*histoire*")
    @register("en-US", ".*tell.*story*")
    def st_tell_story(self, speech, language):
        if language == 'de-DE':
            self.say("Es war einmal ... nein, es ist zu albern")
        if language == 'fr-FR':
            self.say(u"Il \u00E9tait une fois... non, elle est stupide.") 
        else:
            self.say("Far far away, there was ... no, too stupid")
        self.complete_request()

    @register("de-DE", "(.*Was trägst Du?.*)|(.*Was.*hast.*an.*)")
    @register("fr-FR", ".*Que portes? tu.*")
    @register("en-US", ".*what.*wearing*")
    def st_tell_clothes(self, speech, language):
        if language == 'de-DE':
            self.say("Das kleine schwarze oder war es das weiße?")
            self.say("Bin morgends immer so neben der Spur.")  
        if language == 'fr-FR':
            self.say("Un beau costume noir. Ou alors blanc?")
        else:
            self.say("I guess the small black one, or was it white?")
        self.complete_request()

    @register("de-DE", ".*Bin ich dick.*")
    @register("fr-FR", "(.*suis-je gross?e?.*)|(.*je suis gross?e?.*)")
    @register("en-US", ".*Am I fat*")
    def st_fat(self, speech, language):
        if language == 'de-DE':
            self.say("Dazu möchte ich nichts sagen.")       
        if language == 'fr-FR':
            self.say(u"Je pr\u00E9f\u00E8re ne pas me prononcer.")   
        else:
            self.say("I would prefer not to say.")
        self.complete_request()

    @register("de-DE", ".*klopf.*klopf.*")
    @register("fr-FR", ".*toc.*toc.*")
    @register("en-US", ".*knock.*knock.*")
    def st_knock(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Wer ist da?")
            answer = self.ask(u"\"{0}\" wer?".format(answer))
            self.say(u"Wer nervt mich mit diesen Klopf Klopf Witzen?")
        if language == 'fr-FR':
            answer = self.ask(u"Qui est-ce?")
            answer = self.ask(u"\"{0}\" qui?".format(answer))
            self.say(u"Qui m'importune avec ces blagues pu\u00E9riles?")
        else:
            answer = self.ask(u"Who's there?")
            answer = self.ask(u"\"{0}\" who?".format(answer))
            self.say(u"Who is bugging me with knock knock jokes?")
        self.complete_request()

    @register("de-DE", ".*Antwort.*alle.*Fragen.*")
    @register("en-US", ".*Ultimate.*Question.*Life.*")
    @register("fr-FR", ".*sens.*vie.*")
    def st_anstwer_all(self, speech, language):
        if language == 'de-DE':
            self.say("42")      
        if language == 'fr-FR':
            self.say("42")
        else:
            self.say("42")
        self.complete_request()

    @register("de-DE", ".*Ich liebe Dich.*")
    @register("fr-FR", ".*Je t'aime.*")
    @register("en-US", ".*I love you.*")
    def st_love_you(self, speech, language):
        if language == 'de-DE':
            self.say("Oh. Sicher sagst Du das zu allen Deinen Apple-Produkten.")            
        if language == 'fr-FR':
            self.say(u"Oh. Bien s\u00FBr, je parie que vous dites \u00E7a \u00E0 tous vos produits Apple.")
        else:
            self.say("Oh. Sure, I guess you say this to all your Apple products")
        self.complete_request()

    @register("de-DE", ".*Android.*")
    @register("fr-FR", ".*Android.*")
    @register("en-US", ".*Android.*")
    def st_android(self, speech, language):
        if language == 'de-DE':
            self.say("Ich denke da anders.") 
        if language == 'fr-FR':
            self.say(u"Je n'ai pas la m\u00EAme opinion l\u00E0 dessus.") 
        else:
            self.say("I think different about that.")
        self.complete_request()

    @register("de-DE", ".*Test.*1.*2.*3.*")
    @register("fr-FR", ".*test.*1.*2.*3.*")
    @register("en-US", ".*test.*1.*2.*3.*")
    def st_123_test(self, speech, language):
        if language == 'de-DE':
            self.say("Ich kann Dich klar und deutlich verstehen.")
        if language == 'fr-FR':
            self.say(u"Je vous entends tr\u00E8s bien.") 
        else:
            self.say("I can here you very clear.")
        self.complete_request()

    @register("de-DE", ".*Herzlichen.*Glückwunsch.*Geburtstag.*")
    @register("fr-FR", "(.*Joyeux.*anniversaire.*)|(.*Bon.*anniversaire.*)")
    @register("en-US", ".*Happy.*birthday.*")
    def st_birthday(self, speech, language):
        if language == 'de-DE':
            self.say("Ich habe heute Geburtstag?")
            self.say("Lass uns feiern!")       
        if language == 'fr-FR':
            self.say("C'est aujourd'hui mon anniversaire?")
            self.say(u"Faisons la f\u00EAte!")
        else:
            self.say("My birthday is today?")
            self.say("Lets make a party!")
        self.complete_request()

    @register("de-DE", ".*Warum.*bin ich.*Welt.*")
    @register("en-US", ".*Why.*I.*World.*")
    def st_why_on_world(self, speech, language):
        if language == 'de-DE':
            self.say("Das weiß ich nicht.")
            self.say("Ehrlich gesagt, frage ich mich das schon lange!")       
        else:
            self.say("I don't know that.")
            self.say("Ask my self this for a long time!")
        self.complete_request()

    @register("de-DE", ".*Ich bin müde.*")
    @register("fr-FR", u"(.*Je.*fatigu\u00E9.*)|(.*Je.*\u00E9puis\u00E9.*)")
    @register("en-US", ".*I.*so.*tired.*")
    def st_so_tired(self, speech, language):
        if language == 'de-DE':
            self.say("Ich hoffe, Du fährst nicht gerade Auto!") 
        if language == 'fr-FR':
            self.say(u"J'esp\u00E8re juste que vous n'\u00EAtes pas en train de conduire!")
        else:
            self.say("I hope you are not driving a car right now!")
        self.complete_request()

    @register("de-DE", ".*Sag mir.*Schmutzige.*")
    @register("en-US", ".*Tell me.*dirty.*")
    @register("fr-FR", ".*Dis moi.*cochonneries.*")
    def st_dirty(self, speech, language):
        if language == 'de-DE':
            self.say("Humus. Kompost. Bims. Schlamm. Kies.")            
        if language == 'fr-FR':
            self.say("Humus. Compost. Pierre ponce. Gadoue. Graviers.")
        else:
            self.say("Humus. Compost. Pumice. Mud. Gravel.")
        self.complete_request()

    @register("en-US", "(i think.*)")
    @register("fr-FR", "(je pense.*)")
    def st_ithink(self, speech, language):
        if language == 'en-US':
            list = ("Ok, why not.","Your mind is full of interesting things.","What a wonderful thought.","I see.","Why not...","I was thinking the same thing.")
            self.say(random.choice(list))
        else:
            list = ("D\'accord, pourquoi pas.",u"Vous pensez des choses tr\u00E8s int\u00E9ressantes.","Je vois.",u"Je pensais la m\u00EAme chose.","Je le pense aussi.","C'est cela, oui.")
            self.say(random.choice(list))
        self.complete_request()