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
pendingLinks= site.readFromYaml(pth+'/../data/test_file_01.yaml')


# Get test values.
price= site.getPrice()
numChapters= len(site.subcapitulos)

'''
print('price: ', price)
print('num chapters: ', numChapters)
'''

import os
import logging
fname= os.path.basename(__file__)
if ((price==0.0) and (numChapters==2)):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
