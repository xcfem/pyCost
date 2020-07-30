# -*- coding: utf-8 -*-
from __future__ import division

#Class to generate pyCost quantities of wall structural members.

import math
from pycost.measurements.measurement_record import MeasurementRecord

class WallBase(object):
    '''Base class to calculate quantities of a wall.

    :ivar textComment:   string to comment each measuremt line generated
    :ivar nUnits: number of units (defaults to 1)
    :ivar Lenght: wall length
    :ivar meanHeight: mean wall height
    :ivar meanThickness: mean wall thickness 
    :ivar reinfQuant: reinforcement quantity
    '''
    def __init__(self,textComment,nUnits,Length,meanHeight,meanThickness,reinfQuant):
        self.textComment=textComment
        self.nUnits=nUnits
        self.Length=Length
        self.meanHeight=meanHeight
        self.meanThickness=meanThickness
        self.reinfQuant=reinfQuant

    def addReinfConcreteQuant(self,price):
        '''Add reinforcing concrete quantities to be added to a pyCost 
        project '''
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits, self.Length, self.meanThickness, self.meanHeight))
                
    def addReinforcementQuant(self,price,percLosses):
        '''Add reinforcement quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities (if 0-> no quantitie is
                added)
        :ivar percLosses: percentage to add for cutting losses (if 0-> no loss)
        '''
        if self.reinfQuant>0:
            price.quantities.append(MeasurementRecord(self.textComment + ' s/med. aux.',1, self.reinfQuant, None, None))
            if percLosses>0:
                price.quantities.append(MeasurementRecord(self.textComment +' '+ str(percLosses) + '% despuntes y despieces',1, round(percLosses/100.*self.reinfQuant,2), None, None))
        
class SlopedWallBase(WallBase):
    '''Base class to calculate quantities of a sloped wall.

    :ivar textComment:   string to comment each measuremt line generated 
    :ivar nUnits: number of units (defaults to 1)
    :ivar Length: wall length (horizontal projection)
    :ivar Height: wall height (if sloped Height = maximum length of the wall)
    :ivar Thickness: thickness of the stem at the top face. 
    :ivar reinfQuant: reinforcement quantity
    :ivar SlopeTopFace: slope of the top face (V:H) (defaults to 0)
    :ivar SlopeFrontFace: vertical slope at the front face (H:V) (defaults to 0)
    :ivar SlopeBackFace: vertical slope of the back or earth-face (H:V) (defaults to 0)
    '''
    
    def __init__(self,textComment,nUnits,Length,Height,Thickness,reinfQuant,SlopeTopFace=0,SlopeFrontFace=0,SlopeBackFace=0):
        HeightSect2=Height-Length*SlopeTopFace
        mnHeight=round(0.5*(Height+HeightSect2),2) #height at middle section
        mnThickness=round(Thickness+(Height+HeightSect2)*(SlopeFrontFace+SlopeBackFace)/4.,2)
        super(SlopedWallBase,self).__init__(textComment,nUnits,Length,mnHeight,mnThickness,reinfQuant)
        self.Thickness=Thickness
        self.SlopeTopFace=SlopeTopFace
        self.SlopeFrontFace=SlopeFrontFace
        self.SlopeBackFace=SlopeBackFace

