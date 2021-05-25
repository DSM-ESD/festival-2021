from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from game_start import *
import json
import os
import sqlite3

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.con = sqlite3.connect('game_info.db')
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS user_inform \
            (id integer PRIMARY KEY,name text, score integer, game text)")

        self.user_info = {
            "id" : "",
            "score" : "0",
            "game" : ""
        }
        self.ranking_board_arr = []
        self.ranking_board_str = ""

        self.change_game()
        self.game_started()
        self.shoting_ranking_board_setting()
        self.rope_ranking_board_setting()
        self.defense_ranking_board_setting()

    def change_game(self):
        self.ui.game_changer.currentIndexChanged.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.ui.game_changer.currentIndex()))

    def game_started(self):
        self.ui.game_start_button.clicked.connect(self.first_game_started)
        self.ui.game_start_button_2.clicked.connect(self.second_game_started)
        self.ui.game_start_button_3.clicked.connect(self.third_game_started)

    def first_game_started(self):
        if self.ui.id_input.text() != "" and self.cur.execute(f"SELECT * FROM user_inform WHERE name='{self.ui.id_input.text()}'").fetchall() == []:
            self.user_info["id"] = self.ui.id_input.text()
            self.change_user_info()
            os.system(r'games\shoting_game.py')
            self.con.close()
            QCoreApplication.quit()

    def second_game_started(self):
        if self.ui.id_input_2.text() != "" and self.cur.execute(f"SELECT * FROM user_inform WHERE name='{self.ui.id_input.text()}'").fetchall() == []:
            self.user_info["id"] = self.ui.id_input_2.text()
            self.change_user_info()
            os.system(r'games\rope_game.py')
            self.con.close()
            QCoreApplication.quit()

    def third_game_started(self):
        if self.ui.id_input_3.text() != "" and self.cur.execute(f"SELECT * FROM user_inform WHERE name='{self.ui.id_input.text()}'").fetchall() == []:
            self.user_info["id"] = self.ui.id_input_3.text()
            self.change_user_info()
            os.system(r'games\defense_game.py')
            self.con.close()
            QCoreApplication.quit()

    def change_user_info(self):
        self.user_info["game"] = self.ui.game_changer.currentText()
        json_object = json.dumps(self.user_info, indent = 4)
        with open("user_info.json", "w") as outfile:
	        outfile.write(json_object)

    def shoting_ranking_board_setting(self):
        self.read_user_info('shoting')
        self.ui.ranking_board_1.setText(self.ranking_board_str)

    def rope_ranking_board_setting(self):
        self.read_user_info('rope')
        self.ui.ranking_board_2.setText(self.ranking_board_str)

    def defense_ranking_board_setting(self):
        self.read_user_info('defense')
        self.ui.ranking_board_3.setText(self.ranking_board_str)

    def read_user_info(self, game_name):
        self.ranking_board_str = ""
        ret = self.cur.execute(f"SELECT * FROM user_inform WHERE game='{game_name}' ORDER BY score DESC")
        self.ranking_board_arr = ret.fetchall()

        for i in range(0, len(self.ranking_board_arr)):
            self.ranking_board_str += f"{i + 1}  | Name - {self.ranking_board_arr[i][1]}  |score - {self.ranking_board_arr[i][2]}\n"


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())