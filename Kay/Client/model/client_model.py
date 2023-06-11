# model/client_model.py
import socket
import threading
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.is_connected = False
        self.lock = threading.Lock()
        self.reconnect_delay = 5  # 重新连接
        
    def connect(self):
        while not self.is_connected:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                self.is_connected = True
                print("Connected to the server")

                # 在单独的线程中处理接收消息
                receive_thread = threading.Thread(target=self.receive_messages)
                receive_thread.start()
            except ConnectionRefusedError:
                print("Connection refused, retrying...")
                time.sleep(self.reconnect_delay)

    def send_message(self, message):
        with self.lock:
            if self.is_connected:
                self.socket.sendall(message.encode())

    def receive_messages(self):
        while self.is_connected:
            try:
                data = self.socket.recv(1024)
                if data:
                    message = data.decode()
                    # 处理接收到的消息，例如打印或者进行其他操作
                    self.message_received.emit(message)
            except ConnectionResetError:
                print("Connection reset by peer")
                self.close()
                self.reconnect()

    def reconnect(self):
        self.is_connected = False
        self.socket.close()
        print("Reconnecting...")
        self.connect()

    def request_verification_code(self, email):
        # 构建验证请求消息
        message = f"VERIFICATIONCODE|{email}"
        # 发送验证请求
        ret = self.send_message(message)
        print(ret)

    def verify_verification_code(self, email, verification_code):
        message = f"VERIFY|{email}|{verification_code}"
        ret = self.send_message(message)
        print(ret)

    def register_user(self, username, password, email, verification_code):
        # 发送请求给服务器，进行用户注册
        # 返回服务器的响应结果
        pass

    def close(self):
        with self.lock:
            if self.is_connected:
                self.is_connected = False
                self.socket.close()
                print("Connection closed")
