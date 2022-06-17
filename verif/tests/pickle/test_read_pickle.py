# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import pickle
from pycost.structure import obra

# Read from pickle file
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
inputFile= open(pth+'/../data/test_file_05.pkl', 'rb')
rootChapter= pickle.load(inputFile)
inputFile.close()

cost= rootChapter.getPrice()
ratio1= abs(cost-405026.5488452)/405026.5488452

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

