# -*- coding: utf-8 -*-

#Class to generate pyCost quantities of finishing elements

import math
from pycost.measurements.measurement_record import MeasurementRecord



def addNeopreneBearingPadQuant(price,textComment,nUnits,length,width,height):
    '''Add neoprene bearing pad quantities to the price defined as parameter

    :price: instance of object UnitPriceQuantities
    :textComment:   string to comment each measuremt line generated 
    :nUnits: number of units
    :length, width, height: dimensions of the neoprene pad (usually in dm)
    '''
    price.quantities.append(MeasurementRecord(textComment,nUnits, length, width, height))
    
def addSidewalkQuant(price,textComment,nUnits,length,width,height):
    '''Add sidewalk quantities to the price defined as parameter

    :price: instance of object UnitPriceQuantities
    :textComment:   string to comment each measuremt line generated 
    :nUnits: number of units
    :length, width, height: dimensions of the neoprene pad (usually in dm)
    '''
    price.quantities.append(MeasurementRecord(textComment,nUnits, length, width, height))
     
