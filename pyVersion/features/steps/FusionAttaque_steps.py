from dataclasses import dataclass

from behave import *
import Saiyan
import Fusion


@dataclass
class ManageFusionSteps:
    _ki1: int
    _ki2: int
    _ki3: int
    _health1: int
    _health2: int
    _health3: int
    _quantite: int


    @given(
        "Un saiyan de 100 ki et 100 vie et Un saiyan de 100 ki et 100 vie fusionne et un autre Saiyan de 100 ki et 100 vie")
    def les_Saiyans(self):
        self.saiyan1 = Saiyan.Saiyan(100, 100)
        self.saiyan2 = Saiyan.Saiyan(100, 100)
        self.fusion1 = Fusion.Fusion([self.saiyan1, self.saiyan2])
        self.saiyan3 = Saiyan.Saiyan(100, 100)


    @then("il reste au saiyan 70 de vie")
    def vie_restante(self):
        print(self.saiyan3.getHealth())
        assert self.saiyan3.getHealth() == 70


    @given(
        "Un saiyan de {ki1} ki et {health1} vie et Un saiyan  de {ki2} ki et {health2} vie fusionne et un autre Saiyan de {ki3} ki et {health3} vie")
    def deux_saiyan_inconnu(self, ki1, health1, ki2, health2, ki3, health3):
        self.saiyan1 = Saiyan.Saiyan(int(ki1), int(health1))
        self.saiyan2 = Saiyan.Saiyan(int(ki2), int(health2))
        self.saiyan3 = Saiyan.Saiyan(int(ki3), int(health3))
        self.fusion1 = Fusion.Fusion([self.saiyan1, self.saiyan2])


    @when("la fusion utilise kamehameha")
    def attaque(self):
        self.fusion1.getSaiyan().kamehameha(self.saiyan3)


    @then("il reste au saiyan {quantite} de vie")
    def quantite_vie_restante(self, quantite):
        assert self.saiyan3.getHealth() == int(quantite)