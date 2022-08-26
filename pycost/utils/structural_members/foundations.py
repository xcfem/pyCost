# -*- coding: utf-8 -*-
'''Class to generate pyCost quantities of foundation elements.'''

__author__= "Ana Ortega (AO_O) "
__copyright__= "Copyright 2017, AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "ana.Ortega@ciccp.es "

import math
from pycost.measurements.measurement_record import MeasurementRecord
from pycost.utils.structural_members import columns

class FootingBase(object):
    '''Base class to calculate quantities of a footing foundation.

    :ivar textComment:   string to comment each measuremt line generated 
    :ivar nUnits: number of units
    :ivar mnLength, mnWidth: mean length and width of the base of the footing, 
            so that its area can be calculated as 1*mnLength*mnWidth
    :ivar Hfooting: height of the footing
    :ivar ThickLeanConcr: Thickness of lean concrete under foundation
    :ivar excavHeight: mean heigth of excavation (from the bottom of lean concrete)
    :ivar excavSlope: slope of excavation (H:V)
    :ivar fillingHeight: mean heigth of filling (from the bottom of lean concrete)
    :ivar reinfQuant: reinforcement quantity
    :ivar Lformwork: length of formwork (defaults to Lside1+Lside2+Lside3+Lside4)
    :ivar Lexcav: lenght of excavation (defaults to Lside1+Lside2+Lside3+Lside4)
    '''

    def __init__(self,textComment,nUnits,mnLength,mnWidth,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork=None,Lexcav=None):
        self.textComment=textComment
        self.nUnits=nUnits
        self.mnLength=mnLength
        self.mnWidth=mnWidth
        self.Hfooting=Hfooting
        self.ThickLeanConcr=ThickLeanConcr
        self.excavHeight=excavHeight
        self.excavSlope=excavSlope #H:V
        self.fillingHeight=fillingHeight
        self.reinfQuant=reinfQuant
        self.Lformwork=Lformwork
        self.Lexcav=Lexcav

    def addExcavationQuant(self,price):
        '''Add excavation quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities
        '''
        if self.excavHeight>0:
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.mnLength, self.mnWidth, self.excavHeight))
            if self.Lexcav>0:
                price.quantities.append(MeasurementRecord(self.textComment,0.5,self.Lexcav,round(self.excavHeight*self.excavSlope,2),self.excavHeight))

                                   
    def addLeanConcreteQuant(self,price):
        '''Add lean concrete quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities
        '''
        if self.ThickLeanConcr >0:
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.mnLength, self.mnWidth, self.ThickLeanConcr))
        
    def addFillingQuant(self,price):
        '''Add filling material quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities
        '''
        if self.fillingHeight>(self.Hfooting+self.ThickLeanConcr):
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.mnLength, self.mnWidth, self.fillingHeight-self.Hfooting-self.ThickLeanConcr))
        if self.Lexcav>0 and self.fillingHeight>0:
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits*0.5,self.Lexcav,round(self.fillingHeight*self.excavSlope,2),self.fillingHeight))
        
    def addFormworkQuant(self,price):
        '''Add formwork quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        if self.Lformwork>0:
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.Lformwork, None, self.Hfooting))
        
    def addReinfConcreteQuant(self,price):
        '''Add reinforcing concrete quantities to be added to a pyCost 
        project '''
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.mnLength, self.mnWidth, self.Hfooting))
        
    def addReinforcementQuant(self,price,percLosses):
        '''Add reinforcement quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities (if 0-> no quantitie is
                added)
        :ivar percLosses: percentage to add for cutting losses (if 0-> no loss)
        '''
        if self.reinfQuant>0:
            price.quantities.append(MeasurementRecord(self.textComment + ' s/med. aux.',1, self.reinfQuant, None, None))
            if percLosses>0:
                price.quantities.append(MeasurementRecord(self.textComment + ' ' + str(percLosses) + '% despuntes y despieces',1, round(percLosses/100.*self.reinfQuant,2), None, None))
        

class FootingRectang(FootingBase):
    '''Quantities of a rectangular-based footing foundation.

    :ivar textComment:   string to comment each measuremt line generated 
    :ivar nUnits: number of units
    :ivar LengthSide1, LengthSide2: sides of the rectangle
    :ivar Hfooting: height of the footing
    :ivar ThickLeanConcr: Thickness of lean concrete under foundation
    :ivar excavHeight: mean heigth of excavation (from the bottom of lean concrete)
    :ivar excavSlope: slope of excavation (H:V)
    :ivar fillingHeight: mean heigth of filling (from the bottom of lean concrete)
    :ivar reinfQuant: reinforcement quantity
    :ivar Lformwork: length of formwork (defaults to Lside1+Lside2+Lside3+Lside4)
    :ivar Lexcav: lenght of excavation (defaults to Lside1+Lside2+Lside3+Lside4)
    '''
    def __init__(self,textComment,nUnits,LengthSide1,LengthSide2,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork=None,Lexcav=None):
        if not Lformwork:
            Lformwork=2*(LengthSide1+LengthSide2)
        if not Lexcav:
            Lexcav=2*(LengthSide1+LengthSide2)
        super(FootingRectang,self).__init__(textComment,nUnits,LengthSide1,LengthSide2,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork,Lexcav)

class FootingTriang(FootingBase):
    '''Quantities of a triangular-based footing foundation.

    :ivar textComment:   string to comment each measuremt line generated 
    :ivar nUnits: number of units
    :ivar BaseTriang: base of the triangle
    :ivar HeightTriang: heigth of the triangle
    :ivar Hfooting: height of the footing
    :ivar ThickLeanConcr: Thickness of lean concrete under foundation
    :ivar excavHeight: mean heigth of excavation (from the bottom of lean concrete)
    :ivar excavSlope: slope of excavation (H:V)
    :ivar fillingHeight: mean heigth of filling (from the bottom of lean concrete)
    :ivar reinfQuant: reinforcement quantity
    :ivar Lformwork: length of formwork (defaults to Lside1+Lside2+Lside3)
    :ivar Lexcav: lenght of excavation (defaults to Lside1+Lside2+Lside3)
    '''
    def __init__(self,textComment,nUnits,BaseTriang,HeightTriang,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork=None,Lexcav=None):
        perim=round(BaseTriang+2*math.sqrt((BaseTriang/2.)**2+HeightTriang**2),2)
        if not Lformwork:
            Lformwork=perim
        if not Lexcav:
            Lexcav=perim
        super(FootingTriang,self).__init__(textComment,nUnits,0.5*BaseTriang,HeightTriang,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork,Lexcav)

class FootingTrapez(FootingBase):
    '''Quantities of a trapeizoidal-based footing foundation.
    Bottom and top face of foundation are equal trapezoids defined 
    by two bases (Base1Trapez and Base2Trapez) and its height (HeightTrapez)

    :ivar textComment:  string to comment each measuremt line generated 
    :ivar nUnits: number of units
    :ivar Base1Trapez: length of base 1 of trapezoid that shapes the bottom and
                  top faces of the foundation
    :ivar Base2Trapez: length of base 2 of the same trapezoid
    :ivar HeightTrapez: heigth of the same trapezoid
    :ivar Hfooting: height of the footing
    :ivar ThickLeanConcr: Thickness of lean concrete under foundation
    :ivar excavHeight: mean heigth of excavation (from the bottom of lean concrete)
    :ivar excavSlope: slope of excavation (H:V)
    :ivar fillingHeight: mean heigth of filling (from the bottom of lean concrete)
    :ivar reinfQuant: reinforcement quantity
    :ivar Lformwork: length of formwork (defaults to Lside1+Lside2+Lside3+Lside4)
    :ivar Lexcav: lenght of excavation (defaults to Lside1+Lside2+Lside3+Lside4)
    '''
    def __init__(self,textComment,nUnits,Base1Trapez,Base2Trapez,HeightTrapez,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork=None,Lexcav=None):
        perim=round(Base1Trapez+Base2Trapez+2*math.sqrt((abs(Base1Trapez-Base1Trapez)/2.)**2+HeightTrapez**2),2)
        if not Lformwork:
            Lformwork=perim
        if not Lexcav:
            Lexcav=perim
        super(FootingTrapez,self).__init__(textComment,nUnits,0.5*(Base1Trapez+Base2Trapez),HeightTrapez,Hfooting,ThickLeanConcr,excavHeight,excavSlope,fillingHeight,reinfQuant,Lformwork,Lexcav)

class pile(columns.ColumnCylind):
    '''Quantities of a pile.

    :ivar textComment: string to comment each measuremt line generated 
    :ivar nPiles: number of piles
    :ivar DiamPile: diameter
    :ivar Hpile: height of the pile
    :ivar reinfQuant: reinforcement quantity
    '''
    def __init__(self,textComment,nPiles,DiamPile,Hpile,reinfQuant):
        super(pile,self).__init__(textComment,nPiles,DiamPile,Hpile,reinfQuant)

    def addPileDrillingQuant(self,price):
        '''Add quantities of pile drilling to he price defined as parameter

        :param price: instance of object UnitPriceQuantities '''
        
        price.quantities.append(MeasurementRecord(self.textComment,self.nShafts, self.Hcolumn, None, None))

'''
fotRect=FootingRectang('fotRect',nUnits=3,LengthSide1=2,LengthSide2=4,Hfooting=0.75,ThickLeanConcr=0.10,excavHeight=2.75,excavSlope=3/2.,fillingHeight=1.75,reinfQuant=2750,Lformwork=6,Lexcav=7)

fotTriang=FootingTriang('fotTriang',nUnits=3,BaseTriang=2,HeightTriang=4,Hfooting=0.75,ThickLeanConcr=0.10,excavHeight=2.75,excavSlope=3/2.,fillingHeight=1.75,reinfQuant=2750,Lformwork=6,Lexcav=7)
        
fotTrapez=FootingTrapez('fotTrapez',nUnits=3,Base1Trapez=2,Base2Trapez=4,HeightTrapez=1.5,Hfooting=0.75,ThickLeanConcr=0.10,excavHeight=2.75,excavSlope=3/2.,fillingHeight=1.75,reinfQuant=2750,Lformwork=6,Lexcav=7)
'''
        
    
    
