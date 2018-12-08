import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile1 = "error.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

class ErrorDialog(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.try_again_btn.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()  
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = ErrorDialog()
    window.show()
    sys.exit(app.exec_())