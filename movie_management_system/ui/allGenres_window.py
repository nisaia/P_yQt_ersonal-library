# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/allGenres_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allGenres_window(object):
    def setupUi(self, allGenres_window):
        allGenres_window.setObjectName("allGenres_window")
        allGenres_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(allGenres_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allGenres_label = QtWidgets.QLabel(allGenres_window)
        self.allGenres_label.setAlignment(QtCore.Qt.AlignCenter)
        self.allGenres_label.setObjectName("allGenres_label")
        self.verticalLayout.addWidget(self.allGenres_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.searchGenre_lineEdit = QtWidgets.QLineEdit(allGenres_window)
        self.searchGenre_lineEdit.setObjectName("searchGenre_lineEdit")
        self.verticalLayout.addWidget(self.searchGenre_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.allGenres_tableView = QtWidgets.QTableView(allGenres_window)
        self.allGenres_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allGenres_tableView.setObjectName("allGenres_tableView")
        self.verticalLayout.addWidget(self.allGenres_tableView)

        self.retranslateUi(allGenres_window)
        QtCore.QMetaObject.connectSlotsByName(allGenres_window)

    def retranslateUi(self, allGenres_window):
        _translate = QtCore.QCoreApplication.translate
        allGenres_window.setWindowTitle(_translate("allGenres_window", "Form"))
        self.allGenres_label.setText(_translate("allGenres_window", "All genres"))
