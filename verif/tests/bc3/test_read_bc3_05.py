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
    pth= "."
inputFile= open(pth+'/../data/bc3/test_file_05.bc3',mode='r', encoding="utf-8")

site.readBC3(inputFile)
inputFile.close()

# Write in YAML format
site.writeYaml(pth+'/../data/yaml/test_file_05.yaml')


# Get test values.
price= site.getPrice()

print('price: ', price)
quit()

import os
import logging
fname= os.path.basename(__file__)
if ((price==0.0) and (numChapters==3) and (numElementaryPrices==3) and (numQuantities==4)):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
