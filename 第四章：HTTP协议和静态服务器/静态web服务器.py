# 1. 编写一个TCP的服务端流程
# 创建socket
import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定ip地址和端口
tcp_server_socket.bind(("", 1334))
# 设置监听
tcp_server_socket.listen(128)

# 循环接收客户端的请求
while True:
    # 2. 获取浏览器发送的http请求报文数据
    # 建立链接
    client_socket, client_addr = tcp_server_socket.accept()
    # 获取浏览器请求信息
    client_request_data = client_socket.recv(1024).decode()
    print(client_request_data)
    # 读取用户请求网址
    request_data = client_request_data.split(" ")
    # print(request_data)
    request_path = request_data[1]

    # 找不到路径，404
    if request_path == "/":
        request_path = "/index.html"


    # 3. 读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
    try:
        with open("./"+request_path, "rb") as f:
            file_data = f.read()
    except Exception as e:
        # 应答行
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 应答头
        response_header = "Server:pwb\r\n"
        # 应答体
        response_body = "404 Not Found !!"
        response_data = (response_line + response_header).encode() + b"\r\n" + response_body.encode()
        client_socket.send(response_data)
    else:
        # 应答行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 应答头
        response_header = "Server:pwb\r\n"
        # 应答体
        response_body = file_data
        response_data = (response_line + response_header).encode() + b"\r\n" + response_body

        client_socket.send(response_data)
        # 4. HTTP相应报文数据发送以后，关闭服务于客户端的套接字

    finally:
        client_socket.close()
