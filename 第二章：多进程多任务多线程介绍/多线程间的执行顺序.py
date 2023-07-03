import threading
import time

# 获取线程信息函数
def get_info():
    time.sleep(0.5)
    current_thread = threading.current_thread()
    print(current_thread)

# 创建线程
for i in range(10):
    sub_threed = threading.Thread(target=get_info)
    sub_threed.start()