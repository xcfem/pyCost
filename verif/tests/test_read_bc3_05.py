# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import yaml
from pycost.structure import obra

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read section definition from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= "."
inputFile= open(pth+'/data/test_file_05.bc3',mode='r')

site.readBC3(inputFile)

# Write in YAML format
with open(pth+'/data/test_file_05.yaml', 'w') as file:
    outputs= yaml.dump(site.getDict(), file)
file.close()


# Get test values.
price= site.getPrice()

print('price: ', price)
quit()

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if ((price==0.0) and (numChapters==3) and (numElementaryPrices==3) and (numQuantities==4)):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
