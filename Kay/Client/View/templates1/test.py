from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPalette, QBrush
from PyQt5.QtCore import Qt

class SearchWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.lineEdit = CustomLineEdit(self)
        self.lineEdit.setPlaceholderText("输入搜索内容")

        layout = QHBoxLayout()
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buttonVisible = False

        self.searchButton = QPushButton("查找", self)
        self.searchButton.setFixedSize(50, self.height())

        self.searchButton.clicked.connect(self.onSearchButtonClicked)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateButtonGeometry()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.buttonVisible:
            palette = self.palette()
            background_color = palette.color(QPalette.Base)

            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            button_rect = self.searchButton.rect()
            button_rect.setY(0)
            button_rect.setHeight(self.height())

            painter.fillRect(button_rect, background_color)
            self.searchButton.render(painter)

    def updateButtonGeometry(self):
        button_size = self.searchButton.sizeHint()
        button_size.setHeight(self.height())
        self.searchButton.setFixedSize(button_size)

        button_rect = self.searchButton.rect()
        button_rect.moveTopRight(self.rect().topRight())
        self.searchButton.setGeometry(button_rect)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.buttonVisible = True
        self.update()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.buttonVisible = False
        self.update()

    def onSearchButtonClicked(self):
        text = self.text()
        # 执行搜索操作
        print("搜索内容:", text)

app = QApplication([])
widget = SearchWidget()
widget.show()
app.exec_()
