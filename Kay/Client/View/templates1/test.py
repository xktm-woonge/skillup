import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt


class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 30)

        # 创建阴影效果并应用于QLineEdit
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(5)
        shadow.setColor(Qt.black)
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        lineEdit = CustomLineEdit()
        layout.addWidget(lineEdit)

        self.setLayout(layout)
        self.setWindowTitle('QLineEdit 带阴影效果示例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
