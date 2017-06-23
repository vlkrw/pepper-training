#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


"""
    Example: A Simple class using Front and Rear Tactil head sensors to add or subtract one to an initial value 

    Usage : python calcul.py --ip <ip_of_my_robot> 

    Example :
    $ python 10-008-calculs-tactil-head-class.py --ip 10.42.0.38 
    Default value is 10
    [press Front Tactile sensor or qicli call ALMemory.raiseEvent FrontTactilTouched 1 --qi-url 10.42.0.38 ]
    add one on pressing
    11
"""

import qi
import time
import sys
import argparse


class Calculus(object):
    """
    A simple class to do the math.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(Calculus, self).__init__()
        app.start()
        session = app.session

        # 1/ create a connection to service
        self.memory = session.service("ALMemory")

        # 2/ subscribe to events
        self.subscriber_front  = self.memory.subscriber("FrontTactilTouched")
        self.subscriber_rear   = self.memory.subscriber("RearTactilTouched")

        # 3/ get signal 
        self.front_signal = self.subscriber_front.signal
        self.rear_signal  = self.subscriber_rear.signal

        # 4/ connect signal to a callback function called on receiving a signal
        self.front_id = self.front_signal.connect(self.add_one)
        self.rear_id  = self.rear_signal.connect(self.subtract_one)

        # Get the services ALTextToSpeech
        self.tts = session.service("ALTextToSpeech")

    def initialize(self): 
        # 5/ using insertData and getData functions
        # if memory key "Calculator/currentValue" does not exist it will be created
        self.memory.insertData("Calculator/currentValue", 10)
        print "Default value is "  + str(self.memory.getData("Calculator/currentValue"))
        self.tts.say("Default value is "  + str(self.memory.getData("Calculator/currentValue")))

    def print_current_value(self):
        # using getData function
        print self.memory.getData("Calculator/currentValue")
        self.tts.say("Value is "  + str(self.memory.getData("Calculator/currentValue")))


    ### CALLBACK FUNCTIONS ###
    def add_one(self, value):
        if (value == 1):
            print "add one"
            cur_val = self.memory.getData("Calculator/currentValue")
            self.memory.insertData("Calculator/currentValue", cur_val + 1 )
            self.print_current_value()
        pass

    def subtract_one(self, value):
        if (value == 1):
            print "subtract one"
            cur_val = self.memory.getData("Calculator/currentValue")
            self.memory.insertData("Calculator/currentValue", cur_val - 1 )
            self.print_current_value()  
        pass

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting Calculus"
        self.initialize()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping Calculus"
            self.front_signal.disconnect(self.front_id)
            self.front_signal.disconnect(self.rear_id)
            # This is the end !
            sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["Calculus", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    calc = Calculus(app)
    calc.run()

