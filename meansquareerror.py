"""
It calculates the difference between two images.This is just thee coding of a mathematical formula.
This function can called by passing two image object as parameters and then decimal value will be returned.
"""
from PIL import ImageChops,Image
import math, operator

def rootmeansquare(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms



