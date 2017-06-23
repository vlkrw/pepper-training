#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

### Tactil head calculus ###

import qi
import argparse
import sys
import time

def main(session):
    # let's initialize things
    initialize(session)

    # Listen to an event # 
       
    # 1/ create a connection to ALMemory service
    memory = session.service("ALMemory")

    # 2/ subscribe to an event
    subscriber_front  = memory.subscriber("FrontTactilTouched")
    subscriber_rear   = memory.subscriber("RearTactilTouched")

    # 3/ get signal 
    front_signal = subscriber_front.signal
    rear_signal  = subscriber_rear.signal

    # 4/ connect signal to a callback function called on receiving a signal
    front_signal.connect(add_one)
    rear_signal.connect(subtract_one)

    """
    Loop on, wait for events until manual interruption.
    """
    print "Starting Calcul Tactil Head"
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print "Interrupted by user, stopping"
        #stop
        sys.exit(0)

def add_one(value):
    if (value == 1):
        print "add one"
    pass

def subtract_one(value):
    if (value == 1):
        print "subtract one"
    pass

def initialize(session):
    # 1/ create a connection to ALMemory service
    memory = session.service("ALMemory")    
    memory.insertData("Calculator/currentValue", 10)
    print "Default value is "  + str(memory.getData("Calculator/currentValue"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    main(session)
