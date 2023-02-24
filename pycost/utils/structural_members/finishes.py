# -*- coding: utf-8 -*-
'''Class to generate pyCost quantities of finishing elements.'''

__author__= "Ana Ortega (AO_O) "
__copyright__= "Copyright 2017, AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.Ortega@ciccp.es "

import math
from pycost.measurements.measurement_record import MeasurementRecord
from pycost.structure.unit_price_quantities import UnitPriceQuantities



def addNeopreneBearingPadQuant(priceQ,textComment,nUnits,length,width,height):
    '''Add neoprene bearing pad quantities to the price defined as parameter

    :param priceQ: instance of object UnitPriceQuantities
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions of the neoprene pad (usually in dm)
    '''
    priceQ.appendMeasurement(textComment,nUnits, length, width, height)

def addNeopreneBearingPadQuant2chapter(chapter,price,textComment,nUnits,length,width,height):
    '''Add neoprene bearing pad quantities to the chapter and price defined as parameters

    :param chapter: chapter
    :param price: price (can be reached as presup.findPrice(priceCode))
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions of the neoprene pad (usually in dm)
     '''
    priceQ=UnitPriceQuantities(price)
    addNeopreneBearingPadQuant(priceQ,textComment,nUnits,length,width,height)
    chapter.quantities.appendToExistingCode(priceQ)


def addSidewalkQuant(priceQ,textComment,nUnits,length,width,height):
    '''Add sidewalk quantities to the price defined as parameter

    :param priceQ: instance of object UnitPriceQuantities
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions of the sidewalk
    '''
    priceQ.appendMeasurement(textComment,nUnits, length, width, height)
     
def addSidewalkQuant2chapter(chapter,price,textComment,nUnits,length,width,height):
    '''Add sidewalk quantities to the chapter and price defined as parameters

    :param chapter: chapter
    :param price: price (can be reached as presup.findPrice(priceCode))
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions of the sidewalk
    '''
    priceQ=UnitPriceQuantities(price)
    addSidewalkQuant(priceQ,textComment,nUnits,length,width,height)
    chapter.quantities.appendToExistingCode(priceQ)

def addGenericQuant(priceQ,textComment,nUnits,length,width,height):
    '''Add generic quantities to the price defined as parameter

    :param priceQ: instance of object UnitPriceQuantities
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions
    '''
    priceQ.appendMeasurement(textComment,nUnits, length, width, height)
     
def addGenericQuant2chapter(chapter,price,textComment,nUnits,length,width,height):
    '''Add generic quantities to the chapter and price defined as parameters

    :param chapter: chapter
    :param price: price (can be reached as presup.findPrice(priceCode))
    :param textComment:   string to comment each measuremt line generated 
    :param nUnits: number of units
    :param length, width, height: dimensions
    '''
    priceQ=UnitPriceQuantities(price)
    addGenericQuant(priceQ,textComment,nUnits,length,width,height)
    chapter.quantities.appendToExistingCode(priceQ)
