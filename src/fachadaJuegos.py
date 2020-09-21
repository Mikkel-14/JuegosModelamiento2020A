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
        self.puntaje = 0

    def arrancarJuego(self, nombreJuego):
        if nombreJuego == 'laberinto':
            self.laberinto.iniciarJuego()
            self.puntaje += self.laberinto.getPuntos()
        elif nombreJuego == 'puzzle':
            self.puzzle.iniciarJuego()
            self.puntaje += self.puzzle.getPuntos()
        elif nombreJuego == 'ruta':
            self.ruta.iniciarJuego()
            self.puntaje += self.ruta.getPuntos()
            self.ruta = Ruta()
        elif nombreJuego == 'snake':
            self.snake.iniciarJuego()
            self.puntaje += self.snake.getPuntos()
        elif nombreJuego == 'virus':
            self.evitandoVirus.iniciarJuego()
            self.puntaje += self.evitandoVirus.getPuntos()
 
    def getPuntaje(self):
        return self.puntaje
