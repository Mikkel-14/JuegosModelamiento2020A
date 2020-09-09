from virus.virus import EvitandoVirus
from laberinto.laberinto import Laberinto
from ruta.ruta import Ruta
from snake.snake import Snake
from puzzle.puzzle import Puzzle

class FachadaJuegos():
    def __init__(self):
        self.laberinto = Laberinto()
        self.puzzle = Puzzle()
        self.ruta = Ruta()
        self.snake = Snake()
        self.evitandoVirus = EvitandoVirus()

    def arrancarJuego(self, nombreJuego):
        if nombreJuego == 'laberinto':
            self.laberinto.iniciarJuego()
        elif nombreJuego == 'puzzle':
            self.puzzle.iniciarJuego()
        elif nombreJuego == 'ruta':
            self.ruta.iniciarJuego()
        elif nombreJuego == 'snake':
            self.snake.iniciarJuego()
        elif nombreJuego == 'virus':
            self.evitandoVirus.iniciarJuego()
