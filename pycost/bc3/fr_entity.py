# -*- coding: utf-8 -*-
#EntFR.py

from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc

def rdto2str(d):
    return num2str(d,13)


class EntFR(epc.EntPyCost):
    '''Entidad que tiene factor y rendimiento.'''
    def __init__(self, f= 1.0, r=0.0):
        self.factor= f
        self.rendimiento= r
    def Factor(self):
        return self.factor

    def Rendimiento(self):
        return self.rendimiento

    def Producto(self):
        return factor*rendimiento

    def ProductoR(self):
        return ppl_precio4(factor*rendimiento)

    def WriteSpre(self, os):
        os.write(rdto2str(Producto()) + '|')

    def WriteBC3(self, os):
        os.write(factor + '\\' + rdto2str(rendimiento) + '\\')


