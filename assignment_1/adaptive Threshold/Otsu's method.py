import cv2

# 读取图像
image = cv2.imread(r'D:\Desktop\image_analysis\assignment_1\adaptive Threshold\adaptive Threshold.jpg', 0)  # 灰度图像

# 使用大津法进行阈值分割
_, threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 显示原始图像和阈值分割后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
