from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QHBoxLayout, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor
import sys

class HoverableListItem(QListWidgetItem):
    def __init__(self, text):
        super().__init__(text)

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QHBoxLayout()

        # List widget for the left side
        self.list_widget = QListWidget()
        self.list_widget.setMouseTracking(True)  # Enable mouse tracking
        self.list_widget.installEventFilter(self)  # Install event filter

        # Adding sample items to the list widget
        for i in range(10):
            item = HoverableListItem(f'Chat {i+1}')
            self.list_widget.addItem(item)

        # Detail view for the right side
        self.detail_view = QLabel("Details go here")
        self.detail_view.setFrameStyle(QLabel.Panel | QLabel.Sunken)

        # Add widgets to the main layout
        main_layout.addWidget(self.list_widget, 1)  # 1:1 ratio in size
        main_layout.addWidget(self.detail_view, 2)  # 2:1 ratio in size

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove and source is self.list_widget:
            item = self.list_widget.itemAt(event.pos())
            if item:
                item.setBackground(QColor('lightgrey'))
            return True
        elif event.type() == QEvent.Leave:
            for i in range(self.list_widget.count()):
                self.list_widget.item(i).setBackground(QColor('white'))
            return True
        return super().eventFilter(source, event)

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create the main window
chat_window = ChatWindow()
chat_window.resize(600, 400)
chat_window.setWindowTitle('Chat Application')
chat_window.show()

# Execute the application
sys.exit(app.exec_())
