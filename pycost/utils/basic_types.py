# -*- coding: utf-8 -*-

'''Basic data types.'''

from moneyed import Money
from moneyed.localization import format_money
from decimal import getcontext, Decimal

def ppl_dimension(dim, prec= 3):
    getcontext().prec= prec
    return Decimal(dim)

def ppl_price(price, prec= 2):
    getcontext().prec= prec
    return Decimal(dim)
    
def ppl_percentage(dim, prec= 3):
    getcontext().prec= prec
    return Decimal(dim)

def str_tipo(tipo):
    retval= ''
    if(tipo==mdo):
        retval= 'mano de obra'
    elif(tipo==maq):
        retval= 'maquinaria'
    elif(tipo==mat):
        retval= 'materiales'
    else:
        retval= 'sin clasificar'
    return retval

quantitiesCaption= 'Mediciones'

def EnHumano(obj):
    return "{0:.2f}".format(obj)#str(obj);

# import Currency
# typedef Currency<3> ppl_dimension
# typedef Currency<2> ppl_precio; #Para euros dos decimales.
# typedef Currency<2> ppl_precio2; #precio con dos decimales.
# typedef Currency<3> ppl_precio3; #precio con tres decimales.
# typedef Currency<4> ppl_precio4; #precio con cuatro decimales.
# typedef Currency<3> ppl_percentage


