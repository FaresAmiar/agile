class Saiyan:
    _ki: int
    _health: int
    def __init__(self, ki = 100, health = 100, KAMEHAMEHA_ATTACK = 30):
        self.__ki= ki
        self.__health=health
        self.KAMEHAMEHA_ATTACK=30
        
    def kamehameha(self,s2):
        if(s2 is not None and s2.getHealth() > 0):
            self.__ki = self.__ki - self.KAMEHAMEHA_ATTACK
            s2.setHealth(s2.getHealth() - self.KAMEHAMEHA_ATTACK)

    def getKi(self):
        return self.__ki
    def getHealth(self):
        return self.__health
    def setKi(self,ki):
        self.__ki=ki
    def setHealth(self,health):
        self.__health=health
    '''def setKAMEHAMEHA_ATTACK(self,KAMEHAMEHA_ATTACK):
        self.KAMEHAMEHA_ATTACK=KAMEHAMEHA_ATTACK'''
    
