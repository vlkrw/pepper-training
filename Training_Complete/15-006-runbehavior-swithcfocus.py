#!/usr/bin/env python

import signal
import qi
import sys
import time

class BehaviorDemo(object):

    def __init__(self, app):
        self.service_name = self.__class__.__name__
        self.session = app.session

    def do_it(self):
                # extra test 
        self.al = self.session.service("ALAutonomousLife")
        self.bm = self.session.service("ALBehaviorManager")
        # extra test
        self.al.switchFocus("animation-training-demo/behavior_1", 1)
        time.sleep(15)    

        self.bm.runBehavior("animation-training-demo/behavior_1")
        


if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python main.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = BehaviorDemo(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.do_it()
    app.stop()
    app.session.unregisterService(service_id)