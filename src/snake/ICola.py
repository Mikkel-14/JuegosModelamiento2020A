from abc import ABC, abstractmethod

class ICola(ABC):

    @abstractmethod
    def agregarSegmento(self) -> object:
        pass
    
    @abstractmethod
    def dibujar(self) -> object:
        pass
    
    @abstractmethod
    def mover(self) -> object:
        pass

    @abstractmethod
    def quitarUltimo(self) -> object:
        pass

    @abstractmethod
    def obtenerCola(self) -> object:
        pass