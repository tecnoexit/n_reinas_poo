# clase que genera la poblacion
import random
import numpy as np

class GenerarPoblacion(): # genera la poblacion inicial y la matriz inicial acorde a la cantidad de reinas
    def __init__(self) :
        pass
    
    @staticmethod
    def permutacionAleatoria(n): # metodo estatico que genera la poblacion inicial y la estructura del tablero en base a las dimensiones pasadas por parametro
        poblacionInicial = list(range(n))
        random.shuffle(poblacionInicial)

        tablero = np.zeros((n, n), dtype=int)
        for i in range(n):
            tablero[i][poblacionInicial[i]] = 1

        return tablero, poblacionInicial