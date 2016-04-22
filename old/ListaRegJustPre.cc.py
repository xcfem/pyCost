#ListaRegJustPre.cc

#include "ListaRegJustPre.h"
#include "bibXCBasica/src/texto/latex.h"


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
    os << ltx_multicolumn(ltx_datos_multicolumn("4","r","Total "+StrTipo()))
       << " & & " << Total().EnHumano() << ltx_fin_reg << std.endl << ltx_fin_reg << std.endl

def ImprLtxCP2(self, &os):
    total = Total()
    if total>ppl_precio3(0.0):
        os << " & & " << StrTipo()
           << " & " << total.EnHumano() << ltx_fin_reg << std.endl

def ImprLtxCP2Porc(self, &os):
    if(size()<1) return
    const_iterator i
    for(i=begin(); i!=end(); i++)
        (*i).ImprLtxCP2(os)

def Total(self, void):
    ppl_precio3 retval(0.0)
    for(const_iterator i=begin(); i!=end(); i++)
        retval+= (*i).Total()
    return retval


