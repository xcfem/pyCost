#ListaRegJustPre.pyxx




import RegJustPre
from pycost.utils import basic_types

class ListaRegJustPre(list):
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
        base= ppl_precio(b,3)
        for i in self:
            (i).SetBase(base)
            base+= (i).Total()


    def ImprLtxJust(self, os):
        if(size()<1): return
        for i in self:
            (i).ImprLtxJustPre(os)
        os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Total "+StrTipo()))
           + " & & " + Total().EnHumano() + ltx_fin_reg + '\n' + ltx_fin_reg + '\n')

    def ImprLtxCP2(self, os):
        total= self.Total()
        if total>ppl_precio3(0.0):
            os.write(" & & " + StrTipo()
               + " & " + total.EnHumano() + ltx_fin_reg + '\n')

    def ImprLtxCP2Porc(self, os):
        if(size()<1): return
        for i in self:
            (i).ImprLtxCP2(os)

    def Total(self):
        retval= ppl_precio(0.0,3)
        for i in self:
            retval+= (i).Total()
        return retval


