# -*- coding: utf-8 -*-
'''Extract concepts from unit cost databases.''' 
from __future__ import division
from __future__ import print_function

import sys
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
pendingLinks= site.readFromYaml(pth+'/data/yaml/test_file_05.yaml')

employedPrices= site.getEmployedPrices(lowerMeasurementBound= 1000.0)
employedPricesRef= ['DMOVI3001', 'DSELECRI', 'RELL0301', 'ACERO0103', 'DRIESUB', 'USJT10abz', 'DPAVHORPUL', 'DALPEDR']

#print(employedPrices)

import os
import logging
fname= os.path.basename(__file__)
if (employedPrices==employedPricesRef):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
