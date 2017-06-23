#! /usr/bin/env python

import qi, time
"""
	Example for a simple callback function call on receiving a signal
"""
# my callback function
def mycallback_function(value):
	print "Callback function call"
	print "You touched my head"
	print value
    
app = qi.Application(["simplescript", "--qi-url=tcp://10.0.137.66:9559"])
app.start()

# Listen to an event :
# 1. create a service to ALMemory
memory		= app.session.service("ALMemory")

# 2. subscribe to an event
subscriber	= memory.subscriber("MyApp/TestRaiseEvent")

# 3. connect to signal and declare a callback to call on receiving a signal
# get the connection_id to unsubscribe on disconnection
event_connection_id  = subscriber.signal.connect(mycallback_function)    

# use ALTextToSpeech method
tts = app.session.service("ALTextToSpeech")
tts.say("You have 10 seconds to touch my head. See the command line terminal, the callback function is called.")

# wait for 10 seconds
time.sleep(1000)

# 4. leave cleanly
subscriber.signal.disconnect(event_connection_id)
app.stop()
print 'Bye bye'
