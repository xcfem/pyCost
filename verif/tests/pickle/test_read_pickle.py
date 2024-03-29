# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import pickle
import decimal
from pycost.structure import obra

# Read from pickle file
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
inputFile= open(pth+'/../data/pickle/test_file_05.pkl', 'rb')
rootChapter= pickle.load(inputFile)
inputFile.close()

cost= rootChapter.getPrice()
ratio1= abs(cost-400628.3115692)/400628.3115692

roundedCost= float(rootChapter.getRoundedPrice())
ratio2= abs(roundedCost-400628.29)/400628.29

'''
print(cost)
print(ratio1)
print(roundedCost)
print(ratio2)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio1<1e-6) and abs(ratio2<1e-6):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')

