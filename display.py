import tkinter
from PIL import Image,ImageTk
import time
import multiprocessing as mp
import threading
#https://stackoverflow.com/questions/47316266/can-i-display-image-in-full-screen-mode-with-pil

class Display:
    def __init__(self):
        root = tkinter.Tk()
        self.root = root
        self.screen_width = self.root.winfo_screenwidth()/2
        self.screen_height = self.root.winfo_screenheight()/2
        self.root.geometry("%dx%d+0+0"%(self.screen_width,self.screen_height))
        self.root.focus_set()
        self.root.bind("<Escape>",self.quitProg)
        self.root.bind("<<SIG>>",self.handlesignal)
        self.canvas = tkinter.Canvas(self.root,width=self.screen_width,height=self.screen_height)
        self.canvas.pack()
        self.canvas.configure(background="black")
        self.currenttag = 0

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

    def update(self):
        print("Update is clicked")
        pilimage = Image.open("bubu.jpg")
        imgWidth,imgHeight = pilimage.size
        if(imgWidth>self.screen_width or imgHeight>self.screen_height):
            ration = min(self.screen_width/imgWidth,self.screen_height/imgHeight)         
            imgWidth = int(imgWidth*ration)                                  
            imgHeight = int(imtHeight*ration)                                
            pilimage = pilimage.resize((imgWidth,imgHeight),Image.ANTIALIAS) 
        self.updateimage = ImageTk.PhotoImage(pilimage)
        self.canvas.itemconfig(self.currenttag,image=self.updateimage)


    def run(self):
        self.root.overrideredirect(0)
        self.root.mainloop()

    def quitProg(self,event):
        print(event.widget)
        event.widget.destroy()

    def simulatesignal(self):
        time.sleep(5)
        self.root.event_generate('<<SIG>>',when='tail')
    
    def handlesignal(self,event):
        print("handle signal")
        self.update()
if __name__=="__main__":
    pilImage = Image.open("lion.png")
    display = Display()
    display.show(pilImage)
    th = threading.Thread(target=display.simulatesignal)
    th.start()
    display.run()

