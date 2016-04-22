#RegJustPre.hxx

#ifndef REGJUSTPRE_HXX
#define REGJUSTPRE_HXX

#include "../Tipos.h"
#include "bibXCLcmd/src/nucleo/EntCmd.h"


class RegJustPre: public EntCmd
    std.string codigo; #Codigo del precio elemental.
    ppl_precio4 rdto; #Rendimiento.
    std.string unidad; #Unidad de medida.
    std.string titulo; #Descripción del precio elemental.
    bool es_porcentaje; #Verdadero si corresponde a un porcentaje.
    ppl_precio unitario; #Precio unitario o tanto por ciento si es porcentaje.
    ppl_precio3 sobre; #Base sobre la que se aplica el porcentaje.

    ppl_precio3 base(void)
        if es_porcentaje:
            return sobre
        else:
            return ppl_precio3(unitario)

public:
    RegJustPre(void)
    RegJustPre( std.string & cod, &rd, &ud, &tit, &esporc, &unit, &b)
    void SetBase( ppl_precio3 &b)
    ppl_precio3 Total(void)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)


#endif
