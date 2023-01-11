class Saiyan:
    # Propriétés de la classe, stocke les points de ki et de vie de chaque objet
    _ki: int 
    _health: int 
    def __init__(self, ki = 100, health = 100, KAMEHAMEHA_ATTACK = 30, name = ""):
        # Initialise les propriétés de l'objet avec des valeurs par défaut si elles ne sont pas fournies
        self.__ki= ki
        self.__health=health
        # Initialise la constante d'attaque par défaut
        self.KAMEHAMEHA_ATTACK=30
        self.name = name

    def kamehameha(self,s2):
        # Vérifie si l'objet ciblé est existant, a encore de la vie, et si l'objet qui appelle la méthode a suffisamment de ki pour utiliser cette attaque
        if s2 is not None and s2.getHealth() > 0 and self.getKi()>=self.KAMEHAMEHA_ATTACK:
            # L'objet qui appelle la méthode perd de l'énergie
            self.__ki = self.__ki - self.KAMEHAMEHA_ATTACK
            # L'objet ciblé perd de la vie
            s2.setHealth(s2.getHealth() - self.KAMEHAMEHA_ATTACK)

    # Accesseurs pour récupérer les propriétés de l'objet
    def getKi(self):
        return self.__ki
    def getHealth(self):
        return self.__health
    # Mutateurs pour changer les propriétés de l'objet
    def setKi(self,ki):
        self.__ki=ki
    def setHealth(self,health):
        self.__health=health
    '''def setKAMEHAMEHA_ATTACK(self,KAMEHAMEHA_ATTACK):
        self.KAMEHAMEHA_ATTACK=KAMEHAMEHA_ATTACK'''
