#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""
    Example: A Simple class to subscribe to camera

    Usage : python camera.py --ip <ip_of_my_robot> 

"""

import qi
import time
import sys
import argparse
from vision_definitions import kQQQQVGA, kQQQVGA, kQQVGA, kVGA, kQVGA, kVGA, k4VGA, k16VGA, kBGRColorSpace, kDepthColorSpace


class Camera(object):
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
        self.subscribed_cameras = []

        # 1/ create a connection to ALMemory service
        self.video = session.service("ALVideoDevice")
        self.subscribed_cameras = []
        self.camera_index = 0
        self.connection_name_stream = "camera_stream"
        self.connection_name_photo  = "camera_photo"
        self.connection_name_id = "camera"


    def initialize(self):
        for name in [self.connection_name_stream, self.connection_name_photo]:
            for i in range(0, 2):
                print("subscribing " + name + " " + str(i))
                self.connection_name_id = self.video.subscribeCamera(name,
                                                self.camera_index, kQQVGA, kBGRColorSpace,
                                                30)  # k16VGA
                self.subscribed_cameras.append(self.connection_name_id)

        for name in [self.connection_name_stream, self.connection_name_photo]:
            for i in range(0, 7):
                print("unsubscribing " + name + " " + str(i))
                self.video.unsubscribe(name)
                

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
            for cam in self.subscribed_cameras:
                print('unsubscribe ' + cam)
                self.video.unsubscribe(cam)
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

    calc = Camera(app)
    calc.run()
