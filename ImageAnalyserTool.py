"""
This is a standalone application to analyze the image .It uses a tkinter library of python to make gui for windows.
It consist of allanalysis(),rmse(),uac() , npcr() , askopenfile(), doegraphplot().All the modules defined in this file 
is for analyzing image

"""
import os
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image
from coplot import coplot_horizontal
from correlationcofficient import corr_of_rgb
from histogram import rgbhistogram,rgbhistogram2
from npcr import npcrv
from uaci import rootmeansquareerror,uaci
root = Tk()
root.geometry("750x600")
root.configure(background="#019ad2")
root.title("Image Analysis tool")

curr=os.getcwd()

"""
    This module does all the analysis of the first part
"""
def allanalysis():
    global output_loc
    corrvalue = corr_of_rgb(loc1.get())
    cv = Label(root, text=corrvalue)
    cv.grid(row=3, column=1)
    coplot_horizontal(loc1.get(),output_loc)
    coplot=Image.open(output_loc+"/coplot_horizontal.png")
    rgbhistogram(loc1.get(),output_loc)
    rgbimage=Image.open(output_loc+"/rgbhisto.png")
    rgbimage.show()
    coplot.show()

"""
    This module does the analysis of second part
"""
def allanalysis2():
    global output_loc
    corrvalue = corr_of_rgb(loc2.get())
    cv = Label(root, text=corrvalue)
    cv.grid(row=3, column=3)
    coplot_horizontal(loc2.get(),output_loc)
    coplot=Image.open(output_loc+"/coplot_horizontal2.png")
    rgbhistogram2(loc2.get(),output_loc)
    rgbimage=Image.open(output_loc+"/rgbhisto2.png")
    rgbimage.show()
    coplot.show()

"""
    root mean square defined in meansquareerror.py
"""
def rmse():
    value=rootmeansquareerror(loc1.get(),loc2.get())
    vrms=Label(root,text=value)
    vrms.grid(row=8,column=1)


"""
    Number of Pixel Changed Rate is defined in npcr.py
"""
def npcr():
    value=npcrv(loc1.get(),loc2.get())
    npvalue=Label(root,text=value)
    npvalue.grid(row=7,column=1)

def uac():
    value=uaci(loc1.get(),loc2.get())
    ua=Label(root,text=value)
    ua.grid(row=9,column=1)

def askopenfile1():
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg'),("Image File",'.png'),("Image File",'.tiff')]) #allowed image formats are .jpg and .png

    loc1.delete(0,'end') #Delete the address value present in the address bar
    im = Image.open(path) #Opening image with the previous fetched path
    loc1.insert(END, path) # inserting the file location in the address bar
    print(path)
    im = im.resize((200, 200), Image.ANTIALIAS) #resizing the fetched image
    tkimage = ImageTk.PhotoImage(im) #defining the format of the image
   # print(getsize(path))
    myvar = Label(root, image=tkimage) #Displaying the image on the window with the help of label object
    myvar.image = tkimage #assigning the image value
    myvar.grid(row=2, column=0,pady=5,padx=20) #Placing the image using grid layout


def askopenfile2():
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg'),("Image File",'.png'),("Image File",'.tiff')]) #allowed image formats are .jpg and .png
    loc2.delete(0,'end') #Delete the address value present in the address bar
    im = Image.open(path) #Opening image with the previous fetched path
    loc2.insert(END, path) # inserting the file location in the address bar
    im = im.resize((200, 200), Image.ANTIALIAS) #resizing the fetched image
    tkimage = ImageTk.PhotoImage(im) #defining the format of the image
   # print(getsize(path))
    myvar = Label(root, image=tkimage) #Displaying the image on the window with the help of label object
    myvar.image = tkimage #assigning the image value
    myvar.grid(row=2, column=2,pady=5) #Placing the image using grid layout

def doegraphplot():

    loc2=output_loc+"/output.png"
    coplot_horizontal(loc2)

def doographplot():
    loc = loc1.get()
    coplot_horizontal(loc)

def askdirectory():
    global output_loc
    output_loc = filedialog.askdirectory()
    outputl=Label(root,text=output_loc)
    outputl.grid(row=1,column=1)

def bifurcation():
    im=Image.open("bifurcation.png")
    im.show()

"""
    Various button object is created with entry box object .These object are packed in the GUI using
    grid layout.
"""
browse1=Button(root,text="Browse Image",command=askopenfile1,width=15,height=2,bg="#657cc3")
browse2=Button(root,text="Browse Image",command=askopenfile2,width=15,height=2,bg="#657cc3")
loc1=Entry(root,width=28)
loc2=Entry(root,width=28)


browse1.grid(row=0,column=0,padx=10,pady=20)
loc1.grid(row=0,column=1,padx=10,pady=20)
browse2.grid(row=0,column=2,padx=10,pady=20)
loc2.grid(row=0,column=3,padx=10,pady=20)

chooseloc=Button(root,text="Output location",command=askdirectory,width=15,height=2,bg="#657cc3")
chooseloc.grid(row=1,column=0,pady=10)

corrcoff1=Label(root,text="Correlation-Coefficient")
corrcoff2=Label(root,text="Correlation-Coefficient")
corrcoff1.grid(row=3,column=0)
corrcoff2.grid(row=3,column=2)

histo1=Label(root,text="Histogram-Analysis")
histo2=Label(root,text="Histogram-Analysis")
histo1.grid(row=4,column=0,pady=20)
histo2.grid(row=4,column=2,pady=20)

coplot1=Label(root,text="Correlation Plot")
coplot2=Label(root,text="Correlation Plot")
coplot1.grid(row=5,column=0,pady=10)
coplot2.grid(row=5,column=2,pady=10)
analyze1=Button(root,text="Analyse",bg="#f2b91f",command=allanalysis)
analyze2=Button(root,text="Analyse",bg="#f2b91f",command=allanalysis2)
analyze1.grid(row=10,column=0,pady=20)
analyze2.grid(row=10,column=2,pady=20)

npcr=Button(root,text="NPCR Test",bg="#f2b91f",command=npcr)
npcr.grid(row=7,column=2,pady=10)

rms=Button(root,text="RMSE Test",bg="#f2b91f",command=rmse)
rms.grid(row=8,column=2)

uac=Button(root,text="UACI Test",bg="#f2b91f",command=uac)
uac.grid(row=9,column=2,pady=10)
root.mainloop()