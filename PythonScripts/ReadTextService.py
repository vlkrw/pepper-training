#!/usr/bin/env python

import sys
import qi
import time
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract  #<-- Muss zuerst installiert werden!


class ReadTextService(object):

    def __init__(self, application):
        # Getting a session that will be reused everywhere
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)

        # Do some initializations before the service is registered to NAOqi
        self.logger.info("Initializing...")
        self.photoCapture = self.session.service("ALPhotoCapture")
        self.running = True
        self.logger.info("Initialized!")

    @qi.nobind
    def start_app(self):
        # do something when the service starts
        print "Starting app..."
        # @TODO: insert whatever the app should do to start
        while self.running:
            self.readText()
            time.wait(2)

        self.logger.info("Started!")

    def readText(self):
        self.photoCapture.setResolution(2)
        self.photoCapture.setPictureFormat("jpg")
        self.photoCapture.takePicture("/home/nao/recordings/cameras/", "image1")
        print(pytesseract.image_to_string(Image.open("/home/nao/recordings/cameras/image1.jpg"), lang='deu'))

    @qi.nobind
    def stop_app(self):
        # To be used if internal methods need to stop the service from inside.
        # external NAOqi scripts should use ALServiceManager.stopService if they need to stop it.
        self.running = False
        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!")

    @qi.nobind
    def cleanup(self):
        # called when your module is stopped
        self.logger.info("Cleaning...")
        # @TODO: insert cleaning functions here
        self.logger.info("Cleaned!")


if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python main.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = ReadTextService(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.start_app()
    app.run()
    service_instance.cleanup()
    app.session.unregisterService(service_id)
