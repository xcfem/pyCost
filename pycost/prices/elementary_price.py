# -*- coding: utf-8 -*-
#ElementaryPrice.py

from pycost.utils import basic_types
from pycost.utils import measurable as m
from decimal import Decimal


class ElementaryPrice(m.Measurable):
    precision= 2
    places= Decimal(10) ** -precision
    formatString= '{0:.'+str(precision)+'f}'

    def __init__(self, cod="", tit="", ud="", p=0.0, tp= basic_types.sin_clasif):
        super(ElementaryPrice,self).__init__(cod,tit,ud)
        self.precio= p
        self.tipo= tp

    def check_tipo(self):
        if not Codigo().empty():
            if tipo==sin_clasif and not isPercentage():
                lmsg.error("El precio elemental de código: " + Codigo()
                          + " no es un porcentaje y su tipo está sin clasificar." + '\n')

    def getType(self):
        return self.tipo

    def getPrice(self):
        return self.precio

    def readBC3(self, r):
        Measurable.readBC3(r)
        precio= r.Datos().getPrice()
        tipo= sint2TipoConcepto(r.Datos().getType())


    def printLtx(self, data_table):
        row= [pylatex_utils.ascii2latex(self.Codigo())]
        row.append(pylatex_utils.ascii2latex(self.Unidad()))
        row.append(pylatex_utils.ascii2latex(self.getTitle()))
        row.append(self.getLtxPriceString())
        data_table.add_row(row)

