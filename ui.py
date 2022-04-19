# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 412)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Png/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphicsPicture = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsPicture.sizePolicy().hasHeightForWidth())
        self.graphicsPicture.setSizePolicy(sizePolicy)
        self.graphicsPicture.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsPicture.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.graphicsPicture.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsPicture.setRenderHints(QtGui.QPainter.HighQualityAntialiasing)
        self.graphicsPicture.setObjectName("graphicsPicture")
        self.verticalLayout_5.addWidget(self.graphicsPicture)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFormat = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFormat.sizePolicy().hasHeightForWidth())
        self.labelFormat.setSizePolicy(sizePolicy)
        self.labelFormat.setObjectName("labelFormat")
        self.gridLayout.addWidget(self.labelFormat, 0, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 1, 2, 1, 1)
        self.labelMirror = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMirror.sizePolicy().hasHeightForWidth())
        self.labelMirror.setSizePolicy(sizePolicy)
        self.labelMirror.setObjectName("labelMirror")
        self.gridLayout.addWidget(self.labelMirror, 0, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 1, 0, 1, 1)
        self.labelRotate = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRotate.sizePolicy().hasHeightForWidth())
        self.labelRotate.setSizePolicy(sizePolicy)
        self.labelRotate.setObjectName("labelRotate")
        self.gridLayout.addWidget(self.labelRotate, 0, 2, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 1, 3, 1, 1)
        self.buttonFormatInfo = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonFormatInfo.sizePolicy().hasHeightForWidth())
        self.buttonFormatInfo.setSizePolicy(sizePolicy)
        self.buttonFormatInfo.setObjectName("buttonFormatInfo")
        self.gridLayout.addWidget(self.buttonFormatInfo, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboZoom = QtWidgets.QComboBox(self.centralwidget)
        self.comboZoom.setObjectName("comboZoom")
        self.horizontalLayout_3.addWidget(self.comboZoom)
        self.comboGridType = QtWidgets.QComboBox(self.centralwidget)
        self.comboGridType.setObjectName("comboGridType")
        self.horizontalLayout_3.addWidget(self.comboGridType)
        self.buttonPictureGrid = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPictureGrid.sizePolicy().hasHeightForWidth())
        self.buttonPictureGrid.setSizePolicy(sizePolicy)
        self.buttonPictureGrid.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Png/PictureGrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPictureGrid.setIcon(icon1)
        self.buttonPictureGrid.setCheckable(True)
        self.buttonPictureGrid.setFlat(False)
        self.buttonPictureGrid.setObjectName("buttonPictureGrid")
        self.horizontalLayout_3.addWidget(self.buttonPictureGrid)
        self.buttonEditorGrid = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEditorGrid.sizePolicy().hasHeightForWidth())
        self.buttonEditorGrid.setSizePolicy(sizePolicy)
        self.buttonEditorGrid.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Png/EditorGrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEditorGrid.setIcon(icon2)
        self.buttonEditorGrid.setCheckable(True)
        self.buttonEditorGrid.setObjectName("buttonEditorGrid")
        self.horizontalLayout_3.addWidget(self.buttonEditorGrid)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsEditor = QtWidgets.QGraphicsView(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsEditor.sizePolicy().hasHeightForWidth())
        self.graphicsEditor.setSizePolicy(sizePolicy)
        self.graphicsEditor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsEditor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsEditor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsEditor.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.graphicsEditor.setObjectName("graphicsEditor")
        self.horizontalLayout_4.addWidget(self.graphicsEditor)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.show()
        MainWindow.resizeGraphics()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFormat.setText(_translate("MainWindow", "labelFormat"))
        self.labelMirror.setText(_translate("MainWindow", "labelMirror"))
        self.labelRotate.setText(_translate("MainWindow", "labelRotate"))
        self.buttonFormatInfo.setText(_translate("MainWindow", "buttonFormatinfo"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
import Resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
