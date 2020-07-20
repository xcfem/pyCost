# -*- coding: utf-8 -*-
from __future__ import division

#Classes to generate pyCost quantities of column menbers

import math
from pycost.measurements.measurement_record import MeasurementRecord

class ColumnCylind(object):
    '''
    :textComment: string to comment each measuremt line generated 
    :nShafts: number of shafts
    :DiamColumn: diameter
    :Hcolumn: height of the column
    :reinfQuant: reinforcement quantity
    '''
    def __init__(self,textComment,nShafts,DiamColumn,Hcolumn,reinfQuant):
        self.textComment=textComment
        self.nShafts=nShafts
        self.DiamColumn=DiamColumn
        self.Hcolumn=Hcolumn
        self.reinfQuant=reinfQuant
        
    def addReinfConcreteQuant(self,price):
        '''Add reinforcing concrete quantities to he price defined as parameter

        :price: instance of object UnitPriceQuantities '''
        price.quantities.append(MeasurementRecord(self.textComment,self.nShafts, self.Hcolumn, round(math.pi*self.DiamColumn**2/4.,3), None))
        
    def addFormworkQuant(self,price):
        '''Add formwork quantities to he price defined as parameter

        :price: instance of object UnitPriceQuantities  '''
        price.quantities.append(MeasurementRecord(self.textComment,self.nShafts, self.Hcolumn, round(math.pi*self.DiamColumn,3), None))
        
    def addReinforcementQuant(self,price,percLosses):
        '''Add reinforcement quantities to the price defined as parameter

        :price: instance of object UnitPriceQuantities (if 0-> no quantitie is
                added)
        :percLosses: percentage to add for cutting losses (if 0-> no loss)
        '''
        if self.reinfQuant>0:
            price.quantities.append(MeasurementRecord(self.textComment + ' s/med. aux.',1, self.reinfQuant, None, None))
            if percLosses>0:
                price.quantities.append(MeasurementRecord(self.textComment + ' '+ str(percLosses) + '% despuntes y despieces',1, round(percLosses/100.*self.reinfQuant,2), None, None))

'''        
col=ColumnCylind(textComment='column',nShafts=2,DiamColumn=1,Hcolumn=10,reinfQuant=5000)
'''        
