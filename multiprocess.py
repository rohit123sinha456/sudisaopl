import tkinter
from display import Display
from PIL import Image,ImageTk
import multiprocessing as mp
import time

def idk():
    print("In idl")
    time.sleep(5)
    display.update()

if __name__ == "__main__":
    pilimage = Image.open("lion.png")
    display = Display()
    p1 = mp.Process(target=display.show,args=(pilimage,))
    p2 = mp.Process(target=idk)
    p1.start()
    p2.start()


    
