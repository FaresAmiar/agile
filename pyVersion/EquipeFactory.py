import string
from Saiyan import Saiyan
from Equipe import Equipe
from typing import List, Tuple

class EquipeFactory:
    @staticmethod
    def creer_equipe(nom_equipe : str ,saiyans: List[Tuple[int, int,str]], coach: str) -> Equipe:
        saiyans_obj = [Saiyan(ki=ki, health=health,name=nom) for ki, health,nom in saiyans]
        # if capitaine is None:
        #     saiyans_obj.insert(0,saiyans_obj[0])
        return Equipe(nom_equipe, coach,saiyans_obj)