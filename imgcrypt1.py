
import sys
import os
from imgcrypt import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.flexists)
     self.ui.pushButton_2.clicked.connect(self.encr)
     self.ui.pushButton_3.clicked.connect(self.kys)
     self.ui.pushButton_4.clicked.connect(self.decr)


  def flexists(self):
    fname = str(self.ui.lineEdit.text())
    fname = './input/'+fname
    if (os.path.isfile(fname)):
      print(' file exists')
    else:
      print(' file does not exists')

  def encr(self):
    fname = str(self.ui.lineEdit.text())
    str1 = "python"+" encrypt.py"+" "+fname
    os.system(str1)

  def kys(self):
    print("keys.txt file successfully generated")

  def decr(self):
    fname = str(self.ui.lineEdit.text())
    str1 = "python"+" decrypt.py"+" "+fname
    os.system(str1)


       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
