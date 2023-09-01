import loadImage
import galaxyDetection
import cv2

denoise = True

if __name__ == "__main__":
    img = loadImage.load_image("images/outputc.tif")
    if denoise:
        img = loadImage.clean(img, factor=25)
        cv2.imshow("Denoised", img)
    img = loadImage.image_contrast(img, factor=6)
    arr, h, w = loadImage.image_conversions(img)

    mask = galaxyDetection.fastCv2MaskPrediction(arr, thresh=75)
    w = galaxyDetection.fastCv2StarlessPrediction(mask, 1, 7, 1)
    print(f"{w} Pixel Diameter in mask")