import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string

"""
{      
'gmail': ('smtp.gmail.com', 587),
'naver': ('smtp.naver.com', 587),
'daum': ('smtp.daum.net', 465),
'hanmail': ('smtp.daum.net', 465),
'nate': ('smtp.mail.nate.com', 465),
'outlook': ('smtp.outlook.com', 587),
}
"""

class EmailSender:
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.sender_email = "endteamchat@gmail.com"
        self.sender_password = "fxerdbpuijwurack"
        self.smtp = None
        self.smtp_connection = False

    def connect(self):
        self.smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.smtp.starttls()

    def send_email(self, receiver_email, subject, content):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # HTML content and CSS style
        html = f"""
        <html>
        <head>
            <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f6f6f6;
            }}
            
            h2 {{
                color: #333333;
            }}
            
            p {{
                color: #666666;
            }}
            
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
            }}
            </style>
        </head>
        <body>
            <div class="container">
            <h2>아래 인증번호를 확인하십시오</h2>
            <p>{content}</p>
            </div>
        </body>
        </html>
        """

        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

        try:
            if not self.smtp:
                self.connect()
                self.smtp_connection = True

            self.smtp.login(self.sender_email, self.sender_password)
            self.smtp.sendmail(self.sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
            return True

        except Exception as e:
            print("Error sending email:", str(e))
            return False
            
        finally:

            if self.smtp and self.smtp_connection:
                self.smtp.quit()
                
    # 인증 코드 생성 예시 함수
    @staticmethod
    def generate_verification_code():
        # 6자리 임의의 인증 코드 생성
        return ''.join(random.choices(string.digits, k=6))


if __name__ == "__main__":
    message = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f5;
                    padding: 20px;
                }}

                h1 {{
                    color: #333333;
                }}

                .container {{
                    background-color: #ffffff;
                    border-radius: 5px;
                    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                }}

                .verification-code {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #ff3366;
                }}

                .message {{
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>验证码邮件</h1>
                <p>您的验证码是: <span class="verification-code">123456</span></p>
                <p class="message">请将此验证码输入到相应的位置完成验证。</p>
            </div>
        </body>
    </html>
    """
    emailSender = EmailSender('smtp.gmail.com', 587)
    emailSender.send_email("endteamchat@gmail.com", "fxerdbpuijwurack", "longguo0318@naver.com", "test메일", message)