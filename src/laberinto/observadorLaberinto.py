from abc import ABC, abstractmethod
class ObservadorLaberinto(ABC):
    @abstractmethod
    def actualizar(self):
        pass
