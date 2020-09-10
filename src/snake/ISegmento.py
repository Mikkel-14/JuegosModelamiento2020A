from abc import ABC, abstractmethod

class ISegmento(ABC):

    @abstractmethod
    def dibujar(self) -> object:
        pass
    
    @abstractmethod
    def ocultar(self) -> object:
        pass
    
    @abstractmethod
    def obtenerPosicion(self) -> object:
        pass

    @abstractmethod
    def cambiarPosicion(self) -> object:
        pass