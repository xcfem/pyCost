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
pendingLinks= site.readFromYaml(pth+'/../data/test_file_06.yaml')

# Get test values.
price= site.getPrice()
refPrice= 1726.36
ratio= abs(price-refPrice)/refPrice

'''
print("ratio= ", ratio)
'''

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if (ratio<1e-5):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')

