import tkinter
from display import Display
from PIL import Image,ImageTk
import multiprocessing as mp
import time
from rabbitmqclient import MessageBroker as MB
import threading 
import os
import configparser
from Log import Log
from utilities import WORKDIR
if __name__ == "__main__":
    loggerobject = Log()
    logger = loggerobject.getLog()
    logger.info("[-] Stating Application")
    config = configparser.ConfigParser()
    config.read(WORKDIR+'config.ini')
    default_image = config["DEFAULTIMAGE"]["IMGPATH"]
    pilimage = Image.open(default_image)
    display = Display()
    messagebroker = MB(display.root)
    display.show(pilimage)
    th1 = threading.Thread(target=messagebroker.consume)
    #th2 = threading.Thread(target=display.run);
    #th2.start()
    th1.start()
    #th2.start()
    display.run()

    
