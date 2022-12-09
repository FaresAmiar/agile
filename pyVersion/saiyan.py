class Saiyan:
    def __init__(self, ki, health, KAMEHAMEHA_ATTACK):
        self.ki=ki
        self.health=health
        self.KAMEHAMEHA_ATTACK=30
    def __init__(self):
        self.ki=100
        self.health=100
        self.KAMEHAMEHA_ATTACK=30
    def kamehameha(self,s2):
        if(s2 is not  None and s2.health > 0):
            self.ki -= self.KAMEHAMEHA_ATTACK
            s2.health -= self.KAMEHAMEHA_ATTACK

    def Getki(self):
        return self.ki
    def Gethealth(self):
        return self.health
    def GetKAMEHAMEHA_ATTACK(self):
        return self.KAMEHAMEHA_ATTACK
    def Setki(self,ki):
        self.ki=ki
    def Sethealth(self,health):
        self.health=health
    def SetKAMEHAMEHA_ATTACK(self,KAMEHAMEHA_ATTACK):
        self.KAMEHAMEHA_ATTACK=KAMEHAMEHA_ATTACK
    