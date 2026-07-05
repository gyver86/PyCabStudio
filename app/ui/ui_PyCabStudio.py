# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowOceLHi.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 823)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.action_Reset = QAction(MainWindow)
        self.action_Reset.setObjectName(u"action_Reset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitterMain_Right = QSplitter(self.centralwidget)
        self.splitterMain_Right.setObjectName(u"splitterMain_Right")
        self.splitterMain_Right.setFrameShape(QFrame.Shape.NoFrame)
        self.splitterMain_Right.setFrameShadow(QFrame.Shadow.Plain)
        self.splitterMain_Right.setOrientation(Qt.Orientation.Horizontal)
        self.splitterMain_Right.setHandleWidth(20)
        self.widgetLeft = QWidget(self.splitterMain_Right)
        self.widgetLeft.setObjectName(u"widgetLeft")
        self.widgetLeft.setMinimumSize(QSize(800, 0))
        self.verticalLayout = QVBoxLayout(self.widgetLeft)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 2, 0, 0)
        self.splitterMain_Docker = QSplitter(self.widgetLeft)
        self.splitterMain_Docker.setObjectName(u"splitterMain_Docker")
        self.splitterMain_Docker.setFrameShape(QFrame.Shape.NoFrame)
        self.splitterMain_Docker.setOrientation(Qt.Orientation.Vertical)
        self.splitterMain_Docker.setHandleWidth(20)
        self.widgetMain_Middle = QWidget(self.splitterMain_Docker)
        self.widgetMain_Middle.setObjectName(u"widgetMain_Middle")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetMain_Middle)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.widgetLeftButtons = QWidget(self.widgetMain_Middle)
        self.widgetLeftButtons.setObjectName(u"widgetLeftButtons")
        self.widgetLeftButtons.setMinimumSize(QSize(0, 0))
        self.widgetLeftButtons.setMaximumSize(QSize(105, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widgetLeftButtons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameBuild = QFrame(self.widgetLeftButtons)
        self.frameBuild.setObjectName(u"frameBuild")
        self.frameBuild.setMinimumSize(QSize(0, 120))
        self.frameBuild.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.frameBuild.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameBuild.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonWall = QPushButton(self.frameBuild)
        self.pushButtonWall.setObjectName(u"pushButtonWall")
        self.pushButtonWall.setGeometry(QRect(5, 20, 41, 24))
        self.pushButtonWall.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonWall.setCheckable(False)
        self.pushButtonWall.setFlat(False)
        self.pushButtonDoor = QPushButton(self.frameBuild)
        self.pushButtonDoor.setObjectName(u"pushButtonDoor")
        self.pushButtonDoor.setGeometry(QRect(50, 20, 51, 24))
        self.pushButtonDoor.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonDoor.setCheckable(False)
        self.pushButtonDoor.setFlat(False)
        self.pushButtonWindow = QPushButton(self.frameBuild)
        self.pushButtonWindow.setObjectName(u"pushButtonWindow")
        self.pushButtonWindow.setGeometry(QRect(5, 50, 51, 24))
        self.pushButtonWindow.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonWindow.setCheckable(False)
        self.pushButtonWindow.setFlat(False)
        self.pushButtonFloor = QPushButton(self.frameBuild)
        self.pushButtonFloor.setObjectName(u"pushButtonFloor")
        self.pushButtonFloor.setGeometry(QRect(60, 50, 41, 24))
        self.pushButtonFloor.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonFloor.setCheckable(False)
        self.pushButtonFloor.setFlat(False)
        self.pushButtonCeiling = QPushButton(self.frameBuild)
        self.pushButtonCeiling.setObjectName(u"pushButtonCeiling")
        self.pushButtonCeiling.setGeometry(QRect(5, 80, 46, 24))
        self.pushButtonCeiling.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonCeiling.setCheckable(False)
        self.pushButtonCeiling.setFlat(False)
        self.pushButtonBulkhead = QPushButton(self.frameBuild)
        self.pushButtonBulkhead.setObjectName(u"pushButtonBulkhead")
        self.pushButtonBulkhead.setGeometry(QRect(55, 80, 46, 24))
        self.pushButtonBulkhead.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonBulkhead.setCheckable(False)
        self.pushButtonBulkhead.setFlat(False)
        self.labelBuild = QLabel(self.frameBuild)
        self.labelBuild.setObjectName(u"labelBuild")
        self.labelBuild.setGeometry(QRect(5, 0, 49, 16))

        self.verticalLayout_3.addWidget(self.frameBuild)

        self.frameObject = QFrame(self.widgetLeftButtons)
        self.frameObject.setObjectName(u"frameObject")
        self.frameObject.setMinimumSize(QSize(0, 80))
        self.frameObject.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.frameObject.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameObject.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonObject = QPushButton(self.frameObject)
        self.pushButtonObject.setObjectName(u"pushButtonObject")
        self.pushButtonObject.setGeometry(QRect(5, 20, 41, 24))
        self.pushButtonObject.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonObject.setCheckable(False)
        self.pushButtonObject.setFlat(False)
        self.labelObject = QLabel(self.frameObject)
        self.labelObject.setObjectName(u"labelObject")
        self.labelObject.setGeometry(QRect(5, 0, 49, 16))

        self.verticalLayout_3.addWidget(self.frameObject)

        self.frameDraw = QFrame(self.widgetLeftButtons)
        self.frameDraw.setObjectName(u"frameDraw")
        self.frameDraw.setMinimumSize(QSize(0, 80))
        self.frameDraw.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.frameDraw.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameDraw.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonLine = QPushButton(self.frameDraw)
        self.pushButtonLine.setObjectName(u"pushButtonLine")
        self.pushButtonLine.setGeometry(QRect(5, 20, 41, 24))
        self.pushButtonLine.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonLine.setCheckable(False)
        self.pushButtonLine.setFlat(False)
        self.pushButtonMeasure = QPushButton(self.frameDraw)
        self.pushButtonMeasure.setObjectName(u"pushButtonMeasure")
        self.pushButtonMeasure.setGeometry(QRect(50, 20, 51, 24))
        self.pushButtonMeasure.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonMeasure.setCheckable(False)
        self.pushButtonMeasure.setFlat(False)
        self.pushButtonBox = QPushButton(self.frameDraw)
        self.pushButtonBox.setObjectName(u"pushButtonBox")
        self.pushButtonBox.setGeometry(QRect(50, 50, 51, 24))
        self.pushButtonBox.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonBox.setCheckable(False)
        self.pushButtonBox.setFlat(False)
        self.pushButtonCircle = QPushButton(self.frameDraw)
        self.pushButtonCircle.setObjectName(u"pushButtonCircle")
        self.pushButtonCircle.setGeometry(QRect(5, 50, 41, 24))
        self.pushButtonCircle.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonCircle.setCheckable(False)
        self.pushButtonCircle.setFlat(False)
        self.labelDraw = QLabel(self.frameDraw)
        self.labelDraw.setObjectName(u"labelDraw")
        self.labelDraw.setGeometry(QRect(5, 0, 49, 16))

        self.verticalLayout_3.addWidget(self.frameDraw)

        self.frameViewMode = QFrame(self.widgetLeftButtons)
        self.frameViewMode.setObjectName(u"frameViewMode")
        self.frameViewMode.setMinimumSize(QSize(0, 120))
        self.frameViewMode.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.frameViewMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameViewMode.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonPlan = QPushButton(self.frameViewMode)
        self.pushButtonPlan.setObjectName(u"pushButtonPlan")
        self.pushButtonPlan.setGeometry(QRect(5, 50, 46, 31))
        self.pushButtonPlan.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonPlan.setCheckable(False)
        self.pushButtonPlan.setFlat(False)
        self.labelViewMode = QLabel(self.frameViewMode)
        self.labelViewMode.setObjectName(u"labelViewMode")
        self.labelViewMode.setGeometry(QRect(5, 0, 71, 16))
        self.comboBoxViewMode = QComboBox(self.frameViewMode)
        self.comboBoxViewMode.addItem("")
        self.comboBoxViewMode.addItem("")
        self.comboBoxViewMode.addItem("")
        self.comboBoxViewMode.setObjectName(u"comboBoxViewMode")
        self.comboBoxViewMode.setGeometry(QRect(5, 20, 96, 22))
        self.comboBoxViewMode.setStyleSheet(u"QComboBox {\n"
"    background-color: white; \n"
"    color: black;             /* Text color */\n"
"}")
        self.comboBoxViewMode.setEditable(False)
        self.comboBoxViewMode.setFrame(True)
        self.pushButtonFront = QPushButton(self.frameViewMode)
        self.pushButtonFront.setObjectName(u"pushButtonFront")
        self.pushButtonFront.setGeometry(QRect(55, 50, 46, 31))
        self.pushButtonFront.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonFront.setCheckable(False)
        self.pushButtonFront.setFlat(False)
        self.pushButtonSide = QPushButton(self.frameViewMode)
        self.pushButtonSide.setObjectName(u"pushButtonSide")
        self.pushButtonSide.setGeometry(QRect(5, 85, 46, 31))
        self.pushButtonSide.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButtonSide.setCheckable(False)
        self.pushButtonSide.setFlat(False)
        self.pushButton3D = QPushButton(self.frameViewMode)
        self.pushButton3D.setObjectName(u"pushButton3D")
        self.pushButton3D.setGeometry(QRect(55, 85, 46, 31))
        self.pushButton3D.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0; /* Elegant Blue */\n"
"    color: black;             /* Text color */\n"
"}")
        self.pushButton3D.setCheckable(False)
        self.pushButton3D.setFlat(False)

        self.verticalLayout_3.addWidget(self.frameViewMode)

        self.verticalSpacer_LeftButtons_Bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_LeftButtons_Bottom)


        self.horizontalLayout_2.addWidget(self.widgetLeftButtons)

        self.widgetMainCAD = QWidget(self.widgetMain_Middle)
        self.widgetMainCAD.setObjectName(u"widgetMainCAD")
        self.widgetMainCAD.setMinimumSize(QSize(300, 300))
        self.horizontalLayout_5 = QHBoxLayout(self.widgetMainCAD)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frameTemporaryMainCAD = QFrame(self.widgetMainCAD)
        self.frameTemporaryMainCAD.setObjectName(u"frameTemporaryMainCAD")
        self.frameTemporaryMainCAD.setStyleSheet(u"background-color: white;")
        self.frameTemporaryMainCAD.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTemporaryMainCAD.setFrameShadow(QFrame.Shadow.Raised)
        self.labelTemporaryCadView = QLabel(self.frameTemporaryMainCAD)
        self.labelTemporaryCadView.setObjectName(u"labelTemporaryCadView")
        self.labelTemporaryCadView.setGeometry(QRect(245, 265, 286, 56))
        font = QFont()
        font.setPointSize(24)
        self.labelTemporaryCadView.setFont(font)

        self.horizontalLayout_5.addWidget(self.frameTemporaryMainCAD)


        self.horizontalLayout_2.addWidget(self.widgetMainCAD)

        self.splitterMain_Docker.addWidget(self.widgetMain_Middle)
        self.widgetDockerBottom = QWidget(self.splitterMain_Docker)
        self.widgetDockerBottom.setObjectName(u"widgetDockerBottom")
        self.widgetDockerBottom.setMinimumSize(QSize(0, 200))
        self.widgetDockerBottom.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(self.widgetDockerBottom)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidgetDockerBottom = QTabWidget(self.widgetDockerBottom)
        self.tabWidgetDockerBottom.setObjectName(u"tabWidgetDockerBottom")
        self.tabWidgetDockerBottom.setMinimumSize(QSize(0, 0))
        self.tabWidgetDockerBottom.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabCabinetLibrary = QWidget()
        self.tabCabinetLibrary.setObjectName(u"tabCabinetLibrary")
        self.tabWidgetDockerBottom.addTab(self.tabCabinetLibrary, "")
        self.tabMaterialLibrary = QWidget()
        self.tabMaterialLibrary.setObjectName(u"tabMaterialLibrary")
        self.tabWidgetDockerBottom.addTab(self.tabMaterialLibrary, "")

        self.horizontalLayout_3.addWidget(self.tabWidgetDockerBottom)

        self.splitterMain_Docker.addWidget(self.widgetDockerBottom)

        self.verticalLayout.addWidget(self.splitterMain_Docker)

        self.splitterMain_Right.addWidget(self.widgetLeft)
        self.widgetRight = QWidget(self.splitterMain_Right)
        self.widgetRight.setObjectName(u"widgetRight")
        self.widgetRight.setMinimumSize(QSize(250, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widgetRight)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitterProject_ObjectTree = QSplitter(self.widgetRight)
        self.splitterProject_ObjectTree.setObjectName(u"splitterProject_ObjectTree")
        self.splitterProject_ObjectTree.setOrientation(Qt.Orientation.Vertical)
        self.splitterProject_ObjectTree.setHandleWidth(10)
        self.tabWidgetRightMenuTop = QTabWidget(self.splitterProject_ObjectTree)
        self.tabWidgetRightMenuTop.setObjectName(u"tabWidgetRightMenuTop")
        self.tabWidgetRightMenuTop.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabProject = QWidget()
        self.tabProject.setObjectName(u"tabProject")
        self.gridLayout = QGridLayout(self.tabProject)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.tabProject)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label = QLabel(self.tabProject)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.tabProject)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tabProject)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.tabWidgetRightMenuTop.addTab(self.tabProject, "")
        self.tabProperties = QWidget()
        self.tabProperties.setObjectName(u"tabProperties")
        self.gridLayout_2 = QGridLayout(self.tabProperties)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelSelectedToolOrObject = QLabel(self.tabProperties)
        self.labelSelectedToolOrObject.setObjectName(u"labelSelectedToolOrObject")
        self.labelSelectedToolOrObject.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(14)
        self.labelSelectedToolOrObject.setFont(font1)
        self.labelSelectedToolOrObject.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayout_2.addWidget(self.labelSelectedToolOrObject, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.tabWidgetRightMenuTop.addTab(self.tabProperties, "")
        self.tabAdvanced = QWidget()
        self.tabAdvanced.setObjectName(u"tabAdvanced")
        self.tabWidgetRightMenuTop.addTab(self.tabAdvanced, "")
        self.splitterProject_ObjectTree.addWidget(self.tabWidgetRightMenuTop)
        self.tabWidgetRightMenuBottom = QTabWidget(self.splitterProject_ObjectTree)
        self.tabWidgetRightMenuBottom.setObjectName(u"tabWidgetRightMenuBottom")
        self.tabObjectTree = QWidget()
        self.tabObjectTree.setObjectName(u"tabObjectTree")
        self.tabWidgetRightMenuBottom.addTab(self.tabObjectTree, "")
        self.tabWarnings = QWidget()
        self.tabWarnings.setObjectName(u"tabWarnings")
        self.tabWidgetRightMenuBottom.addTab(self.tabWarnings, "")
        self.tabCutlist = QWidget()
        self.tabCutlist.setObjectName(u"tabCutlist")
        self.tabWidgetRightMenuBottom.addTab(self.tabCutlist, "")
        self.splitterProject_ObjectTree.addWidget(self.tabWidgetRightMenuBottom)

        self.verticalLayout_2.addWidget(self.splitterProject_ObjectTree)

        self.splitterMain_Right.addWidget(self.widgetRight)

        self.horizontalLayout.addWidget(self.splitterMain_Right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1088, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTheme = QMenu(self.menuView)
        self.menuTheme.setObjectName(u"menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_Reset)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)

        self.retranslateUi(MainWindow)

        self.pushButtonWall.setDefault(False)
        self.pushButtonDoor.setDefault(False)
        self.pushButtonWindow.setDefault(False)
        self.pushButtonFloor.setDefault(False)
        self.pushButtonCeiling.setDefault(False)
        self.pushButtonBulkhead.setDefault(False)
        self.pushButtonObject.setDefault(False)
        self.pushButtonLine.setDefault(False)
        self.pushButtonMeasure.setDefault(False)
        self.pushButtonBox.setDefault(False)
        self.pushButtonCircle.setDefault(False)
        self.pushButtonPlan.setDefault(False)
        self.pushButtonFront.setDefault(False)
        self.pushButtonSide.setDefault(False)
        self.pushButton3D.setDefault(False)
        self.tabWidgetDockerBottom.setCurrentIndex(1)
        self.tabWidgetRightMenuTop.setCurrentIndex(1)
        self.tabWidgetRightMenuBottom.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyCab Studio", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.action_Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButtonWall.setText(QCoreApplication.translate("MainWindow", u"Wall", None))
        self.pushButtonDoor.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.pushButtonWindow.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.pushButtonFloor.setText(QCoreApplication.translate("MainWindow", u"Floor", None))
        self.pushButtonCeiling.setText(QCoreApplication.translate("MainWindow", u"Ceiling", None))
        self.pushButtonBulkhead.setText(QCoreApplication.translate("MainWindow", u"Bulkh.", None))
        self.labelBuild.setText(QCoreApplication.translate("MainWindow", u"BUILD", None))
        self.pushButtonObject.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.labelObject.setText(QCoreApplication.translate("MainWindow", u"OBJECT", None))
        self.pushButtonLine.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.pushButtonMeasure.setText(QCoreApplication.translate("MainWindow", u"Mes.", None))
        self.pushButtonBox.setText(QCoreApplication.translate("MainWindow", u"Box", None))
        self.pushButtonCircle.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.labelDraw.setText(QCoreApplication.translate("MainWindow", u"DRAW", None))
        self.pushButtonPlan.setText(QCoreApplication.translate("MainWindow", u"Plan", None))
        self.labelViewMode.setText(QCoreApplication.translate("MainWindow", u"VIEW MODE", None))
        self.comboBoxViewMode.setItemText(0, QCoreApplication.translate("MainWindow", u"Wireframe", None))
        self.comboBoxViewMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Hidden", None))
        self.comboBoxViewMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Solid", None))

        self.pushButtonFront.setText(QCoreApplication.translate("MainWindow", u"Front", None))
        self.pushButtonSide.setText(QCoreApplication.translate("MainWindow", u"Side", None))
        self.pushButton3D.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.labelTemporaryCadView.setText(QCoreApplication.translate("MainWindow", u"CAD VIEW HERE", None))
        self.tabWidgetDockerBottom.setTabText(self.tabWidgetDockerBottom.indexOf(self.tabCabinetLibrary), QCoreApplication.translate("MainWindow", u"Cabinet Library ", None))
        self.tabWidgetDockerBottom.setTabText(self.tabWidgetDockerBottom.indexOf(self.tabMaterialLibrary), QCoreApplication.translate("MainWindow", u"Material Library", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Project:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Client:", None))
        self.tabWidgetRightMenuTop.setTabText(self.tabWidgetRightMenuTop.indexOf(self.tabProject), QCoreApplication.translate("MainWindow", u"Project", None))
        self.labelSelectedToolOrObject.setText(QCoreApplication.translate("MainWindow", u"selected tool or object", None))
        self.tabWidgetRightMenuTop.setTabText(self.tabWidgetRightMenuTop.indexOf(self.tabProperties), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.tabWidgetRightMenuTop.setTabText(self.tabWidgetRightMenuTop.indexOf(self.tabAdvanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.tabWidgetRightMenuBottom.setTabText(self.tabWidgetRightMenuBottom.indexOf(self.tabObjectTree), QCoreApplication.translate("MainWindow", u"Object tree", None))
        self.tabWidgetRightMenuBottom.setTabText(self.tabWidgetRightMenuBottom.indexOf(self.tabWarnings), QCoreApplication.translate("MainWindow", u"Warnings", None))
        self.tabWidgetRightMenuBottom.setTabText(self.tabWidgetRightMenuBottom.indexOf(self.tabCutlist), QCoreApplication.translate("MainWindow", u"Cutlist", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

