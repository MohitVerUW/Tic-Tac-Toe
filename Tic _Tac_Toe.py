#--------------------IMPORT BLOCK----------------------------------
# import tkinter GUI library
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#--------------------FUNCTION BLOCKS----------------------------------

def create_Buttons(buttons):
    """This function is used to create the buttons that the user would click to place their \"X" or \"O".
    The function will also position the buttons and define a specified height and width."""

    # Define grid to resize each button as user expands or reduces window size
    for row in range(3):
        for col in range(3):
            tk.Grid.rowconfigure(root, row, weight = 1)
            tk.Grid.columnconfigure(root, col, weight = 1)

    # Initilze variables that will fix the button height and width
    b_width = 6
    b_height = 6

    # for-loop used to make the buttons for the tic-tac-toe board
    for row_index in range(3):
        for col_index in range(3):
            # Create buttons
            bttn = Button(root, text = " ", width = b_width, height = b_height, font = ("Arial", 60))
            # Store button in the 'buttons' list
            buttons[row_index][col_index] = bttn
            # Position the buttons in grid
            bttn.grid(row = row_index, column = col_index, sticky = N + S + E + W)
            # When a button is pressed go to player_move() function to update board
            # lambda is used to pass the value of the variable when it is called
            bttn["command"] = lambda bttn=bttn, row_index = row_index, col_index = col_index: player_move(bttn, row_index, col_index)

def player_move(b_Click, x, y):
    """This function will help us keep track of whose move it is and update information on our virtual tic-tac-toe
    board and determine if there's a winner
    b_Click == button clicked by player
    x == row index of the button clicked
    y == column index of the button clicked"""

    # Called these global variables so we can update the number moves performed and inform user whose turn it is
    global num_Moves
    global player_status             # P1 - player 1 and is X; P2 - player 2 and is O

    if b_Click["text"] == " " and player_status == "P1":

        b_Click["text"] = "X"        # Update the text value in the tkinter button and display on GUI
        num_Moves += 1               # Increment the number of moves played
        board_Update("X", x, y)      # Go into function and update vitural board using arguments passed

        # Once we have completed a total of at least 5 moves, we then determine if there's a winner
        if num_Moves >= 5:
            Winner("X", num_Moves)   # After each move, determine if this player is the winner

        player_status = "P2"         # Update whose turn it is now

    elif b_Click["text"] == " " and player_status == "P2":

        b_Click["text"] = "O"
        num_Moves += 1
        board_Update("O", x, y)

        # Once we have completed a total of at least 5 moves, we then determine if there's a winner
        if num_Moves >= 5:
            Winner("O", num_Moves)

        player_status = "P1"

    # If a tile on the board is selected that is already chosen, throw an error message
    else:
        messagebox.showerror("Game Error", "You cannot select this block since it's already taken!!")

def board_Update(letter, row_B, col_B):
    """This function is used to update the virtual board from which we will information to determine if someone has won
    letter = Either X or O
    row_B == row index of the button clicked
    row_C == column index of the button clicked"""

    # Called variable board as global to update it's value in function
    global board

    # Update value of board to the letter of the player based on the (row, column) pair for the button clicked
    board[row_B][col_B] = letter

    print(board)

def Winner(symbol, count):
    """This function will be to determine which player has one the game!
    There are 3 ways of winning the game:
    1) Either one of 3 rows is full of the same letters
    2) Either one of 3 columns is full of the same letters
    3) Either one of the 2 diagonals is full of the same letters
    If a winner is declared, disable all buttons and return a message congradulating the winner
    If it's a tie game, disable all buttons and return a message saying TIE GAME!"""

    # Called buttons list here to pass into disable_buttons() function to disable all buttons at end of game
    global buttons

    # Declare var win to let us determine if a winner exists
    win = False

    # Check each row, column and diagonal to see if anyone won after their move
    for jj in range(3):
        # Check rows of virtual board for win
        if board[jj][0] == symbol and  board[jj][1] == symbol and board[jj][2] == symbol:
            win = True
            disable_Buttons(buttons)
            print(f"CONGRADULATIONS {symbol}, WON THE GAME!!")
            return messagebox.showinfo(message = f"CONGRADULATIONS {symbol}, WON THE GAME!!")

        # Check columns of virtual board for win
        elif board[0][jj] == symbol and board[1][jj] == symbol and board[2][jj] == symbol:
            win = True
            disable_Buttons(buttons)
            print(f"CONGRADULATIONS {symbol}, WON THE GAME!!")
            return messagebox.showinfo(message = f"CONGRADULATIONS {symbol}, WON THE GAME!!")

        # # Check diagonals for wins
        elif (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or \
                (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
            win = True
            disable_Buttons(buttons)
            print(f"CONGRADULATIONS {symbol}, WON THE GAME!!")
            return messagebox.showinfo(message = f"CONGRADULATIONS {symbol}, WON THE GAME!!")

    # Check to see if there is a tie
    if count == 9 and win == False:
        disable_Buttons(buttons)
        print("IT'S A TIE GAME!!")
        return messagebox.showinfo(message=f"IT'S A TIE GAME!!")

def disable_Buttons(grid_bttns):
    """This function is used to diable the buttons once a winner has been declared or it's a tie!"""

    for ll in range(3):
        for mm in range(3):
            grid_bttns[ll][mm].config(state = DISABLED)


#--------------------MAIN CODE BLOCK----------------------------------
# Create GUI window
root = Tk()
root.title("Tic-Tac-Toe!")

# Create the GUI window so that it has a defined size
root.geometry("500x500")

# Create a 2-Dimensional empty list to mimic the board. This will also be used to store player info to see who wins
# The for-loop that follows will be used to make a 2-D list
board = []

for ii in range(3):
    board.append(["", "", ""])

# Initialize two variables: 1)num_Moves which will tell us how many moves have happened and 2) player_Status to tell us
# whose turn it is
num_Moves = 0
player_status = "P1"

# Create a list that will store the buttons created in create_Buttons(). Since the create_Buttons() function
# will use a for-loop to create buttons I need to store them to deactivate buttons at the end of the game
buttons = [[None, None,None],[ None, None,None], [None, None,None]]

# Create buttons
create_Buttons(buttons)

# This command will have the GUI application running
root.mainloop()