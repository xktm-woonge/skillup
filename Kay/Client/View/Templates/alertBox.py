from PyQt5.QtWidgets import QMessageBox

class AlertBox:

    @staticmethod
    def show(response):
        msg = QMessageBox()

        # Check command and set alert title accordingly
        if response['command'] == 'VERIFICATIONCODE':
            if response['status'] == 'FAIL':
                msg.setWindowTitle('Verification Error')
            elif response['status'] == 'SUCCESS':
                msg.setWindowTitle('Verification Success')
        else:
            msg.setWindowTitle('Info')

        # Set the alert text to the received message
        msg.setText(response['message'])

        # Set the alert icon according to the status
        if response['status'] == 'FAIL':
            msg.setIcon(QMessageBox.Warning)
        elif response['status'] == 'SUCCESS':
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.NoIcon)

        retval = msg.exec_()
