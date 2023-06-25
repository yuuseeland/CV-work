import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'D:\Desktop\image_analysis\assignment_1\adaptive Threshold\adaptive Threshold.jpg', 0)  # 灰度图像

# 初始化阈值为一个初始值
threshold = 128

# 迭代次数
max_iterations = 10

for _ in range(max_iterations):
    # 将图像分割成背景和前景
    background = image <= threshold
    foreground = image > threshold
    
    # 计算背景和前景的像素数量
    w0 = np.sum(background)
    w1 = np.sum(foreground)
    
    # 计算新的阈值（这里使用平均值）
    new_threshold = (np.mean(image[background]) + np.mean(image[foreground])) / 2
    
    # 判断是否达到停止条件（阈值不再变化）
    if np.abs(new_threshold - threshold) < 1e-5:
        break
    
    # 更新阈值
    threshold = new_threshold

# 使用最终的阈值进行图像分割
thresholded_image = np.zeros_like(image)
thresholded_image[image > threshold] = 255

# 显示原始图像和阈值分割后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
