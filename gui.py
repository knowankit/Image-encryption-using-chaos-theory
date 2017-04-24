"""
This is a desktop based GUI application. Libraries like tkinter,PIL have been used to make it.A user can encrypt or decrypt the image file
from this gui.It have to modules encrypt and decrypt.This gui used grid layout which means size will remains same in every window.
"""
from tkinter import *
#Imported from chaos package
from Chaos.Encryption import encrypt
from Chaos.Decryption import decrypt

from tkinter import filedialog #GUI library
from PIL import ImageTk, Image #image manipulation library

from os.path import getsize

import os

root = Tk() #Initialising the window frame
root.geometry("600x550") #Size of the window
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
"""
Encrypt function has two parameters which are image object and secret key of 80 bits.Doencrypt is used to call the encrypt function.
"""
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


"""
Decrypt function has two parameters which are image object and secret key of 80 bits.Dodecrypt is used to call the decrypt function.
"""
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
dloc="dabc.png"
browse_input_file=Button(root,text="Select Image",command=askopenfile,width=15,height=2,bg="#657cc3") #Browse Button
input_file_entry=Entry(root,width=28) #Address Label

password=Label(root,text="Enter Key",width=18,height=1,bg="#657cc3") #Password Label
password_entry=Entry(root,width=20) #Password entry box

encryptb=Button(root, text="Encrypt Image", width=18, height=2,command=doencrypt,bg="#37b448" ) #Placing the object using grid layout
decryptb=Button(root,text="Decrypt Image",width=18,height=2,command=dodecrypt,bg="#37b448") #Placing the object using grid layout


encryptb.grid(row=4,columnspan=5,pady=10)#Placing the object using grid layout
decryptb.grid(row=5,columnspan=5,pady=15)#Placing the object using grid layout
password.grid(row=2,columnspan=5,pady=10)#Placing the object using grid layout
password_entry.grid(row=3,columnspan=5)#Placing the object using grid layout
browse_input_file.grid(row=0,padx=80,pady=50)#Placing the object using grid layout
input_file_entry.grid(row=0,column=1,padx=50)#Placing the object using grid layout

root.mainloop() #Closing the Frame
