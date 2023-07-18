try:
    from model import *
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model import *
    from utils import *


class AuthController:
    def __init__(self):
        self.user_data = {}

    def handle_verification_code_request(self, message, client_socket):
        # 등록 요청 메시지 분석
            _, email = message.split("|")
            
            if check_user(email):
                response = "The account has already been registered"
            else:
                # 이메일 인증코드 생성
                verification_code = EmailSender.generate_verification_code()
                print(f"Verification code for {email}: {verification_code}")

                email_sender = EmailSender()
                email_sent = email_sender.send_email(email, 
                                                    "채팅 프로그램 인증번호", 
                                                    verification_code)

                # 이메일 전송에 성공한 경우
                if email_sent:
                    # 사용자 데이터에 이메일과 인증코드 저장
                    self.user_data[email] = {'verification_code': verification_code}
                    response = "VERIFICATIONCODE SUCCESS"
                else:
                    response = "VERIFICATIONCODE FAIL"

            client_socket.sendall(response.encode())

    def handle_verify(self, message, client_socket):
        # 이메일 인증코드 확인 요청 메시지 분석
        _, email, verification_code = message.split("|")

        # 인증코드 일치 여부 확인
        if email in self.user_data and self.user_data[email]['verification_code'] == verification_code:
            # 인증 성공 응답 보내기
            response = "VERIFY SUCCESS"
        else:
            # 인증 실패 응답 보내기
            response = "VERIFY FAIL"
            
        client_socket.sendall(response.encode())

    def handle_register(self, message, client_socket):
        # Receive the hashed password and salt from the client
        _, email, hashed_password, salt = message.split("|")
        
        # Store the hashed password and salt in the database
        store_in_database(email, hashed_password, salt)
        response = "REGISTER SUCCESS"
        
        client_socket.sendall(response.encode())

    def handle_login(self, message, client_socket):
        _, email, userPassword = message.split("|")
                
        if get_userInfo(email):
            _, dbPassword, salt = get_userInfo(email)
            hashedPassword = hash_password(userPassword, salt)
            
            if dbPassword == hashedPassword:
                response = "LOGIN SUCCESS"
            else:
                response = "LOGIN FAIL"
        else:
            response = "non-existent email"
            
        client_socket.sendall(response.encode())
