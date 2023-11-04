#! /usr/bin/python3
#
# PDF GUI TOOLS - Ui_Windows
# 
# PDF GUI Tools app - Main QT windows file
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# This file is only generated by the files in the project's
# designer directory, change its aspects from there.
#
# -----------------------------------------------------------------------------------

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDockWidget, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, icon):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 827)
        MainWindow.setWindowIcon(icon)
        self.actionAdd_File = QAction(MainWindow)
        self.actionAdd_File.setObjectName(u"actionAdd_File")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionUp = QAction(MainWindow)
        self.actionUp.setObjectName(u"actionUp")
        self.actionDown = QAction(MainWindow)
        self.actionDown.setObjectName(u"actionDown")
        self.actionMerge = QAction(MainWindow)
        self.actionMerge.setObjectName(u"actionMerge")
        self.actionEncrypt = QAction(MainWindow)
        self.actionEncrypt.setObjectName(u"actionEncrypt")
        self.actionDecrypt = QAction(MainWindow)
        self.actionDecrypt.setObjectName(u"actionDecrypt")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionView_Utils = QAction(MainWindow)
        self.actionView_Utils.setObjectName(u"actionView_Utils")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 823, 763))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(20, 35, 20, 20)
        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setStyleSheet(u"")
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setIconSize(QSize(60, 60))
        self.listWidget.setSpacing(20)

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.button_add = QPushButton(self.groupBox)
        self.button_add.setObjectName(u"button_add")
        icon = QIcon(QIcon.fromTheme(u"document-new"))
        self.button_add.setIcon(icon)

        self.verticalLayout_4.addWidget(self.button_add)

        self.button_delete = QPushButton(self.groupBox)
        self.button_delete.setObjectName(u"button_delete")
        icon1 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.button_delete.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.button_delete)

        self.button_up = QPushButton(self.groupBox)
        self.button_up.setObjectName(u"button_up")
        icon2 = QIcon(QIcon.fromTheme(u"go-up"))
        self.button_up.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.button_up)

        self.button_down = QPushButton(self.groupBox)
        self.button_down.setObjectName(u"button_down")
        icon3 = QIcon(QIcon.fromTheme(u"go-down"))
        self.button_down.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.button_down)

        self.button_utils = QPushButton(self.groupBox)
        self.button_utils.setObjectName(u"button_utils")
        icon4 = QIcon(QIcon.fromTheme(u"window-new"))
        self.button_utils.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.button_utils)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.button_merge = QPushButton(self.groupBox)
        self.button_merge.setObjectName(u"button_merge")

        self.verticalLayout_6.addWidget(self.button_merge)

        self.button_encrypt = QPushButton(self.groupBox)
        self.button_encrypt.setObjectName(u"button_encrypt")

        self.verticalLayout_6.addWidget(self.button_encrypt)

        self.button_decrypt = QPushButton(self.groupBox)
        self.button_decrypt.setObjectName(u"button_decrypt")

        self.verticalLayout_6.addWidget(self.button_decrypt)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.label_notice = QLabel(self.groupBox)
        self.label_notice.setObjectName(u"label_notice")

        self.verticalLayout_3.addWidget(self.label_notice)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_4.addWidget(self.scrollArea_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(327, 108))
        self.dockWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_3 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 307, 744))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setContentsMargins(20, 35, 20, 20)
        self.scrollArea_3 = QScrollArea(self.groupBox_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 239, 68))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, 20)
        self.verticalSpacer = QSpacerItem(20, 2000000000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.checkBox_range = QCheckBox(self.groupBox_2)
        self.checkBox_range.setObjectName(u"checkBox_range")
        self.checkBox_range.setFont(font)

        self.verticalLayout_5.addWidget(self.checkBox_range)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.spinBox_range_final = QSpinBox(self.groupBox_2)
        self.spinBox_range_final.setObjectName(u"spinBox_range_final")
        self.spinBox_range_final.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinBox_range_final, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setMargin(3)

        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setMargin(3)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_range_initial = QSpinBox(self.groupBox_2)
        self.spinBox_range_initial.setObjectName(u"spinBox_range_initial")
        self.spinBox_range_initial.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinBox_range_initial, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, 20)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_7.addWidget(self.label_4)

        self.lineEdit_password = QLineEdit(self.groupBox_2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setAcceptDrops(False)
        self.lineEdit_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_password.setText(u"")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText(u"")

        self.verticalLayout_7.addWidget(self.lineEdit_password)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.button_view = QPushButton(self.groupBox_2)
        self.button_view.setObjectName(u"button_view")
        icon5 = QIcon(QIcon.fromTheme(u"document-open"))
        self.button_view.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.button_view)

        self.button_separate = QPushButton(self.groupBox_2)
        self.button_separate.setObjectName(u"button_separate")

        self.verticalLayout_5.addWidget(self.button_separate)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_convert = QPushButton(self.groupBox_2)
        self.button_convert.setObjectName(u"button_convert")

        self.horizontalLayout_2.addWidget(self.button_convert)

        self.combo_filetype = QComboBox(self.groupBox_2)
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.setObjectName(u"combo_filetype")

        self.horizontalLayout_2.addWidget(self.combo_filetype)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignCenter)
        self.scrollVerticalLayout_DocPreview = QWidget()
        self.scrollVerticalLayout_DocPreview.setObjectName(u"scrollVerticalLayout_DocPreview")
        self.scrollVerticalLayout_DocPreview.setGeometry(QRect(0, 0, 287, 144))
        self.scrollVerticalLayout_DocPreview.setMaximumSize(QSize(300, 387))
        self.horizontalLayout = QHBoxLayout(self.scrollVerticalLayout_DocPreview)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_doc_view = QLabel(self.scrollVerticalLayout_DocPreview)
        self.label_doc_view.setObjectName(u"label_doc_view")
        self.label_doc_view.setMaximumSize(QSize(16777215, 16777215))
        self.label_doc_view.setScaledContents(True)
        self.label_doc_view.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_doc_view)

        self.scrollArea_4.setWidget(self.scrollVerticalLayout_DocPreview)

        self.verticalLayout.addWidget(self.scrollArea_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionUp)
        self.menuFile.addAction(self.actionDown)
        self.menuFile.addAction(self.actionView_Utils)
        self.menuFile.addAction(self.actionMerge)
        self.menuFile.addAction(self.actionEncrypt)
        self.menuFile.addAction(self.actionDecrypt)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF GUI Tools", None))
        self.actionAdd_File.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
