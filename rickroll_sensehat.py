import numpy as np
import glob
import os
from PIL import Image
from time import sleep

# Sensehat boilerplate
from sense_hat import SenseHat
sense = SenseHat()


def rickroll(number_of_frames=5300, rel_path="img"):
    """Reads all .png images in path and prints
       them to the SenseHat led array. Provided
       images should be 8x8 pixels and be uniformly
       named with an incrementing number."""

    FPS = 1 / 25

    # Declare path to images
    script_dir = os.path.dirname(__file__)
    img_dir = os.path.join(script_dir, rel_path)

    # Make list of all .png filenames in the provided path
    filepaths = []
    for filepath in glob.glob(os.path.join(img_dir, "*.png")):
        filepaths.append(filepath)

    # Sort filepaths by the numeric value, e.g. "img/sometext0001.png" --> 1
    filepaths.sort(key=lambda s: int("".join([c for c in s if c.isdigit()])))
    
    # Print images to the led array
    for frame_num, frame in enumerate(filepaths):
        if frame_num > number_of_frames:
            break
        with Image.open(filepath) as imgfile:
            img_array = np.asarray(imgfile)
            flat_image_array = [element for sublist in img_array for element in sublist]
            sense.set_pixels(flat_image_array)
            sleep(FPS)


rickroll()
