import math

import Match
import Saiyan
import EquipeFactory
import Equipe
import Potara
import Fusion

class Test:
    def __init__(self):
        self.factory = EquipeFactory.EquipeFactory()
        #Creation d'une équipe à deux Saiyan
        self.equipe1 = self.factory.creer_equipe("Equipe 1", [(1000, 1000, "Goku"), (900, 900, "Vegeta")], "Whis")
        # Création d'une équipe avec un seul saiyan 
        self.equipe2 = self.factory.creer_equipe("Equipe 2",  [(2000, 2000, "Trunks")], "Piccolo")
    def MatchTest(self):
        self.match = Match.Match(self.equipe1,self.equipe2)
        self.match.affronter()
        #print(self.match.get_gagnant().get_joueurs()[0].name)
        assert self.match.get_gagnant() != None
def main():
    Test().MatchTest()

if __name__ == '__main__':
    main()