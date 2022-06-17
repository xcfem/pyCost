# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import re
import os

# Read data from file.
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
inputFileName= pth+'/../data/test_file_09.txt'
file1 = open(inputFileName,"r")

import re

testPrecioUnitario= re.compile('[A-Za-z0-9]+ - .*')

lines = file1.readlines()

modoDescomposicion= False
dictElementales= dict()

# Populate the elementary prices dictionary.
for ln in lines:
    ln= ln.strip()
    inicioPrecioUnitario= testPrecioUnitario.match(ln)
    if(ln=='Descompuesto'):
        modoDescomposicion= True
    if(ln== '#***'):
        modoDescomposicion= False
    if(modoDescomposicion):
        campos= ln.split('\t')
        codElemental= campos[0]
        if(codElemental!='Descompuesto') and (codElemental!='Código') and (len(codElemental)>0):
            strPrecio= campos[4].replace('€','')
            strPrecio= strPrecio.replace('.','')
            strPrecio= strPrecio.replace(',','.')
            try:
                precio= float(strPrecio)
            except ValueError:
                print('Not a float: '+strPrecio+' in line: ', ln)
            tipo= 0
            if(codElemental[:2]=='MO'):
                tipo= 1
            elif(codElemental[:2]=='MQ'):
                tipo= 2
            elif(codElemental[:2]=='MN'):
                tipo= 3
            dictElementales[codElemental]= {'code':codElemental, 'unit':campos[1], 'title':campos[2], 'long_description':campos[2], 'price':precio, 'type':tipo}

# Populate the unit price dictionary.
dictDescompuestos= dict()
for ln in lines:
    ln= ln.strip()
    inicioPrecioUnitario= testPrecioUnitario.match(ln)
    if(inicioPrecioUnitario):
        tmp= ln.split('-')
        codUnitario= tmp[0].strip()
        title= tmp[1]
        descripcion= ''
    else:
        if(ln=='Descompuesto'):
            modoDescomposicion= True
            descomposicion= dict()
            count= 0
        if(ln== '#***'):
            modoDescomposicion= False
        if(modoDescomposicion):
            campos= ln.split('\t')
            codElemental= campos[0]
            if(codElemental!='Descompuesto') and (codElemental!='Código') and (len(codElemental)>0):
                strRendimiento= campos[3]
                strRendimiento= strRendimiento.replace('.','')
                strRendimiento= strRendimiento.replace(',','.')
                try:
                    rendimiento= float(strRendimiento)
                except ValueError:
                    print('Not a float: '+strRendimiento)
                descomposicion[count]= {'ent_code':codElemental, 'production_rate':rendimiento, 'factor':1.0}
                count+= 1
        else:
            if(ln.find(' € / ') != -1):
                tmp= ln.split('/')
                unidad= tmp[1].strip()
            elif (len(ln)>0) and (ln!='#***'):
                descripcion+= ln+'\n'
    if(ln=='#***'): # fin del precio unitario.
        dictDescompuestos[codUnitario]= {'code':codUnitario, 'unit':unidad, 'title':title, 'long_description':descripcion, 'components':descomposicion}

from pycost.structure import obra

site= obra.Obra(cod="test", tit="Test title")

pendingLinks= site.readFromDictionaries(elementaryPricesDict= dictElementales, unitPricesDict= dictDescompuestos)

# Check the number of prices read.
numElementaryPrices= len(site.precios.Elementales())
numElementaryPricesRef= 165
ratio1= abs(numElementaryPrices-numElementaryPricesRef)/numElementaryPricesRef
numUnitPrices= len(site.precios.UdsObra())
numUnitPricesRef= 85
ratio2= abs(numUnitPrices-numUnitPricesRef)/numUnitPricesRef

'''
print(numElementaryPrices)
print(ratio1)
print(numUnitPrices)
print(ratio2)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio1<1e-6) and (ratio2<1e-6):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
