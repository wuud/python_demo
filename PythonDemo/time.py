import time
#获得当前时间戳
print('time():',time.time())

#获得格式化的日期
print('ctime():',time.ctime())

#获得一个时间元组，可以用来格式化
t=time.gmtime()
print("gmtime():",t)

#格式化时间，需要上一步作为基础
t1=time.strftime("%Y-%m-%d %H:%M:%S",t)
print("strftime(%Y-%m-%d %H:%M:%S):",t1)

#strftime与strptime是一对相反作用的函数
#strftime可以把struct_time元组格式化，而strptime则把格式化的时间变为struct_time元组
gettime=time.strptime(t1,"%Y-%m-%d %H:%M:%S")
print(gettime)

#将格式化的时间变为时间戳，需要上一步作为基础
newtime=time.mktime(gettime)
print(newtime)
