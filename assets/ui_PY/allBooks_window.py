# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_XML/allBooks_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allBooks_window(object):
    def setupUi(self, allBooks_window):
        allBooks_window.setObjectName("allBooks_window")
        allBooks_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(allBooks_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(allBooks_window)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(allBooks_window)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(allBooks_window)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(allBooks_window)
        QtCore.QMetaObject.connectSlotsByName(allBooks_window)

    def retranslateUi(self, allBooks_window):
        _translate = QtCore.QCoreApplication.translate
        allBooks_window.setWindowTitle(_translate("allBooks_window", "Form"))
        self.label.setText(_translate("allBooks_window", "All books"))
