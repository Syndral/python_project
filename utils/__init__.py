import numpy as np


# 读取文件中的矩阵数据
def file2matrix(filename):
    fr = open(filename)
    returnMat = []
    for line in fr.readlines():
        line = line.strip().split('    ')
        returnMat.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
    returnMat = np.array(returnMat)
    return returnMat


# 数据归一化，避免数据各维度间的差异过大
def autoNorm(data):
    # 将data数据和类别拆分
    data, label = np.split(data, [3], axis=1)
    min_val = data.min(0)  # data各列的最小值
    max_val = data.max(0)  # data各列的最大值
    ranges = max_val - min_val  # 各列阈值大小
    normDataSet = np.zeros(np.shape(data))
    m = data.shape[0]  # shape[0] 行数
    # tile函数将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = data - np.tile(min_val, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    # 拼接
    normDataSet = np.hstack((normDataSet, label))
    return normDataSet

