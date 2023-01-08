from Coach import Coach
from Saiyan import Saiyan
from typing import List


class Equipe:
    def __init__(self, nom_equipe: str, nom_coach: str, joueurs: List[Saiyan]):
        self.__nom_equipe = nom_equipe
        self.__coach = Coach(nom_coach)
        self.__joueurs=joueurs
        self.capitaine=joueurs[0]

    def get_nom_equipe(self):
        return self.__nom_equipe

    def get_coach(self):
        return self.__coach

    def get_capitaine(self):
        return self.__capitaine
    def get_joueurs(self):
        return self.__joueurs

    def toString(self):
        return "Le nom de votre équipe est "+self.__nom_equipe \
               +" et le nom de votre coach est "+self.__coach.get_nom_coach()
