import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
categories = ['Category A', 'Category B', 'Category C']
values1 = [10, 15, 12]
values2 = [8, 10, 14]
values3 = [12, 9, 11]

# 设置柱状图的宽度
bar_width = 0.2

# 设置 x 轴的刻度位置
x = np.arange(len(categories))

# 绘制柱状图
plt.bar(x, values1, width=bar_width, label='Value 1')
plt.bar(x, values2, width=bar_width, label='Value 2', bottom=values1)
plt.bar(x, values3, width=bar_width, label='Value 3', bottom=np.array(values1) + np.array(values2))

# 设置 x 轴刻度标签
plt.xticks(x, categories)

# 添加图例
plt.legend()

# 显示图形
plt.show()
