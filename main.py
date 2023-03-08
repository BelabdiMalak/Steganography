import cv2 as cv
import numpy as np


def getImage():
    path  = input("Enter the path to your image please \n")
    image = cv.imread(path, 1)
    if image is None:
        print("Empty image path, I can't hide the message.")
        return 0
    else : 
        print("Your image is well entered.")
        return image


def getMessage():
    message = input("Enter a message to hide \n")
    while(message == ''):
        message = input("Enter a message to hide\n")
    print("Your message is well entered.")
    return message



def encodeMessage():
    message = getMessage()
    image = getImage()
    BinaryMessage = ''.join([ format(ord(i), "08b") for i in message ])
    
    # Compare if the image pixels are enough to cover the message
    n_bytes = image.shape[0] * image.shape[1] * 3
    if len(BinaryMessage) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")

encodeMessage()