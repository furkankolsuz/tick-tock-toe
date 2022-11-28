#-------- variables

#game board will come data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# know if the game is over yet
game_still_going = True

# who the winner is
winner = None

# who the current player is (X goes first)
current_player = "X"


# ------------- functions ---------------

# play a game
def play_game():

  #initial game board
  display_board()

  # loop till game over
  while game_still_going:

    # handle a turn
    handle_turn(current_player)

    # check the game is over
    check_if_game_over()

    # flip player
    flip_player()
  
  # when game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# handle a turn for player
def handle_turn(player):

  # get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # make sure it is a valid input
  valid = False
  while not valid:

    # make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # get correct index in our board list
    position = int(position) - 1

    # make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # put the game piece on the board
  board[position] = player

  # print the game board
  display_board()


# check game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# check somebody has won
def check_for_winner():
  # set global variables
  global winner
  # check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# check the rows for a win
def check_rows():
  # set global variables
  global game_still_going
  # check any of the rows have all the same value
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # or return None
  else:
    return None


# check the columns for a win
def check_columns():
  # set global variables
  global game_still_going
  # check any of the columns have all the same value 
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # or return None
  else:
    return None


# check the diagonals for a win
def check_diagonals():
  # set global variables
  global game_still_going
  # check any of the columns have all the same value
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # or return None
  else:
    return None


# check there is a tie
def check_for_tie():
  # set global variables
  global game_still_going
  # if board is full
  if "-" not in board:
    game_still_going = False
    return True
  # else there is no tie
  else:
    return False


# flip the current player
def flip_player():
  # Global variable
  global current_player
  # if the current player was X, change O
  if current_player == "X":
    current_player = "O"
  # or if the current player was O, change X
  elif current_player == "O":
    current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()