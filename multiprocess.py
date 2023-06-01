import tkinter
from display import showPIL
from PIL import Image,ImageTk
import multiprocessing as mp


if __name__ == "__main__":
    pilimage = Image.open("lion.png")

    p1 = mp.Process(target=showPIL,args=(root,pilimage,))
    p1.start()
    
