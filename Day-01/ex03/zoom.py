from load_image import load_image
import numpy as np
import matplotlib.pyplot as plt

def slice_me(img_arr: list) -> (list, list):
    ''' doc '''

    inner_slicing = img_arr[100:500, 400:800, :]
    final_2darr = inner_slicing[:, :, 0]
    final_3darr = final_2darr[:, :, np.newaxis]
    return final_2darr, final_3darr

def zoom(path):
    ''' doc '''

    img_arr = load_image(path)
    img_arr = np.array(img_arr)
    if len(img_arr.shape) == 2:
        img_arr = np.stack((img_arr, ) * 3, axis=-1)
    final_2darr, final_3darr = slice_me(img_arr)
    print(f"The shape of image is: {img_arr.shape}")
    print(f"New shape after slicing: {final_3darr.shape} or {final_2darr.shape}")
    print(final_3darr)
    if len(img_arr.shape) == 3:
        gray = np.dot(img_arr[..., :3], [0.2989, 0.5870, 0.1140])
    print(f"gray's shape : {gray.shape}")
    sliced_gray = gray[100:500, 400:800]
    print(f"sliced_gray's shape : {sliced_gray.shape}")
    plt.imshow(sliced_gray)
    plt.show()


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
