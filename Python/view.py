


from PyQt5 import QtCore, QtGui, QtWidgets
import konwertuj





class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(220, 20, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelTitle.setTextFormat(QtCore.Qt.AutoText)
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setObjectName("labelTitle")
        self.ButtonConvert = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonConvert.setGeometry(QtCore.QRect(280, 440, 221, 28))
        self.ButtonConvert.setObjectName("ButtonConvert")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 140, 241, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TeXFrom = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.TeXFrom.setObjectName("TeXFrom")
        self.horizontalLayout.addWidget(self.TeXFrom)
        self.DocFrom = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.DocFrom.setObjectName("DocFrom")
        self.horizontalLayout.addWidget(self.DocFrom)
        self.MathMLFrom = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.MathMLFrom.setObjectName("MathMLFrom")
        self.horizontalLayout.addWidget(self.MathMLFrom)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(480, 140, 241, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TeXTo = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.TeXTo.setObjectName("TeXTo")
        self.horizontalLayout_2.addWidget(self.TeXTo)
        self.DocTo = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.DocTo.setObjectName("DocTo")
        self.horizontalLayout_2.addWidget(self.DocTo)
        self.MathMLTo = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.MathMLTo.setObjectName("MathMLTo")
        self.horizontalLayout_2.addWidget(self.MathMLTo)
        self.input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 200, 371, 201))
        self.input.setObjectName("input")
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(410, 200, 371, 201))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Konwerter"))
        self.labelTitle.setText(_translate("Dialog", "Konwerter MathML <-> TeX <-> Doc"))
        self.ButtonConvert.setText(_translate("Dialog", "Konwertuj"))
        self.TeXFrom.setText(_translate("Dialog", "TeX"))
        self.DocFrom.setText(_translate("Dialog", "Doc"))
        self.MathMLFrom.setText(_translate("Dialog", "MathML"))
        self.TeXTo.setText(_translate("Dialog", "TeX"))
        self.DocTo.setText(_translate("Dialog", "Doc"))
        self.MathMLTo.setText(_translate("Dialog", "MathML"))

class MainWindow(Ui_Dialog):
    def __init__(self):
        super(MainWindow).__init__()
        self.title = 'Konwerter'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

    def setupUi(self, Dialog):
        super(MainWindow, self).setupUi(Dialog)

        # adding functions to buttons from here
        self.ButtonConvert.clicked.connect(self._clicked_ButtonConvert)
        #

    def _create_window(self):
        self._shared_memory = {}
        self.ex = App(self._shared_memory)
        self._clicked_tool_button()


    def _clicked_ButtonConvert(self):
        inpt=''
        outpt =''
        indexInDic=0
        if self.MathMLFrom.isChecked():
            inpt='mathml'
            indexInDic = 4
        elif self.DocFrom.isChecked():
            inpt='doc'
            indexInDic = 0
        elif self.TeXFrom.isChecked():
            inpt='tex'
            indexInDic = 1
        if self.MathMLTo.isChecked():
            outpt='mathml'
        elif self.DocTo.isChecked():
            outpt='doc'
        elif self.TeXTo.isChecked():
            outpt='tex'
        if inpt !='' and outpt !='':
            try:
                if konwertuj.checkInputString(self.input.toPlainText(),indexInDic):
                    self.output.setPlainText(konwertuj.convert(inpt,outpt,self.input.toPlainText()))
                else:
                    self.output.setPlainText('Przepraszam, ale wpisano coś, czego nie rozumiem lub nie występuje tu żaden matematyczny symbol.')

            except:
                self.output.setPlainText('Przepraszam, ale wpisano coś, czego nie rozumiem.')
        else:
            self.output.setPlainText('Musisz wybrać języki konwersji.')
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
