#right okay so this is going to include two main functions, both to detect the galaxy, crop the image, and then send it off.
#however one is going to be using yolov5, and a pretrained weights file. This may/mayn't be accurate so we will see. I have it made already at
#https://github.com/CRsquared64/Galaxy-Detection
import cv2
import numpy as np
def fastCv2StarlessPrediction(img,adaptive_method, block, c): # all of this code seems extermelly unnecessary, but we prevail
    if adaptive_method == int('1'):
        adaptive_method = cv2.ADAPTIVE_THRESH_MEAN_C
    elif adaptive_method == int('2'):
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
def fastCv2MaskPrediction(img, thresh): # no stars pretty please
    cv2.imshow("Grey", img)
    thresh_m = cv2.THRESH_BINARY
    _, result = cv2.threshold(img, thresh, 255, thresh_m) # anything less then thresh becomes white 255
    cv2.imshow("Thresh", result)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(result, connectivity=8)
    largest_component_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
    largest_component_mask = (labels == largest_component_label).astype(np.uint8) * 255
    cv2.imshow("Isolated", largest_component_mask)
    cv2.imwrite("isolated_mask.png", largest_component_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return largest_component_mask


def yoloGalaxyDetection(): # empty for now
    pass