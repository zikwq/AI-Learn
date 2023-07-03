def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    # 计数
    count = 0
    # 控制比较轮数
    for j in range(0, n - 1):
        # 控制每一轮的比较次数
        for i in range(0, n - j - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            break


alist = [3, 5,4,7,9]
bubble_sort(alist)
print("冒泡排序：", alist)

