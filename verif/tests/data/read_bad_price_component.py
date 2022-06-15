# -*- coding: utf-8 -*-
'''This code must fail returning an exit code of -1.''' 

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
pendingLinks= site.readFromYaml(pth+'/test_bad_price_component.yaml')
