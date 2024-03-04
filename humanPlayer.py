from player import Player
class HumanPlayer(Player):
  '''
  This class represent a human player
  '''
  def make_move(self, board):
  #Implement the move logic of the human player
    move_map = {
          1: (0, 0), 2: (0, 1), 3: (0, 2),
          4: (1, 0), 5: (1, 1), 6: (1, 2),
          7: (2, 0), 8: (2, 1), 9: (2, 2),
    }
    print(f"\nIt is your turn: \n")
    while True:
        move = int(input("Enter a position (1-9): "))
        if move in move_map:
          row, col = move_map[move]
          if board.make_move(row, col, self.symbol):
            break
          else:
            print("The position already taken, try another one")   
        else:
          print("Invalid move, try again..")

