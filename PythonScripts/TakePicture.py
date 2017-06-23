import time
from base64 import b64encode
import json
import requests
import qi
from PIL import Image

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
apikey = ""

class TextReader:

    def __init__(self):
        app = qi.Application(["simplescript", "--qi-url=tcp://10.0.137.152:9559"])
        app.start()

        self.videoCapture = app.session.service("ALVideoDevice")

    def make_image_data_list(self, image_filename):
        f = open(image_filename, 'rb')
        img_request = {
            'image': {'content': b64encode(f.read()).decode()},
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1
            }]
        }
        return img_request

    def make_image_data(self, image_filenames):
        imgdict = self.make_image_data_list(image_filenames)
        return json.dumps({"requests": imgdict }).encode()

    def request_ocr(self, api_key, image_filenames):
        response = requests.post(ENDPOINT_URL,
                                 data=self.make_image_data(image_filenames),
                                 params={'key': api_key},
                                 headers={'Content-Type': 'application/json'})
        return response

    def takePhoto(self):
        self.subscriberId = self.videoCapture.subscribeCamera("subscriber6", 0, 2, 11, 1)
        self.videoCapture.setResolution(self.subscriberId, 2)
        self.videoCapture.setParam(40, 1)

        imageData = self.videoCapture.getImageRemote(self.subscriberId)
        self.videoCapture.unsubscribe(self.subscriberId)

        im = Image.frombytes("RGB", (imageData[0], imageData[1]), str(bytearray(imageData[6])))
        im.save("image1.png", "PNG")

    def getText(self):
        response = self.request_ocr(apikey, "image1.png")
        if response.status_code != 200 or response.json().get('error'):
            return response.text
        else:
            responseText = response.json()['responses']
            if not len(responseText) == 0 and responseText[0].has_key('textAnnotations'):
                t = responseText[0]['textAnnotations'][0]
                return "Text: " + t['description']
            else:
                return "No Text recognized!"

    def start(self):
        while True:
            startseconds = time.time()
            self.takePhoto()
            print self.getText()
            print str(time.time() - startseconds)
            time.sleep(2)


TextReader().start()