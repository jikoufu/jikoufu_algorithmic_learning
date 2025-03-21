import socket

def start_client(host='127.0.0.1', port=65432):
    # 创建一个TCP/IP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 连接到服务器
        client_socket.connect((host, port))
        print(f"已连接到服务器 {host}:{port}")

        while True:
            # 用户输入消息
            message = input("请输入要发送的消息（输入 'exit' 断开连接）: ")
            if message.lower() == 'exit':
                print("断开连接...")
                break

            # 发送数据
            client_socket.sendall(message.encode('utf-8'))
            print(f"发送消息: {message}")

            # 接收响应
            data = client_socket.recv(1024)
            print(f"收到响应: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()