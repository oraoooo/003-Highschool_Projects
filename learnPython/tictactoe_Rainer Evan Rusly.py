from tkinter import *
import random
from tkinter import simpledialog, messagebox

# Inisialisasi jendela
board = Tk()
board.title("Tic-Tac-Toe")
board.resizable(False, False)
board.configure(bg="#f0f0f0")

# Variabel pemain
characters = ["X", "O"]
players = {}
player = random.choice(characters)

# Fungsi memulai ulang permainan
def restart():
    global player
    player = random.choice(characters)
    label.config(text=players[player] + "'s turn (" + player + ")")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="SystemButtonFace")

# Fungsi saat pemain melakukan giliran
def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        result = check_winner()
        if result is False:
            player = characters[0] if player == characters[1] else characters[1]
            label.config(text=players[player] + "'s turn (" + player + ")")
        elif result is True:
            label.config(text=players[player] + " wins!")
            highlight_winner()
        elif result == "Tie":
            label.config(text="It's a Tie!")

# Fungsi memeriksa pemenang
def check_winner():
    # Baris
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            global win_coords
            win_coords = [(row, 0), (row, 1), (row, 2)]
            return True
    # Kolom
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            win_coords = [(0, column), (1, column), (2, column)]
            return True
    # Diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        win_coords = [(0, 0), (1, 1), (2, 2)]
        return True
    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != '':
        win_coords = [(2, 0), (1, 1), (0, 2)]
        return True
    # Cek seri
    if empty_spaces() is False:
        return "Tie"
    return False

# Fungsi mewarnai kotak pemenang
def highlight_winner():
    for coord in win_coords:
        buttons[coord[0]][coord[1]].config(bg="lightgreen")

# Fungsi mengecek sisa ruang kosong
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    return spaces != 0

# Pop-up input nama pemain
players["X"] = simpledialog.askstring("Pemain X", "Masukkan nama pemain untuk 'X':") or "Pemain X"
players["O"] = simpledialog.askstring("Pemain O", "Masukkan nama pemain untuk 'O':") or "Pemain O"

# Label giliran
label = Label(board, text=players[player] + "'s turn (" + player + ")", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
label.pack(pady=10)

# Tombol new game
new_game_button = Button(board, text="New Game", font=("Helvetica", 14), bg="#dddddd", command=restart)
new_game_button.pack(pady=5)

# Grid papan permainan
frame = Frame(board, bg="#f0f0f0")
frame.pack()

buttons = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=('Consolas', 36),
            width=5,
            height=2,
            bg="SystemButtonFace",
            command=lambda row=row, column=column: next_turn(row, column)
        )
        buttons[row][column].grid(row=row, column=column, padx=5, pady=5)

board.mainloop()
