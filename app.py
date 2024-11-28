from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Можливі ходи в грі
moves = ["Камінь", "Ножиці", "Папір"]

# Функція для визначення переможця
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Нічия!"
    elif (player_move == "Камінь" and computer_move == "Ножиці") or \
         (player_move == "Ножиці" and computer_move == "Папір") or \
         (player_move == "Папір" and computer_move == "Камінь"):
        return "Ви виграли!"
    else:
        return "Комп'ютер виграв!"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        player_move = request.form["move"]
        computer_move = random.choice(moves)
        result = determine_winner(player_move, computer_move)
        return render_template("index.html", player_move=player_move, computer_move=computer_move, result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
