from dataclasses import dataclass
from itertools import zip_longest

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
    deathCount = 0
    for equipe1, equipe2 in zip_longest(context.equipe1.get_joueurs(), context.equipe2.get_joueurs(), fillvalue=None):
        if(equipe1.getHealth() <= 0 or equipe2.getHealth() <= 0):
            deathCount = deathCount + 1
    assert (deathCount == 1)
