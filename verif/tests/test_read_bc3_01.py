# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import math
from pycost.structure import obra
site= obra.Obra(cod="test", tit="Test title")

# Read section definition from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
  pth= "."
inputFile= open(pth+'/data/test_file.bc3',mode='r')

site.readBC3(inputFile)

price= site.getPrice()


# print(price)

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if (price==0.0):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
