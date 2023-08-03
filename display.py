import tkinter
from PIL import Image,ImageTk
import time
import multiprocessing as mp
import threading
from getimage import HTTPClient
#https://stackoverflow.com/questions/47316266/can-i-display-image-in-full-screen-mode-with-pil

class Display(object):
    def __init__(self):
        root = tkinter.Tk()
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0"%(self.screen_width,self.screen_height))
        self.root.focus_set()
        self.root.bind("<Escape>",self.quitProg)
        self.root.bind("<<SIG>>",self.handlesignal)
        self.root.bind("<<STOPPROC>>",self.quitProg)
        self.root.bind("<<DFLTSCRN>>",lambda event,imageName="default.png":self.update(imageName))
        self.canvas = tkinter.Canvas(self.root,width=self.screen_width,height=self.screen_height)
        self.canvas.pack()
        self.canvas.configure(background="black")
        self.currenttag = 0
        self.httpclient = HTTPClient()
    
    def getEventRoot(self):
        return self.root

    def show(self,pilimage):
        imgWidth,imgHeight = pilimage.size
        print(imgWidth,imgHeight,self.screen_width,self.screen_height)
        if(imgWidth>self.screen_width or imgHeight>self.screen_height):
            ratio = min(self.screen_width/imgWidth,self.screen_height/imgHeight)
            imgWidth = int(imgWidth*ratio)
            imgHeight = int(imgHeight*ratio)
            pilimage = pilimage.resize((imgWidth,imgHeight),Image.ANTIALIAS)
        self.showimage = ImageTk.PhotoImage(pilimage)
        self.imagesprite = self.canvas.create_image(self.screen_width/2,self.screen_height/2,image=self.showimage)
        self.currenttag = self.imagesprite
        #self.button = tkinter.Button(self.root,text="change",command=self.update)
        #self.button.pack()
        #self.run()

    def update(self,imageName='temp.png'):
        print("[x] Updating the image")
        pilimage = Image.open(imageName)
        print("[x] Reading teamporary image ")
        imgWidth,imgHeight = pilimage.size
        print("[x] Getting Image Size")
        if(imgWidth>self.screen_width or imgHeight>self.screen_height):
            ration = min(self.screen_width/imgWidth,self.screen_height/imgHeight)         
            imgWidth = int(imgWidth*ration)                                  
            imgHeight = int(imgHeight*ration)                                
            pilimage = pilimage.resize((imgWidth,imgHeight),Image.ANTIALIAS)
            print("[x] Resizing Image Done")
        self.updateimage = ImageTk.PhotoImage(pilimage)
        print("[x] Converting Image to TKinter Format")
        self.canvas.itemconfig(self.currenttag,image=self.updateimage)
        print("[x] Pushing Update to aTkinter Cnvas")


    def run(self):
        self.root.overrideredirect(0)
        self.root.mainloop()

    def quitProg(self,event):
        print(event.widget)
        event.widget.destroy()

    def simulatesignal(self):
        time.sleep(5)
        self.root.event_generate('<<DFLTSCRN>>',when='tail')
    
    def handlesignal(self,event):
        print("handle signal")
        try:
            self.httpclient.getresponse()
            filename = self.httpclient.saveimage()
            time.sleep(2)
            self.update(filename)
        except Exception as e:
            print(e)
            print("Some error in http or update")
if __name__=="__main__":
    pilImage = Image.open("lion.png")
    display = Display()
    display.show(pilImage)
    th = threading.Thread(target=display.simulatesignal)
    th.start()
    display.run()

