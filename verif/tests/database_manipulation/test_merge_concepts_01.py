# -*- coding: utf-8 -*-
'''Merge two price databases.''' 
from __future__ import division
from __future__ import print_function

import yaml
import pickle
from pycost.structure import obra
from pycost.structure.chapter import Chapter
from pycost.structure.unit_price_quantities import UnitPriceQuantities

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'

# Read price data from two databases
pendingLinks= site.readFromYaml(pth+'/../data/yaml/test_file_05.yaml')
pendingLinks= site.readFromYaml(pth+'/../data/yaml/test_file_07.yaml')

# Check the number of prices read.
numElementaryPrices= len(site.precios.Elementales())
numElementaryPricesRef= 175+157-1 # SINDESCO counts twice.
ratio1= abs(numElementaryPrices-numElementaryPricesRef)/numElementaryPricesRef
numUnitPrices= len(site.precios.UdsObra())
numUnitPricesRef= 115+77
ratio2= abs(numUnitPrices-numUnitPricesRef)/numUnitPricesRef

# Write in YAML format
site.writeYaml(pth+'/../data/yaml/test_file_08.yaml')

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
