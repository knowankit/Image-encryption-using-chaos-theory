"""
This module two libraries pillow as PIL and math lib.This module is based on a mathematical formula called
 pearson's correlation coefficient.It calculates the relation between two adjacent pixel values.Each component of the
 formula is divided into four parts which are co1,co2,co3,co4.
 
 It has a module named corr_of_rgb().It calculates correlation of all r,g,b and returns the average correlation 
 of the image.This module can be called bu passing te location of the whose correlation coefficient is to be calculated.
 for example-: corr_of_rgb(loc)
"""

from PIL import Image
from math import sqrt

value_of_x=0
value_of_y=0

#color_index_of_rgb 0-red,1-green,2-blue
def co1(color_index_of_rgb,height,width,pixels):
    value=0
    for pixel_coordinate_of_y in range(0, height):
        for pixel_coordinate_of_x in range(0, width):
            if pixel_coordinate_of_x+1==width:
                break
            value=pixels[pixel_coordinate_of_x,pixel_coordinate_of_y][color_index_of_rgb]*pixels[pixel_coordinate_of_x+1,pixel_coordinate_of_y][color_index_of_rgb]+value


    return value*height*width

def co2(color_index_of_rgb,height,width,pixels):
   global value_of_y
   global value_of_x
   for pixel_coordinate_of_y in range(0, height):
        for pixel_coordinate_of_x in range(0, width):
            if pixel_coordinate_of_x+1==width:
                break
            value_of_x=pixels[pixel_coordinate_of_x,pixel_coordinate_of_y][color_index_of_rgb]+value_of_x
            value_of_y=pixels[pixel_coordinate_of_x+1,pixel_coordinate_of_y][color_index_of_rgb]+value_of_y

   return value_of_x*value_of_y


def co3(color_index_of_rgb,height,width,pixels):
    value=0
    for pixel_coordinate_of_y in range(0, height):
        for pixel_coordinate_of_x in range(0, width):
            value=(pixels[pixel_coordinate_of_x,pixel_coordinate_of_y][color_index_of_rgb])**2 +value

    xy=(value*height*width)-(value_of_x**2)
    return  xy

def co4(color_index_of_rgb,height,width,pixels):
    value=0
    for pixel_coordinate_of_y in range(0, height):
        for pixel_coordinate_of_x in range(0, width):
            if pixel_coordinate_of_x+1==width:
                break
            value=(pixels[pixel_coordinate_of_x+1,pixel_coordinate_of_y][color_index_of_rgb]**2)+value

    xy=(value*height*width)-(value_of_y**2)
    return xy

def corr_of_rgb(loc):
    global value_of_y
    global value_of_x
    photo = Image.open(loc)
    # cryptotiger.bmp
    pixels = photo.load()
    width, height = photo.size
    value_of_y = 0
    value_of_x = 0
    r=((co1(0,height,width,pixels)-co2(0,height,width,pixels)) / sqrt(co3(0,height,width,pixels)*co4(0,height,width,pixels)))
    value_of_y=0
    value_of_x=0
    g=((co1(1,height,width,pixels) - co2(1,height,width,pixels)) / sqrt(co3(1,height,width,pixels) * co4(1,height,width,pixels)))
    value_of_x=0
    value_of_y=0
    b=((co1(2,height,width,pixels) - co2(2,height,width,pixels)) / sqrt(co3(2,height,width,pixels) * co4(2,height,width,pixels)))

    return ((r+g+b)/3)
#cr=(co1()-co2()) / sqrt(co3()*co4())

#print(cr)

#corr_of_rgb("abc.png")
