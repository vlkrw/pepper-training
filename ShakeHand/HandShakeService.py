import time
import qi

class HandShakeService(object):

    def __init__(self, application):
        # Getting a session that will be reused everywhere
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)
        # Do some initializations before the service is registered to NAOqi
        self.logger.info("Initializing...")

        self.motion = self.session.service("ALMotion")
        self.posture = self.session.service("ALRobotPosture")
        self.speech = self.session.service("ALTextToSpeech")
        self.memory = self.session.service("ALMemory")

        self.handDetect = False

        self.logger.info("Initialized!")


    @qi.bind(methodName="stop", returnType=qi.Void)
    def stop_app(self):
        # To be used if internal methods need to stop the service from inside.
        # external NAOqi scripts should use ALServiceManager.stopService if they need to stop it.
        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!") 

    @qi.bind(methodName="giveHand", returnType=qi.Void)
    def giveHand(self):
        self.subscribe()
        self.motion.setStiffnesses(["RShoulderPitch", "RWristYaw"], [1.0, 1.0])
        self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RWristYaw"], [0.5, 0.3], 1.0)
        time.sleep(10)
        if not self.handDetect:
            self.posture.goToPosture("StandInit", 0.5)
            self.unsubscribe()

    @qi.nobind
    def unsubscribe(self):
        self.subscriberRightHand.signal.disconnect(self.event_connection_id_righthand)

    @qi.nobind
    def subscribe(self):
        self.subscriberRightHand = self.memory.subscriber("HandRightBackTouched")
        self.event_connection_id_righthand = self.subscriberRightHand.signal.connect(self.shakeHand)

    @qi.nobind
    def shakeHand(self, value):
        print("Hand detected!")
        self.unsubscribe()
        
        self.motion.setExternalCollisionProtectionEnabled("RArm", False)

        self.handDetect = True
        self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.8, 1.0)
        time.sleep(0.5)
        self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.3, 1.0)
        time.sleep(0.5)
        self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.8, 1.0)
        time.sleep(0.5)
        self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.3, 1.0)
        time.sleep(0.5)
        self.motion.angleInterpolationWithSpeed("RElbowRoll", 0.8, 1.0)
        time.sleep(1)
        self.posture.goToPosture("StandInit", 0.5)

        self.motion.setExternalCollisionProtectionEnabled("RArm", True)
        self.memory.raiseEvent("HandShakeService/handShakeCompleted", "1")


if __name__ == "__main__":
    app = qi.Application()
    app.start()
    service_instance = HandShakeService(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    app.run()
    app.session.unregisterService(service_id)