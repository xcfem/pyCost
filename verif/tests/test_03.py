# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

from pycost.structure import obra
from pycost.structure.chapter import Chapter
from pycost.structure.unit_price_quantities import UnitPriceQuantities

obra= obra.Obra(cod="test", tit="Test title")

ch01= obra.subcapitulos.newChapter(Chapter(cod= '01', tit= 'Chapter 01'))

# Measurements
currentUnitPriceQ= UnitPriceQuantities(obra.findPrice('CM1A02A080'))

print(currentUnitPriceQ)
quit()
totalChapters= len(obra.subcapitulos)+len(ch02.subcapitulos)

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if (totalChapters==4):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')
