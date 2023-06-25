import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def dpcm_encode(yBuf, dBuf, w, h):
    for i in range(1, h):
        for j in range(1, w):
            prediction = yBuf[i-1, j-1]
            current_pixel = yBuf[i, j]
            difference = current_pixel - prediction
            dBuf[i, j] = difference

def dpcm_decode(dBuf, reBuf, w, h):
    for i in range(1, h):
        for j in range(1, w):
            prediction = reBuf[i-1, j-1]
            difference = dBuf[i, j]
            reBuf[i, j] = prediction + difference

def quantize_image(image, bitNum):
    levels = 2 ** bitNum
    quantized_image = np.round(image / (256 / levels)) * (256 / levels)
    quantized_image = np.clip(quantized_image, 0, 255)
    return quantized_image.astype(np.uint8)

# 读取灰度图像
image = cv2.imread(r"D:\Desktop\image_analysis\assignment_1\wiener filter\Lena.bmp", cv2.IMREAD_GRAYSCALE)

# 获取图像的宽度和高度
h, w = image.shape

# 将图像数据类型转换为np.int16
image = image.astype(np.int16)

# 初始化编码和解码数组
dBuf = np.zeros_like(image, dtype=np.int16)
reBuf = np.zeros_like(image, dtype=np.int16)

# DPCM编码
dpcm_encode(image, dBuf, w, h)

# 进行量化
bitNum = 4  # 量化比特数
quantized_dBuf = quantize_image(dBuf, bitNum)

# DPCM解码
dpcm_decode(quantized_dBuf, reBuf, w, h)

# 转换数据类型为uint8
reconstructed_image = reBuf.astype(np.uint8)

# 保存重建图像
cv2.imwrite("PCM1.jpg", reconstructed_image)

# 读取原始图像和重建图像
original_image = cv2.imread(r"D:\Desktop\image_analysis\assignment_1\wiener filter\Lena.bmp", cv2.IMREAD_GRAYSCALE)
reconstructed_image = cv2.imread("PCM1.jpg", cv2.IMREAD_GRAYSCALE)

# 将图像转换为 float64 类型
original_image = original_image.astype(np.float64)
reconstructed_image = reconstructed_image.astype(np.float64)

# 计算 PSNR
psnr = peak_signal_noise_ratio(original_image, reconstructed_image, data_range=255)
print("PSNR:", psnr)

# 计算 SSIM
ssim = structural_similarity(original_image, reconstructed_image, data_range=255)
print("SSIM:", ssim)
