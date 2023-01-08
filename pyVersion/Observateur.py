import Equipe
from abc import ABC, abstractmethod

class Observateur(ABC):
    @abstractmethod
    def update(self, gagnant: Equipe, perdant: Equipe):
        pass