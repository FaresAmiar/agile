from Observateur import Observateur
from EquipeFactory import EquipeFactory
from Equipe import Equipe
from Match import Match
from Observable import Observable

class AfficherMatch(Observateur):
    def update(self, gagnant: Equipe, perdant: Equipe):
        print(f"Le gagnant est {gagnant.get_nom_equipe()}")

factory = EquipeFactory()

# Création des équipes
equipe1 = factory.creer_equipe("Equipe 1", [(1000, 1000, "Goku"), (900, 900, "Vegeta")], "Whis")
equipe2 = factory.creer_equipe("Equipe 2", [(800, 800, "Gohan"), (700, 700, "Trunks")], "Piccolo")

# Création du match et ajout de l'observateur
match = Match(equipe1, equipe2)
affichage = AfficherMatch()
match.ajouter_observateur(affichage)

# Affrontement des équipes
match.affronter()