# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alpha\Documents\GitLab Projects\AnonFileSimpleUploader\src\main\python\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ui import mainwindow_rcc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/AnonFileSimpleUploader_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setIconSize(QtCore.QSize(256, 256))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TableOfFiles = QtWidgets.QTableWidget(self.frame_2)
        self.TableOfFiles.setShowGrid(False)
        self.TableOfFiles.setGridStyle(QtCore.Qt.NoPen)
        self.TableOfFiles.setWordWrap(False)
        self.TableOfFiles.setObjectName("TableOfFiles")
        self.TableOfFiles.setColumnCount(8)
        self.TableOfFiles.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TableOfFiles.setHorizontalHeaderItem(7, item)
        self.TableOfFiles.horizontalHeader().setVisible(True)
        self.TableOfFiles.horizontalHeader().setCascadingSectionResizes(False)
        self.TableOfFiles.horizontalHeader().setDefaultSectionSize(100)
        self.TableOfFiles.horizontalHeader().setHighlightSections(True)
        self.TableOfFiles.horizontalHeader().setMinimumSectionSize(40)
        self.TableOfFiles.horizontalHeader().setStretchLastSection(True)
        self.TableOfFiles.verticalHeader().setVisible(True)
        self.TableOfFiles.verticalHeader().setDefaultSectionSize(14)
        self.TableOfFiles.verticalHeader().setMinimumSectionSize(9)
        self.TableOfFiles.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.TableOfFiles)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AddButton = QtWidgets.QPushButton(self.frame_4)
        self.AddButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.AddButton.setObjectName("AddButton")
        self.verticalLayout_2.addWidget(self.AddButton)
        self.RemoveButton = QtWidgets.QPushButton(self.frame_4)
        self.RemoveButton.setObjectName("RemoveButton")
        self.verticalLayout_2.addWidget(self.RemoveButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonUp = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonUp.sizePolicy().hasHeightForWidth())
        self.pushButtonUp.setSizePolicy(sizePolicy)
        self.pushButtonUp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUp.setIcon(icon1)
        self.pushButtonUp.setIconSize(QtCore.QSize(22, 22))
        self.pushButtonUp.setObjectName("pushButtonUp")
        self.gridLayout.addWidget(self.pushButtonUp, 0, 0, 1, 1)
        self.pushButtonDown = QtWidgets.QPushButton(self.frame_5)
        self.pushButtonDown.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDown.sizePolicy().hasHeightForWidth())
        self.pushButtonDown.setSizePolicy(sizePolicy)
        self.pushButtonDown.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDown.setIcon(icon2)
        self.pushButtonDown.setIconSize(QtCore.QSize(22, 22))
        self.pushButtonDown.setAutoDefault(False)
        self.pushButtonDown.setDefault(False)
        self.pushButtonDown.setFlat(False)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.gridLayout.addWidget(self.pushButtonDown, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButtonCopyLinks = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonCopyLinks.setObjectName("pushButtonCopyLinks")
        self.verticalLayout_2.addWidget(self.pushButtonCopyLinks)
        self.pushButtonRetryAll = QtWidgets.QPushButton(self.frame_4)
        self.pushButtonRetryAll.setObjectName("pushButtonRetryAll")
        self.verticalLayout_2.addWidget(self.pushButtonRetryAll)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBoxMaxParallel = QtWidgets.QSpinBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxMaxParallel.sizePolicy().hasHeightForWidth())
        self.spinBoxMaxParallel.setSizePolicy(sizePolicy)
        self.spinBoxMaxParallel.setMinimum(1)
        self.spinBoxMaxParallel.setProperty("value", 3)
        self.spinBoxMaxParallel.setObjectName("spinBoxMaxParallel")
        self.horizontalLayout_3.addWidget(self.spinBoxMaxParallel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_6)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.UploadButton = QtWidgets.QPushButton(self.frame_3)
        self.UploadButton.setObjectName("UploadButton")
        self.verticalLayout_3.addWidget(self.UploadButton)
        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuLanguage = QtWidgets.QMenu(self.menuMenu)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShort_Link = QtWidgets.QAction(MainWindow)
        self.actionShort_Link.setCheckable(True)
        self.actionShort_Link.setChecked(True)
        self.actionShort_Link.setObjectName("actionShort_Link")
        self.actionFull_Link = QtWidgets.QAction(MainWindow)
        self.actionFull_Link.setCheckable(True)
        self.actionFull_Link.setObjectName("actionFull_Link")
        self.actionOutput_format = QtWidgets.QAction(MainWindow)
        self.actionOutput_format.setObjectName("actionOutput_format")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnglish.setIcon(icon3)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionSpanish = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/spanish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpanish.setIcon(icon4)
        self.actionSpanish.setObjectName("actionSpanish")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionSpanish)
        self.menuMenu.addAction(self.menuLanguage.menuAction())
        self.menuMenu.addAction(self.actionOutput_format)
        self.menuView.addAction(self.actionShort_Link)
        self.menuView.addAction(self.actionFull_Link)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AnonFile Simple Uploader"))
        self.TableOfFiles.setSortingEnabled(False)
        item = self.TableOfFiles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.TableOfFiles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.TableOfFiles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Progress"))
        item = self.TableOfFiles.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Short Link"))
        item = self.TableOfFiles.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Full Link"))
        item = self.TableOfFiles.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Uploading"))
        item = self.TableOfFiles.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Finished"))
        item = self.TableOfFiles.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Error"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
        self.RemoveButton.setText(_translate("MainWindow", "Remove"))
        self.pushButtonCopyLinks.setText(_translate("MainWindow", "Copy Links"))
        self.pushButtonRetryAll.setText(_translate("MainWindow", "Retry All Errors"))
        self.label.setText(_translate("MainWindow", "Number of parallels uploads:"))
        self.UploadButton.setText(_translate("MainWindow", "Upload"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionShort_Link.setText(_translate("MainWindow", "Short Link"))
        self.actionFull_Link.setText(_translate("MainWindow", "Full Link"))
        self.actionOutput_format.setText(_translate("MainWindow", "Output format"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionSpanish.setText(_translate("MainWindow", "Español"))
