from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


window_height = 10
begin_width_spacing = 20
begin_height_spacing = 16
icon_width = 40
icon_height = 40
text_width_spacing = 12
text_height_spacing = 12
triangle_width = 6
triangle_height = 10
triangle_height_spacing = 10
text_min_width = 0
min_width = 0
text_max_width = 0
real_width = 0
text_height = 0

class MyWidget(QWidget):
    def __init__(self, parent=None, data='', type_mess=0):
        super(MyWidget, self).__init__(parent)
        self.setObjectName('MyWidget')
        self.user_chat_content = data
        self.init_data()

    def init_data(self):
        self.font = QFont()
        self.font.setFamily("Arial")  # 폰트 설정
        self.font.setPointSize(12)
        self.metrics = QFontMetrics(self.font)
        self.text_min_width = max(self.metrics.width("A") * 2 + begin_height_spacing * 1.5 - text_width_spacing, 0)
        self.min_width = begin_width_spacing + icon_width + triangle_width + text_width_spacing + text_width_spacing + icon_width + begin_width_spacing
        self.text_max_width = self.width() - self.min_width
        self.real_width = self.metrics.width(self.user_chat_content)
        if self.real_width < self.text_max_width:
            self.text_max_width = self.real_width
        self.text_height = max(text_height_spacing + self.metrics.height() + text_height_spacing, triangle_height_spacing + triangle_height + triangle_height_spacing)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(self.font)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 0))

        # 말풍선 그리기 로직 추가 예정

        # 텍스트 그리기
        text_rect = QRect(begin_width_spacing + icon_width + triangle_width + text_width_spacing, begin_height_spacing, self.text_max_width, self.text_height)
        painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignTop, self.user_chat_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget(data='안녕하세요, 이것은 테스트 메시지입니다.', type_mess=0)
    widget.show()
    sys.exit(app.exec_())
