import time
import multiprocessing
import os

a = 10

# 打印字符
def coding(num, name):
    # 使用os.getppid()方法显示子进程的父进程编号
    print("coding父进程>>>%d" % os.getppid())

    # 使用os.getpid()获取子进程的当前进程编号
    print("coding>>>%d"%os.getpid())
    for i in range(num):
        print(name)
        print("coding")
        time.sleep(0.2)

def music(num):
    # 使用os.getppid()方法显示子进程的父进程编号
    print("music父进程>>>%d" % os.getppid())

    # 使用os.getpid()获取子进程的当前进程编号
    print("music>>>%d" % os.getpid())
    for i in range(num):
        print("music")
        time.sleep(0.2)


# 获取主进程的当前进程编号
print("主进程>>> %d" % os.getpid())

# 使用进程类创建进程对象
# num为形参，3为实参
coding_process = multiprocessing.Process(target=coding, args=(3, "传参"))
music_process = multiprocessing.Process(target=music, kwargs={"num": 3})

# 启动进程执行程序
coding_process.start()
music_process.start()
