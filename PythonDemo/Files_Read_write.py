write=open("1.txt",'w')
ls=['1','2','3']
for i in ls:
    print(i)
    write.write(i)
write.close()
write1=open("1.txt",'a')
text="python大法好!!!hhh"
write1.write(text)
write1.close()
read=open("read.txt",encoding='utf-8')
txt=read.readlines()
for line in txt:
    print(line)
    
