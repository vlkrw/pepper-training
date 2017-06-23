#! /usr/bin/env python

import qi
import time

# app = qi.Application(["simplescript", "--qi-url=tcp://127.0.0.1:9559"])
app = qi.Application()
app.start()

tts = app.session.service("ALTextToSpeech")

# my callback function
def mycallback_function(value):
    if value > 0:
        print "Call back"
        tts.say("You touched me!")
        print value

# Listen to an event :
# 1. create a service to ALMemory
memory		= app.session.service("ALMemory")

# 2. subscribe to an event
subscriber	= memory.subscriber("FrontTactilTouched")

# 3. connect to signal and declare a callback to call on receiving a signal
# get the connection_id to unsubscribe on disconnection
event_connection_id  = subscriber.signal.connect(mycallback_function)    

# use ALTextToSpeech method
tts.say("You have 10 seconds to touch my head.")

# wait for 10 seconds
time.sleep(10)

# 4. leave cleanly
subscriber.signal.disconnect(event_connection_id)
app.stop()

print 'Bye bye'