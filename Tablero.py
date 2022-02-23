from Ficha import *

class Tablero:

    #Defina aquí los atributos de Tablero
    
    casillas = 0
    fichas = []

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno




    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self, casillas_, fichas ):
        self.casillas = casillas_
        self.fichas = fichas
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase


    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self

ficha1 = Ficha("azul")
ficha2 = Ficha("roja")
tablero = Tablero(40, [fichas])
print("Tablero", tablero.fichas[0].color)
#print("casillas", tablero.casillas)