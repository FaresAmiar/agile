import Equipe as E
import Saiyan
from behave import *


@given("Le nom d'une équipe {equipe} et d'un coach {coach}")
def step_impl(context, equipe, coach):
    context.equipe = E.Equipe(equipe, coach, [Saiyan.Saiyan(),Saiyan.Saiyan()])
    assert context.equipe is not None


@when("je lui demande le nom de son entraîneur")
def step_impl(context):
    context.result = context.equipe.get_coach().get_nom_coach()


@then("elle me répond par le nom de son coach {coach}")
def step_impl(context, coach):
    assert context.result == coach
