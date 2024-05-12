
import pandas as pd


if __name__ == '__main__':
    ls_mode = ['quaternion', 'euler', '6df']
    for name_mode in ls_mode:
        print(name_mode)
        for item in range(1, 11):
            path_csv = "../datasets/train_result/num_groups__z_{0}_{1}.csv".format(name_mode, item)
            # path_csv = "../datasets/train_result/num_groups__c_quaternion_1.csv"
            df = pd.read_csv(path_csv)
            # print(df.shape)
            # print(df.values[0, :])
            print(df.values.mean(axis=1))

    # print(df['Data_0'])
    # # 使用 .iloc[] 选择第一行（索引为 0）
    # first_row = df.iloc[0]
    # print("First row using iloc:")
    # print(first_row)

    (8,  1.13833569)
    (16, 1.13568089)
    (24, 1.13593818)
    (32, 1.13597268)
    (40, 1.1357167 )
    (48, 1.13533473)
    (56, 1.13489776)
    (64, 1.13444254)
    (72, 1.13398684)
    (80, 1.13358697)
