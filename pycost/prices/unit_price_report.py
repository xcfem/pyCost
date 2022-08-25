# -*- coding: utf-8 -*-
#UnitPriceReport.py
from pycost.utils import pylatex_utils
from pycost.utils import basic_types


class UnitPriceReport(object):
    def __init__(self,u,mt):
        self.ud= u
        self.med_total= mt
    def Unidad(self):
        return self.ud
    def Medicion(self):
        return self.med_total
    def printLtx(self, data_table):
        precision= 2
        if self.ud:
            row= [self.ud.Codigo()]
            row.append(pylatex_utils.ascii2latex(self.ud.getLongDescription()))
            row.append(basic_types.human_readable(self.med_total,precision))
            row.append(basic_types.human_readable(self.med_total*float(self.ud.getPrice()),precision))
            data_table.add_row(row)


