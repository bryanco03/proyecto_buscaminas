from casilla import Casilla
from random import random


class Tablero():
    def __init__(self,tamaño, prob_bomba):
        self.tamaño = tamaño
        self.prob_bomba = prob_bomba 
        self.perder = False
        self.ganar = False 
        self.num_clicked = 0
        self.num_nobombas = 0
        self.set_tablero()


    def set_tablero(self):
        self.tablero = []

        for row in range(self.tamaño[0]):
            row = []
            for col in range(self.tamaño[1]):

                bomba = random() < self.prob_bomba
                    
                if (not bomba):
                    self.num_nobombas +=1
                casilla = Casilla(bomba)
                row.append(casilla)
            self.tablero.append(row)
        self.set_casillas_cercanas()



    def set_casillas_cercanas(self):
        for row in range(self.tamaño[0]):
            for col in range(self.tamaño[1]):
                casilla = self.get_casilla((row,col))
                vecinos = self.get_lista_vecinos((row,col))
                casilla.set_vecinos(vecinos)

    def get_lista_vecinos(self,index):
        vecinos = []
        for row in range(index[0]-1, index[0]+2):
            for col in range(index[1]-1, index[1]+2):
                fuera_rango = row < 0 or row >= self.tamaño[0] or col < 0 or col >= self.tamaño[1]
                fuera_rango2 = row == index[0] and col == index[1]
                if fuera_rango or fuera_rango2:
                    continue
                vecinos.append(self.get_casilla((row,col)))
        return vecinos

    def get_size(self):
        return self.tamaño
    
    def get_casilla(self,index):
        return self.tablero[index[0]][index[1]]
    
    def handleclick(self,casilla, bandera):
        if (casilla.get_clicked()) or (not bandera and casilla.get_bandera()):
            return 
        if bandera:
            casilla.toggle_bandera()
            return
        casilla.click()
        if casilla.get_bomba():
            self.perder =  True
            return
        self.num_clicked +=1
        if casilla.get_num_alrededor() != 0:
            return
        for vecino in casilla.get_vecinos():
            if not vecino.get_bomba() and not vecino.get_clicked():
                self.handleclick(vecino,False)


    def get_perder(self):
        return self.perder




    def get_ganar(self):
        return self.num_clicked == self.num_nobombas




