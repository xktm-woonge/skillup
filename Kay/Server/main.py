# ./server/main.py
import socket
import threading
import random
import string
from model.email_sender import EmailSender

# 나중에 DB로 추가해야 됨
user_data = {}

smtp_info = {      
    'gmail': ('smtp.gmail.com', 587),
    'naver': ('smtp.naver.com', 587),
    'daum': ('smtp.daum.net', 465),
    'hanmail': ('smtp.daum.net', 465),
    'nate': ('smtp.mail.nate.com', 465),
    'outlook': ('smtp.outlook.com', 587),
}

def handle_client_connection(client_socket):
    try:
        while True:
            # 수신한 클라이언트 메시지 받기
            message = client_socket.recv(1024).decode()
            
            if not message:
                raise ConnectionError("Client disconnected")

            if message.startswith("VERIFICATIONCODE"):
                # 등록 요청 메시지 분석
                _, email = message.split("|")
                # 이메일 인증코드 생성
                verification_code = generate_verification_code()
                print(f"Verification code for {email}: {verification_code}")

                email_sender = EmailSender(*smtp_info['gmail'])
                email_sent = email_sender.send_email("endteamchat@gmail.com", 
                                        "fxerdbpuijwurack", 
                                        email, 
                                        "채팅 프로그램 인증번호", 
                                        verification_code)

                # 이메일 전송에 성공한 경우
                if email_sent:
                    # 사용자 데이터에 이메일과 인증코드 저장
                    user_data[email] = {'verification_code': verification_code}
                    response = "Send email success"
                else:
                    response = "Send email fail"

                client_socket.sendall(response.encode())

            elif message.startswith("VERIFY"):
                # 이메일 인증코드 확인 요청 메시지 분석
                _, email, verification_code = message.split("|")

                # 인증코드 일치 여부 확인
                if email in user_data and user_data[email]['verification_code'] == verification_code:
                    # 인증 성공 응답 보내기
                    response = "Verification successful"
                    client_socket.sendall(response.encode())
                else:
                    # 인증 실패 응답 보내기
                    response = "Verification failed"
                    client_socket.sendall(response.encode())

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
    server_address = ('192.168.35.167', 8000)
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

# 인증 코드 생성 예시 함수
def generate_verification_code():
    # 6자리 임의의 인증 코드 생성
    return ''.join(random.choices(string.digits, k=6))


if __name__ == "__main__":
    start_server()