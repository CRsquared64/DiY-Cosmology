import cv2
import numpy as np
#going to include comments from now on, i have evolved
def load_image(filepath): # function to load image... wow
    img = cv2.imread(filepath)
    return img
def image_conversions(img): # takes the image, gets values, makes it gray and then converts to numpy array. yipee
    h = img.shape[0]
    w = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arr = np.array(gray)

