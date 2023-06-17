import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.fft import fft2, ifft2
from scipy.linalg import cholesky

def compute_autocovariance(image):
    image = image.astype(np.float64)
    mean_subtracted_image = image - np.mean(image)
    covariance_matrix = np.cov(mean_subtracted_image, rowvar=False)
    epsilon = 1e-8
    covariance_matrix += epsilon * np.eye(covariance_matrix.shape[0])
    autocovariance = np.real(cholesky(covariance_matrix))
    return autocovariance

def wiener_filter(image, autocovariance, snr):
    image_freq = fft2(image)
    autocovariance_freq = fft2(autocovariance)
    power_spectrum = np.abs(autocovariance_freq) ** 2
    snr_inv = 1 / snr
    transfer_func = np.conj(autocovariance_freq) / (np.abs(autocovariance_freq) ** 2 + snr_inv * power_spectrum)
    filtered_image_freq = image_freq * transfer_func
    filtered_image = np.real(ifft2(filtered_image_freq))
    return filtered_image

# 读取图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\wiener filter\Lena.bmp").convert("L")
image = np.array(image)

# 计算图像的自协方差
autocovariance = compute_autocovariance(image)

# 设置信噪比和截断参数
snr = 30  # 信噪比
k = 0.01  # 截断参数

# 使用维纳滤波进行图像复原
filtered_image = wiener_filter(image, autocovariance, snr)
filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)

# 显示原始图像和滤波后的图像
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image (SNR = 30)')
plt.axis('off')

plt.show()
