import time
import qi
import functools

class HandShakeService(object):

    def __init__(self, application):
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)
        
        self.logger.info("Initializing...")

        self.handDetect = False

        def awaitServiceStartup(p):

            try:
                self.motion = self.session.service("ALMotion")
                self.posture = self.session.service("ALRobotPosture")
                self.speech = self.session.service("ALTextToSpeech")
                self.memory = self.session.service("ALMemory")
                
                self.speakingMovement = self.session.service("ALSpeakingMovement")
                self.listeningMovement = self.session.service("ALListeningMovement")
                self.backgroundMovement = self.session.service("ALBackgroundMovement")
            except RuntimeError:
                self.logger.info("Services not found")
                return

            self.logger.info("Services found")
            p.setValue("SERVICES_READY")

        p = qi.Promise()
        f = p.future()

        pt = qi.PeriodicTask()
        pt.setCallback(functools.partial(awaitServiceStartup, p))
        pt.setUsPeriod(2000000)
        pt.start(True)

        if f.value(30000) == "SERVICES_READY":
            self.service_id = self.session.registerService(self.service_name, self)
            self.logger.info("Initialized!")
        else:
            self.logger.info("Initialization failed!")

        pt.stop()


    @qi.bind(methodName="stop", returnType=qi.Void)
    def stop_app(self):
        self.logger.info("Stopping service...")
        self.session.unregisterService(self.service_id)
        self.application.stop()
        self.logger.info("Stopped!") 

    @qi.bind(methodName="initiateHandShake", returnType=qi.Void)
    def initiateHandShake(self):
        """Initiates the robot to shake a hand.

        The robot will stop moving in general, because autonomous activities disturb the hand shaking animation. 
        The robot then raises it's hand to shake a hand.
        """
        self.speakingMovement.setEnabled(0)
        self.stopMovement()
        self.posture.goToPosture("StandInit", 0.7)
        self.giveHand()

    @qi.bind(methodName="giveHand", returnType=qi.Void)
    def giveHand(self):
        """Raises the robots right hand.

        This method only mechanically raises the robots arm. If the robot is active the animation tends to be interrupted.
        In that case one should call initiateHandShake.

        If the robots hand is not shaken it will return to a StandInit posture after 10 seconds.

        A successful handshake will raise a 'HandShakeService/handShakeCompleted' event. 
        """
        self.subscribe()
        self.motion.setStiffnesses(["RShoulderPitch", "RWristYaw"], [1.0, 1.0])
        self.motion.angleInterpolationWithSpeed(["RShoulderPitch", "RWristYaw"], [0.5, 0.3], 1.0)
        time.sleep(10)
        if not self.handDetect:
            self.resetRobot()
            self.unsubscribe()
    
    @qi.bind(methodName="startMovement", returnType=qi.Void)
    def startMovement(self):
        """Starts the robots autonomous movements. This should be called after the autonomous activity was stopped with 
        stopMovement.
        """
        self.setMovement(1)

    @qi.bind(methodName="stopMovement", returnType=qi.Void)
    def stopMovement(self):
        """Stops the robots autonomous movements. 
        """
        self.setMovement(0)

    @qi.nobind
    def setMovement(self, val):
        self.listeningMovement.setEnabled(val)
        self.motion.setBreathEnabled("Body", val)
        self.motion.setIdlePostureEnabled("Body", val)
        self.backgroundMovement.setEnabled(val)

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

        self.resetRobot()

    @qi.nobind
    def resetRobot(self):
        self.posture.goToPosture("StandInit", 0.5)
        self.startMovement()    
        self.speakingMovement.setEnabled(1)

if __name__ == "__main__":
    app = qi.Application()
    app.start()
    handShaker = HandShakeService(app)
    app.run()