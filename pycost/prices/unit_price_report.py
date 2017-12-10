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
    def ImprLtx(self, os):
        if ud:
            doc.append(ud.Codigo() + " & "
               + pylatex_utils.ascii2latex(ud.getLongDescription()) + " & "
               + en_humano(med_total,0) + " & "
               + en_humano(med_total*ud.Precio(),0))


