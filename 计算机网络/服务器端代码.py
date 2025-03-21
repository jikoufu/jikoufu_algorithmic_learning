import socket
import threading

def handle_client(conn, addr):
    with conn:
        print(f"已连接到 {addr}")
        while True:
            # 接收数据
            data = conn.recv(1024)
            if not data:
                print(f"客户端 {addr} 已断开连接")
                break
            message = data.decode('utf-8')
            print(f"收到来自 {addr} 的消息: {message}")

            # 发送响应
            response = input("请输入要发送给客户端的消息: ")
            conn.sendall(response.encode('utf-8'))
            print(f"发送消息: {response}")

def start_server(host='127.0.0.1', port=65432):
    # 创建一个TCP/IP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 绑定套接字到指定的地址和端口
        server_socket.bind((host, port))
        # 监听连接
        server_socket.listen()
        print(f"服务器正在 {host}:{port} 上监听...")

        while True:
            # 接受客户端连接
            conn, addr = server_socket.accept()
            # 创建一个新线程来处理客户端连接
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()