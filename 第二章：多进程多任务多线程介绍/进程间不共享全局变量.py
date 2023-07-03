import multiprocessing

# 定义一个全局变量
my_list = []

# 写入数据
def write_data():
    for i in range(3):
        my_list.append(i)
        print("add:",i)
    print(my_list)

# 读取数据
def read_data():
    print(my_list)

# 创建进程对象
write_process = multiprocessing.Process(target = write_data)
read_process = multiprocessing.Process(target = read_data)


# 启动进程任务
write_process.start()
read_process.start()