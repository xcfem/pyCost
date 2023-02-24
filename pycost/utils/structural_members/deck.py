# -*- coding: utf-8 -*-
'''Class to generate pyCost quantities of slabs and bridge decks.'''

__author__= "Ana Ortega (AO_O) "
__copyright__= "Copyright 2017, AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.Ortega@ciccp.es "

import math
from pycost.measurements.measurement_record import MeasurementRecord
from pycost.structure.unit_price_quantities import UnitPriceQuantities

class DeckUnifCrossSect(object):
    '''Class to calculate quantities of a generic deck (or deck section) with
    uniform cross section.

    :textComment:   string to comment each measuremt line generated 
    :nUnits: number of units
    :LdeckUnifSect: length of bridge with uniform cross-section
    :AreaUnifSect: area of uniform cross-section 
    :reinfQuant: reinforcement quantity (total kg)
    :LexposFormwork: length of formwork in exposed sides of the cross-section
    :LhiddFormwork: length of formwork in hidden sides of the cross-section
                   (defaults to None)
    :nLateralFormwork: number of lateral sections with formwork (defaults to 0)
     '''

    def __init__(self,textComment,nUnits,LdeckUnifSect,AreaUnifSect,reinfQuant,LexposFormwork,LhiddFormwork= 0.0,nLateralFormwork=0):
        self.textComment=textComment
        self.nUnits=nUnits
        self.LdeckUnifSect=LdeckUnifSect
        self.AreaUnifSect=AreaUnifSect
        self.reinfQuant=reinfQuant
        self.LexposFormwork=LexposFormwork
        self.LhiddFormwork=LhiddFormwork
        self.nLateralFormwork=nLateralFormwork

    def addReinfConcreteQuant(self,priceQ):
        '''Add reinforcing concrete quantities to the price passed as parameter
 
        :param priceQ: instance of object UnitPriceQuantities 
        '''
        priceQ.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.LdeckUnifSect, self.AreaUnifSect, None))
        
    def addReinfConcreteQuant2chapter(self,chapter,price):
        '''Add reinforcing concrete quantities to the chapter and price passed as parameters
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        '''
        priceQ=UnitPriceQuantities(price)
        self.addReinfConcreteQuant(priceQ)
        chapter.quantities.appendToExistingCode(priceQ)

    def addReinforcementQuant(self,priceQ,percLosses):
        '''Add reinforcement quantities to the price defined as parameter

        :param priceQ: instance of object UnitPriceQuantities 
        :param percLosses: percentage to add for cutting losses (if 0-> no loss)
        '''
        if self.reinfQuant>0:
            priceQ.quantities.append(MeasurementRecord(self.textComment + ' s/med. aux.',1, self.reinfQuant, None, None))
            if percLosses>0:
                priceQ.quantities.append(MeasurementRecord(self.textComment + ' ' + str(percLosses) + '% despuntes y despieces',1, round(percLosses/100.*self.reinfQuant,2), None, None))
            
    def addReinforcementQuant2chapter(self,chapter,price,percLosses):
        '''Add reinforcement quantities to the chapter and price defined as parameters
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        '''
        priceQ=UnitPriceQuantities(price)
        self.addReinforcementQuant(priceQ,percLosses)
        chapter.quantities.appendToExistingCode(priceQ)

    def addExposedWallFormworkQuant(self,priceQ):
        '''Add exposed-wall formwork quantities to the price defined as parameter

        :param priceQ: instance of object UnitPriceQuantities 
        '''
        if self.LexposFormwork>0:
                priceQ.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.LdeckUnifSect,self.LexposFormwork,None))
        
    def addExposedWallFormworkQuant2chapter(self,chapter,price):
        '''Add exposed-wall formwork quantities to the price defined as parameter
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        '''
        priceQ=UnitPriceQuantities(price)
        self.addExposedWallFormworkQuant(priceQ)
        chapter.quantities.appendToExistingCode(priceQ)

    def addHiddenWallFormworkQuant(self,priceQ):
        '''Add hidden-wall formwork quantities to the price defined as parameter

        :param priceQ: instance of object UnitPriceQuantities 
        '''
        if self.LhiddFormwork>0.0:
            priceQ.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.LdeckUnifSect,self.LhiddFormwork,None))
        if self.nLateralFormwork>0:
            priceQ.quantities.append(MeasurementRecord(self.textComment,self.nLateralFormwork*self.AreaUnifSect,None,None,None))
        
    def addHiddenWallFormworkQuant2chapter(self,chapter,price):
        '''Add hidden-wall formwork quantities to the chapter and price defined as parameters
         
        :param chapter: chapter
        :param price: price (can be reached as presup.findPrice(priceCode))
        '''
        priceQ=UnitPriceQuantities(price)
        self.addHiddenWallFormworkQuant(priceQ)
        chapter.quantities.appendToExistingCode(priceQ)

'''
deck=DeckUnifCrossSect('deck',nUnits=2,LdeckUnifSect=30,AreaUnifSect=1.5,reinfQuant=5000,LexposFormwork=2.5,nLateralFormwork=0)    
'''
