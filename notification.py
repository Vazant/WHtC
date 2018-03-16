from PyQt5 import QtGui, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
systemtray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon('D:\Course Project\Python\img-2018-03-12-12-54-34.jpg'))
systemtray_icon.show()
systemtray_icon.showMessage('Title', 'Content')