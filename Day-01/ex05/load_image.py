from PIL import Image
import numpy as np


def load_image(path: str) -> list:
    ''' doc '''

    img = Image.open(path, mode='r')
    img_arr = np.array(img)
    return img_arr
