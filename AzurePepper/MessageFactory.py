import cStringIO as StringIO
import datetime
import uuid
import struct
import json

requestId = str(uuid.uuid4()).replace("-", "").encode('utf8').upper()
receivedMessages = {}
connection = {}

MESSAGE_TYPE_TURN_END = 1
MESSAGE_TYPE_PHRASE = 2
MESSAGE_TYPE_HYPOTHESIS = 3

def getIsoTime():
    return datetime.datetime.utcnow().isoformat()[:-3] + "Z"

#RIFF Header siehe http://www.topherlee.com/software/pcm-tut-wavformat.html
def createRiffHeader():

    nchannels = 1
    bytes_per_sample = 2730
    frame_rate = 16000

    output = StringIO.StringIO()
    output.write('RIFF')
    output.write(struct.pack('<L', 0))
    output.write('WAVE')
    output.write('fmt ')
    output.write(struct.pack('<L', 21840))
    output.write(struct.pack('<H', 0x0001))
    output.write(struct.pack('<H', nchannels))
    output.write(struct.pack('<L', frame_rate))
    output.write(struct.pack('<L', frame_rate * nchannels * bytes_per_sample))
    output.write(struct.pack('<H', nchannels * bytes_per_sample))
    output.write(struct.pack('<H', bytes_per_sample * 8))
    output.write('data')
    output.write(struct.pack('<L', 0))

    data = output.getvalue()
    output.close()

    return data


def createConfigHeader():
    header =    "path: speech.config" + "\r\n"\
                "x-requestid: " + requestId + "\r\n"\
                "x-timestamp: " + getIsoTime() + "\r\n"\
                "content-type:	application/json; charset=utf-8" + "\r\n"

    header += "\r\n"
    return header


def createTelemetryHeader():
    header =    "path: telemetry" + "\r\n"\
                "x-requestid: " + requestId + "\r\n"\
                "x-timestamp: " + getIsoTime() + "\r\n"\
                "content-type: application/json" + "\r\n"

    header += "\r\n"
    return header


def createAudioHeader():
    output = StringIO.StringIO()
    output.write(struct.pack('>H', 0x007e))         #Header Size
    output.write("Path: audio")
    output.write(struct.pack('>H', 0x0d0a))
    output.write("X-RequestId: " + requestId)
    output.write(struct.pack('>H', 0x0d0a))
    output.write("X-Timestamp: " + getIsoTime())
    output.write(struct.pack('>H', 0x0d0a))
    output.write("Content-Type: audio/x-wav")

    data = output.getvalue()
    output.close()

    return data


def createConfigMessage():
    data = {
          "context": {
            "system": {
              "version": "2.0.12341",
            },
            "os": {
              "platform": "Linux",
              "name": "Debian",
              "version": "2.14324324"
            },
            "device": {
              "manufacturer": "Contoso",
              "model": "Fabrikan",
              "version": "7.341"
            }
          }
        }

    return createConfigHeader() + json.dumps(data).encode('utf8')


def createTelemetryMessage():
    message = createTelemetryHeader()

    connection["Id"] = requestId
    connection["Name"] = "Connection"

    microphone = {}
    microphone["Name"] = "Microphone"
    microphone["Start"] = connection["Start"]
    microphone["End"] = connection["End"]

    messageBody = {
        "Metrics": [connection, microphone],
        "ReceivedMessages": receivedMessages
    }

    message += json.dumps(messageBody)

    return message


def saveMessage(message):
    for line in str(message).splitlines():
        if "path:" in line.lower():
            messageType = line.lower().split(":")[1]
            if not messageType in receivedMessages.keys():
                receivedMessages[messageType] = []
            receivedMessages[messageType].append(getIsoTime())
            break


def connectionStart():
    connection["Start"] = getIsoTime()


def connectionEstablished():
    connection["End"] = getIsoTime()

def getMessageContent(message):
    return str(message).split("\r\n\r\n")[1]

def getMessageType(message):
    for line in str(message).splitlines():
        if "path:turn.end" in line.lower():
            return MESSAGE_TYPE_TURN_END
        if "path:speech.phrase" in line.lower():
            return MESSAGE_TYPE_PHRASE
        if "path:speech.hypothesis" in line.lower():
            return MESSAGE_TYPE_HYPOTHESIS