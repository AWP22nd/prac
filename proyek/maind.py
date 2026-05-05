import sys
from PyQt5.QtWidgets import QApplication
from gui import siswaGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = siswaGUI()
    window.show()
    sys.exit(app.exec_()) 


