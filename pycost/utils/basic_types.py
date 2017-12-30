# -*- coding: utf-8 -*-

'''Basic data types.'''

from decimal import getcontext, Decimal
from num2words import num2words
import locale

''' TIPO: Tipo de concepto, se reservan los siguientes tipos: '''

''' 0 (Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales). '''

sin_clasif, mdo, maq, mat= range(0, 4)

def str2tipo_concepto(self, Str):
    if(len(Str)<1):
        return sin_clasif
    elif(Str[0]=='0'):
        return sin_clasif
    elif(Str[0]=='1'):
        return mdo
    elif(Str[0]=='2'):
        return maq
    elif(Str[0]=='3'):
        return mat
    else:
        return sin_clasif

def sint2tipo_concepto(self, si):
    if(si==0):
        return sin_clasif
    elif(si==1):
        return mdo
    elif(si==2):
        return maq
    elif(si==3):
        return mat
    else:
        return sin_clasif

def tipo_concepto2str(self, t):
    if(t==0):
        return "sin_clasif"
    elif(t==1):
        return "mdo"
    elif(t==2):
        return "maq"
    elif(t==3):
        return "mat"
    else:
        return "sin_clasif"
    return "sin_clasif"

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

sin_desc_string= u'Sin descomposición'

def to_words(number, genre, lng= 'es'):
    return num2words(number, lang= lng)

def human_readable(number,decPlaces= 3):
    #return locale.format('%d',number, grouping= True)
    formatString= '{0:.'+str(decPlaces)+'f}'
    return formatString.format(number, grouping= True)

# import Currency
# typedef Currency<3> ppl_dimension
# typedef Currency<3> ppl_percentage


