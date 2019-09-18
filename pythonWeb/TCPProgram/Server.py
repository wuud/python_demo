import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print("Waiting for connection...")
def tcplink(sock,addr):
    sock.send(b'welcome')
    while True:
        data=sock.recv(1024)
        print('服务端收到：{}'.format(data))
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        s=("hello,%s" %data.decode('utf-8')).encode('utf-8').upper()
        sock.send(s)
        print("服务端发出：{}".format(s))
    sock.close
    print("Connection from {} close".format(addr))
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

