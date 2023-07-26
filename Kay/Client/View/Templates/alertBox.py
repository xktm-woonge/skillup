from PyQt5.QtWidgets import QMessageBox


def warningBox(screen, msg):
    alert_box = QMessageBox(screen)
    alert_box.setIcon(QMessageBox.Warning)
    alert_box.setWindowTitle("Warning")
    alert_box.setText(msg)
    alert_box.exec_()

def informationBox(screen, msg):
    alert_box = QMessageBox(screen)
    alert_box.setIcon(QMessageBox.Information)
    alert_box.setWindowTitle("Information")
    alert_box.setText(msg)
    alert_box.exec_()


# class AlertBox:
#     def __init__(self, screen):
#         self.screen = screen

#     def show(self, type, msg):
#         alert_box = QMessageBox(self.screen)
#         if type.lower() == 'warning':
#             alert_box.setIcon(QMessageBox.Warning)
#             alert_box.setWindowTitle("Warning")
#         elif type.lower() == 'information':
#             alert_box.setIcon(QMessageBox.Information)
#             alert_box.setWindowTitle("Information")
#         else:
#             raise ValueError(f"Unknown type: {type}")
#         alert_box.setText(msg)
#         alert_box.exec_()