# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alpha\Documents\GitLab Projects\AnonFileSimpleUploader\src\main\python\ui\output_format.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ui import output_format_rcc

class Ui_OutputFormat(object):
    def setupUi(self, OutputFormat):
        OutputFormat.setObjectName("OutputFormat")
        OutputFormat.resize(400, 168)
        OutputFormat.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        OutputFormat.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(OutputFormat)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(OutputFormat)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditOutputFormat = QtWidgets.QLineEdit(OutputFormat)
        self.lineEditOutputFormat.setObjectName("lineEditOutputFormat")
        self.horizontalLayout.addWidget(self.lineEditOutputFormat)
        self.pushButtonOk = QtWidgets.QPushButton(OutputFormat)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.help = QtWidgets.QLabel(OutputFormat)
        self.help.setEnabled(False)
        self.help.setFrameShape(QtWidgets.QFrame.Panel)
        self.help.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.help.setObjectName("help")
        self.verticalLayout.addWidget(self.help)

        self.retranslateUi(OutputFormat)
        QtCore.QMetaObject.connectSlotsByName(OutputFormat)

    def retranslateUi(self, OutputFormat):
        _translate = QtCore.QCoreApplication.translate
        OutputFormat.setWindowTitle(_translate("OutputFormat", "Output Format"))
        self.label.setText(_translate("OutputFormat", "Output format:"))
        self.lineEditOutputFormat.setPlaceholderText(_translate("OutputFormat", "$short_link$"))
        self.pushButtonOk.setText(_translate("OutputFormat", "Ok"))
        self.help.setText(_translate("OutputFormat", "Name: $name$  ; example.txt\n"
"File Path: $path$  ; /home/example.txt\n"
"Size: $size$  ; 1.22 MB\n"
"Short Link: $short_link$  ; https://anonfile.com/p0v3ycF2n5\n"
"Full Link: $full_link$  ; https://anonfile.com/p0v3ycF2n5/example.txt\n"
"Error: $error$  ; Error, invalid reply. Verify your Internet connection\n"
"Example:\n"
"$name$: $short_link$ => example.txt: https://anonfile.com/p0v3ycF2n5\n"
""))

