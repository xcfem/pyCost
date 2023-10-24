# -*- coding: utf-8 -*-
'''Check that measurement records for objects differents that chapters are
   detected.'''

from __future__ import division
from __future__ import print_function

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import logging
from pycost.structure import obra
from pycost.structure import chapter
from pycost.structure import unit_price_quantities

# Create main object.
rootChapter= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= "."
inputFile= open(pth+'/../data/bc3/measurement_outside_chapter.bc3',mode='r', encoding="latin-1")
# Don't show error messages.
logging.basicConfig(filename="/tmp/erase.log", format='%(asctime)s %(message)s', filemode='w')
ok= rootChapter.readBC3(inputFile)
inputFile.close()

# print(ok)

# For now, the test pass when the value returned by readBC3 is false.
# When a solution for this problem has been implemented this
# test should be modified.
import os
import logging
fname= os.path.basename(__file__)
if(ok==False):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')


# doc= rootChapter.getLatexDocument()
# doc.generate_tex('presupuesto_conexion_fase_ii')
