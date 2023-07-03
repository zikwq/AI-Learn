# 流程
# 1. 创建服务端套接字对象
# 2. 绑定IP地址和端口
# 3. 设置监听
# 4. 等待接受客户端的连接请求
# 5. 接收数据
# 6. 发送数据
# 7. 关闭套接字

# 导入socket模块
import socket

# 创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定IP地址和端口，如果bind中ip地址设置为“”，默认为本机ip地址
tcp_server_socket.bind(("",8888))

# 设置监听 128:代表服务端等待排队连接的最大数量
tcp_server_socket.listen(128)

# 等待接受客户端的连接请求，accept阻塞等待，返回一个用以和客户端通信的socket，客户端地址
conn_socket,ip_port = tcp_server_socket.accept()
print("客户端地址：",ip_port)


# 接收数据
recv_data = tcp_server_socket.recv(1024)
print("客户端：",recv_data.decode())

# 发送数据
tcp_server_socket.send("服务端收到！".encode('uft-8'))

# 关闭套接字
conn_socket.close()
tcp_server_socket.close()