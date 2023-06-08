import socket
import threading
import random
import string
from Model.email_sender import EmailSender

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
    while True:
        # 接收客户端的消息
        message = client_socket.recv(1024).decode()

        if message.startswith("VERIFICATIONCODE"):
            # 解析注册请求消息
            _, email = message.split("|")
            # 处理邮箱验证码功能
            verification_code = generate_verification_code()
            print(f"Verification code for {email}: {verification_code}")

            emailSender = EmailSender(*smtp_info['naver'])
            emailSender.send_email("longguo0318@naver.com", "fydrnrlek318", email, "인증번호", verification_code)

            # 将用户名、邮箱和验证码保存到全局变量中
            user_data[email] = {'verification_code': verification_code}

            # 假设验证通过，发送注册成功响应
            response = "Registration successful"
            client_socket.sendall(response.encode())

        elif message.startswith("VERIFY"):
            # 解析邮箱验证码请求消息
            _, email, verification_code = message.split("|")

            # 检查验证码是否匹配
            if email in user_data and user_data[email]['verification_code'] == verification_code:
                # 验证通过，发送验证通过响应
                response = "Verification successful"
                client_socket.sendall(response.encode())
            else:
                # 验证不通过，发送验证失败响应
                response = "Verification failed"
                client_socket.sendall(response.encode())

        # elif message.startswith("VERIFICATIONCODE"):
        #     random_number = random.randint(100000, 999999)
        #     _, email = message.split("|")
        #     emailSender = EmailSender('smtp.navaer.com', 587)
        #     emailSender.send_email("longguo0318@naver.com", "fydrnrlek318", email, "인증번호", random_number)

        else:
            # 处理其他聊天功能
            # ...
            pass

    # 关闭客户端连接
    client_socket.close()

# 示例用法（续）
def start_server():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP地址和端口号
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)
    # 开始监听连接
    server_socket.listen(5)

    print("Server started. Listening for connections...")

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")

        # 创建新线程处理客户端连接
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()

# 生成验证码的示例函数
def generate_verification_code():
    # 生成6位随机验证码
    return ''.join(random.choices(string.digits, k=6))

start_server()
