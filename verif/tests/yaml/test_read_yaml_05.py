# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import yaml
from pycost.structure import obra

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read section definition from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
inputFile= open(pth+'/../data/test_file_05.yaml',mode='r')
dataDict= yaml.safe_load(inputFile)
inputFile.close()

pendingLinks= site.solvePendingLinks(site.setFromDict(dataDict))

# Get test values.
price= site.getPrice()

print('price= ', price)
