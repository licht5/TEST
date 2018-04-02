
# 在这里如果直接使用打印函数，会出现"b''"的情况，解决办法就是将要打印的信息用b'信息'的方式表示出来，如第九行所示。
import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
mess=b'thanks '
while  True:
    c,addr=s.accept()
    print("get connection from",addr)
    c.send(mess)
    c.close()