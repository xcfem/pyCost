# -*- coding: utf-8 -*-
#UnitPriceReport.py


class UnitPriceReport(object):
    def __init__(self,u,mt):
        self.ud= u
        self.med_total= mt
    def Unidad(self):
        return self.ud
    def Medicion(self):
        return self.med_total
    def printLtx(self, data_table):
        if ud:
            row= [self.ud.Codigo()]
            row.append(pylatex_utils.ascii2latex(self.ud.getLongDescription()))
            row.append(en_humano(med_total,0))
            row.append(en_humano(med_total*ud.getPrice(),0))
            data_table.add_row(row)


