# -*- coding: utf-8 -*-
#EntFR.py

from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc

def rdto2str(d):
    return num2str(d,13)


class EntFR(epc.EntPyCost):
    '''Entity that has a factor and production rate.'''
    def __init__(self, f= 1.0, r=0.0):
        self.factor= f
        self.productionRate= r
        
    def getFactor(self):
        return self.factor

    def getProductionRate(self):
        return self.productionRate

    def Producto(self):
        return self.factor*self.productionRate

    def ProductoR(self):
        return basic_types.ppl_price(self.factor*self.productionRate,4)

    def WriteSpre(self, os):
        os.write(rdto2str(Producto()) + '|')

    def WriteBC3(self, os):
        os.write(factor + '\\' + rdto2str(productionRate) + '\\')


