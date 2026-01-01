这是 freeCodeCamp 数据分析课程的第四个项目 Page View Time Series Visualizer。这个项目要求你处理时间序列数据，并通过三种不同的图表（折线图、柱状图、箱线图）展示数据的趋势和季节性。

以下是完整的代码实现，你可以直接将其填入 time_series_visualizer.py 文件中：

代码实现
Python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. 导入数据并设置索引
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# 2. 清洗数据：过滤掉前 2.5% 和后 2.5% 的数据
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# 3. 绘制折线图
def draw_line_plot():
    # 拷贝数据
    df_line = df.copy()

    # 创建绘图
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)

    # 设置标题和标签
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # 保存并返回
    fig.savefig('line_plot.png')
    return fig

# 4. 绘制柱状图（按年分组，按月显示平均值）
def draw_bar_plot():
    # 准备数据
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # 按照年份和月份分组计算平均值
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # 重新排列月份顺序
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot[months]

    # 绘图
    fig = df_pivot.plot(kind='bar', figsize=(15, 10), xlabel='Years', ylabel='Average Page Views').get_figure()
    plt.legend(title='Months', labels=months)

    # 保存并返回
    fig.savefig('bar_plot.png')
    return fig

# 5. 绘制箱线图
def draw_box_plot():
    # 准备数据（样板代码已包含部分逻辑）
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # 绘图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

    # 左图：年度箱线图 (趋势)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # 右图：月度箱线图 (季节性)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=month_order)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # 保存并返回
    fig.savefig('box_plot.png')
    return fig
