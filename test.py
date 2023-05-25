import tkinter
from PIL import Image,ImageTk
#https://stackoverflow.com/questions/47316266/can-i-display-image-in-full-screen-mode-with-pil
def quitProg(event):
    print("hey",event.widget)
    event.widget.destroy()

def showPIL(pilImage):
    root = tkinter.Tk()
    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    root.focus_set()
    root.bind("<Escape>", quitProg)
    root.update_idletasks()
    root.overrideredirect(1)
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background="black")
    imgWidth,imgHeight = pilImage.size
    if(imgWidth>w or imgHeight>h):
        ratio = min(w/imgWidth,h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight),Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()

if __name__=="__main__":
    pilImage = Image.open("lion.png")
    showPIL(pilImage)
