from game import Game
from tablero import Tablero

"""
Crea una instancia de la clase Game

Con el método run() inicia el juego de buscaminas.

Muestra el menú principal y maneja los eventos del juego.
"""
def main():
    game =  Game() 
    game.run()

if __name__ == "__main__":
    main()