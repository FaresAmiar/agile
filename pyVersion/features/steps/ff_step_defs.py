import Equipe as E
from behave import *


@given("Le nom d'une {equipe} et d'un {coach}")
def step_impl(context, equipe, coach):
    context.equipe = E.Equipe(equipe, coach)
    assert context.equipe is not None


@when("je lui demande le nom de son entraîneur")
def step_impl(context):
    context.result = context.equipe.get_coach().get_nom_coach()


@then("elle me répond par le nom de son {coach}")
def step_impl(context, coach):
    assert context.result == coach
