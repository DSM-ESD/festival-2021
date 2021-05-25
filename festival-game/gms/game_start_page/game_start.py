# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_start.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 450)
        self.game_changer = QtWidgets.QComboBox(Form)
        self.game_changer.setGeometry(QtCore.QRect(70, 20, 191, 31))
        self.game_changer.setObjectName("game_changer")
        self.game_changer.addItem("")
        self.game_changer.addItem("")
        self.game_changer.addItem("")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 60, 761, 371))
        self.stackedWidget.setObjectName("stackedWidget")
        self.shoting_game = QtWidgets.QWidget()
        self.shoting_game.setObjectName("shoting_game")
        self.game_displayer = QtWidgets.QLabel(self.shoting_game)
        self.game_displayer.setGeometry(QtCore.QRect(10, 10, 500, 280))
        self.game_displayer.setStyleSheet("background-color: rgb(255, 250, 172);")
        self.game_displayer.setObjectName("game_displayer")
        self.game_start_button = QtWidgets.QPushButton(self.shoting_game)
        self.game_start_button.setGeometry(QtCore.QRect(410, 310, 101, 41))
        self.game_start_button.setObjectName("game_start_button")
        self.id_label = QtWidgets.QLabel(self.shoting_game)
        self.id_label.setGeometry(QtCore.QRect(10, 310, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.id_label.setFont(font)
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label.setObjectName("id_label")
        self.under_line = QtWidgets.QPushButton(self.shoting_game)
        self.under_line.setGeometry(QtCore.QRect(70, 350, 311, 5))
        self.under_line.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.under_line.setText("")
        self.under_line.setObjectName("under_line")
        self.score_board_background = QtWidgets.QLabel(self.shoting_game)
        self.score_board_background.setGeometry(QtCore.QRect(530, 10, 221, 341))
        self.score_board_background.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.score_board_background.setText("")
        self.score_board_background.setObjectName("score_board_background")
        self.ranking_board_1 = QtWidgets.QLabel(self.shoting_game)
        self.ranking_board_1.setGeometry(QtCore.QRect(535, 50, 211, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ranking_board_1.setFont(font)
        self.ranking_board_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.ranking_board_1.setObjectName("ranking_board_1")
        self.score_board = QtWidgets.QLabel(self.shoting_game)
        self.score_board.setGeometry(QtCore.QRect(535, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.score_board.setFont(font)
        self.score_board.setStyleSheet("background-color: rgb(9, 9, 9);\n"
"color: rgb(255, 255, 0);")
        self.score_board.setAlignment(QtCore.Qt.AlignCenter)
        self.score_board.setObjectName("score_board")
        self.id_input = QtWidgets.QLineEdit(self.shoting_game)
        self.id_input.setGeometry(QtCore.QRect(70, 310, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.id_input.setFont(font)
        self.id_input.setText("")
        self.id_input.setObjectName("id_input")
        self.stackedWidget.addWidget(self.shoting_game)
        self.rope_game = QtWidgets.QWidget()
        self.rope_game.setObjectName("rope_game")
        self.under_line_2 = QtWidgets.QPushButton(self.rope_game)
        self.under_line_2.setGeometry(QtCore.QRect(70, 350, 311, 5))
        self.under_line_2.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.under_line_2.setText("")
        self.under_line_2.setObjectName("under_line_2")
        self.game_displayer_2 = QtWidgets.QLabel(self.rope_game)
        self.game_displayer_2.setGeometry(QtCore.QRect(10, 10, 500, 280))
        self.game_displayer_2.setStyleSheet("background-color: rgb(255, 250, 172);")
        self.game_displayer_2.setObjectName("game_displayer_2")
        self.score_board_2 = QtWidgets.QLabel(self.rope_game)
        self.score_board_2.setGeometry(QtCore.QRect(535, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.score_board_2.setFont(font)
        self.score_board_2.setStyleSheet("background-color: rgb(9, 9, 9);\n"
"color: rgb(255, 255, 0);")
        self.score_board_2.setAlignment(QtCore.Qt.AlignCenter)
        self.score_board_2.setObjectName("score_board_2")
        self.ranking_board_2 = QtWidgets.QLabel(self.rope_game)
        self.ranking_board_2.setGeometry(QtCore.QRect(535, 50, 211, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ranking_board_2.setFont(font)
        self.ranking_board_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.ranking_board_2.setObjectName("ranking_board_2")
        self.id_input_2 = QtWidgets.QLineEdit(self.rope_game)
        self.id_input_2.setGeometry(QtCore.QRect(70, 310, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.id_input_2.setFont(font)
        self.id_input_2.setText("")
        self.id_input_2.setObjectName("id_input_2")
        self.game_start_button_2 = QtWidgets.QPushButton(self.rope_game)
        self.game_start_button_2.setGeometry(QtCore.QRect(410, 310, 101, 41))
        self.game_start_button_2.setObjectName("game_start_button_2")
        self.id_label_2 = QtWidgets.QLabel(self.rope_game)
        self.id_label_2.setGeometry(QtCore.QRect(10, 310, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.id_label_2.setFont(font)
        self.id_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label_2.setObjectName("id_label_2")
        self.score_board_background_2 = QtWidgets.QLabel(self.rope_game)
        self.score_board_background_2.setGeometry(QtCore.QRect(530, 10, 221, 341))
        self.score_board_background_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.score_board_background_2.setText("")
        self.score_board_background_2.setObjectName("score_board_background_2")
        self.score_board_background_2.raise_()
        self.under_line_2.raise_()
        self.game_displayer_2.raise_()
        self.score_board_2.raise_()
        self.ranking_board_2.raise_()
        self.id_input_2.raise_()
        self.game_start_button_2.raise_()
        self.id_label_2.raise_()
        self.stackedWidget.addWidget(self.rope_game)
        self.defense_game = QtWidgets.QWidget()
        self.defense_game.setObjectName("defense_game")
        self.under_line_3 = QtWidgets.QPushButton(self.defense_game)
        self.under_line_3.setGeometry(QtCore.QRect(70, 350, 311, 5))
        self.under_line_3.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.under_line_3.setText("")
        self.under_line_3.setObjectName("under_line_3")
        self.game_displayer_3 = QtWidgets.QLabel(self.defense_game)
        self.game_displayer_3.setGeometry(QtCore.QRect(10, 10, 500, 280))
        self.game_displayer_3.setStyleSheet("background-color: rgb(255, 250, 172);")
        self.game_displayer_3.setObjectName("game_displayer_3")
        self.score_board_3 = QtWidgets.QLabel(self.defense_game)
        self.score_board_3.setGeometry(QtCore.QRect(535, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.score_board_3.setFont(font)
        self.score_board_3.setStyleSheet("background-color: rgb(9, 9, 9);\n"
"color: rgb(255, 255, 0);")
        self.score_board_3.setAlignment(QtCore.Qt.AlignCenter)
        self.score_board_3.setObjectName("score_board_3")
        self.ranking_board_3 = QtWidgets.QLabel(self.defense_game)
        self.ranking_board_3.setGeometry(QtCore.QRect(535, 50, 211, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ranking_board_3.setFont(font)
        self.ranking_board_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.ranking_board_3.setObjectName("ranking_board_3")
        self.id_input_3 = QtWidgets.QLineEdit(self.defense_game)
        self.id_input_3.setGeometry(QtCore.QRect(70, 310, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.id_input_3.setFont(font)
        self.id_input_3.setText("")
        self.id_input_3.setObjectName("id_input_3")
        self.game_start_button_3 = QtWidgets.QPushButton(self.defense_game)
        self.game_start_button_3.setGeometry(QtCore.QRect(410, 310, 101, 41))
        self.game_start_button_3.setObjectName("game_start_button_3")
        self.id_label_3 = QtWidgets.QLabel(self.defense_game)
        self.id_label_3.setGeometry(QtCore.QRect(10, 310, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.id_label_3.setFont(font)
        self.id_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label_3.setObjectName("id_label_3")
        self.score_board_background_3 = QtWidgets.QLabel(self.defense_game)
        self.score_board_background_3.setGeometry(QtCore.QRect(530, 10, 221, 341))
        self.score_board_background_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.score_board_background_3.setText("")
        self.score_board_background_3.setObjectName("score_board_background_3")
        self.score_board_background_3.raise_()
        self.under_line_3.raise_()
        self.game_displayer_3.raise_()
        self.score_board_3.raise_()
        self.ranking_board_3.raise_()
        self.id_input_3.raise_()
        self.game_start_button_3.raise_()
        self.id_label_3.raise_()
        self.stackedWidget.addWidget(self.defense_game)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.game_changer.setItemText(0, _translate("Form", "Shoting"))
        self.game_changer.setItemText(1, _translate("Form", "rope"))
        self.game_changer.setItemText(2, _translate("Form", "defense"))
        self.game_displayer.setText(_translate("Form", "shoting game"))
        self.game_start_button.setText(_translate("Form", "Game start"))
        self.id_label.setText(_translate("Form", "ID"))
        self.ranking_board_1.setText(_translate("Form", "Ranking | Name : asfas | score"))
        self.score_board.setText(_translate("Form", "Score Board"))
        self.game_displayer_2.setText(_translate("Form", "Rope_game"))
        self.score_board_2.setText(_translate("Form", "Score Board"))
        self.ranking_board_2.setText(_translate("Form", "Ranking | Name : asfas | score"))
        self.game_start_button_2.setText(_translate("Form", "Game start"))
        self.id_label_2.setText(_translate("Form", "ID"))
        self.game_displayer_3.setText(_translate("Form", "Defense game"))
        self.score_board_3.setText(_translate("Form", "Score Board"))
        self.ranking_board_3.setText(_translate("Form", "Ranking | Name : asfas | score"))
        self.game_start_button_3.setText(_translate("Form", "Game start"))
        self.id_label_3.setText(_translate("Form", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())