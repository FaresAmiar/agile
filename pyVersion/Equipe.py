from Coach import Coach
from Saiyan import Saiyan
from typing import List

# Classe Equipe qui représente une équipe de joueurs de type Saiyan
class Equipe:
    def __init__(self, nom_equipe: str, nom_coach: str, joueurs: List[Saiyan]):
        # propriété qui stocke le nom de l'équipe
        self.__nom_equipe = nom_equipe
        # propriété qui stocke l'objet Coach lié à l'équipe
        self.__coach = Coach(nom_coach)
        # propriété qui stocke la liste des joueurs de l'équipe
        self.__joueurs=joueurs
        # propriété qui stocke le capitaine de l'équipe
        self.capitaine=joueurs[0]

    # Accesseur pour récupérer le nom de l'équipe
    def get_nom_equipe(self):
        return self.__nom_equipe

    # Accesseur pour récupérer le coach de l'équipe
    def get_coach(self):
        return self.__coach

    # Accesseur pour récupérer le capitaine de l'équipe'

    def get_capitaine(self):
        return self.__capitaine

    # Accesseur pour récupérer les joueurs de l'équipe'
    def get_joueurs(self):
        return self.__joueurs

    #Implémentation de la méthode toString de la classe
    def toString(self):
        return "Le nom de votre équipe est "+self.__nom_equipe \
               +" et le nom de votre coach est "+self.__coach.get_nom_coach()
