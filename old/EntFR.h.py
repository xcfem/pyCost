#EntFR.h

#ifndef ENTFR_H
#define ENTFR_H

#include "EntPpl.h"
#include "Tipos.h"

inline std.string rdto2str( long double &d)
    return num2str(d,13)


class EntFR: public EntPpl
#Entidad que tiene factor y rendimiento.
private:
    float factor
    double rendimiento
public:
    EntFR( float &f= 1.0, &r=0.0)
     float &Factor(void)
        return factor

    float &Factor(void)
        return factor

     double &Rendimiento(void)
        return rendimiento

    double &Rendimiento(void)
        return rendimiento

    double Producto(void)
    double ProductoR(void)
    void EscribeSpre(std.ostream &os)
    void EscribeBC3(std.ostream &os)


#endif
