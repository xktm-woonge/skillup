smtp_info = {      
    'gmail.com': ('smtp.gmail.com', 587),
    'naver.com': ('smtp.naver.com', 587),
    'daum.net': ('smtp.daum.net', 465),
    'hanmail.net': ('smtp.daum.net', 465),
    'nate.com': ('smtp.mail.nate.com', 465),
    'outlook.com': ('smtp.outlook.com', 587),
    }

a, b = smtp_info['gmail.com']
print(a, b)

print(type(*smtp_info['gmail.com']))