这是 freeCodeCamp 数据分析认证的最后一个项目：Sea Level Predictor（海平面预测）。这个项目要求你结合 Pandas 进行数据处理，并使用 scipy.stats 中的线性回归功能来预测未来的气候变化趋势。

你可以将以下代码填入你的 sea_level_predictor.py 文件中：

代码实现
Python

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. 导入数据
    df = pd.read_csv('epa-sea-level.csv')

    # 2. 创建散点图
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Original Data')

    # 3. 第一条最佳拟合线 (使用所有数据)
    # 获取回归参数：斜率、截距、相关系数等
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # 创建预测到 2050 年的年份序列
    years_extended = pd.Series([i for i in range(1880, 2051)])
    # 计算 y 值: y = mx + c
    line1 = res.slope * years_extended + res.intercept
    
    plt.plot(years_extended, line1, 'r', label='Best Fit Line 1 (1880-2050)')

    # 4. 第二条最佳拟合线 (仅使用 2000 年以后的数据)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # 创建预测从 2000 到 2050 年的年份序列
    years_recent = pd.Series([i for i in range(2000, 2051)])
    # 计算 y 值
    line2 = res_recent.slope * years_recent + res_recent.intercept
    
    plt.plot(years_recent, line2, 'green', label='Best Fit Line 2 (2000-2050)')

    # 5. 设置标签和标题
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 6. 保存并返回图像 (样板代码自带)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
