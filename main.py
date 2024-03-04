from board import Board
from humanPlayer import HumanPlayer
from computerPlayer import ComputerPlayer

def print_welcome():
    print("""
 _____ _        _____            _____          
|_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \\ / _ \\
  | | | | (__    | | (_| | (__    | | (_) |  __/
  |_| |_|\\___|   |_|\\__,_|\\___|   |_|\\___/ \\___|
    """)

    print("You win- you get 100$, you lose- you give me 5$. deal?\n")

  #display the initial board so the user could see the cells numbers
    print("The Board:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")



def main():
  print_welcome()
  board = Board()
  #  0  represents O (the player), and 1 is  X (the computer)
  human = HumanPlayer(0)
  computer = ComputerPlayer(1)
  current_player = human

  while True:
      
      current_player.make_move(board)

      #check for a win
      if board.is_winner(current_player.symbol):
         print(f"Player {current_player.symbol} wins")
         break
      
      #check for a tie
      if board.is_full():
         print("Tie")
         break
      
      board.display_board()
      #switch players if the game continues
      current_player = computer if current_player == human else human

  board.display_board()


if __name__ == "__main__":
    main()