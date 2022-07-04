
from aptitud import EvaluarAptitud  # importamos la clase para crear el objeto 



algoritmoGenetico = EvaluarAptitud(5) # creamos el objeto algoritmoGenetico  y le pasamos por parametro la dimension del tablero
algoritmoGenetico.Evaluar()           # llamamos al metodo del objeto para crear la primera poblacion y evaluar su desempeños hasta alcanzar la mejor solucion
algoritmoGenetico.imprimir_tablero()  #imprimimos el tablero por consola y la posicion de cada reina en cada fila

algoritmoGenetico.set_nReinas(9)      # mediante el metodo set_nReinas modificamos la dimension del tablero y reseteamos los atributos para una nueva evaluacion
algoritmoGenetico.Evaluar()
algoritmoGenetico.imprimir_tablero()

algoritmoGenetico.set_nReinas(12)
algoritmoGenetico.Evaluar()
algoritmoGenetico.imprimir_tablero()