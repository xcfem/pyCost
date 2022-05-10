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
inputFile= open(pth+'/data/test_file_05.yaml',mode='r')
dataDict= yaml.safe_load(inputFile)
inputFile.close()

pendingLinks= site.solvePendingLinks(site.setFromDict(dataDict))

conceptCodes= ['ACERO0103', 'AR0005b', 'ANILLO01']
extract= site.extractConcepts(conceptCodes)


# Write in YAML format
yamlFile= pth+'/data/test_extract_concepts.yaml'
with open(yamlFile, 'w') as outputFile:
    outputs= yaml.dump(extract.getDict(), outputFile, allow_unicode=True)
outputFile.close()

# Clear data
site.clear()
extract.clear()

# Read the new YAML file.
inputFile= open(yamlFile,mode='r')
newDataDict= yaml.safe_load(inputFile)
inputFile.close()

newRoot= obra.Obra()
pendingLinks= newRoot.solvePendingLinks(newRoot.setFromDict(newDataDict))

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
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if ((price==0.0) and (numChapters==0) and (numElementaryPrices==11) and (numUnitPrices==2) and (numQuantities==0)):
    print('test: '+fname+': ok.')
else:
    lmsg.error('test: '+fname+' ERROR.')


