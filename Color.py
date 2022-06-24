from turtle import exitonclick
from cv2 import CALIB_CB_MARKER
import numpy as np
import cv2
import pandas as pd
import keyboard 

img  =  cv2.imread("testpic.jpg") # sample image to read the colors from 
click = False # boolean variable to check if the mouse is clicked

index  = ["color","color_name","hex","r","g","b"] 
csv = pd.read_csv("colors.csv", names = index, header = None)

cv2.namedWindow("Color Detection")

def call_back_function (event ,x,y,flags,param):
   # call back function: when the mouse is clicked, the color of the pixel that the mouse clicked on is displayed
    if event == cv2.EVENT_LBUTTONDOWN:
        global r,g,b ,x_pos,y_pos,click
        click = True
        x_pos = x
        y_pos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

def get_color_name(r,g,b):
    # get the color name from the csv file using the r,g,b values
    min_color_diff = 10000
    for i in range(len(csv)):
        difff = abs(r- int(csv.loc[i,"r"])) + abs(g- int(csv.loc[i,"g"])) + abs(b - int(csv.loc[i,"b"]))
        if difff < min_color_diff:
            min_color_diff = difff
            color_name = csv.loc[i,"color_name"]
    return color_name

# create window to display the image and call the call back function when the mouse is clicked
cv2.setMouseCallback("Color Detection", call_back_function)


loop = 1 # loop variable to keep the program running
while (1):
    cv2.imshow("Color Detection", img)
    cv2.waitKey(0) 
    if click == True :
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text  = "Color: " + get_color_name(r,g,b) + " RGB: " + str(r) + " ," + str(g) + " ," + str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if (r+b+g>= 600) :
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        click = False
    if keyboard.is_pressed('Esc'):
        break
cv2.destroyAllWindows()

print("hello world")