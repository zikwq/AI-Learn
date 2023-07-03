# 如果a+b+c=1000，且a^2+b^2=c^2,求得a、b、c的值
# 预计耗费20分钟
# 算法二耗费0.5秒
import time

start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
            # for c in range(0,1001)
            c = 1000 - a -b
            if a**2+b**2==c**2 and a+b+c==1000:
                print("a:",a)
                print("b:",b)
                print("c:",c)
end_time = time.time()
cost_time = end_time - start_time


print("耗费时间：",cost_time)