# -*- coding: utf-8 -*-

'''Basic data types.'''

from moneyed import Money
from moneyed.localization import format_money
from decimal import getcontext, Decimal

dimensionPrecision= 3
dimensionPlaces= Decimal(10) ** -dimensionPrecision
dimensionFormatString= '{0:.'+str(dimensionPrecision)+'f}'

def ppl_dimension(dim, prec= dimensionPrecision):
    txtDim=  dimensionFormatString.format(dim)
    return Decimal(txtDim)

pricePrecision= 3
pricePlaces= Decimal(10) ** -pricePrecision
priceFormatString= '{0:.'+str(pricePrecision)+'f}'

def ppl_price(price, prec= pricePrecision):
    txtDim=  dimensionFormatString.format(dim)
    return Decimal(txtDim)
    
percentagePrecision= 3
percentagePlaces= Decimal(10) ** -percentagePrecision
percentageFormatString= '{0:.'+str(percentagePrecision)+'f}'

def ppl_percentage(dim, prec= percentagePrecision):
    txtDim=  dimensionFormatString.format(dim)
    return Decimal(txtDim)

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

def EnHumano(obj,decPlaces= 3):
    formatString= '{0:.'+str(decPlaces)+'f}'
    return formatString.format(obj)#str(obj);

# import Currency
# typedef Currency<3> ppl_dimension
# typedef Currency<2> ppl_precio; #Para euros dos decimales.
# typedef Currency<2> ppl_precio2; #precio con dos decimales.
# typedef Currency<3> ppl_precio3; #precio con tres decimales.
# typedef Currency<4> ppl_precio4; #precio con cuatro decimales.
# typedef Currency<3> ppl_percentage


