import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile1 = "deflection.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

class deflectionWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ErrorDialog,self).__init__()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
    def closeWindow(self):
        self.close()  
   
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = deflectionWindow()
    window.show()
    sys.exit(app.exec_())