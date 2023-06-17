from PIL import Image

# 打开图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\point arithmetic\point arithmetic.jpg").convert("L")

# 定义线性点运算的参数
# 增益（乘法因子）
gain = 1.1
# 偏移（加法因子）
bias = 10

# 应用线性点运算
output_image = image.point(lambda x: x * gain + bias)

# 保存结果图像
output_image.save("L-p a.jpg")
