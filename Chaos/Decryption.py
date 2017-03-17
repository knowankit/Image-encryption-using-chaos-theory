## Importing all the required modules for decryption function to work
from PIL import Image
from Yn import *
from Check import *
from Encryption import *


## This function uses all the functions of previous modules, takes an encrypted image file and a 80 bit ascii key provided by the user
## and returns an decrypted image object
def decrypt(encrypted_image_file , secret_key_80bits):
    encrypted_image = Image.open(encrypted_image_file,"r").convert("RGBA")

    #global count

    encrypted_pixels = encrypted_image.load()
    width, height = encrypted_image.size

    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size,(254,254,254,0))
    decrypted_pixels = decrypted_image.load()

    binary_keys = to_8bit_keys(secret_key_80bits)

    hex_keys = to_hex_keys(secret_key_80bits)

    x_knot = x0(x01(binary_keys), x02(hex_keys))

    f24 = xn(x_knot)

    # p24 = pk(f24)


    # y_knot = y0(y01(binary_keys), y02(binary_keys, p24))

    # yn_values_after_iterating_k10_times = yn(y_knot, binary_list_to_int(binary_keys[9]))



    for y in range(0, height):
        for x in range(0, width):

            if x < 16 and y == 0:
                f24 = xn(f24[23])

                p24 = pk(f24)

                y_knot = y0(y01(binary_keys), y02(binary_keys, p24))

                yn_values_after_iterating_k10_times = yn(y_knot, binary_list_to_int(binary_keys[9]))

                r, g, b = check_operations_to_be_performed(yn_values_after_iterating_k10_times, encrypted_pixels[x, y][0],
                                                           encrypted_pixels[x, y][1], encrypted_pixels[x, y][2], binary_keys,
                                                           decryption=True)
                decrypted_pixels[x, y] = (r, g, b)





            else:
                if x % 16 == 0:
                    binary_keys = modifying_session_keys(binary_keys)

                    # count+=1

                f24 = xn(f24[23])

                p24 = pk(f24)

                y_knot = y0(y01(binary_keys), y02(binary_keys, p24))

                yn_values_after_iterating_k10_times = yn(y_knot, binary_list_to_int(binary_keys[9]))

                r, g, b = check_operations_to_be_performed(yn_values_after_iterating_k10_times, encrypted_pixels[x, y][0],
                                                           encrypted_pixels[x, y][1], encrypted_pixels[x, y][2], binary_keys,
                                                           decryption=True)
                decrypted_pixels[x, y] = (r, g, b)


    return decrypted_image





## Test code
######################################################################
## Here we test the decryption modules by creating an image object and loading the image to be decrypted
## Then we use the decrypt() function to decrypt the image using the key
## The decrypted image object is then saved at the output directory specified

# im = encrypt("encrypted/tiger_ankit12345.png","ankit12345")
#
# im.show()
# im.save("decrypted/decrypted.jpg")

