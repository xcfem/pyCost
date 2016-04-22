//InformeUdObra.h

#ifndef INFORMEUDOBRA_H
#define INFORMEUDOBRA_H

#include "Medible.h"

class InformeUdObra
{
    Medible const *ud;
    long double med_total;
public:
    InformeUdObra(Medible const *u,const long double &mt)
        : ud(u), med_total(mt) {}
    Medible const *Unidad(void) const
    {
        return ud;
    }
    const long double &Medicion(void) const
    {
        return med_total;
    }
    void ImprLtx(std::ostream &os) const;
};

#endif
