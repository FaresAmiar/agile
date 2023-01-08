import random
from Observable import Observable
from Equipe import Equipe

class Match(Observable):
    def __init__(self, equipe1: Equipe, equipe2: Equipe):
        super().__init__()
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.gagnant = None
        self.perdant = None
    
    def affronter(self):
        while True:
            joueur1 = random.choice(self.equipe1.get_joueurs())
            joueur2 = random.choice(self.equipe2.get_joueurs())
            joueur1.kamehameha(joueur2)
            if joueur2.getHealth() <= 0:
                self.gagnant = self.equipe1
                self.perdant = self.equipe2
                self.notifier_observateurs(self.gagnant, self.perdant)
                break
            joueur2.kamehameha(joueur1)
            if joueur1.getHealth() <= 0:
                self.gagnant = self.equipe2
                self.perdant = self.equipe1
                self.notifier_observateurs(self.gagnant, self.perdant)
                break
    
    def get_gagnant(self):
        return self.gagnant
    
    def get_perdant(self):
        return self.perdant