from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MessageBubble(QWidget):
    def __init__(self, timestamp, text, sender, parent=None):
        super(MessageBubble, self).__init__(parent)
        self.timestamp = timestamp
        self.text = text
        self.sender = sender  # True if the user sent the message, False otherwise
        self.initUI()

    def initUI(self):
        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(12)
        self.metrics = QFontMetrics(self.font)
        self.calculateDimensions()
        self.setMinimumSize(self.width(), self.height())
        self.update()

    def calculateDimensions(self):
        # 텍스트의 최대 너비를 현재 위젯의 너비로 설정하거나, 특정 최대 값으로 제한할 수 있습니다.
        # self.text_max_width를 여기에서 계산하거나 설정합니다.
        self.text_max_width = self.width() - 40  # 여백을 고려하여 너비를 설정합니다.
        text_rect = self.metrics.boundingRect(0, 0, self.text_max_width, 10000, Qt.TextWordWrap, self.text)
        self.text_height = text_rect.height()
        self.bubble_width = max(text_rect.width() + 20, 100)  # 텍스트 너비에 따라 말풍선 너비를 조정합니다.
        self.bubble_height = self.text_height + 20  # 텍스트 높이에 따라 말풍선 높이를 조정합니다.

    def sizeHint(self):
        # 말풍선 위젯에 대한 크기 제안을 반환합니다.
        return QSize(self.bubble_width, self.bubble_height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.font)

        # Set colors based on who sent the message
        if self.sender:  # If the user sent the message
            bubble_color = QColor("#800080")  # Purple
            text_color = QColor("#FFFFFF")  # White
        else:  # If someone else sent the message
            bubble_color = QColor("#D3D3D3")  # Light Gray
            text_color = QColor("#000000")  # Black

        # Paint the bubble
        painter.setBrush(bubble_color)
        painter.setPen(Qt.NoPen)
        rect = self.rect().adjusted(5, 5, -5, -5)
        painter.drawRoundedRect(rect, 10, 10)

        # Paint the text
        painter.setPen(text_color)
        text_rect = QRect(rect.left() + 10, rect.top() + 10, rect.width() - 20, rect.height() - 20)
        painter.drawText(text_rect, Qt.AlignLeft | Qt.TextWordWrap, self.text)

        # Paint the tail of the bubble
        # The tail direction will be based on who sent the message
        # This is a simple example and should be adjusted according to your UI design
        tail_start = QPoint(rect.right() - 15, rect.bottom()) if self.sender else QPoint(rect.left() + 15, rect.bottom())
        tail_mid = QPoint(rect.right(), rect.bottom() + 10) if self.sender else QPoint(rect.left(), rect.bottom() + 10)
        tail_end = QPoint(rect.right() - 30, rect.bottom()) if self.sender else QPoint(rect.left() + 30, rect.bottom())
        tail_polygon = QPolygon([tail_start, tail_mid, tail_end])
        painter.drawPolygon(tail_polygon)



# Test the widget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    bubble_user = MessageBubble("12:00", "Hi, this is a test message from user.", True)
    bubble_other = MessageBubble("12:01", "Hi, this is a test message from someone else.", False)
    bubble_user.show()
    bubble_other.show()
    sys.exit(app.exec_())
