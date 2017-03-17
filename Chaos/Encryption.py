## PIL (Python Imaging Library) module is used to perform image manipulations
from PIL import Image

## Importing all the previous modules
from Yn import *
from Check import *


## This function uses all the functions of previous modules, takes an image file and a 80 bit ascii key provided by the user
## and returns an encrypted image object
def encrypt(image_file , secret_key_80bits):
    image = Image.open(image_file,"r").convert("RGBA")
    global count

    pixels = image.load()
    width, height = image.size


    encrypted_image = Image.new(image.mode, image.size,(254,254,254,0))
    encrypted_pixels = encrypted_image.load()


    binary_keys = to_8bit_keys(secret_key_80bits)

    hex_keys = to_hex_keys(secret_key_80bits)

    x_knot = x0(x01(binary_keys), x02(hex_keys))

    f24 = xn(x_knot)


    for y in range(0, height):
        for x in range(0, width):

            if x<16 and y==0:
                f24 = xn(f24[23])

                p24 = pk(f24)

                y_knot = y0(y01(binary_keys), y02(binary_keys, p24))

                yn_values_after_iterating_k10_times = yn(y_knot, binary_list_to_int(binary_keys[9]))


                r,g,b = check_operations_to_be_performed(yn_values_after_iterating_k10_times, pixels[x, y][0],
                                                         pixels[x, y][1], pixels[x, y][2], binary_keys,decryption=False)
                encrypted_pixels[x, y] = (r,g,b)




            else:
                if x % 16 == 0:
                    binary_keys = modifying_session_keys(binary_keys)

                f24 = xn(f24[23])

                p24 = pk(f24)

                y_knot = y0(y01(binary_keys), y02(binary_keys, p24))

                yn_values_after_iterating_k10_times = yn(y_knot, binary_list_to_int(binary_keys[9]))

                r, g, b = check_operations_to_be_performed(yn_values_after_iterating_k10_times, pixels[x, y][0],
                                                           pixels[x, y][1], pixels[x, y][2], binary_keys,
                                                           decryption=False)
                encrypted_pixels[x, y] = (r, g, b)


    return encrypted_image


##Test code
######################################################################
## Here we test the encryption modules by creating an image object and loading the image to be encrypted
## Then we use the encrypt() function to encrypt the image using the key
## The encrypted image object is then saved at the output directory specified

# im = encrypt("images/tiger.jpg","ankit12345")
#
# im.show()
# im.save("encrypted/encrypted.jpg")

