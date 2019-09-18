import time
a=eval(input("请输入身高(m)："))
b=eval(input("请输入体重(kg)："))
i=b/a**2
print("您的BMI值约为{:.2f}".format(i))
who,nat="",""
if i<18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<=i<24:
    who,nat="正常","正常"
elif 24<=i<25:
    who,nat="正常","偏胖"
elif 25<=i<28:
    who,nat="偏胖","偏胖"
elif 28<=i<=30:
    who,nat="偏胖","肥胖"
else:
    who,nat="肥胖","肥胖"
print("国际标准为{},国内标准为{}".format(who,nat))
time.sleep(1)
