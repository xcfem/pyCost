# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import yaml
from pycost.structure import obra

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
pendingLinks= site.readFromYaml(pth+'/../data/yaml/test_file_04.yaml')

numElementaryPrices= 0
numQuantities= 0
for sc in site.subcapitulos:
    numElementaryPrices+= len(sc.precios.Elementales())
    numQuantities+= len(sc.quantities)
    
# Get test values.
price= site.getPrice()
ratio1= abs(price-395.20)/395.20
numChapters= len(site.subcapitulos)

'''
print('price: ', price)
print('ratio1: ', ratio1)
print('num chapters: ', numChapters)
print('num quantities: ', numQuantities)
print('num. elementary prices: ', numElementaryPrices)
'''

import os
import logging
fname= os.path.basename(__file__)
if ((ratio1<1e-6) and (numChapters==3) and (numElementaryPrices==3) and (numQuantities==4)):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
