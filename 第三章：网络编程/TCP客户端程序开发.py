import socket

# 创建客户端对象
# socket.AF_INET为IPv4地址
# socket。SOCK_STREAM为TCP的通讯协议
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 和服务端建立连接
tcp_client_socket.connect(("192.168.0.115",8888))

# 发送数据
tcp_client_socket.send('你可以收到我的信息吗？'.encode(encoding='utf-8'))

# 接收数据
recv_data = tcp_client_socket.recv(1024)
print(recv_data.decode)

# 关闭客户端连接
tcp_client_socket.close()
