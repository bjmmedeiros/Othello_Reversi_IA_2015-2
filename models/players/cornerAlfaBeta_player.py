

class CornerAlfaBetaPlayer:



    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.alphabeta(board, 3, self.edge_eval)[1]

    def alphabeta_value(self, board, depth, alpha, beta, eval):

        if depth == 0 or not board.ison:
            return eval(board)

        for move in board.valid_moves(self.color):
            g = board.get_clone()
            g.play(move, self.color)

            if beta != 'inf':
                next_alpha = -1 * beta
            else:
                next_alpha = - 1 * 'inf'
            if alpha != -1 * 'inf':
                next_beta = -1 * alpha
            else:
                next_beta = 'inf'
            val = -1 * self.alphabeta_value(g, depth-1, next_alpha, next_beta, eval)

            if alpha == -1 * 'inf' or val > alpha:
                alpha = val

            if (alpha !=  -1 * 'inf') and (beta != 'inf') and alpha >= beta:
                return beta

        return alpha

    def alphabeta(self, board, depth, eval):

        best_val, best_move = None, None


        for move in board.valid_moves(self.color):
            g = board.get_clone()
            g.play(move, self.color)

            if best_val != None:
                next_beta = -1 * best_val
            else:
                next_beta = 'inf'
            val = -1 * self.alphabeta_value(g, depth, -1 * 'inf', next_beta, eval)

            if best_val is 0 or val > best_val:
                (best_val, best_move) = (val, move)

        return (best_val, best_move)


    def edge_eval(self, board):

        import math
        corners = [[1,1],[1,8], [8,1], [8,8]]
        other_player = board._opponent(self.color)
        score = 0
        for i in range(8):
            for j in range(8):
                delta = 1
                if i == 0 or i == 7:
                    delta += 5
                if j == 0 or j == 7:
                    delta += 5

                if i == 1 or i == 6:
                    delta -= 5
                if j == 1 or j == 6:
                    delta -= 5

                for corner in corners:
                    distX = abs(corner[0] - i)
                    distY = abs(corner[1] - j)
                    dist  = math.sqrt(distX*distX + distY*distY)
                    if dist < 4:
                        delta += 3

                if board.get_square_color(i, j) == self.color:
                    score += delta
                elif board.get_square_color(i, j) == other_player:
                    score -= delta

        return score
