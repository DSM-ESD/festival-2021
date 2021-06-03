from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
    app.database = database

    @app.route('/save-game-data', methods = ['POST'])
    def save_game_data():
        game_data = request.json
        user_id = app.database.execute(text("""
                                            INSERT INTO game_result (
                                            id,
                                            score,
                                            game_type
                                           ) VALUES (
                                            :id,
                                            :score,
                                            game_type
                                           )
                                            """), game_data).lastrowid

        return "", 200


    @app.route("/")
    def hello_world():
        return "Hello World"

    return app

if __name__ == "__main__":
    app = create_app()

    app.run()