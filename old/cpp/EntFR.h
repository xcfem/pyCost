//EntFR.h

#ifndef ENTFR_H
#define ENTFR_H

#include "EntPpl.h"
#include "Tipos.h"

inline std::string rdto2str(const long double &d)
{
    return num2str(d,13);
}

class EntFR: public EntPpl
//Entidad que tiene factor y rendimiento.
{
private:
    float factor;
    double rendimiento;
public:
    EntFR(const float &f= 1.0,const double &r=0.0);
    const float &Factor(void) const
    {
        return factor;
    }
    float &Factor(void)
    {
        return factor;
    }
    const double &Rendimiento(void) const
    {
        return rendimiento;
    }
    double &Rendimiento(void)
    {
        return rendimiento;
    }
    double Producto(void) const;
    double ProductoR(void) const;
    void EscribeSpre(std::ostream &os) const;
    void EscribeBC3(std::ostream &os) const;
};

#endif
