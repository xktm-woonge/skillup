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
        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(12)
        self.metrics = QFontMetrics(self.font)
        self.padding = 10
        self.bubble_padding = 20  # 텍스트와 말풍선 테두리 사이의 여백
        self.calculateDimensions()

    def calculateDimensions(self):
        # 텍스트의 최대 너비를 설정합니다.
        self.text_max_width = 200
        # 텍스트 렉트를 계산합니다.
        text_rect = self.metrics.boundingRect(0, 0, self.text_max_width, 10000, Qt.TextWordWrap, self.text)
        # 말풍선의 실제 크기를 계산합니다.
        self.bubble_width = text_rect.width() + self.bubble_padding * 2
        self.bubble_height = text_rect.height() + self.bubble_padding * 2 + self.metrics.height()
        self.setFixedSize(self.bubble_width, self.bubble_height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.font)

        # Set colors based on who sent the message
        bubble_color = QColor("#800080") if self.sender else QColor("#D3D3D3")
        text_color = QColor("#FFFFFF") if self.sender else QColor("#000000")
        time_color = QColor("#888888")

        # Paint the bubble
        painter.setBrush(bubble_color)
        painter.setPen(Qt.NoPen)
        bubble_rect = QRect(0, 0, self.bubble_width, self.bubble_height - self.metrics.height())
        painter.drawRoundedRect(bubble_rect, 10, 10)

        # Paint the text
        painter.setPen(text_color)
        text_rect = QRect(self.bubble_padding / 2, self.bubble_padding / 2, 
                          self.bubble_width - self.bubble_padding, 
                          self.bubble_height - self.bubble_padding - self.metrics.height())
        painter.drawText(text_rect, Qt.AlignLeft | Qt.TextWordWrap, self.text)

        # Paint the timestamp outside the bubble
        painter.setPen(time_color)
        time_rect = QRect(bubble_rect.left() if not self.sender else bubble_rect.right() - self.metrics.width(self.timestamp) - self.padding,
                          bubble_rect.bottom() - self.padding / 2, self.metrics.width(self.timestamp), self.metrics.height())
        painter.drawText(time_rect, Qt.AlignCenter, self.timestamp)

        # Paint the tail of the bubble
        tail_direction = 1 if self.sender else -1
        tail_start = QPoint(bubble_rect.right() - 10 if self.sender else bubble_rect.left() + 10, bubble_rect.bottom())
        tail_mid = QPoint(bubble_rect.right() + 10 * tail_direction if self.sender else bubble_rect.left() - 10 * tail_direction, bubble_rect.bottom() + 10)
        tail_end = QPoint(tail_start.x() - 20 * tail_direction, tail_start.y())
        tail_polygon = QPolygon([tail_start, tail_mid, tail_end])
        painter.drawPolygon(tail_polygon)

    def sizeHint(self):
        # Provide a suggested size for the widget based on the text content
        return QSize(self.bubble_width, self.bubble_height)

# Test the widget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    text = "Hi, this is a test message that should wrap into a bubble without overflowing."
    bubble_user = MessageBubble("13:00", text, True)
    bubble_other = MessageBubble("13:00", "This is a reply from someone else that also should not overflow.", False)
    bubble_user.show()
    bubble_other.show()
    sys.exit(app.exec_())

