import cv2 as cv
import numpy as np


def getImage():
    path  = input("Enter the path to your image please \n")
    image = cv.imread(path, 1)
    if image is None:
        print("Empty image path, I can't hide the message.\n")
        return 0
    else : 
        return image


def getMessage():
    message = input("Enter a message to hide \n")
    while(message == ''):
        message = input("Enter a message to hide\n")
    return message



def toBinary(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes):
        return ''.join([ format(i, "08b") for i in data ])
    elif isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


def encodeMessage():

    message = getMessage()
    image = getImage()
    maxBytes = image.shape[0] * image.shape[1] * 3

    if len(message) > maxBytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    else : 
        print("[*] Encoding data...\n")
        # add stopping criteria
        message += "====="
        binaryMessage = toBinary(message)
        messageIndex = 0
        messageLen = len(binaryMessage)
        for row in image:
            for pixel in row:
                # convert RGB values to binary format
                r, g, b = toBinary(pixel)
                 # modify the least significant bit only if there is still data to store
                if messageIndex < messageLen:
                    # least significant red pixel bit
                    pixel[0] = int(r[:-1] + binaryMessage[messageIndex], 2)
                    messageIndex += 1
                if messageIndex < messageLen:
                    # least significant green pixel bit
                    pixel[1] = int(g[:-1] + binaryMessage[messageIndex], 2)
                    messageIndex += 1
                if messageIndex < messageLen:
                    # least significant bleu pixel bit
                    pixel[2] = int(b[:-1] + binaryMessage[messageIndex], 2)
                    messageIndex += 1
                # if data is encoded, just break out of the loop
                if messageIndex >= messageLen:
                    break
        return image
    

def decodeMessage(image):
    print("[+] Decoding...\n")
    binaryMessage = ""
    for row in image:
        for pixel in row:
            r, g, b = toBinary(pixel)
            binaryMessage += r[-1]
            binaryMessage += g[-1]
            binaryMessage += b[-1]
    # split by 8-bits
    allBytes = [ binaryMessage[i: i+8] for i in range(0, len(binaryMessage), 8)]
    # convert from bits to characters
    decodedMessage = ''
    for byte in allBytes:
        decodedMessage += chr(int(byte,2))
        if decodedMessage[-5:] == "=====":
            break
    print("Your hidden message is : \"", decodedMessage[:-5], "\"")
    return decodedMessage[:-5]

