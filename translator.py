from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from window import Ui_MainWindow
import threading
import requests
import sys
import re

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.Button.clicked.connect(self.switchLabel)
        self.ui.ExpNrw.clicked.connect(self.expandNarrow)
        self.ui.ExitButton.clicked.connect(self.main_win.close)
        self.ui.LeftText.textChanged.connect(self.process)
        self.ui.centralwidget.mousePressEvent = self.mousePressEvent
        self.ui.centralwidget.mouseReleaseEvent = self.mouseReleaseEvent
        self.ui.centralwidget.mouseMoveEvent = self.mouseMoveEvent
        self.trText = self.ui.RightLabel.text()
        self.main_win.m_flag = False
        self.threads = 0
        self.url = 'http://tureng.com/en/turkish-english/'

    def show(self):
        self.main_win.show()

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.main_win.m_flag=True
            self.main_win.m_Position=event.globalPos()-self.main_win.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.main_win.m_flag:  
            self.main_win.move(QMouseEvent.globalPos()-self.main_win.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.main_win.m_flag=False

    def expandNarrow(self):
        if self.ui.ExpNrw.text() == 'Expand':
            self.main_win.setFixedHeight(291)
            self.ui.ExpNrw.setText('Narrow')
        else:
            self.main_win.setFixedHeight(103)
            self.ui.ExpNrw.setText('Expand')
    
    def switchLabel(self):
        txt = self.ui.RightLabel.text()
        self.ui.RightLabel.setText(self.ui.LeftLabel.text())
        self.ui.LeftLabel.setText(txt)
        self.ui.LeftText.setPlainText(self.ui.RightText.placeholderText())
        self.ui.RightText.setPlaceholderText('')

    def translate(self, order):
        link = self.url + re.sub('\s', '%20', self.ui.LeftText.toPlainText())
        page = requests.get(link)
        if self.ui.LeftLabel.text() == self.trText:
            pattern = 'tr ts.*?en tm.*?><.*?>(.*?)<'
        else:
            pattern = 'en tm.*?tr ts.*?><.*?>(.*?)<'
        try:
            arr = re.findall(pattern, str(page.content))
            text = arr[0]
            text = re.sub('\s+$', '', text)
            text = re.sub('\\\\xc4\\\\xb1', 'ı', text)
            text = re.sub('\\\\xc4\\\\x9f', 'ğ', text)
            text = re.sub('\\\\xc5\\\\x9f', 'ş', text)
            text = re.sub('&#246;', 'ö', text)
            text = re.sub('&#252;', 'ü', text)
            text = re.sub('&#231;', 'ç', text)
        except:
            text = 'None'
        if order == self.threads:
            self.ui.RightText.setPlaceholderText(text)
            self.ui.details.setPlaceholderText('')
            self.threads = 0
            if self.ui.ExpNrw.text() == 'Narrow' and text != 'None':
                wordSet = set()
                try:
                    counter = 1
                    while len(wordSet) < 14:
                        txt = arr[counter]
                        txt = re.sub('\s+$', '', txt)
                        txt = re.sub('\\\\xc4\\\\xb1', 'ı', txt)
                        txt = re.sub('\\\\xc4\\\\x9f', 'ğ', txt)
                        txt = re.sub('\\\\xc5\\\\x9f', 'ş', txt)
                        txt = re.sub('&#246;', 'ö', txt)
                        txt = re.sub('&#252;', 'ü', txt)
                        txt = re.sub('&#231;', 'ç', txt)
                        counter += 1
                        wordSet.add(txt)
                except:
                    None
                string = '\n'.join(wordSet)
                self.ui.details.setPlaceholderText(string)

    def process(self):
        if self.ui.LeftText.toPlainText() == '': 
            self.ui.RightText.setPlaceholderText('')
            return
        threading.Thread(target=self.translate, args=(self.threads+1,)).start()
        self.threads+=1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
