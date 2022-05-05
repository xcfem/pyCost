# -*- coding: utf-8 -*-
#UnitPriceQuantities.py

import pylatex
from pycost.structure import unit_price_quantities_base as ptp
from pycost.measurements import measurement_detail as m
from pycost.measurements import measurement_record as mr
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
        ''' Read quantities from BC3 record.'''
        empty= len(m.med.lista_med)==0
        if(empty):
            rm= mr.MeasurementRecord("",m.med.med_total)
            self.quantities.append(rm)
        else:
            self.quantities.readBC3(m.med.lista_med)

