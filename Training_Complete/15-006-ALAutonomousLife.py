#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to play with autonomous life """

import qi
import time
import sys
import argparse


class AutonomousLifeTesting(object):
    """
    A simple class to check if memory key are added.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        self.application = app
        self.session = app.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)

        # create a connection to ALMemory service
        self.memory = self.session.service("ALMemory")
        self.al     = self.session.service("ALAutonomousLife")
        self.tts    = self.session.service("ALTextToSpeech")
        #self.tts.say("App started")

    def start_app(self):
        print "getState " + self.al.getState()
        print "getRobotOffsetFromFloor" + str(self.al.getRobotOffsetFromFloor())
        for s in ['RobotPushed', 'RobotFell', 'RobotMoved', 'CriticalDiagnosis', 'CriticalTemperature']:
            print "isSafeguardEnabled " + s + " : " + str(self.al.isSafeguardEnabled(s))
        print "getLifeTime " + str(self.al.getLifeTime())
        print "getAutonomousActivityStatistics " + str(self.al.getAutonomousActivityStatistics())
        print "getFocusHistory " + str(self.al.getFocusHistory())
        print "getActivityNature " + str(self.al.getActivityNature("animations/Stand/Emotions/Positive/Amused_1"))
        #print "getFocusContext " + str(self.al.getFocusContext())
        for alab in ['AutonomousBlinking', 'BackgroundMovement', 'BasicAwareness', 'SpeakingMovement']:
            print "getAutonomousAbilityEnabled " + alab + " : " + str(self.al.getAutonomousAbilityEnabled(alab))
        print "getAutonomousAbilitiesStatus " 
        print self.al.getAutonomousAbilitiesStatus()

        # Autonomous Ability  Description For further details see ...
        # AutonomousBlinking  Enables the robot to make its eye LEDs blink when it sees someone and when it is interacting.   ALAutonomousBlinking
        # BackgroundMovement  Defines which slight movements the robot does autonomously when its limbs are not moving.   ALBackgroundMovement
        # BasicAwareness  Allows the robot to react to the environment to establish and keep eye contact with people. ALBasicAwareness
        # ListeningMovement   Enables some slight movements showing that the robot is listening.  ALListeningMovement
        # SpeakingMovement

# ALAutonomousLifeProxy::setState
# ALAutonomousLifeProxy::getState
# ALAutonomousLifeProxy::setRobotOffsetFromFloor
# ALAutonomousLifeProxy::getRobotOffsetFromFloor
# ALAutonomousLifeProxy::setSafeguardEnabled
# ALAutonomousLifeProxy::isSafeguardEnabled
# Methods for Activity focus management:
# ALAutonomousLifeProxy::focusedActivity
# ALAutonomousLifeProxy::switchFocus
# ALAutonomousLifeProxy::stopFocus
# ALAutonomousLifeProxy::stopAll
# Methods for Activity utilities:
# ALAutonomousLifeProxy::getLifeTime
# ALAutonomousLifeProxy::getActivityStatistics
# ALAutonomousLifeProxy::getAutonomousActivityStatistics
# ALAutonomousLifeProxy::getFocusHistory
# ALAutonomousLifeProxy::getStateHistory
# ALAutonomousLifeProxy::getActivityNature
# ALAutonomousLifeProxy::getActivityContextPermissionViolations
# ALAutonomousLifeProxy::getFocusContext
# Methods for Autonomous Ability management:
# ALAutonomousLifeProxy::setAutonomousAbilityEnabled
# ALAutonomousLifeProxy::getAutonomousAbilityEnabled
# ALAutonomousLifeProxy::getAutonomousAbilitiesStatus


    ### CALLBACK FUNCTIONS ###
    def default_callback(self, value):
        pass

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting AutonomousLifeTesting"
        self.al.switchFocus("untitled-a205b8/behavior_1", 1)
        #self.al.switchFocus("tabletfirstexercice-705510/behavior_1", 0)
 
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping AutonomousLifeTesting"

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
        app = qi.Application(["AutonomousLifeTesting", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    app.start()
    service_instance = AutonomousLifeTesting(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.start_app()
    service_instance.run()
    #service_instance.cleanup()
    app.session.unregisterService(service_id)