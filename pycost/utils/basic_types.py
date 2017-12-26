# -*- coding: utf-8 -*-

'''Basic data types.'''

from moneyed import Money
from moneyed.localization import format_money
from decimal import getcontext, Decimal
from num2words import num2words
import locale

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
    txtPrice=  priceFormatString.format(price)
    return Decimal(txtPrice)
    
percentagePrecision= 3
percentagePlaces= Decimal(10) ** -percentagePrecision
percentageFormatString= '{0:.'+str(percentagePrecision)+'f}'

def ppl_percentage(perc, prec= percentagePrecision):
    txtPercentage=  percentageFormatString.format(perc)
    return Decimal(txtPercentage)

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

def to_words(number, genre, lng= 'es'):
    return num2words(number, lang= lng)

def human_readable(number,decPlaces= 3):
    return locale.format('%d',number, grouping= True)

# import Currency
# typedef Currency<3> ppl_dimension
# typedef Currency<3> ppl_percentage


