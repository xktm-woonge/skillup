# ./server/main.py
import socket
import threading
from model import *
from controller import *


auth_controller = AuthController()

def handle_client_connection(client_socket):
    try:
        while True:
            # 수신한 클라이언트 메시지 받기
            message = client_socket.recv(1024).decode()
            
            if not message:
                raise ConnectionError("Client disconnected")

            if message.startswith("VERIFICATIONCODE"):
                auth_controller.handle_verification_code_request(message, client_socket)

            elif message.startswith("VERIFY"):
                auth_controller.handle_verify(message, client_socket)
                
            elif message.startswith("REGISTER"):
                auth_controller.handle_register(message, client_socket)
                
            elif message.startswith("LOGIN"):
                auth_controller.handle_login(message, client_socket)
                
            else:
                # 다른 채팅 기능 처리
                # ...
                print('test')

    except ConnectionError:
        print(f"Client {client_socket.getpeername()} disconnected.")

    finally:
        # 클라이언트 연결 종료
        client_socket.close()

# 예시 사용 (계속)
def start_server():
    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # IP 주소와 포트 번호 바인딩
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)
    # 연결 수신 대기 시작
    server_socket.listen(20)

    print("Server started. Listening for connections...")

    while True:
        # 클라이언트 연결 수락
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")

        # 클라이언트 연결을 처리하는 새로운 스레드 생성
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    start_server()