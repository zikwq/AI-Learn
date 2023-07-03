import time
import threading


a = 10

# 打印字符
def coding(num, name):
    for i in range(num):
        print(name)
        print("coding")
        time.sleep(0.2)

def music(num): 
    for i in range(num):
        print("music")
        time.sleep(0.2)

# 使用进程类创建进程对象
# num为形参，3为实参
coding_process = threading.Thread(target=coding, args=(3, "传参"))
music_process = threading.Thread(target=music, kwargs={"num": 3})

# 启动进程执行程序
coding_process.start()
music_process.start()
