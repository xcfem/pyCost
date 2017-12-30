# -*- coding: utf-8 -*-
#ElementaryPrice.py

from pycost.utils import basic_types
from pycost.utils import measurable as m


class ElementaryPrice(m.Measurable):
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

    def Precio(self):
        return self.precio

    def LeeBC3(self, r):
        Measurable.LeeBC3(r)
        precio= r.Datos().Precio()
        tipo= sint2TipoConcepto(r.Datos().getType())


    def printLtx(self, os):
        doc.append(pylatex_utils.ascii2latex(Codigo()) + " & "
           + pylatex_utils.ascii2latex(Unidad()) + " & "
           + pylatex_utils.ascii2latex(getTitle()) + " & "
           + StrPrecioLtx() + "\\\\" + '\n')

