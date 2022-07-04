
class Descendencia():
    
    @staticmethod
    def cruce(board, i, j):# metodo que genera los hijos
        board[i], board[j] = board[j].copy(), board[i].copy()