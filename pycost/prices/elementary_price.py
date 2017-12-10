# -*- coding: utf-8 -*-
#ElementaryPrice.py

from pycost.bc3 import bc3_entity as bc3
from pycost.utils import measurable as m


class ElementaryPrice(m.Measurable):
    def __init__(self, cod="", tit="", ud="", p=0.0, tp= bc3.sin_clasif):
        super(ElementaryPrice,self).__init__(cod,tit,ud)
        self.precio= p
        self.tipo= tp

    def check_tipo(self):
        if not Codigo().empty():
            if tipo==sin_clasif and not IsPercentage():
                lmsg.error("El precio elemental de código: " + Codigo()
                          + " no es un porcentaje y su tipo está sin clasificar." + '\n')

    def Tipo(self):
        return self.tipo

    def Precio(self):
        return self.precio

    def LeeBC3(self, r):
        Measurable.LeeBC3(r)
        precio= r.Datos().Precio()
        tipo= sint2TipoConcepto(r.Datos().Tipo())


    def ImprLtx(self, os):
        doc.append(pylatex_utils.ascii2latex(Codigo()) + " & "
           + pylatex_utils.ascii2latex(Unidad()) + " & "
           + pylatex_utils.ascii2latex(getTitle()) + " & "
           + StrPrecioLtx() + "\\\\" + '\n')

