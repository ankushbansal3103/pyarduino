# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarduino.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import subprocess
from serial.tools.list_ports import comports
import sys
import time
import icon_rc
cwd = os.getcwd()



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))                                                  #defining the main window and it's layout
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        icon = QtGui.QIcon()
        MainWindow.setIconSize(QtCore.QSize(30, 24))

        myPixmap = QtGui.QPixmap(_fromUtf8(":/icons/Python Arduino Logo4.png"))                            # adding main window icon
        #myScaledPixmap = myPixmap.scaled(QtCore.QSize(512,512))
        icon.addPixmap(myPixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)                                               #defining the tab widget and it's layout
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(_fromUtf8("Qtool::QTabWidget{url(:/icons/File-New-icon (1).png)}"))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)


        self.textEdit_2 = QtGui.QTextEdit(self.tab)                                                          # Main Editor
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_2.setStyleSheet("QTextEdit{padding-left:20}")
        self.verticalLayout.addWidget(self.textEdit_2,2)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout.addWidget(self.groupBox)
        self.textEdit = QtGui.QTextEdit(self.tab)                                                             # Console

        """self.horizontalLayout = QtGui.QHBoxLayout(self.textEdit)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolBar_2 = QtGui.QToolBar(self.textEdit)
        self.toolBar_2.setMovable(True)
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        self.horizontalLayout.addWidget(self.toolBar_2,20)"""

        palette = QtGui.QPalette()                                                                            # backgorund color of console
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setTextColor(QtGui.QColor(255,0,55))

        font = QtGui.QFont()                                                                                  #Font appearances
        font.setBold(False)
        font.setItalic(False)
        font.setFamily(_fromUtf8("Consolas"))
        font.setUnderline(False)
        font.setWeight(50)
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)                                                                       #Console should be read on;y
        font.setWordSpacing(0)
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit,1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 0, 0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)                                                               #Adding Menu Bar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menuHelp)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuEdit_2 = QtGui.QMenu(self.menubar)
        self.menuEdit_2.setObjectName(_fromUtf8("menuEdit_2"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)

        self.toolBar = QtGui.QToolBar(MainWindow)                                                               #Adding Toolbar
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.statusBar = QtGui.QStatusBar(MainWindow)                                                           #Adding Status bar
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.dockWidget = QtGui.QDockWidget(MainWindow)                                                         #Dockwidget for list of experiments
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidget.setTitleBarWidget(QtGui.QWidget())
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        self.treeWidget = QtGui.QTreeWidget(self.dockWidgetContents_2)                                           #TreeWidget appearances for experiments list
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropOverwriteMode(True)
        self.treeWidget.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.treeWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))

        font = QtGui.QFont()                                                                                  #font for tree widgets
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(25)                                                                                    #setting font size
        font.setKerning(True)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(169, 163, 170))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(0, brush)

        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)                                                       #defining tree widget's item
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)

         ####### CHANGE 1 ######
        ###item_0 = QtGui.QTreeWidgetItem(self.treeWidget)    TO ADD MAIN HEADING
        ###item_1 = QtGui.QTreeWidgetItem(item_0)             ADD THIS LINE ONCE TO ADD EACH EXPERIMENT
        ###item_1 = QtGui.QTreeWidgetItem(item_0)
        ###item_1 = QtGui.QTreeWidgetItem(item_0)

        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(33)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 0, 0)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

       ######################################## Defining and adding icon to each option in menu bar ###########################################

        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/File-New-icon (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))

        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/File-Open-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))

        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Actions-document-save-as-icon (3).png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.actionPlot = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/plot256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon9)
        self.actionPlot.setObjectName(_fromUtf8("actionPlot"))

        self.actionRun = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/run256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon10)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))

        self.actioncc = QtGui.QAction(MainWindow)
        self.actioncc.setObjectName(_fromUtf8("actioncc"))

        self.actionDebug = QtGui.QAction(MainWindow)
        self.actionDebug.setObjectName(_fromUtf8("actionDebug"))

        self.actionAbout_Software = QtGui.QAction(MainWindow)
        self.actionAbout_Software.setObjectName(_fromUtf8("actionAbout_Software"))
        self.actionAbout_company = QtGui.QAction(MainWindow)
        self.actionAbout_company.setObjectName(_fromUtf8("actionAbout_company"))

        self.actionCut = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cut-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))

        self.actionCopy = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Document-Copy-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))

        self.actionPaste = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Paste-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon6)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))

        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))

        self.actionSelect_All = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Actions-edit-select-all-icon.png")), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionSelect_All.setIcon(icon7)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))

        self.actionUndo = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Undo-icon.png")), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))

        self.actionRedo = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Redo-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon9)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))

        self.actionToolbar = QtGui.QAction(MainWindow)
        self.actionToolbar.setObjectName(_fromUtf8("actionToolbar"))
        self.actionStatusbar = QtGui.QAction(MainWindow)
        self.actionStatusbar.setObjectName(_fromUtf8("actionStatusbar"))

       #################################### Adding all the actions to options of menu bar ########################

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menuEdit_2.addAction(self.actionCut)
        self.menuEdit_2.addAction(self.actionCopy)
        self.menuEdit_2.addAction(self.actionPaste)
        self.menuEdit_2.addAction(self.actionDelete)
        self.menuEdit_2.addAction(self.actionSelect_All)
        self.menuEdit_2.addSeparator()
        self.menuEdit_2.addAction(self.actionUndo)
        self.menuEdit_2.addAction(self.actionRedo)

        self.menuView.addAction(self.actionStatusbar)
        self.menuView.addAction(self.actionToolbar)

        self.menuEdit.addAction(self.actionPlot)
        self.menuEdit.addAction(self.actionRun)
        self.menuEdit.addAction(self.actionDebug)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actioncc)

        self.menuAbout.addAction(self.actionAbout_Software)
        self.menuAbout.addAction(self.actionAbout_company)

        self.menuHelp.addAction(self.menuAbout.menuAction())

        ############################# Adding file,edit,view,help,edit_2 to menubar ################################################

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit_2.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        ############################### Adding icons to tool bar ###################################################

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionSelect_All)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlot)
        self.toolBar.addAction(self.actionRun)


        ############################### Showing port no. on status bar ####################################################

        ports = list(comports())
        port="None"
        for i in ports:
            for j in i:
                if 'Arduino' in j:
                    port = i[0]
        if(port=="None"):
            self.lblBoard = QtGui.QLabel("Arduino Board-- Port NONE--")
        else:
            self.lblBoard = QtGui.QLabel("Arduino -- Port %s--" %port[len(port)-1])
        self.statusBar.addPermanentWidget(self.lblBoard)

        ########### TO DO ############
        ########### Adding new tab  ############

        """self.tabWidget.connect(self.tabWidget, QtCore.SIGNAL("tabCloseRequested (int)"), self.on_close_tab_requested)
        self.tabWidget.connect(self.tabWidget, QtCore.SIGNAL("currentChanged (int)"), self.on_tab_change)

        self.tabButton = QtGui.QToolButton()
        self.tabButton.setText('+')
        self.tabButton.adjustSize()
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tabWidget.setCornerWidget(self.tabButton)
        #self.tabButton.clicked.connect()"""

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #def on_close_tab_requested(self, tabIndex):
        #self.tabWidget.removeTab(tabIndex)

    #def on_tab_change(self, index):
        #self.setWindowTitle(self.title_text % self.tabWidget.tabText(index))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyarduino", None))
        MainWindow.setDockNestingEnabled(True)
        self.groupBox.setTitle(_translate("MainWindow", "Console ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))

        ################ Names to menubar options #################################
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Tool", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuEdit_2.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

        ######################## font for tree widget ###########################################
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setFamily(_fromUtf8("Comic sans"))
        font.setWeight(60)
        font.setPointSize(10)
        font.setUnderline(True)
        self.dockWidget.setFont(font)
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Experiments", None))
        font.setUnderline(False)
        font.setBold(False)
        self.dockWidget.setFont(font)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "                 Experiments ", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.expandAll()

        self.textEdit_2.setFrameStyle(0)

        ############################# Names and icons for tree wadget items #############################

        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", " To glow an LED", None))
        iconled = QtGui.QIcon()
        iconled.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/led256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(0).setIcon(0,iconled)
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "1.1 LED", None))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "1.2 LED", None))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "1.3 LED", None))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "1.4 LED", None))

        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", " Using the Pushbutton", None))
        iconpb = QtGui.QIcon()
        iconpb.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pushbutton1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(1).setIcon(0, iconpb)
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "2.2 Pushbutton", None))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "2.1 Pushbutton", None))

        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", " Using a LDR", None))
        iconldr = QtGui.QIcon()
        iconldr.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/LDR-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(2).setIcon(0, iconldr)
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "3.2 LDR", None))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "3.1 LDR", None))

        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", " Potentiometer", None))
        iconpot = QtGui.QIcon()
        iconpot.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Potentiometer256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(3).setIcon(0, iconpot)
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "4.1 Potentiometer", None))

        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", " DC Motor", None))
        icondc = QtGui.QIcon()
        icondc.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/motor1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(4).setIcon(0, icondc)
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "5.1 DC Motor", None))
        self.treeWidget.topLevelItem(4).child(1).setText(0, _translate("MainWindow", "5.2 DC Motor", None))
        self.treeWidget.topLevelItem(4).child(2).setText(0, _translate("MainWindow", "5.3 DC Motor", None))

        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", " Servomotor", None))
        iconser = QtGui.QIcon()
        iconser.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Servo256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(5).setIcon(0, iconser)
        self.treeWidget.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "6.1 Servomotor", None))
        self.treeWidget.topLevelItem(5).child(1).setText(0, _translate("MainWindow", "6.2 Servomotor", None))
        self.treeWidget.topLevelItem(5).child(2).setText(0, _translate("MainWindow", "6.3 Servomotor", None))
        self.treeWidget.topLevelItem(5).child(3).setText(0, _translate("MainWindow", "6.4 Servomotor", None))

        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", " Energymeter", None))
        iconenergy = QtGui.QIcon()
        iconenergy.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/energy1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.topLevelItem(6).setIcon(0, iconenergy)
        self.treeWidget.topLevelItem(6).child(0).setText(0, _translate("MainWindow", "Energymeter current", None))
        self.treeWidget.topLevelItem(6).child(1).setText(0, _translate("MainWindow", "Energymeter voltage", None))
        self.treeWidget.topLevelItem(6).child(2).setText(0, _translate("MainWindow", "Energymeter power", None))

        self.treeWidget.setSortingEnabled(__sortingEnabled)

        ############### CHANGE 2 #####################

        #self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", " Heading_Name", None))
        #iconenergy = QtGui.QIcon()
        #iconenergy.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Add_Icon_name.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.treeWidget.topLevelItem(7).setIcon(0, iconenergy)                                                     #TO ADD ICON TO HEADING
        #self.treeWidget.topLevelItem(7).child(0).setText(0, _translate("MainWindow", "EXPERIMENT_NAME1", None))    #TO ADD NAME OF EXPERIMENT IN SOFTWARE
        #self.treeWidget.topLevelItem(7).child(1).setText(0, _translate("MainWindow", "EXPERIMENT_NAME2", None))
        #self.treeWidget.topLevelItem(7).child(2).setText(0, _translate("MainWindow", "EXPERIMENT_NAME3", None))

        ############################### Defining name,status bar tip,whats this and shortcut for each option in menu bar ################################

        self.actionNew.setText(_translate("MainWindow", " New Project", None))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file", None))
        self.actionNew.setWhatsThis(_translate("MainWindow", "To create a new file", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))

        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open an existing File", None))
        self.actionOpen.setWhatsThis(_translate("MainWindow", "To open an existing File", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))

        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the current File", None))
        self.actionSave.setWhatsThis(_translate("MainWindow", "To save the current File", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))

        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Rewrites the current File", None))
        self.actionSave_as.setWhatsThis(_translate("MainWindow", "To save the current File", None))

        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit from the application", None))
        self.actionExit.setWhatsThis(_translate("MainWindow", "To exit from the application ", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Alt+F4", None))

        self.actionPlot.setText(_translate("MainWindow", "Plot", None))
        self.actionPlot.setStatusTip(_translate("MainWindow", "Plot a live graph for analog data ", None))
        self.actionPlot.setWhatsThis(_translate("MainWindow", "To plot a live graph ", None))
        self.actionPlot.setShortcut(_translate("MainWindow", "F5", None))

        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionRun.setStatusTip(_translate("MainWindow", "Run the current experiment ", None))
        self.actionRun.setWhatsThis(_translate("MainWindow", "To run the current experiment", None))
        self.actionRun.setShortcut(_translate("MainWindow", "F6", None))

        self.actioncc.setText(_translate("MainWindow", "Clear console", None))
        self.actioncc.setStatusTip(_translate("MainWindow", "Clear the console", None))
        self.actioncc.setWhatsThis(_translate("MainWindow", "To clear the console", None))
        self.actioncc.setShortcut(_translate("MainWindow", "Del", None))

        self.actioncc = QtGui.QAction(MainWindow)
        self.actioncc.setObjectName(_fromUtf8("actioncc"))

        self.actionDebug.setText(_translate("MainWindow", "Debug", None))

        self.actionAbout_Software.setText(_translate("MainWindow", "About Pyarduino", None))
        self.actionAbout_Software.setStatusTip(_translate("MainWindow", "To know about Pyarduino", None))
        self.actionAbout_Software.setWhatsThis(_translate("MainWindow", "To know about Pyarduino ", None))

        self.actionAbout_company.setText(_translate("MainWindow", "About company", None))
        self.actionAbout_company.setStatusTip(_translate("MainWindow", "to Know about the company", None))
        self.actionAbout_company.setWhatsThis(_translate("MainWindow", "to Know about the company ", None))

        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionCut.setStatusTip(_translate("MainWindow", "cut the selected item", None))
        self.actionCut.setWhatsThis(_translate("MainWindow", "To cut the selected item", None))

        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionCopy.setStatusTip(_translate("MainWindow", "copy the selected item", None))
        self.actionCopy.setWhatsThis(_translate("MainWindow", "To copy the selected item", None))

        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionPaste.setStatusTip(_translate("MainWindow", "paste the selected item", None))
        self.actionPaste.setWhatsThis(_translate("MainWindow", "To paste the selected item", None))

        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setStatusTip(_translate("MainWindow", "delete the selected item", None))
        self.actionDelete.setWhatsThis(_translate("MainWindow", "To delete the selected item", None))

        self.actionSelect_All.setText(_translate("MainWindow", "Select All", None))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionSelect_All.setStatusTip(_translate("MainWindow", "select all items", None))
        self.actionSelect_All.setWhatsThis(_translate("MainWindow", "To select all", None))

        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionUndo.setStatusTip(_translate("MainWindow", "undo the last task", None))
        self.actionUndo.setWhatsThis(_translate("MainWindow", "To undo the last task", None))

        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y", None))
        self.actionRedo.setStatusTip(_translate("MainWindow", "redo the last task", None))
        self.actionRedo.setWhatsThis(_translate("MainWindow", "To redo the last task", None))

        self.actionToolbar.setText(_translate("MainWindow", "Tool bar", None))
        self.actionToolbar.setStatusTip(_translate("MainWindow", "hide/show the tool bar", None))
        self.actionToolbar.setWhatsThis(_translate("MainWindow", "To hide/show the tool bar", None))

        self.actionStatusbar.setText(_translate("MainWindow", "Status bar", None))
        self.actionStatusbar.setStatusTip(_translate("MainWindow", "hide/show the Status bar", None))
        self.actionStatusbar.setWhatsThis(_translate("MainWindow", "To hide/show the Status bar", None))

        ##################################### Connecting each option with their associated functions ############################
        self.actionNew.triggered.connect(self.newDialog)
        self.actionOpen.triggered.connect(self.openDialog)
        self.actionSave.triggered.connect(self.saveDialog)
        self.actionExit.triggered.connect(self.ExitDialog)

        self.actionCut.triggered.connect(self.cutdialog)
        self.actionCopy.triggered.connect(self.copydialog)
        self.actionPaste.triggered.connect(self.pastedialog)
        self.actionDelete.triggered.connect(self.deletedialog)
        self.actionSelect_All.triggered.connect(self.selectalldialog)
        self.actionUndo.triggered.connect(self.undodialog)
        self.actionRedo.triggered.connect(self.redodialog)

        self.actionToolbar.triggered.connect(self.toggleToolbar)
        self.actionStatusbar.triggered.connect(self.toggleStatusbar)

        self.actionPlot.triggered.connect(self.on_plot_button_clicked)
        self.actionRun.triggered.connect(self.on_run_button_clicked)
        self.actioncc.triggered.connect(self.on_cc_button_clicked)

        self.actionAbout_company.triggered.connect(self.on_about_qt)

        #################################### Adding the lower title bar ################################################
        fileInfoBox = QtGui.QHBoxLayout()
        self.verticalLayout.addLayout(fileInfoBox, 0)
        self.lblFileName = QtGui.QLabel()
        self.lblFileName.setText("Welcome to Pyarduino !")
        style_grad = "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #efefef, stop: 1 %s);" % "#6A7885"
        style_grad += "font-weight: bold; border: 1px outset #41484E; padding: 3px;"
        self.lblFileName.setStyleSheet(style_grad)
        fileInfoBox.addWidget(self.lblFileName, 4)

        ##################################Adding the 'RUN' and 'PLOT' button to lower title bar ########################
        self.buttonRun = QtGui.QPushButton()
        self.buttonRun.setText("  RUN")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/run256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRun.setIcon(icon10)
        fileInfoBox.addWidget(self.buttonRun, 1)
        self.buttonRun.clicked.connect(self.on_run_button_clicked)

        self.buttonPlot = QtGui.QPushButton()
        self.buttonPlot.setText("  PLOT")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/plot256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlot.setIcon(icon9)
        fileInfoBox.addWidget(self.buttonPlot, 1)
        self.buttonPlot.clicked.connect(self.on_plot_button_clicked)

        self.buttoncc = QtGui.QPushButton()
        self.buttoncc.setText(" Clear Console")
        iconcc = QtGui.QIcon()
        iconcc.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/clear1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttoncc.setIcon(iconcc)
        fileInfoBox.addWidget(self.buttoncc, 1)
        self.buttoncc.clicked.connect(self.on_cc_button_clicked)

        self.treeWidget.itemDoubleClicked.connect(self.open_Dialog) # function called if any tree item is double clicked

    def open_Dialog(self, index):                                   # opens the corresponding file and set it's data to the text editor,changes

        colmIndex = 0                                               # title bar name and tab name
        f = None
        if ((self.treeWidget.currentItem().text(colmIndex)) == "1.1 LED"):
            f = open(cwd+"\\Examples\\4.1LED.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1.1 LED", None))
            self.lblFileName.setText("1.1 LED")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "1.2 LED"):
            f = open(cwd+"\\Examples\\4.2LED.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1.2 LED", None))
            self.lblFileName.setText("1.2 LED")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "1.3 LED"):
            f = open(cwd+"\\Examples\\4.3LED.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1.3 LED", None))
            self.lblFileName.setText("1.3 LED")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "1.4 LED"):
            f = open(cwd+"\\Examples\\4.4LED.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1.4 LED", None))
            self.lblFileName.setText("1.4 LED")

        elif ((self.treeWidget.currentItem().text(colmIndex)) == "2.1 Pushbutton"):
            f = open(cwd+"\\Examples\\5.1Pushbutton.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2.1 Pushbutton", None))
            self.lblFileName.setText("2.1 Pushbutton")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "2.2 Pushbutton"):
            f = open(cwd+"\\Examples\\5.2Pushbutton.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2.2 Pushbutton", None))
            self.lblFileName.setText("2.2 Pushbutton")

        elif ((self.treeWidget.currentItem().text(colmIndex)) == "3.1 LDR"):
            f = open(cwd+"\\Examples\\6.1LDR.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),_translate("MainWindow", "3.1LDR", None))
            self.lblFileName.setText("3.1 LDR")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "3.2 LDR"):
            f = open(cwd+"\\Examples\\6.2LDR.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "3.2LDR", None))
            self.lblFileName.setText("3.2 LDR")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "4.1 Potentiometer"):
            f = open(cwd+"\\Examples\\8.1Potentiometer.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "4.1 Potentiometer", None))
            self.lblFileName.setText("4.1 Potentiometer")

        elif ((self.treeWidget.currentItem().text(colmIndex)) == "5.1 DC Motor"):
            f = open(cwd+"\\Examples\\7.1DCMotor.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "5.1 DC Motor", None))
            self.lblFileName.setText("5.1 DC Motor")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "5.2 DC Motor"):
            f = open(cwd+"\\Examples\\7.2DCMotor.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "5.2 DC Motor", None))
            self.lblFileName.setText("5.2 DC Motor")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "5.3 DC Motor"):
            f = open(cwd+"\\Examples\\7.3DCMotor.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "5.3 DC Motor", None))
            self.lblFileName.setText("5.3 DC Motor")

        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.1 Servomotor"):
            f = open(cwd+"\\Examples\\9.1Servo.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "6.1Servomotor", None))
            self.lblFileName.setText("6.1 Servomotor")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.2 Servomotor"):
            f = open(cwd+"\\Examples\\9.2Servo.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "6.2Servomotor", None))
            self.lblFileName.setText("6.2 Servomotor")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.3 Servomotor"):
            f = open(cwd+"\\Examples\\9.3Servo.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "6.3Servomotor", None))
            self.lblFileName.setText("6.3 Servomotor")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.4 Servomotor"):
            f = open(cwd+"\\Examples\\9.4Servo.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "6.4Servomotor", None))
            self.lblFileName.setText("6.4 Servomotor")

        elif ((self.treeWidget.currentItem().text(colmIndex)) == "Energymeter current"):
            f = open(cwd+"\\Examples\\energy_meter_current.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Energymeter current", None))
            self.lblFileName.setText("Energymeter current")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "Energymeter voltage"):
            f = open(cwd+"\\Examples\\energy_meter_voltage.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),_translate("MainWindow", "Energymeter voltage", None))
            self.lblFileName.setText("Energymeter voltage")
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "Energymeter power"):
            f = open(cwd+"\\Examples\\energy_meter_power.py", 'r')
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),_translate("MainWindow", "Energymeter power", None))
            self.lblFileName.setText("Energymeter power")

         ####################### CHANGE 3 #################

        #elif ((self.treeWidget.currentItem().text(colmIndex)) == "EXPERIMENT_NAME1"):
            #f = open(cwd+"\\Examples\\File_name.py", 'r')
            #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
             #                         _translate("MainWindow", "EXPERIMENT_NAME1", None))                  #TO CHANGE TAB NAME
            #self.lblFileName.setText("EXPERIMENT_NAME1")                                                   #TO CHANGE LABEL NAME AT THE BOTTOM

        with f:
            self.textEdit_2.clear()
            data = f.read()
            self.textEdit_2.setText(data)

    def on_cc_button_clicked(self):                                          ##### clears the console
        self.textEdit.clear()


    def on_run_button_clicked(self):                                         ###### runs the corresponding experiment in the background
        colmIndex=0
        if ((self.treeWidget.currentItem().text(colmIndex)) == "1.1 LED"):
            pathname='4.1LED.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "1.2 LED"):
            pathname = '4.2LED.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "1.3 LED"):
            pathname = '4.3LED.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "1.4 LED"):
            pathname = '4.4LED.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "2.1 Pushbutton"):
            pathname = '5.1Pushbutton.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "2.2 Pushbutton"):
            pathname = '5.2Pushbutton.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "3.1 LDR"):
            pathname = '6.1LDR.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "3.2 LDR"):
            pathname = '6.2LDR.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "4.1 Potentiometer"):
            pathname='8.1Potentiometer.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "5.1 DC Motor"):
            pathname = '7.1DCMotor.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "5.1 DC Motor"):
            pathname = '7.2DCMotor.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "5.1 DC Motor"):
            pathname = '7.3DCMotor.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.1 Servomotor"):
            pathname = '8.1Servo.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.2 Servomotor"):
            pathname = '8.2Servo.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.3 Servomotor"):
            pathname = '8.3Servo.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "6.4 Servomotor"):
            pathname = '8.4Servo.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "Energymeter current"):
            pathname = 'energy_meter_current.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "Energymeter voltage"):
            pathname = 'energy_meter_voltage.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "Energymeter power"):
            pathname = 'energy_meter_power.py'

        ############## CHANGE 4 ########################

        #elif ((self.treeWidget.currentItem().text(colmIndex)) == "EXPERIMENT_NAME"):
        #   pathname = 'FILE_NAME.py'

        os.chdir(cwd+"\\Examples")
        subprocess.call(['python', pathname], shell=True)
        try:
            #otput = subprocess.check_output(['python', pathname],stderr=subprocess.STDOUT, shell=True)
            p = subprocess.Popen(['python', pathname], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            color = QtGui.QColor(255, 0, 0)
            self.textEdit.setTextColor(color)
            self.textEdit.append(exc.output)
        else:
            color=QtGui.QColor(255,10,10)
            self.textEdit.setTextColor(color)

            for line in iter(p.stdout.readline, b""):
                self.textEdit.append(line)
            p.stdout.close()
            p.wait()

    def on_plot_button_clicked(self):                                             # plots for the analog data
        colmIndex = 0
        if ((self.treeWidget.currentItem().text(colmIndex)) == "2.1 Pushbutton"):
            pathname = '5.1Pushbuttonplot.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "2.2 Pushbutton"):
            pathname = '5.2Pushbuttonplot.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "3.1 LDR"):
            pathname = '6.1LDRplot.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "3.2 LDR"):
            pathname = '6.2LDRplot.py'
        elif ((self.treeWidget.currentItem().text(colmIndex)) == "4.1 Potentiometer"):
            pathname = '8.1Potentiometerplot.py'

        os.chdir(cwd+"\\Examples")                                                 # changes the current directory
        subprocess.call(['python', pathname], shell=True)                          # calls the command in the terminal
        try:
            # otput = subprocess.check_output(['python', pathname],stderr=subprocess.STDOUT, shell=True)
            p = subprocess.Popen(['python', pathname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)   #checks  for the output from the command
        except subprocess.CalledProcessError as exc:
            color = QtGui.QColor(255, 0, 0)
            self.textEdit.append(exc.output)
        else:
            color = QtGui.QColor(0, 0, 255)
            self.textEdit.setTextColor(color)
            for line in iter(p.stdout.readline, b""):
                self.textEdit.append(line)
            p.stdout.close()
            p.wait()

    def newDialog(self):                            # opens blank editor
        self.textEdit_2.clear()

    def openDialog(self):                           # opens file browser dialog box
        fname = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open file', 'C://', 'All files (*.*)')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit_2.setText(data)

    def saveDialog(self):                            # saves the current text in a file
        fname = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save file', cwd,
                                                  'Python files (*.py)')
        f = open(fname, 'w')
        with f:
            data = self.textEdit_2.toPlainText()
            f.write(data)
            f.close()

    def ExitDialog(self):                            #TO exit from the application
        exit_msg = "Are you sure you want to exit the program ? All unsaved data will be lost."
        reply = QtGui.QMessageBox.question(MainWindow,'Message',
                                            exit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            QtGui.qApp.quit()
        else:
            pass

    ######### to edit texts in the editor ########################
    def cutdialog(self):
        self.textEdit_2.cut()

    def copydialog(self):
        self.textEdit_2.copy()

    def pastedialog(self):
        self.textEdit_2.paste()

    def deletedialog(self):
        self.textEdit_2.clear()

    def selectalldialog(self):
        self.textEdit_2.selectAll()

    def undodialog(self):
        self.textEdit_2.undo()

    def redodialog(self):
        self.textEdit_2.redo()

    def on_about_qt(self):
        QtGui.QMessageBox.aboutQt('About Qt')

    def toggleToolbar(self):                        # To check visibility of toolbar
        state = self.toolBar.isVisible()
        self.toolBar.setVisible(not state)           # Set the visibility to its inverse
        if state:
            self.actionToolbar.setText(_translate("MainWindow", "Show Tool bar", None))
        else:
            self.actionToolbar.setText(_translate("MainWindow", "Hide Tool bar", None))


    def toggleStatusbar(self):                     # To check visibility of statusbar
        state = self.statusBar.isVisible()
        self.statusBar.setVisible(not state)        # Set the visibility to its inverse


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    #splash_pix = QtGui.QPixmap('../../images/Python Arduino Logo4.png')
    #splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    #splash.setMask(splash_pix.mask())
    #splash.show()

    ################################# to display welcome screen #########################################################

    splash_pix = QtGui.QPixmap(_fromUtf8(":/icons/Python Main Page.jpg"))
    splash = QtGui.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    progressBar = QtGui.QProgressBar(splash)                                              # adding progress bar
    progressBar.setTextVisible(False)
    splash.showMessage('Discovering Nodes...')                                            # adding message
    splash.show()
    app.processEvents()
    for i in range(0, 100):
        progressBar.setValue(i)
        time.sleep(0.05)                                                                    # Simulate something that takes time
    splash.close()

    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
