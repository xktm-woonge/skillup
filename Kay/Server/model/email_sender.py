import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp = None

    def connect(self):
        self.smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.smtp.starttls()

    def send_email(self, sender_email, sender_password, receiver_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        body = MIMEText(message, 'plain')
        msg.attach(body)

        try:
            if not self.smtp:
                self.connect()

            self.smtp.login(sender_email, sender_password)
            self.smtp.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")

        except Exception as e:
            print("Error sending email:", str(e))

        finally:
            if self.smtp:
                self.smtp.quit()


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
    emailSender = EmailSender('smtp.naver.com', 587)
    emailSender.send_email("longguo0318@naver.com", "aaaabbbb", "sulkyungkim@naver.com", "test메일", message)