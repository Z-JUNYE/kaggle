import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# 生成一些样本数据
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.normal(scale=0.3, size=x.shape)

# 创建平滑样条
spline = UnivariateSpline(x, y, s=2)  # `s` 控制平滑度，值越大越平滑

# 在新的点上评估样条
x_smooth = np.linspace(0, 10, 500)
y_smooth = spline(x_smooth)

# 绘图
plt.figure(figsize=(8, 5))
plt.scatter(x, y, label="Data", color="blue", alpha=0.6)
plt.plot(x_smooth, y_smooth, label="Smooth Spline", color="red", lw=2)
plt.legend()
plt.title("Smooth Spline using SciPy")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

