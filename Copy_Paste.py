from PySide2.QtWidgets import  QWidget, QLabel,QPushButton,QApplication,QMainWindow,QHBoxLayout,QVBoxLayout
import sys
from PySide2.QtCore import Qt

from PySide2.QtGui import  QGuiApplication


class Copy_paste(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Copy_Paste")
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)

        self.copy_button_1 = QPushButton("copy")
        self.copy_button_2 = QPushButton("copy")
        self.copy_button_3 = QPushButton("copy")
        self.copy_button_4 = QPushButton("copy")
        self.copy_button_5 = QPushButton("copy")

        self.copy_button_1.clicked.connect(lambda: self.copy_button_clicked(self.copy_button_1))
        self.copy_button_2.clicked.connect(lambda: self.copy_button_clicked(self.copy_button_2))
        self.copy_button_3.clicked.connect(lambda: self.copy_button_clicked(self.copy_button_3))
        self.copy_button_4.clicked.connect(lambda: self.copy_button_clicked(self.copy_button_4))
        self.copy_button_5.clicked.connect(lambda: self.copy_button_clicked(self.copy_button_5))
        


        
        self.paste_button_1 = QPushButton("paste")
        self.paste_button_2 = QPushButton("paste")
        self.paste_button_3 = QPushButton("paste")
        self.paste_button_4 = QPushButton("paste")
        self.paste_button_5 = QPushButton("paste")

        self.paste_button_1.clicked.connect(lambda: self.paste_button_clicked(self.paste_button_1))
        self.paste_button_2.clicked.connect(lambda: self.paste_button_clicked(self.paste_button_2))
        self.paste_button_3.clicked.connect(lambda: self.paste_button_clicked(self.paste_button_3))
        self.paste_button_4.clicked.connect(lambda: self.paste_button_clicked(self.paste_button_4))
        self.paste_button_5.clicked.connect(lambda: self.paste_button_clicked(self.paste_button_5))
        

        self.label_1 = QLabel("Copy_Paste")
        self.label_2 = QLabel("Copy_Paste")
        self.label_3 = QLabel("Copy_Paste")
        self.label_4 = QLabel("Copy_Paste")
        self.label_5 = QLabel("Copy_Paste")

        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5.setAlignment(Qt.AlignCenter)


        self.qh_1 = QHBoxLayout()
        #self.qh_1.addStretch(1)
        self.qh_1.addWidget(self.paste_button_1)
        self.qh_1.addWidget(self.label_1)
        self.qh_1.addWidget(self.copy_button_1)

        self.qh_2 = QHBoxLayout()
        #self.qh_2.addStretch(1)
        self.qh_2.addWidget(self.paste_button_2)
        self.qh_2.addWidget(self.label_2)
        self.qh_2.addWidget(self.copy_button_2)

        self.qh_3 = QHBoxLayout()
        #self.qh_3.addStretch(1)
        self.qh_3.addWidget(self.paste_button_3)
        self.qh_3.addWidget(self.label_3)
        self.qh_3.addWidget(self.copy_button_3)

        self.qh_4 = QHBoxLayout()
        #self.qh_4.addStretch(1)
        self.qh_4.addWidget(self.paste_button_4)
        self.qh_4.addWidget(self.label_4)
        self.qh_4.addWidget(self.copy_button_4)

        self.qh_5 = QHBoxLayout()
        #self.qh_5.addStretch(1)
        self.qh_5.addWidget(self.paste_button_5)
        self.qh_5.addWidget(self.label_5)
        self.qh_5.addWidget(self.copy_button_5)

        self.qv = QVBoxLayout()
        #self.qv.addStretch(2)
        self.qv.addLayout(self.qh_1)
        self.qv.addLayout(self.qh_2)
        self.qv.addLayout(self.qh_3)
        self.qv.addLayout(self.qh_4)
        self.qv.addLayout(self.qh_5)







        self.w=QWidget()
        self.w.setLayout(self.qv)
        self.setCentralWidget(self.w)
        self.show()



    def copy_button_clicked(self,button):
        clipboard = QGuiApplication.clipboard()

        self.button=button

        if self.button==self.copy_button_1:

            clipboard.setText(self.label_1.text())

        elif self.button==self.copy_button_2:
            clipboard.setText(self.label_2.text())


        elif self.button==self.copy_button_3:
            clipboard.setText(self.label_3.text())


        elif self.button==self.copy_button_4:
            clipboard.setText(self.label_4.text())


        elif self.button==self.copy_button_5:
            clipboard.setText(self.label_5.text())


    def paste_button_clicked(self, button):
        clipboard = QGuiApplication.clipboard()


        self.button = button

        if self.button == self.paste_button_1:
            self.label_1.setText(clipboard.text())


        elif self.button == self.paste_button_2:
            self.label_2.setText(clipboard.text())


        elif self.button == self.paste_button_3:
            self.label_3.setText(clipboard.text())


        elif self.button == self.paste_button_4:
            self.label_4.setText(clipboard.text())


        elif self.button == self.paste_button_5:
            self.label_5.setText(clipboard.text())














myApp= QApplication(sys.argv)
copy_paste=Copy_paste()
sys.exit(myApp.exec_())