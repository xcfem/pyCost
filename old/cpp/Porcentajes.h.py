#Porcentajes.h

#ifndef PORCENTAJES_H
#define PORCENTAJES_H

#include "EntPpl.h"
#include "Tipos.h"

class Porcentajes: public EntPpl
    float gg; #Gastos generales.
    float bi; #Beneficio industrial.
    float iva; #Impuesto sobre el valor añadido.
    inline static ppl_precio AplicaPorcentaje( ppl_precio &p, &pc)
         ppl_porcentaje temp2(pc)
        ppl_precio temp3(p)
        temp3*=temp2
        return temp3

    inline ppl_precio GGenerales( ppl_precio &p)
        return AplicaPorcentaje(p,gg)

    inline ppl_precio BIndustrial( ppl_precio &p)
        return AplicaPorcentaje(p,bi)

    inline ppl_precio IVA( ppl_precio &p)
        return AplicaPorcentaje(p,iva)

public:
    Porcentajes( float &g= .17, &b=.06, i=.16)
        : gg(g), bi(b), iva(i) {
    void ImprLtx(std.ostream &os, &precio_ejec_mat)


#endif
