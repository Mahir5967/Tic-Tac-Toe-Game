from tkinter import *
from tkinter import messagebox

current_player = "X"
board = [""] * 9
buttons = []
game_over = False

# Create window with formal theme
def create_window():
    window = Tk()
    window.title("Tic Tac Toe Game")
    window.config(bg='#2c3e50')  # Dark background
    window.geometry('400x550')
    window.resizable(False, False)
    return window

# Check winner or tie
def check_winner():
    winning_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combination:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            global game_over
            game_over = True
            messagebox.showinfo("Game Over", f"Player {board[combo[0]]} Wins")
            return True
    if "" not in board:
        game_over = True
        messagebox.showinfo("Game Over", "It's a tie")
        return True
    return False

# Button click
def button_click(position):
    global current_player
    if game_over or board[position] != "":
        return
    board[position] = current_player
    buttons[position].config(text=current_player, state="disabled",
                             disabledforeground="#e74c3c" if current_player == "X" else "#3498db")
    if not check_winner():
        current_player = "O" if current_player == "X" else "X"
        update_status_label()

# Reset game
def reset_game():
    global current_player, board, game_over
    current_player = "X"
    board = [""] * 9
    game_over = False
    for button in buttons:
        button.config(text="", state="normal", bg="#34495e", fg="white")
    update_status_label()

# Update current player status
def update_status_label():
    status_label.config(text=f"Current Player: {current_player}",
                        bg='#2c3e50', fg='#ecf0f1')

# Create 3x3 board
def create_game_board(window):
    global buttons
    board_frame = Frame(window, bg='#2c3e50')
    board_frame.pack(pady=10)
    for i in range(9):
        row = i // 3
        col = i % 3
        button = Button(board_frame,
                        text="",
                        width=6,
                        height=3,
                        font=("Arial", 20, "bold"),
                        bg="#34495e",  # Dark blue-gray
                        fg="white",
                        activebackground="#16a085",  # Teal on hover
                        command=lambda pos=i: button_click(pos))
        button.grid(row=row, column=col, padx=3, pady=3)
        buttons.append(button)

# Status label and reset button
def create_control(window):
    global status_label
    status_label = Label(window,
                         text=f"Current Player: {current_player}",
                         fg='#ecf0f1',
                         bg='#2c3e50',
                         font=("Arial", 12))
    status_label.pack(pady=5)

    reset_button = Button(window,
                          text="New Game",
                          bg='#2980b9',  # Blue
                          fg='white',
                          activebackground='#8e44ad',  # Purple
                          font=("Arial", 12),
                          command=reset_game)
    reset_button.pack(pady=5)

# Main function
def main():
    window = create_window()
    title_label = Label(window,
                        text="Tic Tac Toe",
                        font=("Arial", 16, "bold"),
                        bg='#2c3e50',
                        fg='#f1c40f')  # Golden yellow
    title_label.pack(pady=10)
    create_game_board(window)
    create_control(window)
    window.mainloop()

main()
