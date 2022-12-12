import behave

@given("Un saiyan {saiyan} de {ki} ki et {health} vie")
def step_impl(context,saiyan,ki,health):
    context.saiyan1= saiyan.Saiyan(ki,health)

