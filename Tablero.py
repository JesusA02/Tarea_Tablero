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
        tablero = Tablero(40, fichas)
        
        ficha1 = Ficha("roja")
        fichas.append(ficha1)

        ficha2 = Ficha("azul")
        fichas.append(ficha2)
        

        ficha3 = Ficha("verde")
        fichas.append(ficha3)
        
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    def turnos(self):
        contador = 0
        avanzar = True
        while avanzar:
            if contador == 0:
                self.fichas[0].avanzar()
                contador +=1
            elif contador == 1:
                self.fichas[1].avanzar()
                contador +=1
            elif contador == 2:
                self.fichas[2].avanzar()
                contador +=1
            elif contador == 3:
                contador = 0


    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self

#ficha = Ficha("azul")
#ficha2 = Ficha("roja")
#tablero = Tablero(40, [ficha])
#print("Tablero", tablero.fichas[0].color)
#print("casillas", tablero.casillas)