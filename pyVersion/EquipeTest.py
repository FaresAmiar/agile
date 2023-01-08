import unittest
import Saiyan
import Equipe as E

nom_equipe = "Maroc"
nom_coach = "Walid Regragui"


class EquipeTestCase(unittest.TestCase):

    def test_toString(self):
        self.Vegeta = Saiyan.Saiyan()
        equipe = E.Equipe(nom_equipe, nom_coach,[self.Vegeta])
        self.assertEqual("Le nom de votre équipe est " + nom_equipe + " et le nom de votre coach est " + nom_coach,
                         equipe.toString())

    def test_get_nom_equipe(self):
        self.Vegeta = Saiyan.Saiyan()
        equipe = E.Equipe(nom_equipe, nom_coach,[self.Vegeta])
        self.assertEqual(nom_equipe, equipe.get_nom_equipe())


if __name__ == '__main__':
    unittest.main()