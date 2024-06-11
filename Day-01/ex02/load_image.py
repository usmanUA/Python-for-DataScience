from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    ''' doc '''

    img = Image.open(path, mode='r')
    img_arr = np.array(img)
    print(f"The shape of image is: {img_arr.shape}")
    return img_arr

