from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyleFactory
from PyQt5 import sip
from shutil import copyfile
import json
import os
import requests
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(721, 416)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(721, 416))
        MainWindow.setMaximumSize(QtCore.QSize(721, 416))
        MainWindow.setBaseSize(QtCore.QSize(721, 379))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 701, 231))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Bundle ID', 'Version', 'Status'])
        #self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(630, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnLoad.setFont(font)
        self.btnLoad.setCheckable(False)
        self.btnLoad.setFlat(False)
        self.btnLoad.setObjectName("btnLoad")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 250, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Bundle ID")
        self.lineEdit.setDragEnabled(True)
        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setGeometry(QtCore.QRect(10, 360, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.removeBtn.setFont(font)
        self.removeBtn.setObjectName("removeBtn")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(10, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.rightTopFrame = QtWidgets.QFrame(self.centralwidget)
        self.rightTopFrame.setGeometry(QtCore.QRect(180, 250, 141, 22))
        self.rightTopFrame.setStyleSheet("background-color: #DCDCDC; border-radius: 3px; border: 1px solid #ababab")

        self.label = DropLabel("", self.centralwidget)
        self.label.move(180, 250)
        self.label.resize(141, 22)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.btnLoad.clicked.connect(self.load_entries)
        self.pushButton.clicked.connect(self.add)
        self.lineEdit.returnPressed.connect(self.on_enter_do)
        self.removeBtn.clicked.connect(lambda: remove_entry(self.lineEdit.text()))
        self.updateBtn.clicked.connect(lambda: update_entry(self.lineEdit.text()))
        self.tableWidget.keyPressEvent = self.del_entry



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CheatManager"))
        self.tableWidget.setSortingEnabled(True)
        self.btnLoad.setText(_translate("MainWindow", "Refresh"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.removeBtn.setText(_translate("MainWindow", "Remove"))
        self.updateBtn.setText(_translate("MainWindow", "Update"))

    def load_entries(self):
        global data
        self.tableWidget.setRowCount(0)
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            copyfile('data.json', 'data.backup')
            with open('data.json', 'w') as data_file:
                data = {}
                json.dump(data, data_file, indent = 4, sort_keys = True)
        for rowN, rowD in enumerate(data):
            if fetch_version(rowD) != data[rowD]['version']:
                status = "Outdated"
            else:
                status = "Up to Date"
            self.tableWidget.insertRow(rowN)
            self.tableWidget.setItem(rowN, 0, QtWidgets.QTableWidgetItem(data[rowD]['name']))
            self.tableWidget.setItem(rowN, 2, QtWidgets.QTableWidgetItem(data[rowD]['version']))
            self.tableWidget.setItem(rowN, 1, QtWidgets.QTableWidgetItem(rowD))
            self.tableWidget.setItem(rowN, 3, QtWidgets.QTableWidgetItem(status))
            if status == "Outdated":
                self.tableWidget.item(rowN, 3).setBackground(QtGui.QColor(255,0,0))
            else:
                self.tableWidget.item(rowN, 3).setBackground(QtGui.QColor(50,205,50))

    def add(self):
        txt = self.lineEdit.text()
        fetch_info(txt)


    def on_enter_do(self):
        if self.lineEdit.text().strip() in data:
            update_entry(self.lineEdit.text())
        else:
            fetch_info(self.lineEdit.text())

    def del_entry(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            remove_entry(selected_row())
        elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            update_entry(selected_row())


class DropLabel(QtWidgets.QLabel):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        fetch_info(e.mimeData().text())

def selected_row():
    row = ui.tableWidget.currentRow()
    firstColumnInRow = ui.tableWidget.item(row, 1)
    try:
        text = firstColumnInRow.text()
    except:
        text = None
    return text

def is_ready():
    if not os.path.isfile('data.json'):
        try:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent = 4, sort_keys = True)
        except:
            pass

def fetch_info(bundle_id):
    global data
    try:
        bundle_id = bundle_id.strip()
    except:
        pass
    info_url = "http://itunes.apple.com/lookup?bundleId="
    info = requests.get(info_url + bundle_id).json()
    if is_bundle_id(info, None):
        data[bundle_id] = {
                            "name": info['results'][0]['trackName'],
                            "version": info['results'][0]['version']
                            }
        ui.lineEdit.setText('')
    dump_info()
    ui.load_entries()

def fetch_version(bundle_id):
    try:
        bundle_id = bundle_id.strip()
    except:
        pass
    info = requests.get(info_url + bundle_id).json()
    return info['results'][0]['version']

def dump_info():
    with open('data.json', 'w') as data_file:
        json.dump(data, data_file, indent = 4, sort_keys = True)

def remove_entry(bundle_id):
    if bundle_id == "":
        try:
            bundle_id = selected_row()
        except:
            pass
    try:
        bundle_id = bundle_id.strip()
    except:
        pass
    try:
        entry_name = data[bundle_id]['name']
        del data[bundle_id]
        ui.lineEdit.setText('')
        dump_info()
        ui.load_entries()
    except:
        pass

def update_entry(bundle_id):
    if bundle_id == "":
        try:
            bundle_id = selected_row()
        except:
            pass
    try:
        bundle_id = bundle_id.strip()
    except:
        pass
    if is_bundle_id(None, bundle_id):
        try:
            data[bundle_id]['version'] = fetch_version(bundle_id)
            ui.lineEdit.setText('')
            dump_info()
            ui.load_entries()
        except:
            pass

def is_bundle_id(info, bundle_id):
    if bundle_id != None:
        try:
            bundle_id = bundle_id.strip()
        except:
            pass
    if info == None:
        try:
            info = requests.get(info_url + bundle_id).json()
        except:
            info = {}
            info['resultCount'] = 0
            pass
    if info['resultCount'] == 1:
        return True
    else:
        return False

def handler(msg_type, msg_log_context, msg_string):
    pass

QtCore.qInstallMessageHandler(handler)
os.environ["QT_SCALE_FACTOR"] = "1"
data = {}
info_url = "http://itunes.apple.com/lookup?bundleId="
is_ready()
app = QtWidgets.QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app.setStyle(QStyleFactory.create('Fusion'))
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.load_entries()
sys.exit(app.exec_())
