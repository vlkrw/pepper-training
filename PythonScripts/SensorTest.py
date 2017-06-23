#! /usr/bin/env python

import qi, time

app = qi.Application(["simplescript", "--qi-url=tcp://10.0.137.152:9559"])
app.start()

memory		= app.session.service("ALMemory")
subscriberHead	= memory.subscriber("FrontTactilTouched")
subscriberRightHand = memory.subscriber("HandRightBackTouched")
subscriberLeftHand = memory.subscriber("HandLeftBackTouched")
tts 		= app.session.service("ALTextToSpeech")
audio = app.session.service("ALAudioDevice")

def callBackHead(value):
    if value > 0:
        tts.say("You touched my head!")
        print "Head touched"

def callBackRightHand(value):
    if value > 0:
        newvalue = audio.getOutputVolume() + 10
        if newvalue > 100:
            newvalue = 100
        audio.setOutputVolume(newvalue)
        tts.say("Volume is " + str(newvalue))
        print "Right Hand Touched"

def callBackLeftHand(value):
    if value > 0:
        newvalue = audio.getOutputVolume() - 10
        if newvalue < 0:
            newvalue = 0
        audio.setOutputVolume(newvalue)
        tts.say("Volume is " + str(newvalue))
        print "Left Hand Touched"

event_connection_id_head  = subscriberHead.signal.connect(callBackHead)
event_connection_id_righthand = subscriberRightHand.signal.connect(callBackRightHand)
event_connection_id_lefthand = subscriberLeftHand.signal.connect(callBackLeftHand)

time.sleep(100)

subscriberHead.signal.disconnect(event_connection_id_head)
subscriberRightHand.signal.disconnect(event_connection_id_righthand)
subscriberLeftHand.signal.disconnect(event_connection_id_lefthand)
app.stop()

print 'Bye bye'
