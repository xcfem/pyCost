#ListaRegJustPre.hxx

#ifndef LISTAREGJUSTPRE_HXX
#define LISTAREGJUSTPRE_HXX

import RegJustPre
#include <deque>
import ../EntBC3

class ListaRegJustPre(std.deque<RegJustPre>, EntCmd):
    tipo_concepto tipo
public:
    ListaRegJustPre( tipo_concepto &tp)
        : tipo(tp) {
    void SetBase( ppl_precio3 &b)
    void SetBaseAcum( ppl_precio3 &b)
    ppl_precio3 Total(void)
    std.string StrTipo(void)
        switch(tipo)
        case mdo:
            return "mano de obra"
        case mat:
            return "materiales"
        case maq:
            return "maquinaria"
        default:
            return "porcentajes"


    void ImprLtxJust(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void ImprLtxCP2Porc(std.ostream &os)


#endif
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


