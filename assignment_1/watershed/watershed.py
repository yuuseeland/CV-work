import cv2
import numpy as np

# 读取图像
image = cv2.imread(r"D:\Desktop\image_analysis\assignment_1\wiener filter\Lena.bmp")

# 将图像转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 平滑图像
smooth = cv2.medianBlur(gray, 5)

# 二值化图像
_, binary = cv2.threshold(smooth, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 形态学操作 - 开运算去除噪声
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# 形态学操作 - 膨胀填充区域
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 距离变换
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# 获得未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 标记未知区域
_, markers = cv2.connectedComponents(sure_fg)

# 增加标记以避免与背景标记冲突
markers = markers + 1
markers[unknown == 255] = 0

# 应用分水岭算法
markers = cv2.watershed(image, markers)

# 根据标记结果绘制边界
image[markers == -1] = [0, 0, 255]

# 显示结果图像
cv2.imshow('Segmented Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
