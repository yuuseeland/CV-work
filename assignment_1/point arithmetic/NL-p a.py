from PIL import Image
import numpy as np

# 打开图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\point arithmetic\point arithmetic.jpg").convert("L")

# 定义幂次变换的参数
gamma = 0.8  # 幂次

# 对每个像素应用幂次变换
output_image = image.point(lambda x: int(((x / 255) ** gamma) * 255))

# 保存结果图像
output_image.save("NL-p a.jpg")
