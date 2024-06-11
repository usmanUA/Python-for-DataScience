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
    print(f"The shape of image is: {final_3darr.shape} or {final_2darr.shape}")
    print(final_3darr)
    transposed = np.transpose(final_2darr, axes=None)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    plt.imshow(transposed)
    plt.show()


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
