#  Copyright (client) 2022.
#  Maxwell Anderson Ielpo do Amaral
#  max@maxwellanderson.com.br
#  All rights reserved

"""
módulo de ambiente de comportamento para testar o behave-django
"""


def django_ready(context):
    context.django = True
