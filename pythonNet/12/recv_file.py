from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)

f = open('cxk.jpg','wb')

#　接受内容写入文件
while True:
    data = c.recv(1024) #　字节串
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
