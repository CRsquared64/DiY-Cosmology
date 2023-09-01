# angular size and actual size (estimation) to distance :)
def GetGalaxySizeFromArray(w, pixel_scale): # longer names sound more professional, right?
    angular_size = (w / pixel_scale) / 3600 # in degrees
    return angular_size

def GetGalaxyDistanceFromSize(angular_size, size): # size in parsecs
    distance = (size / angular_size) / 3.086
    print(distance, " Estimated Distance In Light Years")


