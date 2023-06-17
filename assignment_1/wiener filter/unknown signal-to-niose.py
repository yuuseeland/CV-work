import numpy as np
from scipy import fftpack
from PIL import Image

def wiener_filter(image, snr=30, k=1):
    # 转换为灰度图像
    gray_image = image.convert("L")
    
    # 将图像转换为numpy数组
    img = np.array(gray_image)
    
    # 对图像进行傅里叶变换
    img_fft = fftpack.fftshift(fftpack.fft2(img))
    
    # 计算噪声功率谱
    noise_power = np.mean(np.abs(img_fft) ** 2)
    
    # 估计信噪比
    estimated_snr = snr * noise_power
    
    # 使用维纳滤波进行图像恢复
    restored_img_fft = img_fft / (img_fft + estimated_snr)
    restored_img = np.abs(fftpack.ifft2(fftpack.ifftshift(restored_img_fft)))
    
    # 将图像转换回PIL图像对象
    restored_image = Image.fromarray(restored_img.astype(np.uint8))
    
    return restored_image

# 打开图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\wiener filter\Lena.bmp")

# 进行维纳滤波
restored_image = wiener_filter(image)

# 保存结果图像
restored_image.save("unknown signal-to-niose ratio.bmp")
