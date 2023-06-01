import tkinter
from display import Display
from PIL import Image,ImageTk
import multiprocessing as mp
import time
from rabbitmqclient import MessageBroker as MB
import threading 

if __name__ == "__main__":
    pilimage = Image.open("lion.png")
    display = Display()
    messagebroker = MB(display.root)
    display.show(pilimage)
    th = threading.Thread(target=messagebroker.consume)
    th.start()
    display.run()

    
