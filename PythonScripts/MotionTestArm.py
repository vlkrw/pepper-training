import time
import qi

class HandShaker(object):

    def __init__(self):
        app = qi.Application()
        app.start()

        self.motion = app.session.service("ALMotion")
        self.posture = app.session.service("ALRobotPosture")
        self.speech = app.session.service("ALTextToSpeech")
        self.memory = app.session.service("ALMemory")

        self.handDetect = False

        self.motion.wakeUp()
        self.posture.goToPosture("StandInit", 0.5)

        time.sleep(1)

    def giveHand(self):
        self.subscribe()
        self.motion.setStiffnesses(["RShoulderPitch", "RWristYaw"], [1.0, 1.0])
        self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RWristYaw"], [0.5, 0.3], 1.0)
        time.sleep(10)
        if not self.handDetect:
            self.posture.goToPosture("StandInit", 0.5)

    def unsubscribe(self):
        self.subscriberRightHand.signal.disconnect(self.event_connection_id_righthand)

    def subscribe(self):
        self.subscriberRightHand = self.memory.subscriber("HandRightBackTouched")
        self.event_connection_id_righthand = self.subscriberRightHand.signal.connect(self.shakeHand)

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

handShaker = HandShaker()
handShaker.giveHand()