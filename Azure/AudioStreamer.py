import threading
import MessageFactory
import pyaudio

class AudioStreamer(threading.Thread):
    def __init__(self, websocket):
        self.running = False
        self.websocket = websocket
        super(AudioStreamer, self).__init__()

    def start(self):
        self.running = True
        super(AudioStreamer, self).start()

    def run(self):
        p = pyaudio.PyAudio()

        CHUNK = 16
        RATE = 16000

        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        isFirstChunk = True
        while self.running:
            message = MessageFactory.createAudioHeader()

            if isFirstChunk:
                message += MessageFactory.createRiffHeader()
                isFirstChunk = False

            message += stream.read(CHUNK)
            self.websocket.send(message, True)

        stream.close()

    def stop(self):
        self.running = False