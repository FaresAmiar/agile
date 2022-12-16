from dataclasses import dataclass

from behave import *
import Saiyan


@dataclass
class ManageSaiyanSteps:
    _ki1: int
    _ki2: int
    _health1: int
    _health2: int
    _quantite: int

    @given("Un saiyan de 100 ki et 100 vie et Un saiyan de 100 ki et 100 vie")
    def les_Saiyans(self):
        self.saiyan1b = Saiyan.Saiyan(100, 100)
        self.saiyan2b = Saiyan.Saiyan(100, 100)

    @when("Goku utilise kamehameha")
    def attaque(self):
        self.saiyan1b.kamehameha(self.saiyan2b)

    @then("il reste 70 de vie")
    def vie_restante(self):
        assert self.saiyan2b.getHealth() == 70

    @given("Un saiyan de {ki1} ki et {health1} vie et Un saiyan  de {ki2} ki et {health2} vie")
    def deux_saiyan_inconnu(self, ki1, health1, ki2, health2):
        self.saiyan1 = Saiyan.Saiyan(int(ki1), int(health1))
        self.saiyan2 = Saiyan.Saiyan(int(ki2), int(health2))

    @when("j'utilise kamehameha")
    def attaque(self):
        self.saiyan1.kamehameha(self.saiyan2)

    @then("il reste {quantite} de vie")
    def quantite_vie_restante(self, quantite):
        print(self.saiyan2.getHealth())
        print(quantite)
        assert self.saiyan2.getHealth() == int(quantite)


    @given("Un saiyan de 100 ki et 100 vie et Un saiyan de 10 ki et -5 vie")
    def les_Saiyans(self):
        self.saiyan1t = Saiyan.Saiyan(100, 100)
        self.saiyan2t = Saiyan.Saiyan(00, -5)


    @when("Goku utilise kamehameha sur le mort")
    def attaque(self):
        self.saiyan1t.kamehameha(self.saiyan2t)


    @then("le ki de Goku n'a pas changé")
    def vie_restante(self):
        assert self.saiyan1t.getKi() == 100