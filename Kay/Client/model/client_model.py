# ./model/client_model.py

import socket
import threading
import time
import json

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *

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
                if self.socket is None or self.socket.fileno() == -1:
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.connect((self.host, self.port))
                    self.is_connected = True
                    clmn.HLOG.info("Connected to the server")

                    # 별도의 스레드에서 메시지 수신 처리
                    receive_thread = threading.Thread(target=self.receive_messages)
                    receive_thread.start()

            except ConnectionRefusedError:
                clmn.HLOG.info("Connection refused, retrying...")
                time.sleep(self.reconnect_delay)

            except TimeoutError as e:
                clmn.HLOG.info("Connection timed out:", str(e))
                time.sleep(self.reconnect_delay)

    def send_message(self, message):
        with self.lock:
            if self.is_connected:
                self.socket.sendall(message.encode())
                clmn.HLOG.info(f'{message} 전송')

    def receive_messages(self):
        while self.is_connected:
            try:
                data = self.socket.recv(1024)
                if data:
                    message = data.decode()
                    clmn.HLOG.info(f'{message} 수신')
                    self.message_callback(message)
                else:  # 소켓이 정상적으로 닫힌 경우
                    self.is_connected = False
                    self.socket.close()
                    self.socket = None
                    self.reconnect()
            except (ConnectionResetError, ConnectionAbortedError):
                clmn.HLOG.info("Connection reset by peer")
                self.is_connected = False
                self.socket = None
                self.reconnect()

    def reconnect(self):
        if self.socket is not None:
            try:
                self.socket.close()
            except Exception as e:
                clmn.HLOG.error(f"Error closing socket: {str(e)}")
            self.socket = None
        self.is_connected = False
        clmn.HLOG.info("Reconnecting...")
        self.connect()
        
    # def request_verification_code(self, email):
    #     # 인증 요청 메시지 작성
    # message = json.dumps({
    #     "command": "VERIFICATIONCODE",
    #     "email": email
    # })
    # # 인증 요청 전송
    # self.send_message(message)

# def verify_verification_code(self, email, verification_code):
#     message = json.dumps({
#         "command": "VERIFY",
#         "email": email,
#         "verification_code": verification_code
#     })
#     self.send_message(message)

# def register_user(self, email, password, salt):
#     # 서버에 등록 요청을 보내고, 서버의 응답 결과를 반환
#     message = json.dumps({
#         "command": "REGISTER",
#         "email": email,
#         "password": password,
#         "salt": salt
#     })
#     self.send_message(message)

# def login(self, email, password):
#     message = json.dumps({
#         "command": "LOGIN",
#         "email": email,
#         "password": password
#     })
#     self.send_message(message)

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
                clmn.HLOG.info("Connection closed")
