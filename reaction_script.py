import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile1 = "reaction.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

class reactionWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.back_btn.clicked.connect(self.closeWindow)
        wp=open("data.txt", "r")
        contents=wp.read().split("\n")
        wp.close() 
        length =len(contents)
        contents.pop(length-1)
        print(contents)
        print(length)

        self.P1.setText(str(contents[6]))
        self.P2.setText(str(contents[7]))
        self.P3.setText(str(contents[8]))
        self.P4.setText(str(contents[9]))
        self.P5.setText(str(contents[10]))
        self.P6.setText(str(contents[11]))
        self.P7.setText(str(contents[12]))
        self.P8.setText(str(contents[13]))
        self.P9.setText(str(contents[14]))
        self.P10.setText(str(contents[15]))
        self.P11.setText(str(contents[16]))
        self.P12.setText(str(contents[17]))

    def closeWindow(self):
        self.close()  
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = reactionWindow()
    window.show()
    sys.exit(app.exec_())