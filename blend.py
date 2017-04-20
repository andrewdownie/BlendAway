import os
import sys
import numpy as np
import cv2
import statistics
import datetime

def getMedian(arr, x, y):
    values = []
    for a in arr:
        values.append(a[x][y])
    return statistics.median_grouped(values)

def getMean(arr, x, y):
    values = []
    for a in arr:
        values.append(a[x][y])
    return statistics.mean(values)

def getMode(arr, x, y):
    values = []
    for a in arr:
        values.append(a[x][y])
    try:
        mode =  statistics.mode(values)
        return mode
    except statistics.StatisticsError: # all values are the same
        return getMedian(arr,x,y)

method = sys.argv[1]

imgs = ["1.png","2.png", "3.png", "4.png", "5.png"] # image
#direct = os.getcwd() + "/images/" # where to get test images
#saved = os.getcwd() + "/saved/" # where to get test images
direct = "/var/www/html/" # where to get test images
saved = "/var/www/html/" # where to get test images
i=0
images = []

for img in imgs:
    image = cv2.imread(direct + img) # open template image
    images.append(image)
    (height, width) = image.shape[:2] # get dimensions



red = []
green = []
blue = []

for image in images:

    redMatrix = [[0 for x in range(width)] for y in range(height)]
    greenMatrix = [[0 for x in range(width)] for y in range(height)]
    blueMatrix = [[0 for x in range(width)] for y in range(height)]

    for x in range(height):
        for y in range(width):
            redMatrix[x][y] = image[x,y,0]
            greenMatrix[x][y] = image[x,y,1]
            blueMatrix[x][y] = image[x,y,2]
    red.append(redMatrix)
    green.append(greenMatrix)
    blue.append(blueMatrix)

newImage = np.zeros((height,width,3), np.uint8)

for x in range(height):
    for y in range(width):

        rgb = []

        if(method == "median"):
            redMedian = getMedian(red,x,y)
            greenMedian = getMedian(green,x,y)
            blueMedian = getMedian(blue,x,y)

        if(method == "mean"):
            redMedian = getMean(red,x,y)
            greenMedian = getMean(green,x,y)
            blueMedian = getMean(blue,x,y)

        if(method == "mode"):
            redMedian = getMode(red,x,y)
            greenMedian = getMode(green,x,y)
            blueMedian = getMode(blue,x,y)


        rgb.append(redMedian)
        rgb.append(greenMedian)
        rgb.append(blueMedian)

        newImage[x][y] = rgb

cv2.imwrite(saved + "results.jpg", newImage) # save image
