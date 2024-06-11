from load_image import load_image
from pimp_image import *
import matplotlib.pyplot as plt

array = load_image("landscape.jpg")
img1 = ft_invert(array)
img2 = ft_red(array)
img3 = ft_green(array)
img4 = ft_blue(array)
img5 = ft_grey(array)

fig, axs = plt.subplots(3, 2, figsize=(8, 12))

axs[0, 0].imshow(array)
axs[0, 0].set_title('Original')
axs[0, 0].axis('off')

axs[0, 1].imshow(img1)
axs[0, 1].set_title('Invert')
axs[0, 1].axis('off')

axs[1, 0].imshow(img2)
axs[1, 0].set_title('Red')
axs[1, 0].axis('off')

axs[1, 1].imshow(img3)
axs[1, 1].set_title('Green')
axs[1, 1].axis('off')

axs[2, 0].imshow(img4)
axs[2, 0].set_title('Blue')
axs[2, 0].axis('off')

axs[2, 1].imshow(img5, cmap='gray')
axs[2, 1].set_title('Gray')
axs[2, 1].axis('off')

plt.tight_layout()

plt.show()

print(ft_invert.__doc__)
