#!/usr/bin/env python
import qi
import time

class SubscriptionMaster(object):
    def __init__(self,ip,port):
        connection_url = "tcp://" + ip + ":" + str(port)
        app = qi.Application(["SubscriptionMaster", "--qi-url=" + connection_url])
        super(SubscriptionMaster, self).__init__()
        app.start()
        self.memory = app.session.service("ALMemory")
        self.subscriber = {}
        
    def subscribe(self,topic,callback):
        subscriber = self.memory.subscriber(topic)
        subscriber.signal.connect(self.__cb)
        id = subscriber.signal.connect(callback)
        print "subscribed to event",topic
        self.subscriber[id] = subscriber
        return id
    
    def __cb(self,value):
        pass
        
    def unsubscribe(self,id):
        self.subscriber[id].signal.disconnect(id)
        print "unsubscribed"
        
class CustomClass():
    def __init__(self,ip):
        self.sm = SubscriptionMaster(ip,9559)
        self.id = self.sm.subscribe("myEvent", self.callback)
        self.id2 = self.sm.subscribe("myEvent2", self.callback)
        
    def callback(self,value):
        print"outer callback", value
            
    def unsubscribe(self):
        self.sm.unsubscribe(self.id)
        self.sm.unsubscribe(self.id2)

if __name__=="__main__":
    ip = "localhost"
    # Create a customized class that listens for 5 second to an event an then stops listening
    c = CustomClass(ip)
    time.sleep(5)
    c.unsubscribe()
    time.sleep(1)   
#     while True:
#         time.sleep(1)
