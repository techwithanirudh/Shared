from PyQt5 import QtCore, QtGui, QtWidgets
import os
import youtube_dl 
import webbrowser
import time
import threading

def splash():
    import tkinter as tk

    splashScreen = tk.Tk()
    splashScreen.geometry('800x400+450+250')
    splashScreen.overrideredirect(1)
    splashScreen.configure(bg='darkblue')

    lblTitle = tk.Label(splashScreen, fg='white', bg='darkblue', font=('arial', 40, 'bold'), text='\n' * 2 + 'Youtube Video Downloader') 
    lblTitle.pack() 

    lblCreatedBy = tk.Label(splashScreen, fg='white', bg='darkblue', font=('arial', 15, 'bold'), text='\n' * 6 + '© 2020 Anirudh Sriram')
    lblCreatedBy.pack()

    def destroySp():
        splashScreen.destroy()

    splashScreen.after(6000, destroySp)
    splashScreen.mainloop()

class main(object):
    def saveFile(self):
        _translate = QtCore.QCoreApplication.translate
        fileName = str(QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', 'MP4 (*.mp4)'))
        fileName = fileName.replace(')', '')
        fileName = fileName.replace('(', '')
        fileName = fileName.replace('\'', '')
        fileName = fileName.split(',')[0]
        if fileName != '':
            self.txtFileName.setText(_translate('winMain', fileName))

    def openYoutube(self):
        webbrowser.open('https://www.youtube.com/')

    def _downloadVideo(self):
        self.btnDownload.setEnabled(False)
        fileName = self.txtFileName.toPlainText().replace('\n', '')
        link = self.txtURL.toPlainText().replace('\n', '')
        ydl_opts = {'outtmpl': fileName}

        if fileName and link != '':
            with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
                ydl.download([link]) 
        self.btnDownload.setEnabled(True)

    def downloadVideo(self):
        downloadVid = threading.Thread(target=self._downloadVideo)
        downloadVid.start()

    def setupUi(self, winMain):
        winMain.setObjectName('winMain')
        winMain.resize(830, 90)
        try:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            winMain.setWindowIcon(icon)
        except FileNotFoundError:
            pass
        splash()
        self.centralwidget = QtWidgets.QWidget(winMain)
        self.centralwidget.setObjectName('centralwidget')
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 767, 61))
        self.layoutWidget.setObjectName('layoutWidget')
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName('gridLayout')
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        self.lblURL = QtWidgets.QLabel(self.layoutWidget)
        self.lblURL.setObjectName('lblURL')
        self.horizontalLayout_4.addWidget(self.lblURL)
        self.txtURL = QtWidgets.QTextEdit(self.layoutWidget)
        self.txtURL.setObjectName('txtURL')
        self.horizontalLayout_4.addWidget(self.txtURL)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.btnOpenYoutube = QtWidgets.QPushButton(self.layoutWidget)
        self.btnOpenYoutube.setObjectName('btnOpenYoutube')
        self.horizontalLayout_3.addWidget(self.btnOpenYoutube)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.lblFileName = QtWidgets.QLabel(self.layoutWidget)
        self.lblFileName.setObjectName('lblFileName')
        self.horizontalLayout.addWidget(self.lblFileName)
        self.txtFileName = QtWidgets.QTextEdit(self.layoutWidget)
        self.txtFileName.setObjectName('txtFileName')
        self.horizontalLayout.addWidget(self.txtFileName)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.btnBrowse = QtWidgets.QPushButton(self.layoutWidget)
        self.btnBrowse.setObjectName('btnBrowse')
        self.horizontalLayout_2.addWidget(self.btnBrowse)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.btnDownload = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDownload.setObjectName('btnDownload')
        self.gridLayout_2.addWidget(self.btnDownload, 1, 0, 1, 1)
        winMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(winMain)
        self.statusbar.setObjectName('statusbar')
        winMain.setStatusBar(self.statusbar)

        self.retranslateUi(winMain)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        _translate = QtCore.QCoreApplication.translate
        winMain.setWindowTitle(_translate('winMain', 'Youtube Video Downloader'))
        self.lblURL.setText(_translate('winMain', 'URL'))
        self.txtURL.setText(_translate('winMain', 'https://www.youtube.com/watch?v=II7UCUbxOus&amp'))
        self.btnOpenYoutube.setText(_translate('winMain', 'Open Youtube'))
        self.lblFileName.setText(_translate('winMain', 'Filename'))
        downloads = os.path.expanduser('~') + '\Downloads'
        self.txtFileName.setText(_translate('winMain', f'{downloads}\download.mp4'))
        self.btnBrowse.setText(_translate('winMain', 'Browse'))
        self.btnDownload.setText(_translate('winMain', 'Download'))
        self.btnDownload.clicked.connect(self.downloadVideo)
        self.btnOpenYoutube.clicked.connect(self.openYoutube)
        self.btnBrowse.clicked.connect(self.saveFile)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winMain = QtWidgets.QMainWindow()
    main = main()
    main.setupUi(winMain)
    winMain.show()
    sys.exit(app.exec_())