import Equipe as E
import EquipeFactory


if __name__ == '__main__':
    # equipe = E.Equipe("Maroc", "Walid Regragui")
    # print(equipe.toString())
    factory = EquipeFactory.EquipeFactory()

    equipe1 = factory.creer_equipe("Equipe 1", [(1000, 1000, "Goku"), (900, 900, "Vegeta")], "Whis")

    print(equipe1.get_joueurs()[1].name)

    # Création d'une équipe avec un seul saiyan
    equipe2 = factory.creer_equipe("Equipe 2", [(800, 800, "Gohan")], "Piccolo")
