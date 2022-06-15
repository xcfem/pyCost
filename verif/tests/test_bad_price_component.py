# -*- coding: utf-8 -*-
'''Check exit code when reading a buggy data file.''' 
from __future__ import division
from __future__ import print_function

import subprocess
import sys
import os

# Get file path.
pth= os.path.dirname(__file__)
if(not pth):
    pth= '.'
testBadPriceComponent= pth+'/./data/read_bad_price_component.py'

retcode = subprocess.call([sys.executable, testBadPriceComponent], 
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)

'''
print(retcode)
'''

from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if(retcode!=0):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')

