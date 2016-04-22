//Porcentajes.h

#ifndef PORCENTAJES_H
#define PORCENTAJES_H

#include "EntPpl.h"
#include "Tipos.h"

class Porcentajes: public EntPpl
{
    float gg; //Gastos generales.
    float bi; //Beneficio industrial.
    float iva; //Impuesto sobre el valor añadido.
    inline static ppl_precio AplicaPorcentaje(const ppl_precio &p, const float &pc)
    {
        const ppl_porcentaje temp2(pc);
        ppl_precio temp3(p);
        temp3*=temp2;
        return temp3;
    }
    inline ppl_precio GGenerales(const ppl_precio &p) const
    {
        return AplicaPorcentaje(p,gg);
    }
    inline ppl_precio BIndustrial(const ppl_precio &p) const
    {
        return AplicaPorcentaje(p,bi);
    }
    inline ppl_precio IVA(const ppl_precio &p) const
    {
        return AplicaPorcentaje(p,iva);
    }
public:
    Porcentajes(const float &g= .17,const float &b=.06,const float i=.16)
        : gg(g), bi(b), iva(i) {}
    void ImprLtx(std::ostream &os,const ppl_precio &precio_ejec_mat) const;
};

#endif
