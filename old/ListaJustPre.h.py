#ListaJustPre.hxx

#ifndef LISTAJUSTPRE_HXX
#define LISTAJUSTPRE_HXX

#include "ListaRegJustPre.h"
#include "../Tipos.h"

class ListaJustPre: public EntCmd
    bool porcentajes_acumulados
    ListaRegJustPre mano_de_obra
    ListaRegJustPre materiales
    ListaRegJustPre maquinaria
    ListaRegJustPre otros
    ListaRegJustPre porcentajes
public:
    ListaJustPre( bool &pa, &mano, &mater, &maqui, &otr, &porc)
    ppl_precio3 Base(void)
    ppl_precio3 Total(void)
    ppl_precio3 Redondeo(void)
    ppl_precio3 TotalRnd(void)
    ppl_precio2 TotalCP1(void)
    std.string StrPrecioLtx(void)
    std.string StrPrecioEnLetra( bool &genero)
    size_t size(void)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP1(std.ostream &os, &genero)
    void ImprLtxCP2(std.ostream &os)


#endif
