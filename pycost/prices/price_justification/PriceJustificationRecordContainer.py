#PriceJustificationRecordContainer.pyxx




import PriceJustificationRecord
from pycost.utils import basic_types
from pycost.utils import pylatex_utils

class PriceJustificationRecordContainer(list):
    def __init__(self,tp):
        self.tipo= tp

    def StrTipo(self):
        return basic_types.str_tipo(self.tipo)

    def SetBase(self, b):
        for i in self:
            (i).SetBase(b)

    def SetBaseAcum(self, b):
        if(len(self)):
            base= basic_types.ppl_price(b,3)
            for i in self:
                (i).SetBase(base)
                base+= (i).getTotal()


    def ImprLtxJust(self, doc):
        if(len(self)):
            for i in self:
                (i).ImprLtxJustPre(os)
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Total "+StrTipo()))
               + " & & " + basic_types.human_readable(Total()) + pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_fin_reg + '\n')

    def writePriceTableTwoIntoLatexDocument(self, data_table):
        total= self.getTotal()
        if total>basic_types.ppl_price(0.0,3):
            data_table.add_row(['','',self.StrTipo(),basic_types.human_readable(total)])

    def writePriceTableTwoIntoLatexDocumentPorc(self, os):
        if(len(self)):
            for i in self:
               (i).writePriceTableTwoIntoLatexDocument(os)

    def getTotal(self):
        retval= basic_types.ppl_price(0.0,3)
        for i in self:
            retval+= (i).getTotal()
        return retval


