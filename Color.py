from cv2 import CALIB_CB_MARKER
import numpy as np
import cv2
import pandas as pd

img  =  cv2.imread("testpic.jpg") # sample image to read the colors from 

index  = ["color","color_name","hex","r","g","b"] 
data = pd.read_csv("colors.csv", names = index, header = None)

# create window to display the image and call the call back function when the mouse is clicked
cv2.namedWindow("Color Detection")
cv2.setMouseCallback("Color Detection", call_back)

def call_back (event ,x,y,flags , param):
   # call back function: when the mouse is clicked, the color of the pixel that the mouse clicked on is displayed
    if event == cv2.EVENT_LBUTTONDOWN:
        global r,g,b ,x_pos , y_pos ,click
        click = True
        x_pos = x
        y_pos = y
        b = int (b)
        g = int (g)
        r = int (r)

def get_color_name(r,g,b):
    # get the color name from the csv file
    min_color_diff = 1000
    for i in range(len(data)):
        difff = abs(r-data.r[i]) + abs(g-data.g[i]) + abs(b-data.b[i])
        if difff < min_color_diff:
            min_color_diff = difff
            color_name = data.color_name[i]
    return color_name

