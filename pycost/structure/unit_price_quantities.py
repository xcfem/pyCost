# -*- coding: utf-8 -*-
#UnitPriceQuantities.py

import unit_price_quantities_base as ptp
from pycost.measurements import measurement_detail as m
import pylatex
from pycost.utils import pylatex_utils

class UnitPriceQuantities(ptp.UnitPriceQuantitiesBase):
    '''UnitPriceQuantities del presupuesto correspondiente 
       a una unidad de obra.'''

    def __init__(self, u= None):
        super(UnitPriceQuantities,self).__init__(u)
        self.quantities= m.Quantities()

    def Copia(self):
        return UnitPriceQuantities(self)

    def getTotal(self):
        return self.quantities.getTotal()

    def getTotalR(self):
        return self.quantities.getTotalR()

    def LeeBC3(self, m):
        if m.med.lista_med.empty():
            rm= MeasurementRecord("",m.med.med_total)
            quantities.append(rm)
        else:
            quantities.LeeBC3(m.med.lista_med)

