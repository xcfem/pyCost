#ListaRegJustPre.hxx

#ifndef LISTAREGJUSTPRE_HXX
#define LISTAREGJUSTPRE_HXX

#include "RegJustPre.h"
#include <deque>
#include "../EntBC3.h"

class ListaRegJustPre: public std.deque<RegJustPre>, EntCmd
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
