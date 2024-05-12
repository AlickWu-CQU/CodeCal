import re
import ast
import json
import numpy as np
import calTrans
from calProj import fun_proj_p


def calStr2Ms(str_file: str):
    ls_file = str_file.split(',')
    ls_file = [float(str_name) for str_name in ls_file]
    m_lig2ndi = calTrans.fourElement2Matrix(ls_file[:7])
    m_pad2ndi = calTrans.fourElement2Matrix(ls_file[7:])
    return m_lig2ndi, m_pad2ndi


def calStr2List(str_file: str):
    ls_file = str_file.split(',')
    ls_file = [float(str_name) for str_name in ls_file]
    return ls_file


def calList2p_q(list_file: list):
    ls_p_cam = []
    for str_file in list_file:
        ls_p_cam.append(calStr2List(str_file))
    array_p_q = np.array(ls_p_cam)
    p_ndi = array_p_q[:, :3]
    q_img = array_p_q[:, 3:]

    p_ndi = np.concatenate((p_ndi, np.ones((p_ndi.shape[0], 1))), axis=1)
    p_proj = np.concatenate((q_img,
                             np.zeros((q_img.shape[0], 1)),
                             np.ones((q_img.shape[0], 1))), axis=1)

    return p_ndi, p_proj


def calList2Array(ls_samp):
    m_lig2ndi_, m_pad2ndi_ = calStr2Ms(ls_samp[0])
    arr_p_ndi_, arr_q_proj_ = calList2p_q(ls_samp[1:])
    return m_lig2ndi_, m_pad2ndi_, arr_p_ndi_, arr_q_proj_


class DataSamp:
    def __init__(self, m_lig2ndi_, m_pad2ndi_, arr_p_ndi_, arr_q_proj_):
        self.m_lig2ndi = m_lig2ndi_
        self.m_pad2ndi = m_pad2ndi_
        self.arr_p_ndi = arr_p_ndi_
        self.arr_q_proj = arr_q_proj_

    def pre_q_with_s_lig(self, pos_s_lig, mat_pad2proj):
        m_lig2pad = np.dot(np.linalg.inv(self.m_pad2ndi),
                           self.m_lig2ndi)
        m_lig2proj = np.dot(mat_pad2proj, m_lig2pad)

        m_ndi2proj = np.dot(mat_pad2proj,
                            np.linalg.inv(self.m_pad2ndi))

        pos_s_proj = np.dot(m_lig2proj, pos_s_lig)
        arr_p_proj = np.dot(m_ndi2proj, self.arr_p_ndi.T).T
        pre_q_proj = fun_proj_p(pos_s_proj, arr_p_proj)
        return pre_q_proj


class DataSamps:
    def __init__(self, path_file: str):
        self.path_file = path_file
        self.list_samps = self.init_list_samps()

    def __len__(self):
        return len(self.list_samps)

    def init_s_lig(self, pos_s_proj, mat_pad2proj):
        DataSample = self.__getitem__(0)
        m_lig2pad = np.dot(np.linalg.inv(DataSample.m_pad2ndi),
                           DataSample.m_lig2ndi)
        m_lig2proj = np.dot(mat_pad2proj, m_lig2pad)
        pos_s_lig = np.dot(np.linalg.inv(m_lig2proj), pos_s_proj)
        return pos_s_lig

    def init_list_samps(self):
        with open(self.path_file, 'r') as file:
            list_samps = []
            data_samp = ""
            for item, file_line in enumerate(file):
                if file_line == "},\n":
                    data_samp += "}"
                    ls_samp = data_samp.split("},{")
                    for k, file_name in enumerate(ls_samp):
                        ls_samp[k] = file_name.replace("{", "").replace("}", "")
                    list_samps.append(ls_samp)
                    data_samp = ""
                else:
                    file_line = file_line.replace("\n", "")
                    data_samp += file_line
        return list_samps

    def __getitem__(self, item):
        m_lig2ndi, m_pad2ndi, arr_p_ndi, arr_q_proj = calList2Array(self.list_samps[item])
        DataSamp_ = DataSamp(m_lig2ndi, m_pad2ndi, arr_p_ndi, arr_q_proj)
        return DataSamp_

    def fun_pre_p_q_proj(self, pos_s_lig, mat_pad2proj, ls_ids):
        DataSample = self.__getitem__(ls_ids[0])
        pre_q_proj = DataSample.pre_q_with_s_lig(pos_s_lig, mat_pad2proj)
        arr_q_proj = DataSample.arr_q_proj
        if len(ls_ids) <= 1:
            return pre_q_proj, arr_q_proj
        else:
            for item in range(1, len(ls_ids)):
                DataSample_ = self.__getitem__(ls_ids[item])
                pre_q_proj_ = DataSample_.pre_q_with_s_lig(pos_s_lig, mat_pad2proj)
                pre_q_proj = np.concatenate((pre_q_proj, pre_q_proj_), axis=0)
                arr_q_proj = np.concatenate((arr_q_proj, DataSample_.arr_q_proj), axis=0)
        return pre_q_proj, arr_q_proj

    def fun_opt_p_q_proj(self, pos_s_lig, mat_pad2proj, ls_ids):
        DataSample = self.__getitem__(ls_ids[0])
        pre_q_proj = DataSample.pre_q_with_s_lig(pos_s_lig, mat_pad2proj)
        arr_q_proj = DataSample.arr_q_proj
        if len(ls_ids) <= 1:
            return pre_q_proj, arr_q_proj
        else:
            for item in range(1, len(ls_ids)):
                DataSample_ = self.__getitem__(ls_ids[item])
                pre_q_proj_ = DataSample_.pre_q_with_s_lig(pos_s_lig, mat_pad2proj)
                arr_q_proj_ = DataSample_.arr_q_proj
                pre_q_proj = np.concatenate((pre_q_proj, pre_q_proj_), axis=0)
                arr_q_proj = np.concatenate((arr_q_proj, arr_q_proj_), axis=0)
            return pre_q_proj, arr_q_proj


if __name__ == '__main__':
    path_file = "../datasets/train_zc/train_z.txt"
    path_json = "../datasets/train_zc/settings.json"
    with open(path_json, "r", encoding="utf-8") as f:
        content = json.load(f)

    # pos_s_Lig = np.array(content['lateralLightMatrix']).reshape(1, 3)
    # pos_s_Lig = np.concatenate((pos_s_Lig, np.ones((1, 1))), axis=1)
    # mat_proj2pad = np.array(content['lateralPadPoseMatrix']).reshape(4, 4)

    pos_s_Lig = np.array(content['positiveLightMatrix']).reshape(1, 3)
    pos_s_Lig = np.concatenate((pos_s_Lig, np.ones((1, 1))), axis=1)
    mat_proj2pad = np.array(content['positivePadPoseMatrix']).reshape(4, 4)

    DataSamps_ = DataSamps(path_file)
    pre_q_proj_, arr_q_proj_ = DataSamps_.fun_pre_p_q_proj(pos_s_Lig, mat_proj2pad)

    loss_ = pre_q_proj_ - arr_q_proj_
    print()
