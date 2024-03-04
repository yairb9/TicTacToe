class Board:
  def __init__(self) -> None:
    #initialize a 3X3 board game
    self.board = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]
  
  def display_board(self):
  #Print the board
    for row in self.board:
      display_row = []
      for cell in row:
        if cell == None:
          display_row.append(" ")
        elif cell == 0:
          display_row.append("O")
        else:
          display_row.append("X")
      print('|'.join(display_row))
      print("-----")

  def make_move(self, row, col, player):
  # Make a move on the board
    if self.board[row][col] is None:
      self.board[row][col] = player
      return True
    return False
  
  def is_winner(self, player):
  # Check for a win condition
  # Check rows
    for row in self.board:
      if all(cell == player for cell in row):
        return True
  # Check columns
    for col in range(3):
      if all(self.board[row][col] == player for row in range(3)):
        return True
  # Check diagonals(the main diagonal or the secondary)
    if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
      return True
    return False
  
  def is_full(self):
  #Check if the board is full
    for row in self.board:
      if None in row:
        return False
    return True
      
  def get_available_moves(self):
  #Search and return for all the empty cells on the board
    moves = []
    for row in range(3):
      for col in range(3):
        if self.board[row][col] == None:
          moves.append((row, col))
    return moves


