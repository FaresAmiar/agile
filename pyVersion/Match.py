import random
from Observable import Observable
from Equipe import Equipe
from Potara import Potara

class Match(Observable):
    def __init__(self, equipe1: Equipe, equipe2: Equipe):
        super().__init__()
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.gagnant = None
        self.perdant = None
    
    def affronter(self):
        # Récupération des saiyans de chaque équipe
        saiyans_equipe1 = self.equipe1.get_joueurs()
        saiyans_equipe2 = self.equipe2.get_joueurs()

        # Génération aléatoire d'un nombre entre 1 et 2 pour déterminer qui attaque en premier
        alea = random.randint(1, 2)

        # Nombre de tours
        nbTours = 1

        # Boucle infinie jusqu'à ce qu'un des deux saiyans soit K.O.
        while True:

            # Sélection aléatoire d'un saiyan de l'équipe 1 et de l'équipe 2
            saiyan1 = random.choice(saiyans_equipe1)
            saiyan2 = random.choice(saiyans_equipe2)

            # Si le nombre aléatoire est égal à 1, c'est l'équipe 1 qui attaque en premier
            if alea == 1 :
                # Génération aléatoire d'un nombre entre 1 et 20 pour déterminer si le saiyan 1 est placé dans une Potara
                alea_potara = random.randint(1, 20)

                # Si le nombre est égal à 1, le saiyan 1 est placé dans une Potara
                if alea_potara == 1:
                    potara1 = Potara(saiyan1)
                    potara1.improveKamehameha(saiyan2)
                else:
                    saiyan1.kamehameha(saiyan2)

                # Si le saiyan 2 est K.O., l'équipe 1 remporte la victoire et le match s'arrête
                if saiyan2.getHealth() <= 0:
                    self.gagnant = self.equipe1
                    self.perdant = self.equipe2
                    break
            # Si le nombre aléatoire est égal à 2, c'est l'équipe 2 qui attaque en premier
            else:
                # Génération aléatoire d'un nombre entre 1 et 20 pour déterminer si le saiyan 2 est placé dans une Potara
                alea_potara = random.randint(1, 20)

                # Si le nombre est égal à 1, le saiyan 2 est placé dans une Potara
                if alea_potara == 1:
                    potara2 = Potara(saiyan2)
                    potara2.improveKamehameha(saiyan1)
                else:
                    saiyan2.kamehameha(saiyan1)

                # Si le saiyan 1 est K.O., l'équipe 2 remporte la victoire et le match s'arrête
                if saiyan1.getHealth() <= 0:
                    self.gagnant = self.equipe2
                    self.perdant = self.equipe1
                    break
            
            nbTours = nbTours + 1
            if nbTours % 5 == 0:
                [s.setKi(s.getKi()+30) for s in saiyans_equipe1+saiyans_equipe2]
            alea = 2 if alea == 1 else 1
        # Appel de la méthode update() de chaque observateur
        self.notifier_observateurs(self.gagnant, self.perdant)
    
    def get_gagnant(self):
        return self.gagnant
    
    def get_perdant(self):
        return self.perdant