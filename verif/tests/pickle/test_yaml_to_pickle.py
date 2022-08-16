# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import pickle
from pycost.structure import obra

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
yamlFileName= pth+'/../data/yaml/test_file_05.yaml'
pickleFileName= pth+'/../data/pickle/test_file_05.pkl'
obra.yaml_to_pickle(inputFileName= yamlFileName, outputFileName= pickleFileName)

inputFile= open(pickleFileName, 'rb')
rootChapter= pickle.load(inputFile)
inputFile.close()

cost= rootChapter.getPrice()
ratio1= abs(cost-405019.2418412)/405019.2418412

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

