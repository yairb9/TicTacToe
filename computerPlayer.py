import random
from player import Player

class ComputerPlayer(Player):
    '''
    This class implement a computer player that choose his steps using the MinMax algorithm
    '''
    def make_move(self, board):
    #Implement the move logic of the computer player using MinMax algorithm to determine the best next move
        print(f"\nIt is the computer turn: \n")
        _, best_move = self.minimax(board, True)
        board.make_move(best_move[0], best_move[1], self.symbol)

    def minimax(self, board, is_maximizing):
        # Base cases: check for win, lose or tie
        if board.is_winner(self.symbol):  # Computer win
            return (1, None)
        elif board.is_winner(1 - self.symbol):  # Human win
            return (-1, None)
        elif board.is_full():  # Tie
            return (0, None)

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for move in board.get_available_moves():
                # Simulate move
                board.make_move(move[0], move[1], self.symbol)
                score = self.minimax(board, False)[0]
                # Undo move
                board.board[move[0]][move[1]] = None

                if score > best_score:
                    best_score = score
                    best_move = move
            return (best_score, best_move)
        
        else:  # Minimizing player
            best_score = float('inf')
            best_move = None

            for move in board.get_available_moves():
                # Simulate move
                board.make_move(move[0], move[1], 1 - self.symbol)
                score = self.minimax(board, True)[0]
                # Undo move
                board.board[move[0]][move[1]] = None

                if score < best_score:
                    best_score = score
                    best_move = move
            return (best_score, best_move)