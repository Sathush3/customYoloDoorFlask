import cv2
import os

result_folder = "\\result"


def saveFile(filename, img):
    # Image directory

    directory = str(os.getcwd() + result_folder)

    # Change the current directory to specified directory
    os.chdir(directory)
    print(os.listdir(directory))
    # Filename
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(filename, img)
    # List files and directories
    return img