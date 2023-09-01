import PIL.ImageFilter
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# going to include comments from now on, i have evolved
def load_image(filepath):  # function to load image... wow
    img = cv2.imread(filepath)
    return img


def image_conversions(img):  # takes the image, gets values, makes it gray and then converts to numpy array. yipee
    h = img.shape[0]
    w = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arr = np.array(gray)
    return arr, h, w

def image_contrast(img, factor):
    img = Image.fromarray(np.uint8(img))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)
    img = np.array(img)
    return img

def to_img(arr):
    return Image.fromarray(np.uint8(arr))

def to_arr(img):
    return np.array(img)


def clean(arr, factor):  # denoiser, may change to make my own if i can be botherd (i cant)
    # img = cv2.fastNlMeansDenoising(arr, None, 10, 7, 21)
    img = to_img(arr)
    img = img.filter(ImageFilter.MedianFilter(size=factor))
    img = to_arr(img)

    return img
