import cv2 as cv
import numpy as np

# Read the image input 
def ReadImage():
    path  = input("Enter the path to your image please \n")
    image = cv.imread(path, 1)
    if image is None:
        print("Empty image path, I can't hide the message.")
        return 0
    else : 
        print("Image well entered")
        return image

ReadImage()