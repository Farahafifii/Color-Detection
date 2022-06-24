from cv2 import CALIB_CB_MARKER
import numpy as np
import cv2
import pandas as pd

click = False # boolean variable to check if the mouse is clicked
img  =  cv2.imread("testpic.jpg") # sample image to read the colors from 

index  = ["color","color_name","hex","r","g","b"] 
data = pd.read_csv("colors.csv", names = index, header = None)

def call_back (event ,x,y,flags , param):
   # call back function: when the mouse is clicked, the color of the pixel that the mouse clicked on is displayed
    if event == cv2.EVENT_LBUTTONDOWN:
        global r1,g1,b1 ,x_pos , y_pos 
        click = True
        x_pos = x
        y_pos = y
        b1 = int(b1)
        g1 = int(g1)
        r1 = int(r1)

def get_color_name(r,g,b):
    # get the color name from the csv file using the r,g,b values
    min_color_diff = 10000
    for i in range(len(data)):
        difff = abs(r- int(data.loc[i,"r"])) + abs(g- int(data.loc[i,"g"])) + abs(b- int(data.loc[i,"b"]))
        if difff < min_color_diff:
            min_color_diff = difff
            color_name = data.loc[i,"color_name"]
    return color_name

# create window to display the image and call the call back function when the mouse is clicked
cv2.namedWindow("Color Detection")
cv2.setMouseCallback("Color Detection", call_back)


while (1):
    cv2.imshow("Color Detection", img)
    if (click):
        cv2.rectangle(img,(20,20),(750,60),(b1,g1,r1),-1)
        text  = "Color: " + get_color_name(r1,g1,b1) + "RGB: " + str(r1) + "," + str(g1) + "," + str(b1)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r1+b1+g1 >= 600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        click = False
        if cv2.waitKey(20) & 0xFF ==27:
            break
cv2.destroyAllWindows()

print("hello world")