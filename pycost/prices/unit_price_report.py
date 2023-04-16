# -*- coding: utf-8 -*-
''' Unit price report.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2017, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

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
            row.append(pylatex_utils.ascii2latex(self.ud.getNoEmptyDescription()))
            row.append(basic_types.human_readable(self.med_total,precision))
            row.append(basic_types.human_readable(self.med_total*float(self.ud.getPrice()),precision))
            data_table.add_row(row)


