def select_sort(alist):
    '''选择排序'''

    # 列表长度
    n = len(alist)
    # 控制轮数
    for j in range(0, n - 1):
        # 假定的最小值的下标
        min_index = j
        # 控制比较次数
        for i in range(j + 1, n):
            # 进行比较，获取最小值
            if alist[i] < alist[min_index]:
                min_index = i
            # 如果假定的最小值的下标发生了变化，那么我们就进行交换
        if min_index != j:
            alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    alist = [1,5,7,2,4,6]
    select_sort(alist)
    print(alist)
