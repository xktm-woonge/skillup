from PyQt5.QtGui import QFont, QFontDatabase
from pathlib import Path


NOTOSAN_FONT_BOLD = None
NOTOSAN_FONT_BLACK = None
NOTOSAN_FONT_THIN = None
NOTOSAN_FONT_REGULAR = None
NOTOSAN_FONT_LIGHT = None
NOTOSAN_FONT_MEDIUM = None

def Init():
    global NOTOSAN_FONT_BOLD, NOTOSAN_FONT_BLACK, NOTOSAN_FONT_THIN, \
        NOTOSAN_FONT_REGULAR, NOTOSAN_FONT_LIGHT, NOTOSAN_FONT_MEDIUM
    NOTOSAN_FONT_BOLD = get_NotoSan_bold_font()
    NOTOSAN_FONT_BLACK = get_NotoSan_black_font()
    NOTOSAN_FONT_THIN = get_NotoSan_thin_font()
    NOTOSAN_FONT_REGULAR = get_NotoSan_regular_font()
    NOTOSAN_FONT_LIGHT = get_NotoSan_light_font()
    NOTOSAN_FONT_MEDIUM = get_NotoSan_medium_font()

def get_NotoSan_bold_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Bold.otf'

    # 폰트 등록
    font_id = QFontDatabase.addApplicationFont(font_path)

    # 폰트 패밀리 이름 가져오기
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # 폰트 생성
    font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

    return font

def get_NotoSan_black_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Black.otf'

    # 폰트 등록
    font_id = QFontDatabase.addApplicationFont(font_path)

    # 폰트 패밀리 이름 가져오기
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # 폰트 생성
    font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

    return font

def get_NotoSan_thin_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Thin.otf'

    # 폰트 등록
    font_id = QFontDatabase.addApplicationFont(font_path)

    # 폰트 패밀리 이름 가져오기
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # 폰트 생성
    font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

    return font

def get_NotoSan_regular_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Regular.otf'

    # 폰트 등록
    font_id = QFontDatabase.addApplicationFont(font_path)

    # 폰트 패밀리 이름 가져오기
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # 폰트 생성
    font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

    return font

def get_NotoSan_light_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Light.otf'

    # 폰트 등록
    font_id = QFontDatabase.addApplicationFont(font_path)

    # 폰트 패밀리 이름 가져오기
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # 폰트 생성
    font = QFont(font_family, 12)  # 폰트 패밀리와 크기 설정

    return font

def get_NotoSan_medium_font():
    # 폰트 파일 경로
    font_path = f'{str(Path(__file__).parents[1])}/view/static/noto-sans-kr/Noto_Sans_KR/NotoSansKR-Medium.otf'

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
