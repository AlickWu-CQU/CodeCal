

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


if __name__ == '__main__':
    list_group_AMSE1, list_group_AMSE2 = [], []
    list_group_MAE1, list_group_MAE2 = [], []
    list_group_AMSE_MAE1, list_group_AMSE_MAE2 = [], []
    list_nums = []
    for item in range(1, 11):
        path_csv = "../datasets/num_groups_lateral_quat_{0}.csv".format(item)
        df = pd.read_csv(path_csv)
        data_ = df.values.mean(axis=1)
        list_group_AMSE1.append(data_[0])
        list_group_AMSE2.append(data_[3])
        list_group_MAE1.append(data_[1])
        list_group_MAE2.append(data_[4])
        list_group_AMSE_MAE1.append(data_[2])
        list_group_AMSE_MAE2.append(data_[5])
        list_nums.append('N{0}'.format(item*8))

    # 设置条形图的宽度
    bar_width = 0.35
    # 生成位置信息
    positions_group1 = np.arange(len(list_nums))
    positions_group2 = [pos + bar_width for pos in positions_group1]

    # 设置图像的大小
    plt.figure(figsize=(10, 9))

    # 创建第一个子图
    plt.subplot(3, 1, 1)  # 2 rows, 1 column, select the first subplot
    # 创建条形图
    plt.bar(positions_group1, list_group_AMSE1, width=bar_width, label='AMSE_1')
    plt.bar(positions_group2, list_group_AMSE2, width=bar_width, label='AMSE_2')
    # 添加数据标签
    for i, value in enumerate(list_group_AMSE1):
        plt.text(positions_group1[i]-0.1, value, f'{value:.3f}', rotation=60, fontsize=11, ha='center', va='bottom')
    for i, value in enumerate(list_group_AMSE2):
        plt.text(positions_group2[i]+0.1, value, f'{value:.3f}', rotation=60, fontsize=11, ha='center', va='bottom')
    # 添加标题和标签
    plt.ylabel('AMSE', fontsize=16)
    plt.xticks((positions_group2+positions_group1)/2, list_nums)  # 设置X轴刻度位置及标签
    plt.ylim(0, 0.8)
    plt.legend(fontsize='medium')
    # 获取当前图的位置和大小
    ax = plt.gca()
    pos = ax.get_position()
    # 设置标题并将其放置在图的左侧
    plt.figtext(0.02, (pos.y0 + pos.y1) / 2, 'a)', fontsize=16, va='center', ha='left')

    # 创建第二个子图
    plt.subplot(3, 1, 2)  # 2 rows, 1 column, select the second subplot
    # 创建条形图
    plt.bar(positions_group1, list_group_MAE1, width=bar_width, label='MAE_1')
    plt.bar(positions_group2, list_group_MAE2, width=bar_width, label='MAE_2')
    # 添加数据标签
    for i, value in enumerate(list_group_MAE1):
        plt.text(positions_group1[i]-0.1, value, f'{value:.3f}', rotation=60, fontsize=11, ha='center', va='bottom')
    for i, value in enumerate(list_group_MAE2):
        plt.text(positions_group2[i]+0.1, value, f'{value:.3f}', rotation=60, fontsize=11, ha='center', va='bottom')
    # 添加标题和标签
    plt.ylabel('MAE', fontsize=16)
    plt.xticks((positions_group2+positions_group1)/2, list_nums)  # 设置X轴刻度位置及标签
    plt.ylim(0, 0.8)
    # 设置标签字体大小
    plt.legend(fontsize='medium')  # 或者可以设置具体的字体大小如 fontsize=12
    # 获取当前图的位置和大小
    ax = plt.gca()
    pos = ax.get_position()
    # 设置标题并将其放置在图的左侧
    plt.figtext(0.02, (pos.y0 + pos.y1) / 2, 'b)', fontsize=16, va='center', ha='left')

    # 创建第二个子图
    plt.subplot(3, 1, 3)  # 2 rows, 1 column, select the second subplot
    # 创建条形图
    plt.bar(positions_group1, list_group_AMSE_MAE1, width=bar_width, label='AMSE/MAE_1')
    plt.bar(positions_group2, list_group_AMSE_MAE2, width=bar_width, label='AMSE/MAE_2')
    # 添加数据标签
    for i, value in enumerate(list_group_AMSE_MAE1):
        plt.text(positions_group1[i]-0.1, value, f'{value:.3f}', rotation=60, fontsize=11, ha='center', va='bottom')
    for i, value in enumerate(list_group_AMSE_MAE2):
        plt.text(positions_group2[i]+0.1, value, f'{value:.3f}', rotation=60, fontsize=11, ha='center', va='bottom')
    # 添加标题和标签
    plt.ylabel('AMSE/MAE', fontsize=16)
    plt.xticks((positions_group2+positions_group1)/2, list_nums)  # 设置X轴刻度位置及标签
    # 设置 Y 轴的取值范围
    plt.ylim(0, 2.8)
    plt.legend(fontsize='medium')   # 显示图例

    # 获取当前图的位置和大小
    ax = plt.gca()
    pos = ax.get_position()
    # 设置标题并将其放置在图的左侧
    plt.figtext(0.02, (pos.y0 + pos.y1) / 2, 'c)', fontsize=16, va='center', ha='left')

    plt.subplots_adjust(wspace=0.25)
    # 显示图形
    plt.show()


