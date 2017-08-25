from auth import AzureAuthClient
from ws4py.client.threadedclient import WebSocketClient
import uuid
import MessageFactory
import AudioStreamer
import json

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
        print "Connected!"
        self.connected = True
        MessageFactory.connectionEstablished()
        self.sendConfigMessage()
        self.audioStreamer = AudioStreamer.AudioStreamer(self)
        self.audioStreamer.start()

    def sendConfigMessage(self):
        self.send(MessageFactory.createConfigMessage())

    def sendTelemetryMessage(self):
        self.send(MessageFactory.createTelemetryMessage())

    def received_message(self, message):
        self.parseAndOutputResult(message)
        MessageFactory.saveMessage(message)
        if "turn.end" in MessageFactory.receivedMessages.keys():
            print "restarting..."
            self.audioStreamer.stop()
            self.sendTelemetryMessage()
            MessageFactory.receivedMessages = {}
            self.audioStreamer.join()
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


def startWebsocket():
    ws = SpeechToTextClient(startWebsocket)
    MessageFactory.connectionStart()
    ws.connect()
    ws.run_forever()

startWebsocket()