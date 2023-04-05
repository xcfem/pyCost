# -*- coding: utf-8 -*-
'''Extract concepts from unit cost databases.''' 
from __future__ import division
from __future__ import print_function

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2017, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

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
pendingLinks= site.readFromYaml(pth+'/../data/yaml/test_file_05.yaml')

employedPrices= site.getEmployedPrices(lowerMeasurementBound= 1000.0)
employedPricesRef= ['DMOVI3001', 'DSELECRI', 'RELL0301', 'ACERO0103', 'DRIESUB', 'USJT10abz', 'DPAVHORPUL', 'DALPEDR']

employedElementaryPrices= site.getEmployedElementaryPrices(lowerMeasurementBound= 1000.0)
employedElementaryPricesRef= ['MQRETR0102', 'PEON', 'MQCAMI0101', '%003', 'UTAMIZ', 'UPALA0101', 'UTRITU', 'UCOMP0202', 'UCAMI0201', 'UMOTO0102', 'OFICFER', 'PEONES', 'MAACE0201', 'OFICMON', 'TH66072', 'TK26300', 'Q004', 'Q003', '%UMAUX0103', 'OFICJAR', 'MMME.6a', 'MO0101', 'MO0201', 'UHORACERO', 'C2003000', 'PULI', 'UZAHO0102', 'UBULL0101', 'UAREN0103']      

'''
print(employedPrices)
print(employedElementaryPrices)
'''

import os
import logging
fname= os.path.basename(__file__)
if (employedPrices==employedPricesRef) and (employedElementaryPrices==employedElementaryPricesRef):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
