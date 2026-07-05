# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowxjCeKz.ui'
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
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

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
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
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
        self.lineEditProject = QLineEdit(self.tabProject)
        self.lineEditProject.setObjectName(u"lineEditProject")

        self.gridLayout.addWidget(self.lineEditProject, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.labelProject = QLabel(self.tabProject)
        self.labelProject.setObjectName(u"labelProject")

        self.gridLayout.addWidget(self.labelProject, 0, 0, 1, 1)

        self.labelClient = QLabel(self.tabProject)
        self.labelClient.setObjectName(u"labelClient")

        self.gridLayout.addWidget(self.labelClient, 1, 0, 1, 1)

        self.lineEditClient = QLineEdit(self.tabProject)
        self.lineEditClient.setObjectName(u"lineEditClient")
        self.lineEditClient.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lineEditClient, 1, 1, 1, 1)

        self.tabWidgetRightMenuTop.addTab(self.tabProject, "")
        self.tabProperties = QWidget()
        self.tabProperties.setObjectName(u"tabProperties")
        self.verticalLayout_5 = QVBoxLayout(self.tabProperties)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widgetProperties_1 = QWidget(self.tabProperties)
        self.widgetProperties_1.setObjectName(u"widgetProperties_1")
        self.widgetProperties_1.setMinimumSize(QSize(0, 25))
        self.widgetProperties_1.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_4 = QHBoxLayout(self.widgetProperties_1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.labelSelectedToolOrObject = QLabel(self.widgetProperties_1)
        self.labelSelectedToolOrObject.setObjectName(u"labelSelectedToolOrObject")
        self.labelSelectedToolOrObject.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(14)
        self.labelSelectedToolOrObject.setFont(font1)
        self.labelSelectedToolOrObject.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_4.addWidget(self.labelSelectedToolOrObject)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.widgetProperties_1)

        self.widgetProperties_2 = QWidget(self.tabProperties)
        self.widgetProperties_2.setObjectName(u"widgetProperties_2")
        self.horizontalLayout_6 = QHBoxLayout(self.widgetProperties_2)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.labelPosition = QLabel(self.widgetProperties_2)
        self.labelPosition.setObjectName(u"labelPosition")
        self.labelPosition.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_6.addWidget(self.labelPosition)

        self.labelPositionX = QLabel(self.widgetProperties_2)
        self.labelPositionX.setObjectName(u"labelPositionX")
        self.labelPositionX.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelPositionX.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelPositionX)

        self.spinBoxPositionX = QSpinBox(self.widgetProperties_2)
        self.spinBoxPositionX.setObjectName(u"spinBoxPositionX")
        self.spinBoxPositionX.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_6.addWidget(self.spinBoxPositionX)


        self.verticalLayout_5.addWidget(self.widgetProperties_2)

        self.widgetProperties_3 = QWidget(self.tabProperties)
        self.widgetProperties_3.setObjectName(u"widgetProperties_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widgetProperties_3)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.labelPositionBlank1 = QLabel(self.widgetProperties_3)
        self.labelPositionBlank1.setObjectName(u"labelPositionBlank1")
        self.labelPositionBlank1.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_8.addWidget(self.labelPositionBlank1)

        self.labelPositionY = QLabel(self.widgetProperties_3)
        self.labelPositionY.setObjectName(u"labelPositionY")
        self.labelPositionY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelPositionY.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.labelPositionY)

        self.spinBoxPositionY = QSpinBox(self.widgetProperties_3)
        self.spinBoxPositionY.setObjectName(u"spinBoxPositionY")
        self.spinBoxPositionY.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_8.addWidget(self.spinBoxPositionY)


        self.verticalLayout_5.addWidget(self.widgetProperties_3)

        self.widgetProperties_4 = QWidget(self.tabProperties)
        self.widgetProperties_4.setObjectName(u"widgetProperties_4")
        self.horizontalLayout_9 = QHBoxLayout(self.widgetProperties_4)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.labelPositionBlank2 = QLabel(self.widgetProperties_4)
        self.labelPositionBlank2.setObjectName(u"labelPositionBlank2")
        self.labelPositionBlank2.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_9.addWidget(self.labelPositionBlank2)

        self.labelPositionZ = QLabel(self.widgetProperties_4)
        self.labelPositionZ.setObjectName(u"labelPositionZ")
        self.labelPositionZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelPositionZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.labelPositionZ)

        self.spinBoxPositionZ = QSpinBox(self.widgetProperties_4)
        self.spinBoxPositionZ.setObjectName(u"spinBoxPositionZ")
        self.spinBoxPositionZ.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_9.addWidget(self.spinBoxPositionZ)


        self.verticalLayout_5.addWidget(self.widgetProperties_4)

        self.line = QFrame(self.tabProperties)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.widgetProperties_5 = QWidget(self.tabProperties)
        self.widgetProperties_5.setObjectName(u"widgetProperties_5")
        self.horizontalLayout_11 = QHBoxLayout(self.widgetProperties_5)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.labelRotation = QLabel(self.widgetProperties_5)
        self.labelRotation.setObjectName(u"labelRotation")
        self.labelRotation.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_11.addWidget(self.labelRotation)

        self.labelRotationX = QLabel(self.widgetProperties_5)
        self.labelRotationX.setObjectName(u"labelRotationX")
        self.labelRotationX.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelRotationX.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.labelRotationX)

        self.spinBoxRotationX = QSpinBox(self.widgetProperties_5)
        self.spinBoxRotationX.setObjectName(u"spinBoxRotationX")
        self.spinBoxRotationX.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_11.addWidget(self.spinBoxRotationX)


        self.verticalLayout_5.addWidget(self.widgetProperties_5)

        self.widgetProperties_6 = QWidget(self.tabProperties)
        self.widgetProperties_6.setObjectName(u"widgetProperties_6")
        self.horizontalLayout_12 = QHBoxLayout(self.widgetProperties_6)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.labelRotationBlank1 = QLabel(self.widgetProperties_6)
        self.labelRotationBlank1.setObjectName(u"labelRotationBlank1")
        self.labelRotationBlank1.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_12.addWidget(self.labelRotationBlank1)

        self.labelRotationY = QLabel(self.widgetProperties_6)
        self.labelRotationY.setObjectName(u"labelRotationY")
        self.labelRotationY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelRotationY.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.labelRotationY)

        self.spinBoxRotationY = QSpinBox(self.widgetProperties_6)
        self.spinBoxRotationY.setObjectName(u"spinBoxRotationY")
        self.spinBoxRotationY.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_12.addWidget(self.spinBoxRotationY)


        self.verticalLayout_5.addWidget(self.widgetProperties_6)

        self.widgetProperties_7 = QWidget(self.tabProperties)
        self.widgetProperties_7.setObjectName(u"widgetProperties_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widgetProperties_7)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.labelRotationBlank2 = QLabel(self.widgetProperties_7)
        self.labelRotationBlank2.setObjectName(u"labelRotationBlank2")
        self.labelRotationBlank2.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_10.addWidget(self.labelRotationBlank2)

        self.labelRotationZ = QLabel(self.widgetProperties_7)
        self.labelRotationZ.setObjectName(u"labelRotationZ")
        self.labelRotationZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelRotationZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.labelRotationZ)

        self.spinBoxRotationZ = QSpinBox(self.widgetProperties_7)
        self.spinBoxRotationZ.setObjectName(u"spinBoxRotationZ")
        self.spinBoxRotationZ.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.spinBoxRotationZ)


        self.verticalLayout_5.addWidget(self.widgetProperties_7)

        self.line_2 = QFrame(self.tabProperties)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.widgetProperties_8 = QWidget(self.tabProperties)
        self.widgetProperties_8.setObjectName(u"widgetProperties_8")
        self.horizontalLayout_14 = QHBoxLayout(self.widgetProperties_8)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.labelDimension = QLabel(self.widgetProperties_8)
        self.labelDimension.setObjectName(u"labelDimension")
        self.labelDimension.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_14.addWidget(self.labelDimension)

        self.labelDimensionWidth = QLabel(self.widgetProperties_8)
        self.labelDimensionWidth.setObjectName(u"labelDimensionWidth")
        self.labelDimensionWidth.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelDimensionWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.labelDimensionWidth)

        self.spinBoxDimensionWidth = QSpinBox(self.widgetProperties_8)
        self.spinBoxDimensionWidth.setObjectName(u"spinBoxDimensionWidth")
        self.spinBoxDimensionWidth.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_14.addWidget(self.spinBoxDimensionWidth)


        self.verticalLayout_5.addWidget(self.widgetProperties_8)

        self.widgetProperties_9 = QWidget(self.tabProperties)
        self.widgetProperties_9.setObjectName(u"widgetProperties_9")
        self.horizontalLayout_13 = QHBoxLayout(self.widgetProperties_9)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.labelDimensionBlank1 = QLabel(self.widgetProperties_9)
        self.labelDimensionBlank1.setObjectName(u"labelDimensionBlank1")
        self.labelDimensionBlank1.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_13.addWidget(self.labelDimensionBlank1)

        self.labelDimensionDepth = QLabel(self.widgetProperties_9)
        self.labelDimensionDepth.setObjectName(u"labelDimensionDepth")
        self.labelDimensionDepth.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelDimensionDepth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.labelDimensionDepth)

        self.spinBoxDimensionDepth = QSpinBox(self.widgetProperties_9)
        self.spinBoxDimensionDepth.setObjectName(u"spinBoxDimensionDepth")
        self.spinBoxDimensionDepth.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_13.addWidget(self.spinBoxDimensionDepth)


        self.verticalLayout_5.addWidget(self.widgetProperties_9)

        self.widgetProperties_10 = QWidget(self.tabProperties)
        self.widgetProperties_10.setObjectName(u"widgetProperties_10")
        self.horizontalLayout_15 = QHBoxLayout(self.widgetProperties_10)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.labelDimensionBlank2 = QLabel(self.widgetProperties_10)
        self.labelDimensionBlank2.setObjectName(u"labelDimensionBlank2")
        self.labelDimensionBlank2.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_15.addWidget(self.labelDimensionBlank2)

        self.labelDimensionHeight = QLabel(self.widgetProperties_10)
        self.labelDimensionHeight.setObjectName(u"labelDimensionHeight")
        self.labelDimensionHeight.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelDimensionHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.labelDimensionHeight)

        self.spinBoxDimensionHeight = QSpinBox(self.widgetProperties_10)
        self.spinBoxDimensionHeight.setObjectName(u"spinBoxDimensionHeight")
        self.spinBoxDimensionHeight.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_15.addWidget(self.spinBoxDimensionHeight)


        self.verticalLayout_5.addWidget(self.widgetProperties_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

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

        self.verticalLayout_4.addWidget(self.splitterMain_Right)

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
        self.labelProject.setText(QCoreApplication.translate("MainWindow", u"Project:", None))
        self.labelClient.setText(QCoreApplication.translate("MainWindow", u"Client:", None))
        self.tabWidgetRightMenuTop.setTabText(self.tabWidgetRightMenuTop.indexOf(self.tabProject), QCoreApplication.translate("MainWindow", u"Project", None))
        self.labelSelectedToolOrObject.setText(QCoreApplication.translate("MainWindow", u"selected tool or object", None))
        self.labelPosition.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.labelPositionX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.labelPositionBlank1.setText("")
        self.labelPositionY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.labelPositionBlank2.setText("")
        self.labelPositionZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.labelRotation.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.labelRotationX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.labelRotationBlank1.setText("")
        self.labelRotationY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.labelRotationBlank2.setText("")
        self.labelRotationZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.labelDimension.setText(QCoreApplication.translate("MainWindow", u"Dimension", None))
        self.labelDimensionWidth.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.labelDimensionBlank1.setText("")
        self.labelDimensionDepth.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
        self.labelDimensionBlank2.setText("")
        self.labelDimensionHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.tabWidgetRightMenuTop.setTabText(self.tabWidgetRightMenuTop.indexOf(self.tabProperties), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.tabWidgetRightMenuTop.setTabText(self.tabWidgetRightMenuTop.indexOf(self.tabAdvanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.tabWidgetRightMenuBottom.setTabText(self.tabWidgetRightMenuBottom.indexOf(self.tabObjectTree), QCoreApplication.translate("MainWindow", u"Object tree", None))
        self.tabWidgetRightMenuBottom.setTabText(self.tabWidgetRightMenuBottom.indexOf(self.tabWarnings), QCoreApplication.translate("MainWindow", u"Warnings", None))
        self.tabWidgetRightMenuBottom.setTabText(self.tabWidgetRightMenuBottom.indexOf(self.tabCutlist), QCoreApplication.translate("MainWindow", u"Cutlist", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

