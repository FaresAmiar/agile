import math
import Saiyan
import Potara
class Fusion:
    def __init__(self, Saiyans):
        self.__Saiyan= Saiyan.Saiyan(1,1)

        for i in range(len(Saiyans)):
             self.__Saiyan.setKi(self.__Saiyan.getKi()*Saiyans[i].getKi())
             self.__Saiyan.setHealth(self.__Saiyan.getHealth()*Saiyans[i].getHealth())
    def getSaiyan(self):
        return self.__Saiyan
             