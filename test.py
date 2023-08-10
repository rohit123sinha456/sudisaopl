import pika

cred = pika.PlainCredentials('root','root')
c = pika.BlockingConnection(
        pika.ConnectionParameters("10.12.1.193",5672,'/',cred)
        )
ch = c.channel()
ch.queue_declare(queue="hello")

def callback(ch,m,p,b):
    print("whatysdgyug  %r"%b)

ch.basic_consume(queue="hello",on_message_callback=callback)
print("Start Comsuming")
ch.start_consuming()
c.close()
