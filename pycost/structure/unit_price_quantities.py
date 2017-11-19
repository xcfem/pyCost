# -*- coding: utf-8 -*-
#UnitPriceQuantities.py



import unit_price_quantities_base as ptp
from pycost.measurements import measurement_detail as m

class UnitPriceQuantities(ptp.UnitPriceQuantitiesBase):
    '''UnitPriceQuantities del presupuesto correspondiente a una unidad de obra.'''

    def __init__(self, u= None):
        super(UnitPriceQuantities,self).__init__(u)
        quantities= m.Quantities()

    def Copia(self):
        return UnitPriceQuantities(self)

    def Total(self):
        return self.quantities.Total()

    def TotalR(self):
        return self.quantities.TotalR()

    def LeeBC3(self, m):
        if m.med.lista_med.empty():
            rm= MeasurementRecord("",m.med.med_total)
            quantities.append(rm)
        else:
            quantities.LeeBC3(m.med.lista_med)

