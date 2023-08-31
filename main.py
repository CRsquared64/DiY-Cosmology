import loadImage
import galaxyDetection

denoise = True

if __name__ == "__main__":
    img = loadImage.load_image("images/bodeangular.tif")
    if denoise:
        img = loadImage.clean(img)
    arr, h, w = loadImage.image_conversions(img)
    w = galaxyDetection.fastCv2StarlessPrediction(arr)
    print(w)