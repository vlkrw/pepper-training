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
    A simple class to check if memory key are added.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        #super(Calculus, self).__init__()
        app.start()
        session = app.session

        # 1/ create a connection to ALMemory service
        self.memory = session.service("ALMemory")
        
        # 2/ subscribe to an event
        self.subscriber_front  = self.memory.subscriber("FrontTactilTouched")
        self.subscriber_rear   = self.memory.subscriber("RearTactilTouched")

        # 3/ get signal 
        self.front_signal = self.subscriber_front.signal
        self.rear_signal  = self.subscriber_rear.signal

        # 4/ connect signal to a callback function called on receiving a signal
        self.id_connect_add = self.front_signal.connect(self.add_one)
        self.id_connect_sub = self.rear_signal.connect(self.subtract_one)

        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")


    def initialize(self):
        #mem = session.service("ALMemory")  
        #mem.insertData("Calculator/currentValue", 10)
        #print "Default value is "  + str(mem.getData("Calculator/currentValue"))
        self.memory.insertData("Calculator/currentValue", 10)
        print "Default value is "  + str(self.memory.getData("Calculator/currentValue"))
        self.tts.say("Default value is "  + str(self.memory.getData("Calculator/currentValue")))

    def print_current_value(self):
        print self.memory.getData("Calculator/currentValue")

    ### CALLBACK FUNCTIONS ###
    def add_one(self, value):
        if (value == 1):
            print "add one on pressing"
            cur_val = self.memory.getData("Calculator/currentValue")
            self.memory.insertData("Calculator/currentValue", cur_val + 1 )
            self.print_current_value()
        pass

    def subtract_one(self, value):
        if (value == 1):
            print "add one on pressing"
            cur_val = self.memory.getData("Calculator/currentValue")
            self.memory.insertData("Calculator/currentValue", cur_val - 1 )
            self.print_current_value()  
        pass

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting Calculus"
        # initialize things 
        self.initialize()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping Calculus"
            # cleanup things
            print "Disconnecting signals..."
            self.front_signal.disconnect(self.id_connect_add)
            self.rear_signal.disconnect(self.id_connect_sub)
            #stop
            print "Exiting"
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
