# Steganography
## Introduction
The aim of this project is to hide a message in an image and Read a hidden message from an image. 

## Tools
OpenCV is the main Python Library used in computer vision (Image manipulation).

## To run the project (Linux)
1. Get sure that you have Python3 installed. In case not run this command : 
```shell
sudo apt-get install python3
```
2. Get sure you have Pip installed. If not run this command : 
```shell
sudo apt-get install python3sudo apt-get install python3
```
3. Install OpenCV library using this command : 
```shell
pip3 install opencv-python
```

4. Run the project running : 
```shell
python3 main.py
```

## Hide a message into an image
Here are steps followed to encode the message into the image:
- First, we should make sure that the number of pixels of the image is enough to contain our data.
- Second, we convert our message to binary format.
- Third, we cycle through the image pixels and convert them to binary.
- Fourth, every pixel contains three values (red, green, bleu), we replace the least significant bit of each one with a bit from our message.

## Read a message from an image
- First, we read the image.
- Second, we convert every pixel of the image to binary.
- Third, we combine the last bits of all pixels and convert them to characters.

