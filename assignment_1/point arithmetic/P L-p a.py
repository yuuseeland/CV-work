from PIL import Image

# 打开图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\point arithmetic\point arithmetic.jpg")
image = image.convert("L")


# 定义分段线性点运算的参数
# 第一段线性点运算的参数
gain1 = 0.5
bias1 = 0

# 第二段线性点运算的参数
gain2 = 1.2
bias2 = -20

# 第三段线性点运算的参数
gain3 = 0.8
bias3 = 30

# 分段线性点运算
output_image = image.point(lambda x: x * gain1 + bias1 if x < 30 else (x * gain2 + bias2) if x < 130 else x * gain3 + bias3)
# 保存结果图像
output_image.save("P L-p a.jpg")
