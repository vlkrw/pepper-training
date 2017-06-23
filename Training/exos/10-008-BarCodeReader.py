#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to check if  a bar code is read """

import qi
import time
import sys
import argparse


class BarCodeReader(object):
    """
    A simple class to check if memory key are added.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(BarCodeReader, self).__init__()
        app.start()
        session = app.session

        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        self.got_barcode = False
        
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("BarcodeReader/BarcodeDetected")
        self.subscriber.signal.connect(self.on_bcr_detected)

        # Get the services ALTextToSpeech and ALBarcodeReader.
        self.tts = session.service("ALTextToSpeech")
        
        self.bcr = session.service("ALBarcodeReader")
        self.bcr.subscribe("BarCodeReader") 
        self.bcr_detected = False

    def on_bcr_detected(self, value):
        """
        Callback for event BarcodeReader/BarcodeDetected.
        """
        if value == []:  # empty value when the barcode disappears
            self.bcr_detected = False
        elif not self.got_barcode:  # only speak the first time a qrcode appears
            self.bcr_detected = True
            print "I saw a bar code!"
            self.tts.say("Hey bar code")
            # First Field = content.
            content = value[0]
            print "Content is: " + str(content)


    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting BarCodeReader"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping BarCodeReader"
            self.bcr.unsubscribe("BarCodeReader")
            #stop
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
        app = qi.Application(["BarCodeReader", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    barcode_patrol = BarCodeReader(app)
    barcode_patrol.run()
