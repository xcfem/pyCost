# -*- coding: utf-8 -*-
'''Extract concepts from unit cost databases.''' 
from __future__ import division
from __future__ import print_function

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
pendingLinks= site.readFromYaml(pth+'/data/test_file_05.yaml')

extracted= obra.Obra(cod="extracted", tit="Extracted concepts.")
conceptCodes= ['ACERO0103', 'AR0005b', 'ANILLO01']
extracted= site.extractConcepts(conceptCodes, extracted)


# Write in YAML format
yamlFile= pth+'/data/test_extract_concepts.yaml'
with open(yamlFile, 'w') as outputFile:
    outputs= yaml.dump(extracted.getDict(), outputFile, allow_unicode=True)
outputFile.close()

# Clear data
site.clear()
extracted.clear()

# Read the new YAML file.
newRoot= obra.Obra()
newRoot.readFromYaml(yamlFile)

numElementaryPrices= len(newRoot.precios.Elementales())
numUnitPrices= len(newRoot.precios.UdsObra())
numQuantities= 0
for sc in newRoot.subcapitulos:
    numElementaryPrices+= len(sc.precios.Elementales())
    numUnitPrices+= len(sc.precios.UdsObra())
    numQuantities+= len(sc.quantities)
    
# Get test values.
price= site.getPrice()
numChapters= len(site.subcapitulos)

'''
print('price: ', price)
print('num chapters: ', numChapters)
print('num quantities: ', numQuantities)
print('num. elementary prices: ', numElementaryPrices)
print('num. unitary prices: ', numUnitPrices)
'''

import os
import logging
fname= os.path.basename(__file__)
if ((price==0.0) and (numChapters==0) and (numElementaryPrices==11) and (numUnitPrices==2) and (numQuantities==0)):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')


