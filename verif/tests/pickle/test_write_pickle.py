# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import pickle
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

# Dump into pickle file.
with open(pth+'/../data/pickle/test_file_05.yaml', 'wb') as fh:
    pickle.dump(site, fh)

# Read from pickle file
inputFile= open(pth+'/../data/pickle/test_file_05.pkl', 'rb')
newRootChapter= pickle.load(inputFile)
inputFile.close()

cost= newRootChapter.getPrice()
ratio1= abs(cost-400628.3115692)/400628.3115692

'''
print(cost)
print(ratio1)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio1<1e-6):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')

