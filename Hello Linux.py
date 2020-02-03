from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from ui import MainWindowUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindowUi.Ui_MainWindow()
        self.ui.setupUi(self)
        

app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())