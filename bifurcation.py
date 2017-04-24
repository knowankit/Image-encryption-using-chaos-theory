"""
This file is used to generate a bifurcation diagram. This diagram is used to detect whether the generated nummbers
are chaotic in nature or not
"""
import math
from PIL import Image



def showbifurcation():
    # Height and width of the image
    imgx = 1000
    imgy = 500

    # fill the image with black color
    image = Image.new("RGB", (imgx, imgy), color=(255, 255, 255))

    xa = 2.9
    xb = 4.0
    maxit = 1000
    r=3.9999
    for point_of_x in range(imgx):

        for point_of_y in range(maxit):
            x = r * x * (1 - x)
            if point_of_y > maxit / 2:
                image.putpixel((point_of_x, int(x * imgy)), (0, 0, 255))
            if 3.6 < r < 4:
                image.putpixel((point_of_x, int(x * imgy)), (1, 154, 210))

    image.save("bifurcation.png")
    image.show()

