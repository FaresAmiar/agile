from Saiyan import Saiyan
from Equipe import Equipe
from typing import List, Tuple

# Classe EquipeFactory qui permet de centraliser la création des objets de la classe Equipe
class EquipeFactory:
    # méthode statique pour créer une équipe
    @staticmethod
    def creer_equipe(nom_equipe : str ,saiyans: List[Tuple[int, int,str]], coach: str) -> Equipe:
        # création d'une liste d'objets saiyan en utilisant la compréhension de liste
        saiyans_obj = [Saiyan(ki=ki, health=health,name=nom) for ki, health,nom in saiyans]
        # création d'un objet de la classe Equipe en utilisant la liste d'objets saiyan
        return Equipe(nom_equipe, coach,saiyans_obj)
