from PIL import Image
from pylab import *

# read image to array

# def histogram(loc,dloc):

# im = array(Image.open("abc.png").convert('RGB'))
#
# im2 = 255 - im  # invert image green
# im3 = (100.0 / 255) * im + 100  # clamp to interval 100...200 red
# im4 = 255.0 * (im / 255.0) ** 2  # squared blue
# axis('equal')
# axis('off')
# figure()
# # hist(im.flatten(), 128)
# # hist(im2.flatten(), 128)
# # hist(im3.flatten(), 128)
# hist(im2.flatten(), 128)
# # hist(im3.flatten(), 128)
# # hist(im4.flatten(), 128)
# show()

def redhistogram(loc):
    im = array(Image.open(loc).convert('RGB')) #Opening the image
    im = (100.0 / 255) * im + 100  # clamp to interval 100...200 red
    #Fecthing red pixels
    axis('equal')
    axis('off')
    figure()
    hist(im.flatten(), 128) #Designing the histogram

    show()


def greenhistogram(loc):
    im = array(Image.open(loc).convert('RGB')) #Opening the image
    im = 255 - im  # invert image green #Fecthing green pixels
    axis('equal')
    axis('off')
    figure()
    hist(im.flatten(), 128)#Designing the histogram
    show()


def bluehistogram(loc):
    im = array(Image.open(loc).convert('RGB')) #Opening the image
    im = 255.0 * (im / 255.0) ** 2  # squared blue #Fecthing blue pixels
    axis('equal')
    axis('off')
    figure()
    hist(im.flatten(), 128)#Designing the histogram
    show()


# im = array(Image.open('abc.png').convert('RGB'))
#
# im2 = 255 - im # invert image green
#
# im3 = (100.0/255) * im + 100 # clamp to interval 100...200 red
#
# im4 = 255.0 * (im/255.0)**2 # squared blue
# # create a new figure
# figure()
# # don't use colors
# #gray()
# # show contours with origin upper left corner
# #contour(im2, origin='image')
#
# axis('equal')
# axis('off')
# figure()
# hist(im2.flatten(),128)
# # hist(im3.flatten(),128)
# # hist(im.flatten(),128)
# # hist(im4.flatten(),128)
# # #
# show()