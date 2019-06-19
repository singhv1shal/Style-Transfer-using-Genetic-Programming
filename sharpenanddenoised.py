# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:45:12 2019

@author: Lenovo
"""

from scipy import ndimage
import numpy
import functools
import operator
from matplotlib import pyplot as plt
from scipy import ndimage
'''
This function sharpens the image with hyperparameter alpha =3
'''

def sharpen3(img):
    blurred_f = ndimage.gaussian_filter(img, 3)
    filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
    alpha = 3
    sharpened = img + alpha * (blurred_f - filter_blurred_f)
    
    fimg = numpy.reshape(a=sharpened,newshape=(functools.reduce(operator.mul, sharpened.shape)))
    return fimg

def sharpen10(img):
    blurred_f = ndimage.gaussian_filter(img, 3)
    filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
    alpha = 10
    sharpened = img + alpha * (blurred_f - filter_blurred_f)
    
    fimg = numpy.reshape(a=sharpened,newshape=(functools.reduce(operator.mul, sharpened.shape)))
    return fimg

def denoised(img): 
    med_denoised = ndimage.median_filter(img, 3)
    
    fimg = numpy.reshape(a=med_denoised,newshape=(functools.reduce(operator.mul, med_denoised.shape)))
    return fimg