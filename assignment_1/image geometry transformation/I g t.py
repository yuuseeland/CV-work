from PIL import Image

# 打开图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\point arithmetic\point arithmetic.jpg").convert("L")

# 平移变换
tx = 20  # X轴平移量
ty = 50  # Y轴平移量
translated_image = image.transform(image.size, Image.AFFINE, (1, 0, tx, 0, 1, ty))

# 镜像变换
mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)

# 旋转变换
angle = 45  # 旋转角度
rotated_image = image.rotate(angle)

# 复合变换：平移 -> 镜像 -> 旋转
combined_image = image.transform(image.size, Image.AFFINE, (1, 0, tx, 0, 1, ty))
combined_image = combined_image.transpose(Image.FLIP_LEFT_RIGHT)
combined_image = combined_image.rotate(angle)

# 保存结果图像
translated_image.save("translated.jpg")
mirrored_image.save("mirrored.jpg")
rotated_image.save("rotated.jpg")
combined_image.save("combined.jpg")
