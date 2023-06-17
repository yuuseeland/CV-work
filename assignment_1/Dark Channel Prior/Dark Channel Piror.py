import numpy as np
from PIL import Image

def dehaze(image, w=0.97, t0=0.09, A=214.95):
    # 转换为numpy数组
    img = np.array(image)
    
    # 获取图像亮度信息
    L = np.maximum(img[:,:,0], np.maximum(img[:,:,1], img[:,:,2]))
    
    # 计算全局大气光
    A_est = np.percentile(L, 100*w)
    
    # 估计初始透射率
    t_est = np.maximum(t0, 1 - A/A_est)
    
    # 优化透射率
    for _ in range(10):
        J = (L - A) / np.maximum(t_est, t0) + A
        J_dark = np.percentile(J, 0.1)
        t_est = np.maximum(t0, 1 - w * (J_dark - A) / (L - A))
    
    # 修复图像
    J = (L - A) / np.maximum(t_est, t0) + A
    J = np.clip(J, 0, 255).astype(np.uint8)
    
    return Image.fromarray(J)

# 打开有雾图像
image = Image.open(r"D:\Desktop\image_analysis\assignment_1\Dark Channel Prior\fog.jpg")

# 去雾处理
dehazed_image = dehaze(image)

# 保存去雾结果
dehazed_image.save("dehazed.jpg")
