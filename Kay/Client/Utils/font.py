from PyQt5.QtGui import QFont, QFontDatabase
from pathlib import Path


def get_NotoSan_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Bold.otf'
    # font_path = r'D:\Skillup\2023_chatting\Kay\Client\view\static\noto-sans-kr\Noto_Sans_KR\NotoSansKR-Bold.otf'

    # 폰트 등록
    font_id = QFontDatabase.addApplicationFont(font_path)

    # 폰트 패밀리 이름 가져오기
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # 폰트 생성
    font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

    return font


# from PyQt5.QtGui import QFont, QFontDatabase
# from PyQt5.QtWidgets import QApplication, QLabel

# # 어플리케이션 생성
# app = QApplication([])

# # 폰트 파일 경로
# font_path = r"D:\Skillup\2023_chatting\Kay\Client\view\static\gfont\GmarketSansBold.otf"

# # 폰트 등록
# font_id = QFontDatabase.addApplicationFont(font_path)

# # 폰트 패밀리 이름 가져오기
# font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

# # 폰트 생성
# font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

# # 레이블 생성
# label = QLabel("새로운 폰트 적용 예제")
# label.setFont(font)  # 폰트 설정

# # 레이블 표시
# label.show()

# # 어플리케이션 실행
# app.exec()
