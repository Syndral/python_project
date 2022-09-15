

# 构建kdTree将特征空间划分
class KdTree:
    """
    定义结点
    value:节点值
    dimension：当前划分的维数
    left:左子树
    right:右子树
    """

    def __init__(self, value):
        self.value = value
        self.dimension = None  # 记录划分的维数
        self.left = None
        self.right = None

    def setValue(self, value):
        self.value = value

    # 类似Java的toString()方法
    def __str__(self):
        return str(self.value)

    def create_kdTree(dataIn, k, root, deep):
        """
        data:要划分的特征空间（即数据集）
        k:表示要选择k个近邻
        root:树的根结点
        deep:结点的深度
        """
        # 选择x(l)(即为第l个特征)为坐标轴进行划分，找到x(l)的中位数进行划分
        #     x_L = data[:,deep%k]        #这里选取第L个特征的所有数据组成一个列表
        # 获取特征值中位数，这里是难点如果numpy没有提供的话

        if (dataIn.shape[0] > 0):  # 如果该区域还有实例数据就继续
            dataIn = dataIn[dataIn[:, int(deep % k)].argsort()]  # numpy的array按照某列进行排序
            data1 = None;
            data2 = None
            # 拿取根据xL排序的中位数的数据作为该子树根结点的value
            if (dataIn.shape[0] % 2 == 0):  # 该数据集有偶数个数据
                mid = int(dataIn.shape[0] / 2)
                root = kd_tree(dataIn[mid, :])
                root.dimension = deep % k
                dataIn = np.delete(dataIn, mid, axis=0)
                data1, data2 = np.split(dataIn, [mid], axis=0)
                # mid行元素分到data2中，删除放到根结点中
            elif (dataIn.shape[0] % 2 == 1):
                mid = int((dataIn.shape[0] + 1) / 2 - 1)  # 这里出现递归溢出，当shape为(1,4)时出现，原因是np.delete时没有赋值给dataIn
                root = kd_tree(dataIn[mid, :])
                root.dimension = deep % k
                dataIn = np.delete(dataIn, mid, axis=0)
                data1, data2 = np.split(dataIn, [mid], axis=0)  # mid行元素分到data1中，删除放到根结点中
            # 深度加一
            deep += 1
            # 递归构造子树
            # 这里犯了严重错误，递归调用是将root传递进去，造成程序混乱，应该给None
            root.left = creat_kdTree(data1, k, None, deep)
            root.right = creat_kdTree(data2, k, None, deep)
        return root