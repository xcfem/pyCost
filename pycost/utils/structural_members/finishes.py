# -*- coding: utf-8 -*-

#Class to generate pyCost quantities of finishing elements

import math
from pycost.measurements.measurement_record import MeasurementRecord



def addNeopreneBearingPadQuant(price,textComment,nUnits,length,width,height):
    '''Add neoprene bearing pad quantities to the price defined as parameter

    :param price: instance of object UnitPriceQuantities
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions of the neoprene pad (usually in dm)
    '''
    price.appendMeasurement(textComment,nUnits, length, width, height)
    
def addSidewalkQuant(price,textComment,nUnits,length,width,height):
    '''Add sidewalk quantities to the price defined as parameter

    :param price: instance of object UnitPriceQuantities
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions of the sidewalk
    '''
    price.appendMeasurement(textComment,nUnits, length, width, height)
     
def addGenericQuant(price,textComment,nUnits,length,width,height):
    '''Add generic quantities to the price defined as parameter

    :param price: instance of object UnitPriceQuantities
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions
    '''
    price.appendMeasurement(textComment,nUnits, length, width, height)
     
