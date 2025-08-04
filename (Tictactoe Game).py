from tkinter import *
from tkinter import messagebox

current_player = "X"
board = [""] * 9
buttons = []
game_over = False

# Define create_window
def create_window():
    window = Tk()
    window.title("Tic Tac Toe Game")
    window.config(bg='#F4F1DE')  # Light beige background
    window.geometry('400x550')
    window.resizable(False, False)
    return window

def check_winner():
    """Check if there is a winner or the game is tie"""
    winning_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combination:
        if (board[combo[0]] == board[combo[1]] == board[combo[2]] != ""):
            global game_over
            game_over = True
            messagebox.showinfo("Game Over", f"Player {board[combo[0]]} Wins")
            return True
    if "" not in board:
        game_over = True
        messagebox.showinfo("Game Over", "It's a tie")
        return True
    return False

def button_click(position):
    """Handle button click"""
    global current_player
    if game_over or board[position] != "":
        return
    board[position] = current_player
    buttons[position].config(text=current_player, state="disabled",
                             disabledforeground="#FF595E" if current_player == "X" else "#1982C4")
    if not check_winner():
        current_player = "O" if current_player == "X" else "X"
        update_status_label()

def reset_game():
    """Reset the game to start over"""
    global current_player, board, game_over
    current_player = "X"
    board = [""] * 9
    game_over = False
    for button in buttons:
        button.config(text="", state="normal", bg="#FFCA3A", fg="black")
    update_status_label()

def update_status_label():
    """Update the status label to show current player"""
    status_label.config(text=f"Current Player: {current_player}",
                        bg='#F4F1DE', fg='#8B5E3C')

# Frame
def create_game_board(window):
    """Create the 3x3 grid of buttons"""
    global buttons

    board_frame = Frame(window, bg='#F4F1DE')
    board_frame.pack(pady=10)

    for i in range(9):
        row = i // 3
        col = i % 3
        button = Button(board_frame,
                        text="",
                        width=6,
                        height=3,
                        font=("Arial", 20, "bold"),
                        bg="#FFCA3A",  # Golden
                        fg="black",
                        activebackground="#8AC926",  # Bright green when hovered
                        command=lambda pos=i: button_click(pos))
        button.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(button)

def create_control(window):
    """Create the control buttons and the status label"""
    global status_label

    status_label = Label(window,
                         text=f"Current Player: {current_player}",
                         fg='#8B5E3C',  # Warm brown
                         bg='#F4F1DE',
                         font=("Arial", 12))
    status_label.pack(pady=5)

    reset_button = Button(window,
                          text="New Game",
                          bg='#1982C4',  # Calm blue
                          fg='white',
                          activebackground='#6A4C93',  # Purple
                          font=("Arial", 12),
                          command=reset_game)
    reset_button.pack(pady=5)

# Define main
def main():
    window = create_window()
    title_label = Label(window,
                        text="Tic Tac Toe",
                        font=("Arial", 16, "bold"),
                        bg='#F4F1DE',
                        fg='#6A4C93')  # Purple
    title_label.pack(pady=10)
    create_game_board(window)
    create_control(window)
    window.mainloop()

main()
