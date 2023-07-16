# ./model/client_model.py

import socket
import threading
import time

class Client:
    def __init__(self, host, port, message_callback):
        self.host = host
        self.port = port
        self.socket = None
        self.is_connected = False
        self.lock = threading.Lock()
        self.reconnect_delay = 5
        self.message_callback = message_callback
        
    def connect(self):
        while not self.is_connected:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                self.is_connected = True
                print("Connected to the server")

                # 별도의 스레드에서 메시지 수신 처리
                receive_thread = threading.Thread(target=self.receive_messages)
                receive_thread.start()

            except ConnectionRefusedError:
                print("Connection refused, retrying...")
                time.sleep(self.reconnect_delay)

            except TimeoutError as e:
                print("Connection timed out:", str(e))
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
                    self.message_callback(message)
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
        # 인증 요청 메시지 작성
        message = f"VERIFICATIONCODE|{email}"
        # 인증 요청 전송
        self.send_message(message)

    def verify_verification_code(self, email, verification_code):
        message = f"VERIFY|{email}|{verification_code}"
        self.send_message(message)

    def register_user(self, email, password, salt):
        # 서버에 등록 요청을 보내고, 서버의 응답 결과를 반환
        # ...
        message = f"REGISTER|{email}|{password}|{salt}"
        self.send_message(message)
        
    def login(self, email, password):
        message = f"LOGIN|{email}|{password}"
        self.send_message(message)
    
    def is_connected(self):
        return self.is_connected

    def close(self):
        with self.lock:
            if self.is_connected:
                self.is_connected = False
                self.socket.close()
                print("Connection closed")
