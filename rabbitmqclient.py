#!/usr/bin/env python
import pika,sys,os
def callback(ch,method,properties,body):
    print("[x] Recieved %r"%body)

def main():
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='10.12.1.131'))
    channel = conn.channel()
    channel.queue_declare(queue="test")
    channel.basic_consume(queue="test",on_message_callback=callback,auto_ack=True)
    print("[x] Waiting for Message")
    channel.start_consuming()

if __name__=="__main__":
    main()
