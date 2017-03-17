from tkinter import *
from Chaos.Encryption import encrypt
from Chaos.Decryption import decrypt
from histogram import redhistogram,bluehistogram,greenhistogram
from tkinter import filedialog
from PIL import ImageTk, Image

from os.path import getsize

import os

root = Tk() #Initialising the window frame
root.geometry("600x700") #Size of the window
root.configure(background="#26292c") #background colorr of the window
root.title("Chaos Based Image Encryption")
#title on the title bar of the window
curr=os.getcwd()


#Function to choose a file from the system directory
def askopenfile():
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg'),("Image File",'.png')]) #allowed image formats are .jpg and .png
    input_file_entry.delete(0,'end') #Delete the address value present in the address bar
    im = Image.open(path) #Opening image with the previous fetched path
    input_file_entry.insert(END, path) # inserting the file location in the address bar
    im = im.resize((200, 200), Image.ANTIALIAS) #resizing the fetched image
    tkimage = ImageTk.PhotoImage(im) #defining the format of the image
    print(getsize(path))
    myvar = Label(root, image=tkimage) #Displaying the image on the window with the help of label object

    myvar.image = tkimage #assigning the image value

    myvar.grid(row=1, column=0) #Placing the image using grid layout

def doencrypt():
    loc=input_file_entry.get() #Fecthing the location of the file to be encrypted
    key=password_entry.get()  #Fetching the key value
    encrypted_image=encrypt(loc,key) #Encrypting the image by calling encrypt method which returns the encrypted image
    encrypted_image.save("abc" + ".png") #Saving the encrypted image  as .png
    im = Image.open("abc.png") #Opening the encryppted  image
    im = im.resize((200, 200), Image.ANTIALIAS)  #Resizing the encrypted image
    tkimage = ImageTk.PhotoImage(im) #Defining the image value
    myvar = Label(root, image=tkimage) #Displaying the with the help of label object
    myvar.image = tkimage # Assigning the image attribute
    myvar.grid(row=1, column=1) #Placing the image using grid layout

    #encrypted_image.show()
   # encrypted_image = encrypted_image.resize((200, 200), Image.ANTIALIAS)
   #  myvar2 = Label(root, image=encrypted_image)
   #  myvar2.image = encrypted_image
   #  myvar2.grid(row=1,column=1)

def orhist():
    loc=input_file_entry.get() #Fetching image location
    redhistogram(loc)   #calling function red pixel distribution analysis
def obhist():
    loc=input_file_entry.get() #Fetching image location
    bluehistogram(loc)  #calling function blue pixel distribution analysis
def oghist():
    loc=input_file_entry.get() #Fetching image location
    greenhistogram(loc) #calling function green pixel distribution analysis

def erhist():
    loc="abc.png" #Encrypted Image
    redhistogram(loc)    #calling function red pixel distribution analysis
def ebhist():
    loc="abc.png" #Encrypted Image
    bluehistogram(loc)   #calling function blue pixel distribution analysis
def eghist():
    loc="abc.png" #Encrypted Image
    greenhistogram(loc)  #calling function green pixel distribution analysis

def dodecrypt():
    loc="abc.png" #Location of decrypted iamge
    decrypted_image=decrypt(loc,password_entry.get()) #Calling decrypt function tod ecrypt the image by passing encryptd image with the key
    decrypted_image.save("dabc"+".png") #saving decrypted image as .png
    im=Image.open("dabc.png") #Opening decrypted image
    im = im.resize((200, 200), Image.ANTIALIAS) #Resizing decrypted image
    tkimage = ImageTk.PhotoImage(im) #Loading image as an Object
    myvar = Label(root, image=tkimage) #Displaying image with the help of Label Object
    myvar.image = tkimage #assigning image value
    myvar.grid(row=1, column=1) #Placing image using grid layout in the window

loc="abc.png"
dloc="abc.png"
browse_input_file=Button(root,text="Select Image",command=askopenfile,width=15,height=2,bg="#657cc3") #Browse Button
input_file_entry=Entry(root,width=28) #Address Label

password=Label(root,text="Enter Key",width=18,height=1,bg="#657cc3") #Password Label
password_entry=Entry(root,width=20) #Password entry box
orb=Button(root,text="R",bg="#cf1b27",command=orhist) #Button for red histogram analysis of original image
ogb=Button(root,text="G",bg="#2fa828",command=obhist)  #Button for green histogram analysis of original image
obb=Button(root,text="B",bg="#006598",command=oghist)#Button for blue histogram analysis of original image

erb=Button(root,text="R",bg="#cf1b27",command=erhist)#Button for red histogram analysis after encryption
egb=Button(root,text="G",bg="#2fa828",command=ebhist)#Button for green histogram analysis after encryption
ebb=Button(root,text="B",bg="#006598",command=eghist)#Button for blue histogram analysis after encryption

encryptb=Button(root, text="Encrypt Image", width=18, height=2,command=doencrypt,bg="#37b448" ) #Placing the object using grid layout
decryptb=Button(root,text="Decrypt Image",width=18,height=2,command=dodecrypt,bg="#37b448") #Placing the object using grid layout
#analyse=Button(root,text="Histogram",width=18,height=2,command=histogramanalysis,bg="#019ad2")
#analyse.grid(row=6,columnspan=5)
#analyse.pack(side=BOTTOM)
#photolabel.grid(row=2,colomnspan=1)
orb.grid(row=6)#Placing the object using grid layout
ogb.grid(row=7)#Placing the object using grid layout
obb.grid(row=8)#Placing the object using grid layout

erb.grid(row=6,column=1)#Placing the object using grid layout
egb.grid(row=7,column=1)#Placing the object using grid layout
ebb.grid(row=8,column=1)#Placing the object using grid layout


encryptb.grid(row=4,columnspan=5,pady=10)#Placing the object using grid layout
decryptb.grid(row=5,columnspan=5,pady=15)#Placing the object using grid layout
password.grid(row=2,columnspan=5,pady=10)#Placing the object using grid layout
password_entry.grid(row=3,columnspan=5)#Placing the object using grid layout
browse_input_file.grid(row=0,padx=80,pady=50)#Placing the object using grid layout
input_file_entry.grid(row=0,column=1,padx=50)#Placing the object using grid layout

root.mainloop() #Closing the Frame
