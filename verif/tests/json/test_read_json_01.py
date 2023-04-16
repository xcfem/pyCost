# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import json
from pycost.structure import obra

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
pendingLinks= site.readFromJson(pth+'/../data/json/test_file_00.json')

unit= site.getUnitPrice('CM1E18CE020')
unitPrice= unit.getPrice()

siteCost= site.getPrice()
refCost= (0.3*22.6+72.56)*1.02


ratio1= abs(float(unitPrice)-refCost)/refCost
ratio2= abs(siteCost-refCost)/refCost

'''
print('unitPrice= ', unitPrice)
print(ratio1)
print('cost= ', siteCost)
print('refCost= ', refCost)
print(ratio2)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio1<1e-3) and (ratio2<1e-3):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
