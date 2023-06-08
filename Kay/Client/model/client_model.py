import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_message(self, message):
        self.socket.sendall(message.encode())

    def receive_message(self):
        data = self.socket.recv(1024)
        return data.decode()
    
    def request_verification_code(self, email):
        # 构建验证请求消息
        message = f"VERIFICATIONCODE|{email}"
        # 发送验证请求
        self.socket.sendall(message.encode())

        # 接收并打印服务器的响应
        response = self.socket.recv(1024).decode()
        print(f"Server response: {response}")

    def verify_verification_code(self, email, verification_code):
        message = f"VERIFY|{email}|{verification_code}"
        self.socket.sendall(message.encode())

        response = self.socket.recv(1024).decode()
        print(f"Server response: {response}")

    def register_user(self, username, password, email, verification_code):
        # 发送请求给服务器，进行用户注册
        # 返回服务器的响应结果
        pass

    def close(self):
        self.socket.close()
