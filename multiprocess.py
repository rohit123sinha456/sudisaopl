import tkinter
from display import Display
from PIL import Image,ImageTk
import multiprocessing as mp
import time
from rabbitmqclient import MessageBroker as MB
import threading 
import os

if __name__ == "__main__":
    pilimage = Image.open(os.path.join(os.getcwd(),"lion.png"))
    display = Display()
    messagebroker = MB(display.root)
    display.show(pilimage)
    th = threading.Thread(target=messagebroker.consume)
    th.start()
    display.run()

    
