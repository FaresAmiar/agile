import Coach as C

class Equipe:
    def __init__(self, nom_equipe: str, nom_coach: str):
        self.__nom_equipe = nom_equipe
        self.__coach = C.Coach(nom_coach)

    def get_nom_equipe(self):
        return self.__nom_equipe

    def get_coach(self):
        return self.__coach

    def toString(self):
        return "Le nom de votre équipe est "+self.__nom_equipe \
               +" et le nom de votre coach est "+self.__coach.get_nom_coach()
