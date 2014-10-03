from behave import *

#from MonApplication import BonjourLeMonde

@when(u'je lance l\'application')
def step_impl(context):
    assert True

@then(u'je devrais voir "{text}"')
def step_impl(context, text):
    assert True
