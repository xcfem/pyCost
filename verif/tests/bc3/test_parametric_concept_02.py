# -*- coding: utf-8 -*-
'''Check reading of parametric prices with matrix component values.''' 
from __future__ import division
from __future__ import print_function

from pycost.structure import obra
from pycost.structure import chapter
from pycost.structure import unit_price_quantities

# Create main object.
site= obra.Obra(cod="test", tit="Test title")

# Read data from file.
import os
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= "."
inputFile= open(pth+'/../data/bc3/test_parametric_02.bc3',mode='r')#, encoding="latin-1")

site.readBC3(inputFile)
inputFile.close()

# Get paramatric concept keys.
parametricConceptKeys= site.precios.unidades.getParametricConceptsKeys()

# Get the first parametric concept
pConcept= site.precios.unidades.getParametricConcept(key= parametricConceptKeys[0])

# Write the object parameters and its options.
# pConcept.writeParameterOptions()
# Set the values for the optional parameters.
options= [('diámetro_perforación', '>0,15 m - 0,20 m'), ('armadura_tubular', 'tubo acero 88,9 mm diámetro exterior y 9,5 mm de espesor'), ('trabajo', 'Nocturno'), ('banda_de_mantenimiento', 'i<3 horas'), ('condiciones_de_ejecución', 'Volumen escaso')]

# Create unit price with the preceding options.
unitPrice= pConcept.getUnitPrice(code= parametricConceptKeys[0], options= options, rootChapter= site)
# unitPrice.Write()

# Append the price to the root chapter price table.
site.precios.unidades.Append(unitPrice)

# Measurements
## New chapter
ch01= site.subcapitulos.newChapter(chapter.Chapter(cod= '01', tit= 'Chapter 01'))
## Quantities.
measurements= unit_price_quantities.UnitPriceQuantities(site.getUnitPrice(unitPrice.codigo))
measurements.appendMeasurement(textComment='test parametric price.', nUnits= 1, length= None, width=None, height=None)
ch01.appendUnitPriceQuantities(measurements)

# Compute cost.
cost= site.getPrice()
totalRefCost= 133.83
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
