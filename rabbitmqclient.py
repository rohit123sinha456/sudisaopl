#!/usr/bin/env python
import pika,sys,os
import configparser
import time
from pika.exceptions import AMQPConnectionError
from pika.exceptions import AMQPHeartbeatTimeout,ChannelWrongStateError
from retry import retry
class MessageBroker:
    def __init__(self,eventloop):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = config["ADMIN"]["URL"]#'10.12.1.131'
        self.queuename = config["RABBITMQ"]["QUEUE"]
        self.eventloop = eventloop
        self.waittime = 40
        self.connect()
        #self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        #self.channel = self.connection.channel()
        #self.channel.queue_declare(queue=self.queuename)
    def connect(self):
        while(True):
            try:
                self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
                self.channel = self.connection.channel()
                self.channel.queue_declare(queue=self.queuename)
                break
            except AMQPConnectionError :
                print("[x] Couldn't connect to Server Retrying in 10 seconds again ..")
                time.sleep(self.waittime)

    def callback(self,ch,method,properties,body):
        print("[x] Recieved %r"%body)
        if(self.eventloop is not None):
            if(body == b'H'):
                self.eventloop.event_generate('<<SIG>>',when='tail')
            if(body == b'K'):
                print("[x] Sending Event to Close Tkinter Windows")
                self.eventloop.event_generate('<<STOPPROC>>',when='tail')
                print("[x] Stopping Channel Consuming")
                self.channel.stop_consuming()
                print("[x] Closing Connection")
                self.connection.close()
                print("[x] Exiting Process")
                sys.exit(0)

    def consume(self):
        self.channel.basic_consume(queue=self.queuename,on_message_callback=self.callback,auto_ack=True)
        print("[x] Waiting for Message")
        while True:
            try:
                print("Starting Message Consuming")
                self.channel.start_consuming()
            except AMQPHeartbeatTimeout:
                print("[x] Failed to get heartbeat from rabbitmq server.Please check rabbitMq Server")
                time.sleep(self.waittime)
            except ChannelWrongStateError:
                print("[x] Channel is closef. Please check ethernet connection")
                time.sleep(self.waittime)
            except KeyboardInterrupt:
                self.channel.stop_consuming()
                self.connection.close()


if __name__=="__main__":
    mb = MessageBroker(None)
    mb.consume()
