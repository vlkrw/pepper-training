#!/usr/bin/env python

"""
    Example using signals
    The script creates a service SignalDemo
    - 2 signals created
    - see decorators
    - use qicli info SignalDemo
    - use qicli watch SignalDemo.startSignal  
    - use qicli call SignalDemo.onStart 1
"""

import signal
import qi
import sys
import time

class SignalDemo(object):

    def __init__(self, app):
        self.startSignal = qi.Signal()
        self.stopSignal = qi.Signal()
        self.service_name = self.__class__.__name__
        self.session = app.session

    @qi.bind(methodName="onStart", returnType=qi.Void, paramsType=[qi.String])    
    def on_start(self, value):
        print "Ok let's start"
        #send signal
        self.startSignal(value)

    @qi.bind(methodName="onStop", returnType=qi.Void)    
    def on_stop(self):
        print "Ok let's stop"
        # send signal
        self.stopSignal()


if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python main.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = SignalDemo(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    app.run()
    app.session.unregisterService(service_id)