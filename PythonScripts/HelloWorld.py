from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "10.0.137.152", 9559)
tts.say("Hello, world!")