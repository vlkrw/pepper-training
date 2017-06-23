#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""
    Exercice : A Simple class to illustrate dynamic concept

    - Complete the code below
    - Look through API documentation online and find the functions you need
    - Check the content of the topic file provided
    - Dynamic concept can be initialized with one or more elements. 
    - More elements can be added from keyboard.
    - Ctrl+C to interrupt

    Warning : 
    This script needs a topic file that should be uploaded to the robot beforehand
    Default location and topic file name should be : /home/nao/10-008-dynamic-concept_enu.top
    $ scp 10-008-dynamic-concept_enu.top nao@<robot_ip>:~

    Usage : python dynamic-concept.py --ip <ip_of_my_robot> 

"""

import qi
import time
import sys
import argparse


class DynConcept(object):
    """
    A Simple class to illustrate dynamic concept.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(DynConcept, self).__init__()
        app.start()
        self.session = app.session
        self.dialog = self.session.service("ALDialog")
        self.service_name="DynConcept"

        # a concept is a list isn't ?
        self.enNames=["Paul"]
        
        # where is the concept name declared 
        self.conceptName = "names"
        self.lang = "enu"

        # let's set the dynamic concept here
        self.dialog.setConcept(self.conceptName,self.lang, self.enNames)


    def initialize(self): 
        pass


    def start_diag(self):
        self.loaded_topic = self.dialog.loadTopic("/home/nao/10-008-dynamic-concept_enu.top")
        self.dialog.activateTopic(self.loaded_topic)
        self.dialog.subscribe(self.service_name)

    def stop_diag(self):    
        self.dialog.unsubscribe(self.service_name)
        self.dialog.deactivateTopic(self.loaded_topic)
        self.dialog.unloadTopic(self.loaded_topic)


    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting DynConcept"
        self.start_diag()

        try:
            while True:
                word = raw_input("Enter a new value to add to concept (ctrl+C to exit): ")
                self.add_concept(word)

        except KeyboardInterrupt:
            print "Interrupted by user, stopping script"
            # unsubscribe what is needed here if necessary
            self.stop_diag()
            #stop
            time.sleep(2)
            sys.exit(0)


    def add_concept(self, word):
        ladd = list()
        ladd.append(word)
        self.dialog.addToConcept(self.conceptName, self.lang, ladd )
        print("added word " + word + " to concept " + self.conceptName)


if __name__ == "__main__":

    print "This script needs a topic file that should be uploaded to the robot beforehand"
    print "Default location and topic file name should be : /home/nao/10-008-dynamic-concept_enu.top"

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["DynConcept", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    calc = DynConcept(app)
    calc.run()
