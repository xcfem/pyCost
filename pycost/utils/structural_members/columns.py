# -*- coding: utf-8 -*-
'''Classes to generate pyCost quantities of column menbers.'''

from __future__ import division

__author__= "Ana Ortega (AO_O) "
__copyright__= "Copyright 2017, AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.Ortega@ciccp.es "

import math
from pycost.measurements.measurement_record import MeasurementRecord
from pycost.structure.unit_price_quantities import UnitPriceQuantities

class ColumnCylind(object):
    '''
    :ivar textComment: string to comment each measuremt line generated 
    :ivar nShafts: number of shafts
    :ivar DiamColumn: diameter
    :ivar Hcolumn: height of the column
    :ivar reinfQuant: reinforcement quantity
    '''
    def __init__(self,textComment,nShafts,DiamColumn,Hcolumn,reinfQuant):
        self.textComment=textComment
        self.nShafts=nShafts
        self.DiamColumn=DiamColumn
        self.Hcolumn=Hcolumn
        self.reinfQuant=reinfQuant
        
    def addReinfConcreteQuant(self,priceQ):
        '''Add reinforcing concrete quantities to he price defined as parameter

        :param priceQ: instance of object UnitPriceQuantities '''
        priceQ.quantities.append(MeasurementRecord(self.textComment,self.nShafts, self.Hcolumn, round(math.pi*self.DiamColumn**2/4.,3), None))
        
    def addReinfConcreteQuant2chapter(self,chapter,price):
        '''Add reinforcing concrete quantities to he chapter and price defined as parameters
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        '''
        priceQ=UnitPriceQuantities(price)
        self.addReinfConcreteQuant(priceQ)
        chapter.quantities.appendToExistingCode(priceQ)

    def addFormworkQuant(self,priceQ):
        '''Add formwork quantities to he price defined as parameter

        :param priceQ: instance of object UnitPriceQuantities  '''
        priceQ.quantities.append(MeasurementRecord(self.textComment,self.nShafts, self.Hcolumn, round(math.pi*self.DiamColumn,3), None))
        
    def addFormworkQuant2chapter(self,chapter,price):
        '''Add formwork quantities to the chapter and price defined as parameters
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        '''
        priceQ=UnitPriceQuantities(price)
        self.addFormworkQuant(priceQ)
        chapter.quantities.appendToExistingCode(priceQ)

    def addReinforcementQuant(self,priceQ,percLosses):
        '''Add reinforcement quantities to the price defined as parameter

        :param priceQ: instance of object UnitPriceQuantities (if 0-> no quantitie is added)
        :param percLosses: percentage to add for cutting losses (if 0-> no loss)
        '''
        if self.reinfQuant>0:
            priceQ.quantities.append(MeasurementRecord(self.textComment + ' s/med. aux.',1, self.reinfQuant, None, None))
            if percLosses>0:
                priceQ.quantities.append(MeasurementRecord(self.textComment + ' '+ str(percLosses) + '% despuntes y despieces',1, round(percLosses/100.*self.reinfQuant,2), None, None))

    def addReinforcementQuant2chapter(self,chapter,price,percLosses):
        '''Add reinforcement quantities to the chapter and price defined as parameters
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        :param percLosses: percentage to add for cutting losses (if 0-> no loss)
        '''
        priceQ=UnitPriceQuantities(price)
        self.addReinforcementQuant(priceQ,percLosses)
        chapter.quantities.appendToExistingCode(priceQ)

                
'''        
col=ColumnCylind(textComment='column',nShafts=2,DiamColumn=1,Hcolumn=10,reinfQuant=5000)
'''        
