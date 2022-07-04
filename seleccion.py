# clase que se encarga de la seleccion
import random
import numpy as np
from reproduccion import Descendencia



class Seleccion(): # metodo que se encarga de los cruces en la poblacion
    
    
    @staticmethod
    def check_cruce(board, queens, mdiag, sdiag, i, j,n):
        Descendencia.cruce(board, i, j)
        mdiag[n - i + queens[i] - 1] -= 1
        sdiag[i + queens[i]] -= 1
        mdiag[n - j + queens[j] - 1] -= 1
        sdiag[j + queens[j]] -= 1
        queens[i], queens[j] = queens[j], queens[i]
        mdiag[n - i + queens[i] - 1] += 1
        sdiag[i + queens[i]] += 1
        mdiag[n - j + queens[j] - 1] += 1
        sdiag[j + queens[j]] += 1

        col_sum = 0
        for i in range(len(board) * 2 - 1):
            if mdiag[i] > 1:
                col_sum += 1
            if sdiag[i] > 1:
                col_sum += 1

        return col_sum