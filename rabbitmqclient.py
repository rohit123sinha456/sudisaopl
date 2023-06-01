#!/usr/bin/env python
import pika,sys,os

class MessageBroker:
    def __init__(self,eventloop):
        self.host = '10.12.1.131'
        self.eventloop = eventloop
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='test')

    def callback(self,ch,method,properties,body):
        print("[x] Recieved %r"%body)
        if(self.eventloop is not None):
            if(body == b'H'):
                self.eventloop.event_generate('<<SIG>>',when='tail')

    def consume(self):
        self.channel.basic_consume(queue="test",on_message_callback=self.callback,auto_ack=True)
        print("[x] Waiting for Message")
        self.channel.start_consuming()


if __name__=="__main__":
    mb = MessageBroker(None)
    mb.consume()
