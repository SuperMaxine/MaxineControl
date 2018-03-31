#-*- coding: UTF-8 -*-
import socket
import sys
import os

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建Socket连接（TCP）
    print('Socket Created')

    try:
        sock.bind(('127.0.0.1', 8004))  # 配置Socket，绑定IP地址和端口号
    except socket.error as e:
        print('Bind Failed...', e)
        sys.exit(0)

    sock.listen(5)  # 设置最大允许连接数，各连接和Server的通信遵循FIFO原则

    while True:  # 循环轮询Socket状态，等待访问
        try:
            conn, addr = sock.accept()
            while True:
                data = conn.recv(1024)
                print('Get value ' + data+'\n\n')
                try:
                    if data[0:2]=='cd ':#不成功
                        os.chdir(data[3::])#不成功
                        result="chdir->"+data[3::]#不成功
                    else:
                        result=os.popen(data).read()
                    #print('command running')
                    print(result)
                    conn.sendall(result)
                    print('result sended')
                    result=''
                except:
                    print('command running error')
                
                if not data:
                    print('Exit Server'+'\n\n')
                    break
                conn.sendall(result)
        except:
            print('client disconnected')
        conn.close()  # 当一个连接监听循环退出后，连接可以关掉
    sock.close()
