class Coach:
    def __init__(self, nom_coach: str):
        #Définir le nom du coach
        self.__nom_coach = nom_coach

    # Accesseur pour récupérer le nom du coach
    def get_nom_coach(self):
        return self.__nom_coach
