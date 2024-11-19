import tkinter as tk
import math


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":

            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    for row in buttons:
        for button in row:
            if button["text"] == "":
                return 0
    return "Tie"


def minimax(depth, is_maximizing, alpha, beta):
    winner = check_winner()
    if winner == "X":
        return -10 + depth
    if winner == "O":
        return 10 - depth
    if winner == "Tie":
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if buttons[i][j]["text"] == "":
                    buttons[i][j]["text"] = "O"
                    eval = minimax(depth + 1, False, alpha, beta)
                    buttons[i][j]["text"] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if buttons[i][j]["text"] == "":
                    buttons[i][j]["text"] = "X"
                    eval = minimax(depth + 1, True, alpha, beta)
                    buttons[i][j]["text"] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                buttons[i][j]["text"] = "O"
                score = minimax(0, False, -math.inf, math.inf)
                buttons[i][j]["text"] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        buttons[best_move[0]][best_move[1]]["text"] = "O"
        buttons[best_move[0]][best_move[1]].config(state="disabled")
        result = check_winner()
        if result:
            show_winner(result)


def player_move(row, col):
    if buttons[row][col]["text"] == "" and not check_winner():
        buttons[row][col]["text"] = "X"
        buttons[row][col].config(state="disabled")
        result = check_winner()
        if result:
            show_winner(result)
        else:
            ai_move()

def color(color):

    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            buttons[i][0].config(background=color)
            buttons[i][1].config(background=color)
            buttons[i][2].config(background=color)
            return 0
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            buttons[0][i].config(background=color)
            buttons[1][i].config(background=color)
            buttons[2][i].config(background=color)
            return 0
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            buttons[0][0].config(background=color)
            buttons[1][1].config(background=color)
            buttons[2][2].config(background=color)
            return 0

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            buttons[0][2].config(background=color)
            buttons[1][1].config(background=color)
            buttons[2][0].config(background=color)
            return 0
    else:
        for row in range (3):
            for column in range (3):
                buttons[row][column].config(background=color)
        return 0

def show_winner(winner):
    if winner == "Tie":
        label.config(text="It's a Tie!", background="yellow")
        color("gold")
    elif winner == "X":
        label.config(text="You Win!", background="Green")
        color("yellowgreen")
    else:
        label.config(text="You Lose!", background="Red")
        color("plum")
    for row in buttons:
        for button in row:
            button.config(state="disabled")


def reset_game():
    global buttons
    label.config(text="Best Of Luck", background="Gray")
    for row in buttons:
        for button in row:
            button.config(text="", state="normal", background="white")

# GUI
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
label = tk.Label(window, text="Best Of Luck", background="Gray", font=("Arial", 20), width=32)
label.pack()

frame = tk.Frame(window)
frame.pack()

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text="", background="white", font=("roboto", 40), width=5, height=2,
                                  command=lambda row=row, col=column: player_move(row, col))
        buttons[row][column].grid(row=row, column=column)

reset_button = tk.Button(window, text="Restart", font=("roboto", 20), command=reset_game, width=32)
reset_button.pack()

window.mainloop()


