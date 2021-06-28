# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_management_system/assets/XML/addBook_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addBook_window(object):
    def setupUi(self, addBook_window):
        addBook_window.setObjectName("addBook_window")
        addBook_window.resize(890, 730)
        self.formLayout = QtWidgets.QFormLayout(addBook_window)
        self.formLayout.setObjectName("formLayout")
        self.addBook_label = QtWidgets.QLabel(addBook_window)
        self.addBook_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addBook_label.setObjectName("addBook_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.addBook_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.bookTitle_label = QtWidgets.QLabel(addBook_window)
        self.bookTitle_label.setObjectName("bookTitle_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookTitle_label)
        self.bookTitle_lineEdit = QtWidgets.QLineEdit(addBook_window)
        self.bookTitle_lineEdit.setObjectName("bookTitle_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookTitle_lineEdit)
        self.bookIsbn_label = QtWidgets.QLabel(addBook_window)
        self.bookIsbn_label.setObjectName("bookIsbn_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bookIsbn_label)
        self.bookIsbn_lineEdit = QtWidgets.QLineEdit(addBook_window)
        self.bookIsbn_lineEdit.setObjectName("bookIsbn_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bookIsbn_lineEdit)
        self.bookAuthor_label = QtWidgets.QLabel(addBook_window)
        self.bookAuthor_label.setObjectName("bookAuthor_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.bookAuthor_label)
        self.bookAuthor_comboBox = QtWidgets.QComboBox(addBook_window)
        self.bookAuthor_comboBox.setObjectName("bookAuthor_comboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bookAuthor_comboBox)
        self.bookGenre_label = QtWidgets.QLabel(addBook_window)
        self.bookGenre_label.setObjectName("bookGenre_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.bookGenre_label)
        self.bookGenre_comboBox = QtWidgets.QComboBox(addBook_window)
        self.bookGenre_comboBox.setObjectName("bookGenre_comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.bookGenre_comboBox)
        self.bookCover_label = QtWidgets.QLabel(addBook_window)
        self.bookCover_label.setObjectName("bookCover_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.bookCover_label)
        self.bookPreview_button = QtWidgets.QPushButton(addBook_window)
        self.bookPreview_button.setObjectName("bookPreview_button")
        self.bookPreview_button.setVisible(False)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.bookPreview_button)
        self.bookDescription_label = QtWidgets.QLabel(addBook_window)
        self.bookDescription_label.setObjectName("bookDescription_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.bookDescription_label)
        self.bookDescription_plainTextEdit = QtWidgets.QPlainTextEdit(addBook_window)
        self.bookDescription_plainTextEdit.setObjectName("bookDescription_plainTextEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.bookDescription_plainTextEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.addBook_button_1 = QtWidgets.QPushButton(addBook_window)
        self.addBook_button_1.setObjectName("addBook_button_1")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.addBook_button_1)
        self.clearAll_button = QtWidgets.QPushButton(addBook_window)
        self.clearAll_button.setObjectName("clearAll_button")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.clearAll_button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uploadCover_button = QtWidgets.QPushButton(addBook_window)
        self.uploadCover_button.setObjectName("uploadCover_button")
        self.horizontalLayout.addWidget(self.uploadCover_button)
        self.bookCoverPath_label = QtWidgets.QLabel(addBook_window)
        self.bookCoverPath_label.setText("")
        self.bookCoverPath_label.setObjectName("bookCoverPath_label")
        self.horizontalLayout.addWidget(self.bookCoverPath_label)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.bookStatus_label = QtWidgets.QLabel(addBook_window)
        self.bookStatus_label.setObjectName("bookStatus_label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.bookStatus_label)
        self.bookStatus_comboBox = QtWidgets.QComboBox(addBook_window)
        self.bookStatus_comboBox.setObjectName("bookStatus_comboBox")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.bookStatus_comboBox)
        self.bookPages_label = QtWidgets.QLabel(addBook_window)
        self.bookPages_label.setObjectName("bookPages_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.bookPages_label)
        self.bookPages_lineEdit = QtWidgets.QLineEdit(addBook_window)
        self.bookPages_lineEdit.setObjectName("bookPages_lineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.bookPages_lineEdit)

        self.retranslateUi(addBook_window)
        QtCore.QMetaObject.connectSlotsByName(addBook_window)

    def retranslateUi(self, addBook_window):
        _translate = QtCore.QCoreApplication.translate
        addBook_window.setWindowTitle(_translate("addBook_window", "Form"))
        self.addBook_label.setText(_translate("addBook_window", "Add book"))
        self.bookTitle_label.setText(_translate("addBook_window", "Title:"))
        self.bookIsbn_label.setText(_translate("addBook_window", "ISBN:"))
        self.bookAuthor_label.setText(_translate("addBook_window", "Author:"))
        self.bookGenre_label.setText(_translate("addBook_window", "Genre:"))
        self.bookCover_label.setText(_translate("addBook_window", "Cover:"))
        self.bookPreview_button.setText(_translate("addBook_window", "Preview"))
        self.bookDescription_label.setText(_translate("addBook_window", "Description:"))
        self.addBook_button_1.setText(_translate("addBook_window", "Add book"))
        self.clearAll_button.setText(_translate("addBook_window", "Clear all"))
        self.uploadCover_button.setText(_translate("addBook_window", "..."))
        self.bookStatus_label.setText(_translate("addBook_window", "Status:"))
        self.bookPages_label.setText(_translate("addBook_window", "Pages:"))
