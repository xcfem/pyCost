# -*- coding: utf-8 -*-
'''Convert BC3 to YAML.''' 
from __future__ import division
from __future__ import print_function

import sys
import logging
from pathlib import Path
from pycost.structure import obra

# Check command line arguments.
if(len(sys.argv)<2):
    logging.error('Syntax: '+sys.argv[0]+ ' input_file_name')
    quit()

inputFile= sys.argv[1]
outputFile= Path(inputFile).stem+'.yaml'

# Convert to yaml
obra.bc3_to_yaml(inputFile, outputFile)

print('done.')
