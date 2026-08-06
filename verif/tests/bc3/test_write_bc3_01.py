# -*- coding: utf-8 -*-
'''Trivial PyCost test.'''

from __future__ import division
from __future__ import print_function

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2022, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import logging
import filecmp
from pycost.structure import obra

def write_bc3(budget, fileName, encoding= 'ANSI'):
    ''' Export the given budget to a file using FIEBDC-3 format.

    :param budget: budget to export.
    :param fileName: name of the BC3 file.
    :param encoding: character encoding system ANSI (formally known 
                     as ISO/IEC 8859-1 or 850 (CP850 or DOS Latin 1)
                     or 437 (CP437).
    '''
    if(encoding== 'ANSI'):
        real_encoding= 'latin1'
    elif(encoding== '850'):
        real_encoding= 'cp850'
    elif(encoding== '437'):
        real_encoding= 'c437'
    with open(fileName,'w', encoding= real_encoding, errors='ignore') as f: 
        budget.WriteBC3(f, encoding= encoding)

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
pendingLinks= site.readFromJson(pth+'/../data/json/test_file_12.json')

# Generate BC3 file.
fname= os.path.basename(__file__)
outputFilesBaseName= fname[:-3]
bc3FileName= fname.replace('.py', '.bc3')
write_bc3(site, bc3FileName, encoding= 'ANSI')

# Compare with reference file.
refFile= pth+'/../data/bc3/ref_'+bc3FileName

ok= filecmp.cmp(refFile, bc3FileName, shallow=False)

# print(ok)
# print(thisFile)

if (ok):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')
    
# Remove BC3 file
if os.path.exists(bc3FileName):
    os.remove(bc3FileName)
else:
    logging.error('ERROR file: '+bc3FileName+' not found.')



