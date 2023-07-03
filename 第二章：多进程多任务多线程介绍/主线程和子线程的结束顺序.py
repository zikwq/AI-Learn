import threading
import time


# 定义执行函数
def work():
    for i in range(10):
        print('工作中~~~')
        time.sleep(0.2)

# 创建进程对象
work_pross = threading.Thread(target=work)

# 守护主进程，当主进程结束后子进程直接销毁，不再执行子进程程序
work_pross.daemon = True

# 启动进程程序
work_pross.start()

time.sleep(1)
print('主进程执行完毕啦~')