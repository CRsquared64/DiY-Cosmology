import loadImage
import galaxyDetection

denoise = True

if __name__ == "__main__":
    img = loadImage.load_image("images/m51.tif")
    if denoise:
        img = loadImage.clean(img)
    img = loadImage.image_contrast(img, factor=5)
    arr, h, w = loadImage.image_conversions(img)

    galaxyDetection.fastCv2MaskPrediction(arr)
