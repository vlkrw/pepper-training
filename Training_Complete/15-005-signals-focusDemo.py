#!/usr/bin/env python

"""
    Example using signals
    The script creates a service FocusDemo
    - connects to ALUserSession.focusedUser signal
    - on robot focusing on human, usid is displayed on terminal
"""

import signal
import qi
import sys

class FocusDemo(object):
    def __init__(self, app):
        self.application = app
        self.session = app.session
        self.service_name = self.__class__.__name__


        # connect a callback on receiving a signal form another service
        us = self.session.service("ALUserSession")
        self.signal_id = us.focusedUser.connect(self.on_focused_user)

    @qi.nobind    
    def on_focused_user(self, value):
        print 'usid is ' + str(value)

if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python main.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = FocusDemo(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    app.run()
    app.session.unregisterService(service_id)