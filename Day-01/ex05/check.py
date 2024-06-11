import numpy as np
import matplotlib.pyplot as plt

# Define the original RGB image array
original_image = np.array([[[112, 153, 204], [41, 208, 137]], [[8, 109, 128], [18, 236, 52]]], dtype=np.uint8)

# Create separate arrays for each channel
red_channel_only = original_image.copy()
red_channel_only[:, :, [1, 2]] = 0  # Set green and blue channels to zero

green_channel_only = original_image.copy()
green_channel_only[:, :, [0, 2]] = 0  # Set red and blue channels to zero

blue_channel_only = original_image.copy()
blue_channel_only[:, :, [0, 1]] = 0  # Set red and green channels to zero

gray_image = np.mean(original_image, axis=2, dtype=np.uint8)

# Plotting
fig, axs = plt.subplots(2, 3, figsize=(10, 7))

# Original RGB Image
axs[0, 0].imshow(original_image)
axs[0, 0].set_title('Original RGB Image')

# Red Channel Only
axs[0, 1].imshow(red_channel_only)
axs[0, 1].set_title('Red Channel Only')

# Green Channel Only
axs[0, 2].imshow(green_channel_only)
axs[0, 2].set_title('Green Channel Only')

# Blue Channel Only
axs[1, 0].imshow(blue_channel_only)
axs[1, 0].set_title('Blue Channel Only')

# Gray Image
axs[1, 1].imshow(gray_image, cmap='gray')
axs[1, 1].set_title('Gray Image')

# Hide remaining axes
for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()

