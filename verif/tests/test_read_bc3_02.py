# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

from pycost.structure import obra

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read section definition from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= "."
inputFile= open(pth+'/data/test_file_02.bc3',mode='r')

site.readBC3(inputFile)

# Write in YAML format
import yaml
with open(pth+'/data/test_file_02.yaml', 'w') as file:
    outputs= yaml.dump(site.getDict(), file)
file.close()

numElementaryPrices= 0
for sc in site.subcapitulos:
    numElementaryPrices+= len(sc.precios.Elementales())
    
# Get test values.
price= site.getPrice()
numChapters= len(site.subcapitulos)

'''
print('price: ', price)
print('num chapters: ', numChapters)
'''

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if ((price==0.0) and (numChapters==1) and (numElementaryPrices==2)):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
