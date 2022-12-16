import math
import Saiyan
import Potara


class Fusion:
    def __init__(self, Saiyans):
        self.__Saiyan= Saiyan.Saiyan(1,1)

        for i in range(len(Saiyans)):
            if(Saiyans[i].getHealth()>0 and Saiyans[i].getKi()>0):
                self.__Saiyan.setKi(self.__Saiyan.getKi()*Saiyans[i].getKi())
                self.__Saiyan.setHealth(self.__Saiyan.getHealth()*Saiyans[i].getHealth())

    def getSaiyan(self):
        return self.__Saiyan
             