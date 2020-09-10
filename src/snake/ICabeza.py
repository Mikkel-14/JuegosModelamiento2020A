from abc import ABC, abstractmethod

class ICabeza(ABC):

    @abstractmethod
    def dibujar(self) -> object:
        pass
    
    @abstractmethod
    def mover(self) -> object:
        pass
    
    @abstractmethod
    def obtenerPosicion(self) -> object:
        pass

    @abstractmethod
    def cambiarPosicion(self) -> object:
        pass

    @abstractmethod
    def retornarPosicion(self) -> object:
        pass