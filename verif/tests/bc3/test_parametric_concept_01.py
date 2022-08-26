# -*- coding: utf-8 -*-
'''Read price database.''' 
from __future__ import division
from __future__ import print_function

from pycost.structure import obra
from pycost.structure import unit_price_quantities
from pycost.structure import chapter

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= "."
inputFile= open(pth+'/../data/bc3/test_parametric_01.bc3',mode='r')
site.readBC3(inputFile)
inputFile.close()

# Get paramatric concept keys.
parametricConceptKeys= site.precios.unidades.getParametricConceptsKeys()

# Get the first parametric concept
pConcept= site.precios.unidades.getParametricConcept(key= parametricConceptKeys[0])

# # Write the object parameters and its options.
# pConcept.writeParameterOptions()

# Set the values for the optional parameters.
options= [('altura_de_apeo', '<6 m'), ('condiciones_de_ejecución', 'Volumen escaso'), ('trabajo', 'Diurno'), ('banda_de_mantenimiento', 'i<3 horas')]

# Create unit price with the preceding options.
unitPrice= pConcept.getUnitPrice(code= parametricConceptKeys[0], options= options, rootChapter= site)

#unitPrice.Write()

# Append the price to the root chapter price table.
site.precios.unidades.Append(unitPrice)

# Measurements
## New chapter
ch01= site.subcapitulos.newChapter(chapter.Chapter(cod= '01', tit= 'Chapter 01'))
## Quantities.
measurements= unit_price_quantities.UnitPriceQuantities(site.getUnitPrice(unitPrice.codigo))
measurements.appendMeasurement(textComment='test parametric price.', nUnits= 4, length= 2, width=12, height=None)
ch01.appendUnitPriceQuantities(measurements)

# Compute cost.
cost= site.getPrice()
totalRefCost= 7237.4400000000005
ratio1= abs(cost-totalRefCost)/totalRefCost

'''
print('cost= ', cost)
print('ratio1= ', ratio1)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio1<1e-6):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')