from game import Game
from tablero import Tablero
size = (9,9)
prob_bomba = 0.14
tablero =  Tablero(size, prob_bomba)
tamaño = (800,880)
game =  Game(tablero,tamaño)
game.run()
