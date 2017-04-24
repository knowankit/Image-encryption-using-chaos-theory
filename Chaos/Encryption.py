"""
    PIL (Python Imaging Library) module is used to perform image manipulations
    Importing all the required modules for encryption function to work.This file has a major module defined as 
    encrypt module.This module is used to encrypt the image with the secret key.Secret key can be fetched be from the 
    input field of GUI.Encrypt module has two parameters image file and secret key.Image file is the location
    of the file.Image location is fetched in the module and converted to rgb pixel values.
    
    you call the decrypt function by calling encrypt(location of image as c://folder_name/file_name).This module returns
    the encrypted image so we need to store this into a variable to save the image file


"""
from PIL import Image
from Chaos.Yn import *
from Chaos.Check import *
import time
#from numba import jit

## Importing all the previous modules



## This function uses all the functions of previous modules, takes an image file and a 80 bit ascii key provided by the user
## and returns an encrypted image object

def encrypt(image_file , secret_key_80bits):
    start_time = time.time()  #start time of this module
    image = Image.open(image_file,"r").convert("RGB") # converting of the image into rgb values

    pixel_count = 0
    # loading of the pixels as rgb(0-255,0-255,0-255)
    pixels = image.load()
    width, height = image.size
    #print(image.size)


    # conversion of secret key(ASCII of alpha numeric values) to 8 bit binary values)
    binary_keys = to_8bit_keys(secret_key_80bits)

    # conversion of secret key(ASCII of alpha numeric values) to hex values
    hex_keys = to_hex_keys(secret_key_80bits)

    x_knot = x0(x01(binary_keys), x02(hex_keys))

    # generating 24 uniques numbers from 0-1
    f24 = xn(x_knot, 24)

    # converting the generated unique number to real number using a formula mentioned in the research paper
    p24 = pk(f24)

    y_knot = y0(y01(binary_keys), y02(binary_keys, p24))

    k10 = binary_list_to_int(binary_keys[9])


    for coordinate_of_y in range(0, height):
        for coordinate_of_x in range(0, width):
            # modifying session after 16 pixels
                if pixel_count%16 == 0:
                    binary_keys = modifying_session_keys(binary_keys)
                    f24 = xn(f24[23])

                    p24 = pk(f24)

                    y_knot = y0(y01(binary_keys), y02(binary_keys, p24))


                yn_values = yn(y_knot, 20)

                for value in yn_values:
                    # storing the converted r,g,b values to the same index
                    r,g,b = check_operations_to_be_performed(value,pixels[coordinate_of_x,coordinate_of_y][0],pixels[coordinate_of_x,coordinate_of_y][1],pixels[coordinate_of_x,coordinate_of_y][2],binary_keys,decryption=False)

                    pixels[coordinate_of_x,coordinate_of_y] = (r,g,b)

                y_knot = yn_values[len(yn_values) - 1]
                pixel_count += 1




    print(count)
    print("--- %s seconds ---" % (time.time() - start_time))
    return image



##Test code
######################################################################
## Here we test the encryption modules by creating an image object and loading the image to be encrypted
## Then we use the encrypt() function to encrypt the image using the key
## The encrypted image object is then saved at the output directory specified

# im = encrypt("images/tiger.jpg","ankit12345")
#
# im.show()
# im.save("encrypted/encrypted.jpg")
#
