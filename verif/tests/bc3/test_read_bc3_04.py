# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

from pycost.structure import obra

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= "."
inputFile= open(pth+'/../data/test_file_04.bc3',mode='r')#, encoding="latin-1")

site.readBC3(inputFile)
inputFile.close()

# Write in YAML format
site.writeYaml(pth+'/../data/test_file_04.yaml')

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
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if ((ratio1<1e-6) and (numChapters==3) and (numElementaryPrices==3) and (numQuantities==4)):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
