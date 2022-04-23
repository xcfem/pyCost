# -*- coding: utf-8 -*-
#UnitPriceQuantities.py

import pylatex
from pycost.structure import unit_price_quantities_base as ptp
from pycost.measurements import measurement_detail as m
from pycost.utils import pylatex_utils

class UnitPriceQuantities(ptp.UnitPriceQuantitiesBase):
    '''UnitPriceQuantities del presupuesto correspondiente 
       a una unidad de obra.'''

    def __init__(self, u= None):
        super(UnitPriceQuantities,self).__init__(u)
        self.quantities= m.Quantities()

    def getTotal(self):
        return self.quantities.getTotal()

    def getRoundedTotal(self):
        return self.quantities.getRoundedTotal()

    def readBC3(self, m):
        if m.med.lista_med.empty():
            rm= MeasurementRecord("",m.med.med_total)
            quantities.append(rm)
        else:
            quantities.readBC3(m.med.lista_med)

