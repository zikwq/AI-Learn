### 1、网络介绍
#### 1.1 网络的概念
1. 将具有独立功能的多台计算机通过通信线路和通信设备连接起来，在网络管理软件及网络通信协议下，实现资源共享和信息传递的虚拟平台
2. 编写基于网络通信的软件或程序，通常来说是网络编程


### 2、 IP地址的介绍
#### 2.1 IP地址概念：
1. IP地址是分配给网络设备上网使用的数字标签，它能够表示网络中唯一的一台设备


### 3、 端口和端口号的介绍
#### 3.1 概念
1. 其实每一个软件运行都会有一个端口，他的定义是传输数据的通道，好比教室的门，就是数据传输的必经之路
2. 每一个端口都会有一个端口号，操作系统为了统一管理这些端口，就对端口进行了编号，这就是端口号，端口号实际上就是一个数字，好比我们生活中的门牌号
3. 端口号有65536个
4. 最终的通信流程，通过ip地址找到对应的设配，通过端口号找到对应的端口，然后通过端口把数据给应用程序

#### 3.2 端口号的分类
1. 端口号可以分为知名端口号和动态端口号
2. 知名端口号：是指0到1023，比如21端口分配给FTP，25端口分配给SMTP（简单邮件传输协议），80端口分配给HTTP服务
3. 动态端口号：是从1024到65536，如果程序员设计程序没有设置一个端口，操作系统会在动态端口号中随机生成一个给开发的应用程序使用
4. 