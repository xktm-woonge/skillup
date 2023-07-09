import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Example')

        # QHBoxLayout 생성
        hbox = QHBoxLayout()

        # QLabel 생성 및 가운데 정렬 설정
        label = QLabel('Label', self)
        label.setAlignment(Qt.AlignCenter)

        # QLabel을 QHBoxLayout에 추가
        hbox.addWidget(label)

        self.setLayout(hbox)

        self.show()

        # QLabel의 x, y 좌표 취득
        label_pos = label.mapToGlobal(QPoint(0, 0))
        label_x = label_pos.x()
        label_y = label_pos.y()
        print("Label의 x 좌표:", label_x)
        print("Label의 y 좌표:", label_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
