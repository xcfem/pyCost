#PriceJustificationRecord.pyxx

from pycost.utils import basic_types
from pycost.utils import pylatex_utils

class PriceJustificationRecord(object):

    def __init__(self, cod= '', rd= 0.0, ud= '', tit= '', isperc= False, unit= 0.0, b= 0.0):
        self.codigo= cod #Codigo del precio elemental.
        self.rdto= rd #Production rate.
        self.unidad= ud #Unidad de medida.
        self.titulo= tit #Descripción del precio elemental.
        self.is_percentage= isperc #True if it's a percentage.
        self.unitario= unit #Unit price (or percentage if is_percentage==True).
        self.sobre= b #Base to apply percentage over.

    def base(self):
        if self.is_percentage:
            return self.sobre
        else:
            return basic_types.ppl_price(self.unitario)

    def SetBase(self, b):
        sobre= b

    def getTotal(self):
        retval= basic_types.ppl_price(self.base())
        retval*= self.rdto
        return retval

    def writePriceJustification(self, data_table):
        row= [pylatex_utils.ascii2latex(self.codigo)]
        row.append(basic_types.human_readable(self.rdto))
        row.append(pylatex_utils.ascii2latex(self.unidad))
        row.append(pylatex_utils.ascii2latex(self.titulo))
        if self.is_percentage:
            row.append(basic_types.human_readable(self.unitario) + pylatex_utils.ltx_porciento); #Percentage
        else:
            row.append(basic_types.human_readable(self.unitario)) #Precio unitario
        row.append(basic_types.human_readable(self.getTotal()))
        data_table.add_row(row)


    def writePriceTableTwoIntoLatexDocument(self, os):
        doc.append(" & & " + pylatex_utils.ascii2latex(self.titulo) + " & ")
        if(self.is_percentage): doc.append(basic_types.human_readable(self.getTotal())) #Total.
        doc.append(pylatex_utils.ltx_fin_reg + '\n')


