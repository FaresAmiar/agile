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


    @given("Un saiyan de 100 ki et 100 vie, Un saiyan de 100 ki et 100 vie et un autre Saiyan de 0 ki et 0 vie")
    def deux_saiyan_inconnu(self):
        self.saiyan1 = Saiyan.Saiyan(100, 100)
        self.saiyan2 = Saiyan.Saiyan(100, 100)
        self.saiyan3 = Saiyan.Saiyan(0, 0)


    @when("ils fusionnent")
    def attaque(self):
        self.fusion2 = Fusion.Fusion([self.saiyan1, self.saiyan2, self.saiyan3])

    @then("la fusion est encore en vie")
    def quantite_vie_restante(self):
        assert self.fusion2.getSaiyan().getHealth() > 0
