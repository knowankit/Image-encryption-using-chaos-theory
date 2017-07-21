## Image Encryption using Chaos theory

This project deals with the encryption and decryption of the image using two logistic equation which is iterated in a loop at a certain number of times to genearte distinct value.The generated distinct value is used in key generatioan where it is further used in operations like XORing with the pixels.

A separate Image analyzer tool is provided to do avarious kinds of analysis on the image.
Analysis like NPCR(Number Of Pixels Changed Rate),UACI(Unified Average Changed Intensity),Correlation coefficient ,RMSE(Root Mean Square Error) ,Histogram are integrated in this
software .

### Prerequisites
* If you want to modify the code then you need to install any IDE for python like PyCharm (optional)
* This codes works on both python 2.7 and 3.2 version

### Installing
Copy this project folder into your project workspace. Open the GUI.py file in the IDE
You will get some errors as many libraries will be unavailable. Libraries required to
run this code are matplotlib, pillow, numbpy, histogram, tkinter

### Built With
* ###### Pycharm IDE
* ###### matplotlib
* ###### numpy
* ###### Tkinter library
* ###### pillow


### Author
* ###### Ankit Kumar
* ###### Aditya Prakash
* ###### [Ghulam Khan](http://github.com/waynetech)

### License
This project is free to use and modify


### Notes:
* Allowed image formats are .jpeg and .png. User can select any of the mentioned image format.

* User can use their own secret key to encrypt and decrypt the image. 

* Encryption and decryption time of the image depends on the size and resolution of the image.

* This project also analyzes the encrypted and original images.

### Modules of this project-

1. Chaos Module
2. Image analyzer tool
3. Web application
4. Desktop application

