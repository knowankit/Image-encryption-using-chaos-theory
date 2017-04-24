"""
this module consists of two module co-plot_horizontal() and co-plot_vertical().These module draws the graph of pearson's
correlation coefficient.Correlation coefficient is the relation between two variable.Here two variables refers to the
two adjacent pixel of a image.Adjacent pixel could be vertically and horizontally

Two libraries have been used which are pillow as PIL and matplotlib to put relation values to a graph

co-plot module can be used by just passing the location of the image and location of the output image.
"""

import matplotlib.pyplot as plt

from PIL import Image

def coplot_horizontal(loc,output):
    image = Image.open(loc)

    #loading of pixels as rgb
    pixels=image.load()
    list_of_pixels_of_x=[]
    list_of_pixels_of_y=[]

    width,height=image.size

    #running for loop to traverse all the pixel values of the image
    for pixel_coordinate_of_y in range(0,50):
        for pixel_coordinate_of_x in range(0,50):

            #adding pixel value to a list
            list_of_pixels_of_x.append(pixels[pixel_coordinate_of_x,pixel_coordinate_of_y][0])
            if pixel_coordinate_of_x+1 == width:
                list_of_pixels_of_x.pop()
                break
            else:
                # adding pixel value to a list
                list_of_pixels_of_y.append(pixels[pixel_coordinate_of_x+1,pixel_coordinate_of_y][0])

    #plotting of values to a graph
    plt.scatter(list_of_pixels_of_x,list_of_pixels_of_y,  label='Pixel',color='k',s=2,edgecolors='r')
    plt.xlabel('Pixel value on location(x,y)')
    plt.ylabel('Pixel value on location(x+1,y)')
    plt.title("correlation coefficient graph")
    plt.legend()
    plt.savefig(output+"/coplot_horizontal.png")

#plt.savefig("fog.png")


def coplot_vertical(loc):
    image = Image.open(loc)
    pixels = image.load()
    list_of_pixels_of_x = []
    list_of_pixels_of_y = []

    width, height = image.size

    #running for loop to traverse all the pixel values of the image
    for pixel_coordinate_of_y in range(0, 50):
        for pixel_coordinate_of_x in range(0, 50):

            # adding pixel value to a list
            list_of_pixels_of_x.append(pixels[pixel_coordinate_of_y,pixel_coordinate_of_x][0])
            if pixel_coordinate_of_y + 1 == height:
                list_of_pixels_of_y.pop()
                break
            else:

                # adding pixel value to a list
                list_of_pixels_of_y.append(pixels[pixel_coordinate_of_y , pixel_coordinate_of_x+1][0])

    #plotting of values to a graph
    plt.scatter(list_of_pixels_of_x, list_of_pixels_of_y, label='Pixel', color='k', s=2, edgecolors='r')
    plt.xlabel('Pixel value on location(x,y)')
    plt.ylabel('Pixel value on location(x+1,y)')
    plt.title("correlation coefficient graph")
    plt.legend()
    plt.show()