from flask import Flask, json, jsonify, request
from sqlalchemy import create_engine, text

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
    app.database = database

    @app.route('/save-game-data', methods = ['POST'])
    def save_game_data():
        try:
            game_data = request.json
            user_id = app.database.execute(text("""
                                                INSERT INTO game_result (
                                                id,
                                                score,
                                                game_type
                                            ) VALUES (
                                                :id,
                                                :score,
                                                :game_type
                                            )
                                                """), game_data).lastrowid
            return jsonify(message="Create Success"), 201
        except:
            return jsonify(message="Create Fail"), 500

    @app.route('/load-first-game/<game_type>', methods = ['GET'])
    def load_first_game(game_type):
        try:
            recive_game_data = app.database.execute(text(f"SELECT * FROM game_result WHERE game_type = \"{game_type}\" ORDER BY score DESC"))
            game_data_arr = recive_game_data.fetchall()

            json_list = []
            number = 1

            for row in game_data_arr:
                json_list.append({f"user{number}": {"id" : row[0], "score" : row[1], "game_type" : row[2]}})
                number += 1

            if json_list == []:
                return jsonify(message="Game datas are empty"), 200

            return jsonify(json_list), 200
        except:
            return jsonify(message="Load Fail"), 500


    @app.route('/set-user-status', methods=['POST'])
    def set_user_status():
        try:
            game_data = request.json
            user_id_in_dict = game_data["id"]
            user_status_in_dict = game_data["status"]

            user = app.database.execute(text(f"SELECT * FROM user_status WHERE id = \"{user_id_in_dict}\""))
            user_info = user.fetchall()

            if user_info == []:
                user_set = app.database.execute(text("""
                                                        INSERT INTO user_status (
                                                        id,
                                                        status
                                                    ) VALUES (
                                                        :id,
                                                        :status
                                                    )
                                                        """), game_data).lastrowid

                return jsonify(message="User status save"), 201
            else:
                user_set = app.database.execute(text(f"UPDATE user_status SET status={user_status_in_dict} WHERE id=\"{user_id_in_dict}\""), game_data).lastrowid

                return jsonify(message="User status change"), 201
        except:
            return jsonify(message="Set User status Fail"), 500

    @app.route("/")
    def hello_world():
        return "Hello World"

    return app

if __name__ == "__main__":
    app = create_app()

    app.run()