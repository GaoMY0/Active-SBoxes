import time
from B_model import *

oldtime=time.time()
#参数设置
rounds=3                         #轮数
M=18

F(rounds,M)

print("求解时间")
newtime=time.time()
print(newtime-oldtime)