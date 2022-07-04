#clase que mide la aptitud

from asyncio.windows_events import NULL
from textwrap import wrap

from poblacion import GenerarPoblacion
from reproduccion import Descendencia
from seleccion import Seleccion


import random
import numpy as np


class EvaluarAptitud(object): # clase para la intancia de un objeto que va a ser evaluado, y modificado hasta que cumpla con las espectativas de la solucion
    
    #---------------------- BLOQUE PARA PATRON DE DISEÑO SINGLETON--------------------------------
    __instancia=None
    def __new__(cls, val):
        if EvaluarAptitud.__instancia is None:
            EvaluarAptitud.__instancia=object.__new__(cls)
        EvaluarAptitud.__instancia.n=val
        return EvaluarAptitud.__instancia
    #---------------------------------------------------------------------------------------------
    
    
    def __init__(self, n):
        self.tablero, self.reinas = [],[] # inicializacion de atibutos para el tablero y las reinas
        self.n=n        # varible entera para la dimension del tablero y la cantidad de reinas 
        self.resuelto=False # varible boleana para terminar el bucle en caso de que se encuentre la solucion
        self.mdiag=[]   # variables de uso temporal en cada ciclo para evaluar las coliciones en las diagonales
        self.sdiag=[]
        self.iteraciones=0
        
    def Evaluar(self): # 
        
        while not self.resuelto:
            self.tablero, self.reinas = GenerarPoblacion.permutacionAleatoria(self.n) #llamamos al metodo estatico de la clase generar poblacion
            
            cant_coliciones=self.diagonal() # metodo 
            n_swaps = -1
            while n_swaps != 0: #Ciclo que evalua cada nueva poblacion 
                
                n_swaps = 0
                for i in range(self.n-1):
                    for j in range(1, self.n):
                        if self.reinaAtacada(self.mdiag, self.sdiag, i,  self.reinas[i], self.n) or self.reinaAtacada(self.mdiag, self.sdiag, i, self.reinas[j], self.n):
                            new_col = Seleccion.check_cruce(self.tablero.copy(),self.reinas.copy(), self.mdiag.copy(), self.sdiag.copy(), i, j,self.n)
                            if new_col < cant_coliciones:
                                Descendencia.cruce(self.tablero, i, j) 
                                self.mdiag[self.n-i+self.reinas[i]-1] -= 1
                                self.sdiag[i+self.reinas[i]] -= 1
                                self.mdiag[self.n - j + self.reinas[j] - 1] -= 1
                                self.sdiag[j + self.reinas[j]] -= 1
                                self.reinas[i], self.reinas[j] = self.reinas[j], self.reinas[i]
                                self.mdiag[self.n - i + self.reinas[i] - 1] += 1
                                self.sdiag[i + self.reinas[i]] += 1
                                self.mdiag[self.n - j + self.reinas[j] - 1] += 1
                                self.sdiag[j + self.reinas[j]] += 1
                                cant_coliciones = new_col
                                n_swaps += 1
                self.iteraciones +=1
            if cant_coliciones == 0:
                self.resuelto = True
    
    
    
    def diagonal(self): # metodo que cuenta la coliciones en las diagonales
        self.mdiag = np.zeros(len(self.tablero)*2 - 1, dtype=int)
        self.sdiag = np.zeros(len(self.tablero)*2 - 1, dtype=int)

        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if self.tablero[i][j] == 1:
                    self.sdiag[i+j] += 1
                    self.mdiag[len(self.tablero) - i + j - 1] += 1

        col_sum = 0
        for i in range(len(self.tablero) * 2 - 1):
            if self.mdiag[i] > 1:
                col_sum += 1
            if self.sdiag[i] > 1:
                col_sum += 1
        
        return col_sum
    
    
    def reinaAtacada(self, mdiag, sdiag, i, j, n): # metodo que chequea si la reina es atacada en las diagonales
        if mdiag[n-i+j-1] > 1: return True
        if sdiag[i+j] > 1: return True
        return False
    
    def set_nReinas(self, n): # metodo que setea en numero de reinas y las dimensiones del tablero
        self.n=n
        self.tablero, self.reinas = [],[]
        self.resuelto=False
        self.mdiag=[]
        self.sdiag=[]
        self.iteraciones=0
        
        
    def imprimir_tablero(self): # metodo que imprime el tablero y la posicion de las reinas en cada fila
        print()
        print("TABLERO")
        print()
        for fila in self.tablero:
            print(fila)
        print()
        print("Posicion de las Reinas: {}".format(self.reinas))
        print("Cantidad de iteraciones hasta la solucion : ", str(self.iteraciones))