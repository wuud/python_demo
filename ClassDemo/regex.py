import re
import time
#匹配不成功，会报错
r=re.compile(r'(\d+\w+)\.(\w+)');
print(r.match("123dsf.hjdk").groups())

t =(time.strftime("%H:%M:%S",time.gmtime()))
print(t)
te = re.compile(r'(\d{2})\:(\d{2})\:(\d{2})')
print(te.match(t).groups())