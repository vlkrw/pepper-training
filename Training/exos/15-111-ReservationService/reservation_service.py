#!/usr/bin/env python
import qi
import sys
import os

class ReservationService:
    services_connected = None
    subscriber_list = []

    def __init__(self, application):
        # Getting a session that will be reused everywhere
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)

        # Do some initializations before the service is registered to NAOqi
        self.logger.info("Initializing...")
        self.connect_services()
        self.create_signals()
        self.logger.info("Initialized!")


    @qi.nobind
    def start_service(self):
        self.logger.info("Starting service...")
        self.lang = "enu"   
        # do something when the service starts
        self.show_tablet()
        self.load_dialog()
        self.logger.info("Started!")

    @qi.nobind
    def stop_service(self):
        # probably useless, unless one method needs to stop the service from inside.
        # external naoqi scripts should use ALServiceManager.stopService if they need to stop it.
        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!")

    @qi.nobind
    def create_signals(self):
        self.logger.info("Creating ColorChosen event...")
        # When you can, prefer qi.Signals instead of ALMemory events
        memory = self.session.service("ALMemory")

        event_name = "form"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.render)
        self.subscriber_list.append([event_subscriber, event_connection])

        event_name = "check"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.check_availability)
        self.subscriber_list.append([event_subscriber, event_connection])

        event_name = "room"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.onRoom)
        self.subscriber_list.append([event_subscriber, event_connection])

        event_name = "html"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.onHtml)
        self.subscriber_list.append([event_subscriber, event_connection])



        event_name = "available"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.onAvailable)
        self.subscriber_list.append([event_subscriber, event_connection])

        event_name = "notAvailable"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.onNotAvailable)
        self.subscriber_list.append([event_subscriber, event_connection])

        event_name = "exit"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_exit)
        self.subscriber_list.append([event_subscriber, event_connection])


        self.logger.info("Event created!")

    @qi.nobind
    def disconnect_signals(self):
        self.logger.info("Unsubscribing to all events...")
        for sub, i in self.subscriber_list :
            try:
                sub.signal.disconnect(i)
            except Exception, e:
                self.logger.info("Error unsubscribing: {}".format(e))
        self.logger.info("Unsubscribe done!")

    @qi.nobind
    def connect_services(self):
        # connect all services required by your module
        # done in async way over 30s,
        # so it works even if other services are not yet ready when you start your module
        # this is required when the service is autorun as it may start before other modules...
        self.logger.info('Connecting services...')
        self.services_connected = qi.Promise()
        services_connected_fut = self.services_connected.future()

        def get_services():
            try:
                self.memory = self.session.service('ALMemory')
                self.dialog = self.session.service('ALDialog')
                # connect other services if needed...
                self.logger.info('All services are now connected')
                self.services_connected.setValue(True)
            except RuntimeError as e:
                self.logger.warning('Still missing some service:\n {}'.format(e))

        get_services_task = qi.PeriodicTask()
        get_services_task.setCallback(get_services)
        get_services_task.setUsPeriod(int(2*1000000))  # check every 2s
        get_services_task.start(True)
        try:
            services_connected_fut.value(30*1000)  # timeout = 30s
            get_services_task.stop()
        except RuntimeError:
            get_services_task.stop()
            self.logger.error('Failed to reach all services after 30 seconds')
            raise RuntimeError


    ### Reservation processing ###

    def check_availability(self, value):
        self.logger.info("Checking availability")

        time = self.memory.getData("time")
        date = self.memory.getData("date")
        # list of rooms
        rooms=["tatooine", "millenium falcon", "chubaka"]

        if date=="samedi" or date=="saturday":
            rooms=[]

        if len(rooms)==0:
            self.memory.raiseEvent("notAvailable",1)
        else:
            # define dynamic concept
            self.dialog.setConcept("available_rooms", self.lang , rooms)
            self.memory.raiseEvent("available",1)

        self.logger.info("Availability checked")


    def render(self, value):
        self.logger.info("Call render")

        rooms=self.dialog.getConcept("available_rooms", self.lang)
        html=""
        for r in rooms:
            s="""
            <input type="submit" class="submit" value="%s" onclick="raiseEvent('clickRoom','%s');"><br/>
            """%(r,r)
            html+=s

        self.memory.raiseEvent("html",html)
        self.logger.info(html)
        self.logger.info("Rendering done")

    def onAvailable(self, value):
        pass

    def onNotAvailable(self, value):
        pass

    def onRoom(self, value):
        pass

    def onHtml(self, value):
        pass

    ### Utility functions ###

    @qi.nobind
    def load_dialog(self):
        # if needed, here is how to load a dialog from Python
        self.logger.info("Loading dialog")
        dialog = self.session.service("ALDialog")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        topic_path = os.path.realpath(os.path.join(dir_path, "reservation", "reservation_enu.top"))
        self.logger.info(topic_path)
        try:
            self.loadedTopic = dialog.loadTopic(topic_path)
            dialog.activateTopic(self.loadedTopic)
            dialog.subscribe(self.service_name)
        except Exception, e:
            self.logger.info("Error while loading dialog: {}".format(e))

    @qi.nobind
    def unload_dialog(self):
        # if needed, here is how to unload a dialog from Python
        self.logger.info("Unloading dialog")
        try:
            dialog = self.session.service("ALDialog")
            dialog.unsubscribe(self.service_name)
            dialog.deactivateTopic(self.loadedTopic)
            dialog.unloadTopic(self.loadedTopic)
        except Exception, e:
            self.logger.info("Error while unloading dialog: {}".format(e))

    @qi.nobind
    def add_memory_subscriber(self, event, callback):
        # add memory subscriber utility function
        self.logger.info("Subscribing to {}".format(event))
        try:
            sub = self.memory.subscriber(event)
            con = sub.signal.connect(callback)
            self.connected_signals.append([sub, con])
        except Exception, e:
            self.logger.info("Error while subscribing: {}".format(e))

    @qi.nobind
    def remove_memory_subscribers(self):
        # remove memory subscribers utility function
        self.logger.info("unsubscribing to all signals...")
        for sub, con in self.connected_signals:
            try:
                sub.signal.disconnect(con)
            except Exception, e:
                self.logger.info("Error while unsubscribing: {}".format(e))

    @qi.nobind
    def show_tablet(self):
        # how to load and display the webpage on the tablet
        dir_path = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__))))
        folder = os.path.basename(dir_path)
        self.logger.info("Loading tablet page for app: {}".format(folder))
        try:
            ts = self.session.service("ALTabletService")
            ts.loadApplication(folder)
            ts.showWebview()
        except Exception, e:
            self.logger.info("Error while loading tablet: {}".format(e))

    @qi.nobind
    def hide_tablet(self):

        self.logger.info("Unloading tablet for app ")
        try:
            ts = self.session.service("ALTabletService")
            ts.hideWebview()
        except Exception, e:
            self.logger.info("Error while unloading tablet: {}".format(e))


    @qi.nobind
    def on_disable_movements(self, useless_value):
        # if needed, here is how to disable movements for a short time
        try:
            self.session.service("ALBasicAwareness").setEnabled(False)
            # ALMotion.setBreathEnabled("Body", 0)
            self.session.service("ALMotion").setIdlePostureEnabled("Head", 1)
            # ALBackgroundMovement.setEnabled(0)
        except Exception, e:
            self.logger.info("Error while disabling movements: {}".format(e))

    @qi.nobind
    def on_enable_movements(self, useless_value):
        # if needed, enable movements back
        try:
            self.session.service("ALBasicAwareness").setEnabled(True)
            # ALMotion.setBreathEnabled("Body", 0)
            self.session.service("ALMotion").setIdlePostureEnabled("Head", 0)
            # ALBackgroundMovement.setEnabled(0)
        except Exception, e:
            self.logger.info("Error while enabling movements: {}".format(e))

    ### ################# ###
    @qi.bind(methodName="onExit", returnType=qi.Void)
    def on_exit(self, value):
        self.stop_app()

    @qi.nobind
    def stop_app(self):
        # To be used if internal methods need to stop the service from inside.
        # external NAOqi scripts should use ALServiceManager.stopService if they need to stop it.
        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!")

    def cleanup(self):
        # called when your module is stopped
        self.logger.info("Cleaning...")
        self.unload_dialog()
        self.hide_tablet()
        self.disconnect_signals()   
        self.logger.info("End!")

if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python my_super_service.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = ReservationService(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.start_service()
    app.run()
    service_instance.cleanup()
    app.session.unregisterService(service_id)
