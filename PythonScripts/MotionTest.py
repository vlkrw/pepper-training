import time
import argparse
from naoqi import ALProxy

def getYawAngle(motionProxy):
    names = ["HeadYaw"]
    return motionProxy.getAngles(names, True)[0]

def getPitchAngle(motionProxy):
    names = ["HeadPitch"]
    return motionProxy.getAngles(names, True)[0]

def turnLeft(motionProxy):
    names = ["HeadYaw"]
    motionProxy.angleInterpolationWithSpeed(names, [getYawAngle(motionProxy)-0.1], 0.2)

def turnDown(motionProxy):
    names = ["HeadPitch"]
    motionProxy.angleInterpolationWithSpeed(names, [getPitchAngle(motionProxy)-0.1], 0.2)

def turnRight(motionProxy):
    names = ["HeadYaw"]
    motionProxy.angleInterpolationWithSpeed(names, [getYawAngle(motionProxy)+0.1], 0.2)

def turnUp(motionProxy):
    names = ["HeadPitch"]
    motionProxy.angleInterpolationWithSpeed(names, [getPitchAngle(motionProxy)+0.1], 0.2)

motionProxy = ALProxy("ALMotion", "10.0.137.152", 9559)

names = ["HeadYaw"]
print(str(motionProxy.getAngles(names, True)))

while getPitchAngle(motionProxy) < 0.3:
    turnUp(motionProxy)
    time.sleep(0.1)

while getPitchAngle(motionProxy) > -0.3:
    turnDown(motionProxy)
    time.sleep(0.1)


time.sleep(3.0)
print(str(motionProxy.getAngles(names, True)))