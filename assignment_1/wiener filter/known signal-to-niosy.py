import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

def wiener_filter(image, snr, kernel_size, sigma):
    # Convert image to numpy array
    img_array = np.array(image, dtype=np.float64)
    
    # Compute noise power using known SNR
    signal_power = np.mean(img_array ** 2)
    noise_power = signal_power / (10 ** (snr / 10))
    
    # Create Gaussian kernel
    kernel = gaussian_filter(np.ones((kernel_size, kernel_size)), sigma)
    
    # Apply Wiener filter
    kernel_power = np.mean(kernel ** 2)
    k = noise_power / kernel_power
    filtered_array = img_array / (1 + k / noise_power)
    
    # Clip the filtered array to the valid intensity range
    filtered_array = np.clip(filtered_array, 0, 255)
    
    # Convert filtered array back to image
    filtered_image = Image.fromarray(filtered_array.astype(np.uint8))
    
    return filtered_image

# Load the image
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\wiener filter\Lena.bmp")

# Specify the known SNR value
snr = 30

# Define kernel size and sigma for Gaussian kernel
kernel_size = 5
sigma = 1.5

# Apply Wiener filter with Gaussian kernel
filtered_image = wiener_filter(image, snr, kernel_size, sigma)

# Save the filtered image
filtered_image.save("known signal-to-niose ratio.bmp")
