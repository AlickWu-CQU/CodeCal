import matplotlib.pyplot as plt
import numpy as np


def show_fig(x, AMSE1, MAE1, AMSE_MAE_1, AMSE2, MAE2, AMSE_MAE_2):

    # 创建图形和第一个 Y 轴
    fig, ax1 = plt.subplots(figsize=(8, 6))
    # 绘制第一个 Y 轴的折线
    ax1.plot(x, AMSE1, color='blue', marker='o', label='AMSE1')  # 使用圆形标识（o）
    ax1.plot(x, AMSE2, color='blue', marker='o', label='AMSE2', markerfacecolor='none')  # 使用圆形标识（o）
    ax1.set_xlabel('number of particles', fontsize=12)
    ax1.set_ylabel('AMSE / (mm)', color='blue', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='blue')
    # 设置Y 轴的取值范围
    ax1.set_ylim(0, 2.5)
    ax1.tick_params(axis='both', labelsize=12)
    # 创建第二个 Y 轴
    ax2 = ax1.twinx()
    # 绘制第二个 Y 轴的折线
    ax2.plot(x, MAE1, color='green', marker='s', label='MAE1')  # 使用正方形标识（s）
    ax2.plot(x, MAE2, color='green', marker='s', label='MAE2', markerfacecolor='none')  # 使用正方形标识（s）
    ax2.set_ylabel('MAE / (mm)', color='green', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='green')
    # 设置Y 轴的取值范围
    ax2.set_ylim(0, 1.2)
    ax2.tick_params(axis='both', labelsize=12)
    # 创建第三个 Y 轴
    ax3 = ax1.twiny()
    # 移动第三个 Y 轴到右侧
    ax3.spines['right'].set_position(('outward', 60))
    ax3.set_frame_on(False)
    ax3.patch.set_visible(False)
    # 绘制第三个 Y 轴的折线
    ax3.plot(x, AMSE_MAE_1, color='red', marker='^', label='AMSE_MAE_1')  # 使用三角形标识（^）
    ax3.plot(x, AMSE_MAE_2, color='red', marker='^', label='AMSE_MAE_2', markerfacecolor='none')  # 使用三角形标识（^）
    ax3.set_xlabel('AMSE/MAE', color='red', fontsize=12)
    ax3.tick_params(axis='x', labelcolor='red')
    # 设置Y 轴的取值范围
    ax3.set_ylim(0, 2.5)
    ax3.tick_params(axis='both', labelsize=12)
    # 添加图例
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()

    ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc='upper right', fontsize=12, )
    # 设置 X 轴刻度
    ax1.set_xticks([8, 16, 24, 32, 40, 48, 56, 64, 72, 80], fontsize=12)
    # 添加网格
    ax1.grid(which='both', axis='both', linestyle='--', alpha=0.5)
    # 显示图形
    plt.show()


if __name__ == '__main__':
    # 生成示例数据
    x = np.linspace(8, 80, 10)
    data_c_ = np.array([[0.46521054, 0.39344775, 1.17969388, 0.49421727, 0.43400857, 1.13833569],
                        [0.35478767, 0.30233881, 1.17125895, 0.3894088,  0.34285547, 1.13568089],
                        [0.31642517, 0.27181445, 1.16285823, 0.35500229, 0.31257508, 1.13593818],
                        [0.29936735, 0.25847518, 1.15756466, 0.3397295,  0.29914092, 1.13597268],
                        [0.29067555, 0.25175473, 1.15426802, 0.33192024, 0.29232103, 1.1357167],
                        [0.2856773,  0.24795487, 1.15194884, 0.32745179, 0.28846832, 1.13533473],
                        [0.28247268, 0.24557985, 1.15012148, 0.32463489, 0.28608258, 1.13489776],
                        [0.28023354, 0.24396496, 1.14860173, 0.32271223, 0.2844897,  1.13444254],
                        [0.2785686,  0.24279062, 1.14733293, 0.32131377, 0.2833593,  1.13398684],
                        [0.27726552, 0.24189928, 1.14620237, 0.32024331, 0.2825044,  1.13358697]])

    data_z_ = np.array([[0.5102702 , 0.44838131, 1.13569513, 0.62298565, 0.52723104, 1.18475882],
                        [0.41061222, 0.36733416, 1.1188775 , 0.57733285, 0.47949917, 1.20653491],
                        [0.37048124, 0.33242546, 1.11476835, 0.55590064, 0.45626518, 1.21950912],
                        [0.34484852, 0.31055514, 1.11076263, 0.5442039 , 0.44235655, 1.23072419],
                        [0.32842687, 0.29662069, 1.10764161, 0.53793205, 0.43385787, 1.24005692],
                        [0.31749652, 0.28744448, 1.10497425, 0.53435336, 0.42843733, 1.24725919],
                        [0.30983904, 0.28123704, 1.10209364, 0.53214973, 0.42487   , 1.25249463],
                        [0.30421327, 0.27689599, 1.09897052, 0.53068442, 0.42241934, 1.25627392],
                        [0.29992556, 0.27370433, 1.09597723, 0.52964867, 0.42069471, 1.25896392],
                        [0.29658083, 0.2712554 , 1.09336378, 0.52888111, 0.41942324, 1.26097235]])

    # AMSE1_, MAE1_, AMSE_MAE_1_, \
    #     AMSE2_, MAE2, AMSE_MAE_2_ = \
    #     data_c_[:, 0], data_c_[:, 1], data_c_[:, 2], \
    #         data_c_[:, 3], data_c_[:, 4], data_c_[:, 5]
    #
    # show_fig(x, AMSE1_, MAE1_, AMSE_MAE_1_, AMSE2_, MAE2, AMSE_MAE_2_)

    AMSE1_, MAE1_, AMSE_MAE_1_, \
        AMSE2_, MAE2, AMSE_MAE_2_ = \
        data_z_[:, 0], data_z_[:, 1], data_z_[:, 2], \
            data_z_[:, 3], data_z_[:, 4], data_z_[:, 5]

    show_fig(x, AMSE1_, MAE1_, AMSE_MAE_1_, AMSE2_, MAE2, AMSE_MAE_2_)
