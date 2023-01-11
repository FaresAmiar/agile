import math
import Saiyan
import Potara

# classe Fusion permettant de fusionner plusieurs objets de type saiyan pour en créer un nouveau
class Fusion:
    def __init__(self, Saiyans):
        # initialise l'objet fusionné
        self.__Saiyan= Saiyan.Saiyan(1,1)
        # boucle pour parcourir la liste des saiyans à fusionner
        for i in range(len(Saiyans)):
            # vérifie si l'objet saiyan courant est valide pour être fusionné 
            if(Saiyans[i].getHealth()>0 and Saiyans[i].getKi()>0):
                # multiplie les propriétés ki et health de l'objet fusionné par celles des objets saiyans courants
                self.__Saiyan.setKi(self.__Saiyan.getKi()*Saiyans[i].getKi())
                self.__Saiyan.setHealth(self.__Saiyan.getHealth()*Saiyans[i].getHealth())
    # retourne l'objet fusionné
    def getSaiyan(self):
        return self.__Saiyan