#if QT_CONFIG(statustip)
        self.actionAdd_File.setStatusTip(QCoreApplication.translate("MainWindow", u"Add File", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionAdd_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(statustip)
        self.actionDelete.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete File", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.actionUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
#if QT_CONFIG(statustip)
        self.actionUp.setStatusTip(QCoreApplication.translate("MainWindow", u"Up list", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionUp.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
#if QT_CONFIG(statustip)
        self.actionDown.setStatusTip(QCoreApplication.translate("MainWindow", u"Down list", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDown.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionMerge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
#if QT_CONFIG(statustip)
        self.actionMerge.setStatusTip(QCoreApplication.translate("MainWindow", u"Merge PDFs", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionMerge.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionEncrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
#if QT_CONFIG(statustip)
        self.actionEncrypt.setStatusTip(QCoreApplication.translate("MainWindow", u"Encrypt PDFs", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionEncrypt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionDecrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
#if QT_CONFIG(statustip)
        self.actionDecrypt.setStatusTip(QCoreApplication.translate("MainWindow", u"Decrypt PDFs", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDecrypt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(statustip)
        self.actionExit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit app", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(statustip)
        self.actionHelp.setStatusTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(statustip)
        self.actionAbout.setStatusTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(statustip)
        self.actionView_Utils.setText(QCoreApplication.translate("MainWindow", u"View Utils", None))
#if QT_CONFIG(statustip)
        self.actionView_Utils.setStatusTip(QCoreApplication.translate("MainWindow", u"View Utilities", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionView_Utils.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"List PDFs", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"  Add File", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"   Delete", None))
        self.button_up.setText("")
        self.button_down.setText("")
        self.button_utils.setText(QCoreApplication.translate("MainWindow", u"  View Utils", None))
        self.button_merge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.button_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.button_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.label_notice.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select a document", None))
#if QT_CONFIG(statustip)
        self.checkBox_range.setStatusTip(QCoreApplication.translate("MainWindow", u"Document page range", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_range.setText(QCoreApplication.translate("MainWindow", u"Page Range", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Initial", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
#if QT_CONFIG(statustip)
        self.lineEdit_password.setStatusTip(QCoreApplication.translate("MainWindow", u"Set an encryption or decryption password", None))
#endif // QT_CONFIG(statustip)
        self.button_view.setText(QCoreApplication.translate("MainWindow", u"  View PDF", None))
        self.button_separate.setText(QCoreApplication.translate("MainWindow", u"Separate PDF", None))
        self.button_convert.setText(QCoreApplication.translate("MainWindow", u"Convert PDF", None))
        self.combo_filetype.setItemText(0, QCoreApplication.translate("MainWindow", u"PNG", None))
        self.combo_filetype.setItemText(1, QCoreApplication.translate("MainWindow", u"JPEG", None))
        self.combo_filetype.setItemText(2, QCoreApplication.translate("MainWindow", u"PS", None))
        self.combo_filetype.setItemText(3, QCoreApplication.translate("MainWindow", u"EPS", None))
        self.combo_filetype.setItemText(4, QCoreApplication.translate("MainWindow", u"SVG", None))
        self.combo_filetype.setItemText(5, QCoreApplication.translate("MainWindow", u"HTML", None))
        self.combo_filetype.setItemText(6, QCoreApplication.translate("MainWindow", u"TXT", None))

#if QT_CONFIG(statustip)
        self.scrollArea_4.setStatusTip(QCoreApplication.translate("MainWindow", u"Document Preview", None))
#endif // QT_CONFIG(statustip)
        self.label_doc_view.setText("")
    # retranslateUi

# =====================================================| About Window |=============================================================

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow, icon, version_app):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(534, 328)
        AboutWindow.setMinimumSize(QSize(491, 302))
        AboutWindow.setMaximumSize(QSize(534, 328))
        self.centralwidget = QWidget(AboutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(icon))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_7.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label_7)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 2, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.button_ok = QPushButton(self.centralwidget)
        self.button_ok.setObjectName(u"button_ok")

        self.gridLayout.addWidget(self.button_ok, 2, 1, 1, 1)

        AboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AboutWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 534, 22))
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AboutWindow)
        self.statusbar.setObjectName(u"statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow, version_app)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow, version_app):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"About", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><a href=\"https://github.com/TheWatcherMultiversal/pdfgui_tools\"><span style=\" text-decoration: underline; color:#3484e2;\">Web Page</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("AboutWindow", u"PDF GUI Tools", None))
        self.label_3.setText(QCoreApplication.translate("AboutWindow", f"Version {version_app}", None))
        self.label_2.setText(QCoreApplication.translate("AboutWindow", u"PDF GUI Tools is a graphical interface tool that integrates several utilities for managing PDF documents.", None))
        self.label_4.setText(QCoreApplication.translate("AboutWindow", u"Developed by: Angel M.", None))
        self.label_5.setText(QCoreApplication.translate("AboutWindow", u"GNU GENERAL PUBLIC LICENSE v3", None))
        self.button_ok.setText(QCoreApplication.translate("AboutWindow", u"Ok", None))
    # retranslateUi