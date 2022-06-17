# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

from pycost.structure import obra
obra= obra.Obra(cod="test", tit="Test title")

price= obra.getPrice()

# print(price)

import os
import logging
fname= os.path.basename(__file__)
if (price==0.0):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
