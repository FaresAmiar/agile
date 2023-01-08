from dataclasses import dataclass

from behave import *
from EquipeFactory import EquipeFactory
from Match import Match

@given("deux équipes sont créées")
def given_deux_equipes_sont_creees(context):
    factory = EquipeFactory()
    context.equipe1 = factory.creer_equipe("Equipe 1", [(1000, 1000, "Goku"), (900, 900, "Vegeta")], "Whis")
    context.equipe2 = factory.creer_equipe("Equipe 2", [(800, 800, "Gohan"), (700, 700, "Trunks")], "Piccolo")

@when("les deux équipes s'affrontent")
def when_les_deux_equipes_saffrontent(context):
    match = Match(context.equipe1, context.equipe2)
    match.affronter()

@then("un gagnant est déterminé")
def then_un_gagnant_est_determine(context):
    assert (context.equipe1.get_joueurs()[0].getHealth() > 0 and context.equipe2.get_joueurs()[0].getHealth() <= 0) or (context.equipe1.get_joueurs()[0].getHealth() <= 0 and context.equipe2.get_joueurs()[0].getHealth() > 0)
