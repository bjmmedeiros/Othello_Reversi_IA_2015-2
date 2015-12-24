from models.board import Board

class MobilPlayer:
    def __init__(self, color):
        self.color = color
        self.opponent_color = self.getOppositeColor(color)

    def getOppositeColor(self, color):
        if color == Board.BLACK:
            return Board.WHITE
        else:
            return Board.BLACK

    def play(self, board):
        alpha = -float('inf')
        beta = float('inf')
        minimax = self.max(board, 2, alpha, beta)
        return minimax[0]

    def getBestMove(self, board, color):
        best_value = -float('inf')
        moves = board.valid_moves(color)
        retMove = None
        movesLength = float('inf')
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,color)

            valid_moves = board_clone.valid_moves(self.getOppositeColor(color))

            if valid_moves.__len__() < movesLength:
                movesLength = valid_moves.__len__()
                retMove = move

        return retMove, (moves.__len__() - movesLength)

    def max(self, board, depth, alpha, beta):
        if depth == 0:
            return self.getBestMove(board, self.color)

        moves = board.valid_moves(self.color)

        if moves.__len__() == 0:
            return None, float('inf')

        best_value = -float('inf')

        retMove = None
        for move in moves:
            #import pdb; pdb.set_trace()
            board_clone = board.get_clone()
            board_clone.play(move,self.color)
            min_value = self.min(board_clone, depth-1, alpha, beta)[1]

            if min_value >= best_value:
                best_value = min_value
                retMove = move

            alpha = max(best_value, alpha)
            #   import pdb; pdb.set_trace()
            if alpha > beta:
                #import pdb; pdb.set_trace()
                return None, float('inf')

        return retMove, best_value



    def min(self, board, depth, alpha, beta):

        if depth == 0:
            return self.getBestMove(board, self.opponent_color)

        moves = board.valid_moves(self.opponent_color)

        if moves.__len__() == 0:
            return None, -float('inf')

        best_value = float('inf')
        retMove = None

        for move in moves:
            # import pdb; pdb.set_trace()
            board_clone = board.get_clone()
            board_clone.play(move,self.opponent_color)
            max_value = self.max(board_clone, depth-1, alpha, beta)[1]

            if max_value <= best_value:
                best_value = max_value
                retMove = move

            beta = min(best_value, beta)

            if alpha > beta:
                #import pdb; pdb.set_trace()
                return None, -float('inf')

        return retMove, best_value