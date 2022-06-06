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
pendingLinks= site.readFromYaml(pth+'/../data/test_file_05.yaml')

# Dump into pickle file.
with open(pth+'/../data/test_file_05.pkl', 'wb') as fh:
    pickle.dump(site, fh)

# Read from pickle file
inputFile= open(pth+'/../data/test_file_05.pkl', 'rb')
newRootChapter= pickle.load(inputFile)
inputFile.close()

cost= newRootChapter.getPrice()
ratio1= abs(cost-405026.5488452)/405026.5488452

'''
print(cost)
print(ratio1)
'''

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if (ratio1<1e-6):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
