#!/usr/bin/env python
import pika,sys,os
import configparser
import time
from pika.exceptions import AMQPConnectionError
class MessageBroker:
    def __init__(self,eventloop):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = config["ADMIN"]["URL"]#'10.12.1.131'
        self.queuename = config["RABBITMQ"]["QUEUE"]
        self.eventloop = eventloop
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
                time.sleep(10)

    def callback(self,ch,method,properties,body):
        print("[x] Recieved %r"%body)
        if(self.eventloop is not None):
            if(body == b'H'):
                self.eventloop.event_generate('<<SIG>>',when='tail')

    def consume(self):
        self.channel.basic_consume(queue=self.queuename,on_message_callback=self.callback,auto_ack=True)
        print("[x] Waiting for Message")
        self.channel.start_consuming()


if __name__=="__main__":
    mb = MessageBroker(None)
    mb.consume()
