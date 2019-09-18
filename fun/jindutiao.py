# -*- coding: utf-8 -*-
"""
Created on Sun May  6 22:33:49 2018

@author: wuu
"""

#TextProBarV3.py
import time
scale = 30
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i # "*"符号的数量在不断增多
    b = '.' * (scale - i) # "."符号数量在不断减少
    c = (i/scale)*100 # 进度百分比
    dur = time.perf_counter() - start # 花费的时间
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))

