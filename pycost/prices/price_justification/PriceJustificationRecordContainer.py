#PriceJustificationRecordContainer.pyxx




import PriceJustificationRecord
from pycost.utils import basic_types

class PriceJustificationRecordContainer(list):
    def __init__(self,tp):
        self.tipo= tp

    def StrTipo(self):
        return basic_types.str_tipo(self.tipo)

    def SetBase(self, b):
        if(size()<1): return
        for i in self:
            (i).SetBase(b)

    def SetBaseAcum(self, b):
        if(size()<1): return
        base= basic_types.ppl_precio(b,3)
        for i in self:
            (i).SetBase(base)
            base+= (i).getTotal()


    def ImprLtxJust(self, os):
        if(size()<1): return
        for i in self:
            (i).ImprLtxJustPre(os)
        doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Total "+StrTipo()))
           + " & & " + Total().EnHumano() + pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_fin_reg + '\n')

    def writePriceTableTwoIntoLatexDocument(self, os):
        total= self.getTotal()
        if total>ppl_precio3(0.0):
            doc.append(" & & " + StrTipo()
               + " & " + total.EnHumano() + pylatex_utils.ltx_fin_reg + '\n')

    def writePriceTableTwoIntoLatexDocumentPorc(self, os):
        if(size()<1): return
        for i in self:
            (i).writePriceTableTwoIntoLatexDocument(os)

    def getTotal(self):
        retval= basic_types.ppl_precio(0.0,3)
        for i in self:
            retval+= (i).getTotal()
        return retval


