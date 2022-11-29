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
pendingLinks= site.readFromYaml(pth+'/../data/yaml/test_file_05.yaml')

siteCost= site.getPrice()

# Dump into json file.
jsonFileName= pth+'/../data/json/test_file_05.json'
site.writeJson(jsonFileName)

# Read from json file
newSite= obra.Obra(cod="newSite", tit="New site")
pendingLinks= newSite.readFromJson(jsonFileName)

newSiteCost= newSite.getPrice()
ratio1= abs(newSiteCost-siteCost)/siteCost

'''
print(siteCost)
print(newSiteCost)
print(ratio1)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio1<1e-6):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
