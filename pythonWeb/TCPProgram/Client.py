import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print('客户端发出：{}'.format(data))
    print("客户端收到：{}".format(s.recv(1024).decode('utf-8')))
s.send(b'exit')
s.close()