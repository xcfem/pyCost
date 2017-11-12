#ListaRegJustPre.pyxx




import RegJustPre
#include <deque>
import ../EntBC3

class ListaRegJustPre(std.deque<RegJustPre>, EntCmd):
    tipo_concepto tipo
public:
    ListaRegJustPre( tipo_concepto &tp)
        : tipo(tp) {
     SetBase( ppl_precio3 &b)
     SetBaseAcum( ppl_precio3 &b)
    ppl_precio3 Total()
    std.string StrTipo()
        switch(tipo)
        case mdo:
            return "mano de obra"
        case mat:
            return "materiales"
        case maq:
            return "maquinaria"
        default:
            return "porcentajes"


     ImprLtxJust(os)
     ImprLtxCP2(os)
     ImprLtxCP2Porc(os)



#ListaRegJustPre.cc

import ListaRegJustPre
import bibXCBasica/src/texto/latex


def SetBase(self, &b):
    if(size()<1) return
    iterator i
    for(i=begin(); i!=end(); i++)
        (*i).SetBase(b)

def SetBaseAcum(self, &b):
    if(size()<1) return
    ppl_precio3 base(b)
    iterator i
    for(i=begin(); i!=end(); i++)
        (*i).SetBase(base)
        base+= (*i).Total()


def ImprLtxJust(self, &os):
    if(size()<1) return
    const_iterator i
    for(i=begin(); i!=end(); i++)
        (*i).ImprLtxJustPre(os)
    os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Total "+StrTipo()))
       + " & & " + Total().EnHumano() + ltx_fin_reg + '\n' + ltx_fin_reg + '\n'

def ImprLtxCP2(self, &os):
    total = Total()
    if total>ppl_precio3(0.0):
        os.write(" & & " + StrTipo()
           + " & " + total.EnHumano() + ltx_fin_reg + '\n'

def ImprLtxCP2Porc(self, &os):
    if(size()<1) return
    const_iterator i
    for(i=begin(); i!=end(); i++)
        (*i).ImprLtxCP2(os)

def Total(self, ):
    ppl_precio3 retval(0.0)
    for(const_iterator i=begin(); i!=end(); i++)
        retval+= (*i).Total()
    return retval


