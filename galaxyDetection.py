#right okay so this is going to include two main functions, both to detect the galaxy, crop the image, and then send it off.
#however one is going to be using yolov5, and a pretrained weights file. This may/mayn't be accurate so we will see. I have it made already at
#https://github.com/CRsquared64/Galaxy-Detection
import cv2

def fastCv2StarlessPrediction(img,adaptive_method, block, c): # all of this code seems extermelly unnecessary, but we prevail
    if adaptive_method == '1':
        adaptive_method = cv2.ADAPTIVE_THRESH_MEAN_C
    elif adaptive_method == '2':
        adaptive_method = cv2. ADAPTIVE_THRESH_GAUSSIAN_C
    else:
        raise Exception('Error, incorrect value/type for adpative_method, argument should be either "1" or "2" as an '
                        'integer. ')
    thresh = cv2.adaptiveThreshold(img, 255, adaptive_method, cv2.THRESH_BINARY, block, c)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = cv2.boundingRect(contours[0])
    return w

def precroppedDetection(img): # method if image is already cropped/w is already known
    w = img.shape[1]
    return w

def yoloGalaxyDetection(): # empty for now
    pass