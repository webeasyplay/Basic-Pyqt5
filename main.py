import sys
import main_windows
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal


class Window(QtWidgets.QMainWindow):
    resized = pyqtSignal()
    def  __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        ui = main_windows.Ui_MainWindow()
        ui.setupUi(self)
        self.resized.connect(self.someFunction)
        self.show()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def someFunction(self):
        print("someFunction")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # MainWindow = QMainWindow()

    # ui = main_windows.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # MainWindow.setFixedSize(MainWindow.size())
    w = Window()
    sys.exit(app.exec_())