class RetainingWall(SlopedWallBase):
    '''Quantities of a retainig wall.

    :ivar textComment:   string to comment each measuremt line generated 
    :ivar nUnits: number of units (defaults to 1)
    :ivar Length: wall length (horizontal projection)
    :ivar Height: wall height (if sloped Height = maximum length of the wall)
    :ivar Thickness: thickness of the stem at the top face. 
    :ivar reinfQuant: reinforcement quantity
    :ivar SlopeTopFace: slope of the top face (V:H) (defaults to 0)
    :ivar SlopeFrontFace: vertical slope at the front face (H:V) (defaults to 0)
    :ivar SlopeEarthFace: vertical slope of the earth-face (H:V) (defaults to 0)
    :ivar FormworkLateral1: if formwork on the highgest lateral face ='Y' 
    (defaults to yes)
    :ivar FormworkLateral2: if formwork on the lowest lateral face ='Y' 
    (defaults to yes)
    :ivar JointLateral1: if dilatation joint in the highgest lateral face ='Y'
    (defaults to 'N')
    :ivar JointLateral2: if dilatation joint in the lowest lateral face ='Y'
    (defaults to 'N')

    '''
    
    def __init__(self,textComment,nUnits,Length,Height,Thickness,reinfQuant,SlopeTopFace=0,SlopeFrontFace=0,SlopeEarthFace=0,FormworkLateral1='Y',FormworkLateral2='Y',JointLateral1='N',JointLateral2='N'):
        self.maxHeight=Height
        super(RetainingWall,self).__init__(textComment,nUnits,Length,Height,Thickness,reinfQuant,SlopeTopFace,SlopeFrontFace,SlopeEarthFace)
        self.FormworkLateral1=FormworkLateral1
        self.FormworkLateral2=FormworkLateral2
        self.JointLateral1=JointLateral1
        self.JointLateral2=JointLateral2

    def addHiddenWallFormworkQuant(self,price):
        '''Add hidden-wall formwork quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        formWidth=round(self.meanHeight*math.sqrt(1+self.SlopeBackFace**2),2)
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.Length,formWidth,None))
        if self.FormworkLateral1.lower()[0]=='y':
            H=self.maxHeight
            B1=self.Thickness
            B2=self.Thickness+H*self.SlopeFrontFace+H*self.SlopeBackFace
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,None,round((B1+B2)/2.,2),H))
        if self.FormworkLateral2.lower()[0]=='y':
            H=round(self.maxHeight-self.Length*self.SlopeTopFace,2)
            B1=self.Thickness
            B2=self.Thickness+H*self.SlopeFrontFace+H*self.SlopeBackFace
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,None,round((B1+B2)/2.,2),H))
        
    def addExposedWallFormworkQuant(self,price):
        '''Add exposed-wall formwork quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        formWidth=round(self.meanHeight*math.sqrt(1+self.SlopeFrontFace**2),2)
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.Length,formWidth,None))
        
    def addWaterproofingPrimerQuant(self,price):
        '''Add waterproofing primer quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        watproofWidth=round(self.meanHeight*math.sqrt(1+self.SlopeBackFace**2),2)
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.Length,watproofWidth,None))
                
    def addWaterproofingLayerQuant(self,price):
        '''Add waterproofing layer quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        self.addWaterproofingPrimerQuant(price)

    def addDrainageTubeQuant(self,price):
        '''Add drainage tube quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.Length,None,None))
    def addJointsQuant(self,price):
        '''Add dilatation-joint quantities to the price defined as parameter
        :ivar price: instance of object UnitPriceQuantities '''
        if self.JointLateral1.lower()[0]=='y':
            H=self.maxHeight
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,None,None,H))
        if self.JointLateral2.lower()[0]=='y':
            H=round(self.maxHeight-self.Length*self.SlopeTopFace,2)
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,None,None,H))

        
class TwoExposedSideWall(SlopedWallBase):
    '''Quantities of a two-exposed-side wall.

    :ivar textComment:   string to comment each measuremt line generated 
    :ivar nUnits: number of units (defaults to 1)
    :ivar Length: wall length (horizontal projection)
    :ivar Height: wall height (if sloped Height = maximum length of the wall)
    :ivar Thickness: thickness of the stem at the top face. 
    :ivar reinfQuant: reinforcement quantity
    :ivar SlopeTopFace: slope of the top face (V:H) (defaults to 0)
    :ivar SlopeFrontFace: vertical slope at the front face (H:V) (defaults to 0)
    :ivar SlopeBackFace: vertical slope of the back face (H:V) (defaults to 0)
    :ivar FormworkLateral1: if formwork on the highgest lateral face ='Y' (defaults 
    to yes)
    :ivar FormworkLateral2: if formwork on the highgest lateral face ='Y' (defaults 
    to yes)
    '''
    
    def __init__(self,textComment,nUnits,Length,Height,Thickness,reinfQuant,SlopeTopFace=0,SlopeFrontFace=0,SlopeBackFace=0,FormworkLateral1='Y',FormworkLateral2='Y'):
        self.maxHeight=Height
        super(TwoExposedSideWall,self).__init__(textComment,nUnits,Length,Height,Thickness,reinfQuant,SlopeTopFace,SlopeFrontFace,SlopeBackFace)
        self.FormworkLateral1=FormworkLateral1
        self.FormworkLateral2=FormworkLateral2

    def addExposedWallFormworkQuant(self,price):
        '''Add exposed-wall formwork quantities to the price defined as parameter

        :ivar price: instance of object UnitPriceQuantities '''
        formWidth=round(self.meanHeight*math.sqrt(1+self.SlopeFrontFace**2),2)
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.Length,formWidth,None))
        formWidth=round(self.meanHeight*math.sqrt(1+self.SlopeBackFace**2),2)
        price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,self.Length,formWidth,None))
        if self.FormworkLateral1.lower()[0]=='y':
            H=self.maxHeight
            B1=self.Thickness
            B2=self.Thickness+H*self.SlopeFrontFace+H*self.SlopeBackFace
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,None,round((B1+B2)/2.,2),H))
        if self.FormworkLateral2.lower()[0]=='y':
            H=round(self.maxHeight-self.Length*self.SlopeTopFace,2)
            B1=self.Thickness
            B2=self.Thickness+H*self.SlopeFrontFace+H*self.SlopeBackFace
            price.quantities.append(MeasurementRecord(self.textComment,self.nUnits,None,round((B1+B2)/2.,2),H))
        
'''
wall=RetainingWall(textComment='wall',nUnits=2,Length=5,Height=4,Thickness=0.3,reinfQuant=5000,SlopeTopFace=1/4.,SlopeFrontFace=1/15.,SlopeEarthFace=1/12.,FormworkLateral1='Y',FormworkLateral2='Y')    

wallExp=TwoExposedSideWall(textComment='wall',Length=5,nUnits=2,Height=4,Thickness=0.3,reinfQuant=5000,SlopeTopFace=1/4.,SlopeFrontFace=1/15.,SlopeBackFace=1/12.,FormworkLateral1='Y',FormworkLateral2='Y')    
'''
