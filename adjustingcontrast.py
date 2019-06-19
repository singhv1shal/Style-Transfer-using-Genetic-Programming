# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:49:03 2019

@author: Lenovo
"""

import cv2
import numpy
import functools
import operator
from matplotlib import pyplot as plt

'''
This function adjusts the contrast through Histogram Equalization
'''

def adjustCONTRAST100(img):
    
    # Adaptive Histogram Equalization)
    c = cv2.createCLAHE(clipLimit=100., tileGridSize=(8,8))
    
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    
    l2 = c.apply(l)  # apply CLAHE to the L-channel
    
    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    #plt.imshow(img2)
    #plt.show()
    fimg = numpy.reshape(a=img2,newshape=(functools.reduce(operator.mul, img2.shape)))
    return fimg

def adjustCONTRAST3(img):
    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
    
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    
    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    #plt.imshow(img2)
    #plt.show()
    fimg = numpy.reshape(a=img2,newshape=(functools.reduce(operator.mul, img2.shape)))
    return fimg