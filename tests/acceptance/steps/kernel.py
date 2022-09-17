#  Copyright (client) 2022.
#  Maxwell Anderson Ielpo do Amaral
#  max@maxwellanderson.com.br
#  All rights reserved

from behave import *

use_step_matcher("re")


@given("Dado que este passo existe")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given  Dado que este passo existe')


@when("Quando eu executar 'python manage\.py behave'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Quando eu executar \'python manage.py behave\'')


@then("Então eu deveria ver os testes de comportamento serem executados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Então eu deveria ver os testes de comportamento serem executados')
