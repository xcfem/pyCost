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
pendingLinks= site.readFromYaml(pth+'/../data/test_file_03.yaml')

numElementaryPrices= len(site.precios.Elementales())
numQuantities= 0
for sc in site.subcapitulos:
    numElementaryPrices+= len(sc.precios.Elementales())
    numQuantities+= len(sc.quantities)
    
# Get test values.
price= site.getPrice()
numChapters= len(site.subcapitulos)

'''
print('price: ', price)
print('num chapters: ', numChapters)
print('num quantities: ', numQuantities)
print('num. elementary prices: ', numElementaryPrices)
'''

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if ((price==140.0) and (numChapters==1) and (numElementaryPrices==2) and (numQuantities==1)):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
