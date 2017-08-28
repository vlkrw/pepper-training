from auth import AzureAuthClient
from ws4py.client.threadedclient import WebSocketClient
import uuid
import MessageFactory
import json
import qi
from threading import Lock
import sys

client_secret = '7c8dbb5b479847d0b840102d13cc348a'
ws_url = "wss://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?format=simple&language=de-DE"
auth_client = AzureAuthClient(client_secret)

class SpeechToTextClient(WebSocketClient):

    def __init__(self, stoppedCallback):
        self.stoppedCallback = stoppedCallback

        super(SpeechToTextClient, self).__init__(ws_url,
            headers=[
                ('Authorization', 'Bearer ' + auth_client.get_access_token()),
                ('X-ClientTraceId', uuid.uuid4())
        ])

    def opened(self):
        print("Connected!")
        self.connected = True
        MessageFactory.connectionEstablished()
        self.sendConfigMessage()
        self.speechToText = SpeechToTextModule("SpeechToText", session, self)
        self.serviceid = session.registerService("SpeechToText", self.speechToText)
        self.speechToText.startStreaming()

    def sendConfigMessage(self):
        self.send(MessageFactory.createConfigMessage())

    def sendTelemetryMessage(self):
        self.send(MessageFactory.createTelemetryMessage())

    def received_message(self, message):
        self.parseAndOutputResult(message)
        MessageFactory.saveMessage(message)
        if "turn.end" in MessageFactory.receivedMessages.keys():
            print "restarting..."
            session.unregisterService(self.serviceid)
            self.speechToText.stopStreaming()
            self.sendTelemetryMessage()
            MessageFactory.receivedMessages = {}
            self.stoppedCallback()

    def parseAndOutputResult(self, message):
        if MessageFactory.getMessageType(message) == MessageFactory.MESSAGE_TYPE_PHRASE:
            result = json.loads(MessageFactory.getMessageContent(message))
            if result["RecognitionStatus"] == "Success":
                print result["DisplayText"]

        if MessageFactory.getMessageType(message) == MessageFactory.MESSAGE_TYPE_HYPOTHESIS:
            result = json.loads(MessageFactory.getMessageContent(message))
            print "[" + result["Text"] + "]"


    def close(self, code, reason):
        print "Closing (" + str(code) + "): " + str(reason)


@qi.multiThreaded()
class SpeechToTextModule():

    def __init__( self, strName, session, stt_client):
        self.session = session
        self.name = strName
        self.ALAudioDevice = self.session.service("ALAudioDevice")
        self.isProcessingDone = False
        self.lock = Lock()
        self.stt_client = stt_client

    def startStreaming(self):
        """ Process one speech sentence """
        # ask for all microphones signals interleaved sampled at 48kHz
        self.ALAudioDevice.setClientPreferences(self.name, 16000, 3, 0)
        self.ALAudioDevice.subscribe(self.name)
        self.sentFirstChunk = False
        print("stream started!")

    def stopStreaming(self):
        """ Interrupt recognition """
        self.lock.acquire()
        self.isProcessingDone = True
        self.lock.release()
        print("stream stopped!")

    def processRemote(self, nbOfChannels, nbOfSamplesByChannel, timestamp, inputBuffer):
        """ This is the callback that receives the audio buffers """
        message = MessageFactory.createAudioHeader()

        if not self.sentFirstChunk:
            message += MessageFactory.createRiffHeader()
            self.sentFirstChunk = True

        self.lock.acquire()
        message += inputBuffer
        
        self.stt_client.send(message, binary=True)

        self.lock.release()


def startWebsocket():
    ws = SpeechToTextClient(startWebsocket)
    MessageFactory.connectionStart()
    ws.connect()
    ws.run_forever()


qiapp = qi.Application(sys.argv)
qiapp.start()
session = qiapp.session
startWebsocket()