import Saiyan

# Classe Potara qui permet d'améliorer l'attaque kamehameha d'un saiyan
class Potara:
    def __init__(self, saiyan = None):
        # propriété qui stocke l'objet saiyan à améliorer
        self.__s = saiyan
    
    def improveKamehameha(self,s2):
        # augmente de 10% la valeur ki de l'objet saiyan stocké
        self.__s.setKi(self.__s.getKi()*1.1);
        # appelle la fonction kamehameha de l'objet saiyan stocké avec l'objet ciblé en argument
        self.__s.kamehameha(s2)
