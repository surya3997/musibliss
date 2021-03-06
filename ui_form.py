#!/usr/bin/python3
from PyQt4 import QtCore, QtGui
import pymongo
from pymongo import MongoClient
import vlc
import json
from time import sleep
import threading, re

config = json.load(open('configuration.json'))
setup = config[config["current_state"]]
mongo_connection = setup["mongo"]
http_file_path = setup["http_path"]

try:
    client = MongoClient(mongo_connection)
    db = client.hd15pd38
except:
    print("DB connection error")

search_by = ["song_title", "song_album", "song_artist"]

results = []
result_cursor = db.songs.find()

for i in result_cursor:
    results.append(i)

number = len(results)

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

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.resize(717, 475)
        self.gridLayout = QtGui.QGridLayout(widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(widget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_3 = QtGui.QPushButton(widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_2 = QtGui.QPushButton(widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(widget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.treeWidget = QtGui.QTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 691, 311))
        self.treeWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        

        for i in range(number):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)

        self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 1)
        

        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.treeWidget_3 = QtGui.QTreeWidget(self.tab_3)
        self.treeWidget_3.setGeometry(QtCore.QRect(0, 40, 691, 281))
        self.treeWidget_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.treeWidget_3.setObjectName(_fromUtf8("treeWidget_3"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_3)
        self.comboBox_3 = QtGui.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 10, 91, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 441, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(570, 10, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.treeWidget_3, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 4)
        self.label_4 = QtGui.QLabel(widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)
        self.dial = QtGui.QDial(widget)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.gridLayout.addWidget(self.dial, 3, 3, 3, 1)
        self.horizontalSlider = QtGui.QSlider(widget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 3, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox_2 = QtGui.QComboBox(widget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_5 = QtGui.QLabel(widget)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout, 4, 2, 1, 1)

        self.retranslateUi(widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def pressedNextButton(self):
        if self.current_play_index < number - 1:
            self.current_play_index += 1
            play_path = results[self.current_play_index]["song_path"].split("songs")[1]
            self.play_file = http_file_path + play_path
            self.play_file = "%20".join(self.play_file.split(" "))
            # print(self.play_file)

            if self.first_time_play == 0:
                self.vlcPlay.stop()
                self.resetSeek()
            self.first_time_play = 0

            self.vlcPlay = vlc.MediaPlayer(self.play_file)
            self.vlcPlay.play()
            self.play_status = 1
            self.startSeek()

        ''' 
        '''
        # print("Next button is pressed!")

    def seekStatusAdd(self):
        if self.counterSeek < 100:
            self.happeningThread = threading.Timer(1.0, self.seekStatusAdd)
            self.happeningThread.daemon = True
            self.happeningThread.start()
        self.horizontalSlider.triggerAction(self.horizontalSlider.SliderSingleStepAdd)
        self.counterSeek += 1

    def startSeek(self):
        self.counterSeek = 0
        self.seekStatusAdd()

    def stopSeek(self):
        self.counterSeek = 100
        
    def resetSeek(self):
        self.horizontalSlider.setValue(0)

    def pressedPlayButton(self):
        if self.first_time_play == 1 and number > 0:
            play_path = results[0]["song_path"].split("songs")[1]
            self.play_file = http_file_path + play_path
            self.play_file = "%20".join(self.play_file.split(" "))
            # print(self.play_file)
            self.first_time_play = 0

            self.vlcPlay = vlc.MediaPlayer(self.play_file)
            self.vlcPlay.play()
            self.play_status = 1

            self.startSeek()

        elif self.first_time_play == 0:
            if self.play_status == 1:
                self.vlcPlay.pause()
                self.play_status = 0
                self.stopSeek()
            else:
                self.vlcPlay.play()
                self.play_status = 1
                self.startSeek()

        # print("Play button is pressed!")

    def pressedBackButton(self):
        if self.current_play_index > 0:
            self.current_play_index -= 1
            play_path = results[self.current_play_index]["song_path"].split("songs")[1]
            self.play_file = http_file_path + play_path
            self.play_file = "%20".join(self.play_file.split(" "))
            # print(self.play_file)

            if self.first_time_play == 0:
                self.vlcPlay.stop()
                self.resetSeek()
            self.first_time_play = 0

            self.vlcPlay = vlc.MediaPlayer(self.play_file)
            self.vlcPlay.play()
            self.play_status = 1
            self.startSeek()

        # print("Back button is pressed!")

    def indexChangeSort(self, item):
        # print(search_by[item])
        sort_results = []
        sort_result_cursor = db.songs.find().sort([(search_by[item], pymongo.ASCENDING)])
        self.treeWidget.clear()

        for i in sort_result_cursor:
            sort_results.append(i)

        # print(sort_results[:5])

        sort_number = len(sort_results)
        for i in range(sort_number):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)

        for i in range(sort_number):
            self.treeWidget.topLevelItem(i).setText(0, _translate("widget", str(sort_results[i]["song_title"]), None))
            self.treeWidget.topLevelItem(i).setText(1, _translate("widget", str(sort_results[i]["song_album"]), None))
            self.treeWidget.topLevelItem(i).setText(2, _translate("widget", str(sort_results[i]["song_artist"]), None))
            song_len = sort_results[i]["song_length"]
            song_length = str(int(song_len / 60)) + ":" + str(int(song_len % 60))
            self.treeWidget.topLevelItem(i).setText(3, _translate("widget", song_length, None))

    def indexChangeSearch(self, item):
        self.default_search_index = item

    def pressedSearchButton(self):
        search_query = self.lineEdit.text()
        search_key = search_by[self.default_search_index]
        searchResults = []
        # search_result_cursor = db.songs.find({search_key:re.compile('^' + re.escape(search_query) + '$', re.IGNORECASE)})

        search_result_cursor = db.songs.find({search_key:{'$regex' : ".*" + search_query +  ".*"}})
        for i in search_result_cursor:
            searchResults.append(i)

        search_number = len(searchResults)
        # print(searchResults)

        self.treeWidget_3.clear()

        for i in range(search_number):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget_3)

        for i in range(search_number):
            self.treeWidget_3.topLevelItem(i).setText(0, _translate("widget", str(searchResults[i]["song_title"]), None))
            self.treeWidget_3.topLevelItem(i).setText(1, _translate("widget", str(searchResults[i]["song_album"]), None))
            self.treeWidget_3.topLevelItem(i).setText(2, _translate("widget", str(searchResults[i]["song_artist"]), None))
            song_len = searchResults[i]["song_length"]
            song_length = str(int(song_len / 60)) + ":" + str(int(song_len % 60))
            self.treeWidget_3.topLevelItem(i).setText(3, _translate("widget", song_length, None))

    def sliderChange(self, valueOfSlider):
        # print(valueOfSlider)
        pass
    
    def dialChange(self, valueOfDial):
        self.vlcPlay.audio_set_volume(valueOfDial)
        # print(valueOfDial)

    def clickItemAllSongs(self, item):
        for index, i in enumerate(results):
            if i["song_title"] == item.text(0):
                play_path = i["song_path"].split("songs")[1]
                self.play_file = http_file_path + play_path
                self.play_file = "%20".join(self.play_file.split(" "))
                # print(self.play_file)
                self.current_play_index = index

                if self.first_time_play == 0:
                    self.vlcPlay.stop()
                    self.resetSeek()
                self.first_time_play = 0

                self.vlcPlay = vlc.MediaPlayer(self.play_file)
                self.vlcPlay.play()
                self.play_status = 1
                self.startSeek()
                break

    def clickItemSearch(self, item):
        for index, i in enumerate(results):
            if i["song_title"] == item.text(0):
                play_path = i["song_path"].split("songs")[1]
                self.play_file = http_file_path + play_path
                self.play_file = "%20".join(self.play_file.split(" "))
                # print(self.play_file)
                self.current_play_index = index

                if self.first_time_play == 0:
                    self.vlcPlay.stop()
                    self.resetSeek()
                self.first_time_play = 0

                self.vlcPlay = vlc.MediaPlayer(self.play_file)
                self.vlcPlay.play()
                self.play_status = 1
                self.startSeek()
                break


    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "MUSIBLISS", None))
        self.pushButton_4.setText(_translate("widget", "⏪", None))
        self.pushButton_3.setText(_translate("widget", "▮▮ ▶", None))
        self.pushButton_2.setText(_translate("widget", "⏩", None))
        self.treeWidget.headerItem().setText(0, _fromUtf8("song"))
        self.treeWidget.headerItem().setText(1, _translate("widget", "album", None))
        self.treeWidget.headerItem().setText(2, _translate("widget", "artist", None))
        self.treeWidget.headerItem().setText(3, _translate("widget", "length", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        # custom values
        self.first_time_play = 1
        self.play_status = 0
        self.current_play_index = 0
        self.counterSeek = 0
        self.default_search_index = 0
        self.default_sort_index = 0

        for i in range(number):
            self.treeWidget.topLevelItem(i).setText(0, _translate("widget", str(results[i]["song_title"]), None))
            self.treeWidget.topLevelItem(i).setText(1, _translate("widget", str(results[i]["song_album"]), None))
            self.treeWidget.topLevelItem(i).setText(2, _translate("widget", str(results[i]["song_artist"]), None))
            song_len = results[i]["song_length"]
            song_length = str(int(song_len / 60)) + ":" + str(int(song_len % 60))
            self.treeWidget.topLevelItem(i).setText(3, _translate("widget", song_length, None))

        
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("widget", "All Songs", None))
        self.treeWidget_3.headerItem().setText(0, _translate("widget", "song", None))
        self.treeWidget_3.headerItem().setText(1, _translate("widget", "album", None))
        self.treeWidget_3.headerItem().setText(2, _translate("widget", "artist", None))
        self.treeWidget_3.headerItem().setText(3, _translate("widget", "length", None))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.comboBox_3.setItemText(0, _translate("widget", "Title", None))
        self.comboBox_3.setItemText(1, _translate("widget", "Album", None))
        self.comboBox_3.setItemText(2, _translate("widget", "Artist", None))
        self.pushButton.setText(_translate("widget", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("widget", "Search", None))
        self.label_4.setText(_translate("widget", "Sort by", None))
        self.comboBox_2.setItemText(0, _translate("widget", "Title", None))
        self.comboBox_2.setItemText(1, _translate("widget", "Album", None))
        self.comboBox_2.setItemText(2, _translate("widget", "Artist", None))


        # custom function calls
        self.dial.setValue(99)
        self.pushButton_2.clicked.connect(self.pressedNextButton)
        self.pushButton_3.clicked.connect(self.pressedPlayButton)
        self.pushButton_4.clicked.connect(self.pressedBackButton)
        self.comboBox_2.currentIndexChanged.connect(self.indexChangeSort)
        self.comboBox_3.currentIndexChanged.connect(self.indexChangeSearch)
        self.pushButton.clicked.connect(self.pressedSearchButton)
        self.horizontalSlider.valueChanged[int].connect(self.sliderChange)
        self.dial.valueChanged.connect(self.dialChange)
        self.treeWidget.itemClicked.connect(self.clickItemAllSongs)
        self.treeWidget_3.itemClicked.connect(self.clickItemSearch)
        #self.seekStatus()




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
