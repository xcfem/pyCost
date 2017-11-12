#CompBC3.h

#ifndef COMPBC3_H
#define COMPBC3_H

#include "EntFR.h"
#include "EntBC3.h"

class RegJustPre

#not  Componente de una descomposición
class CompBC3: public EntFR
private:
    EntBC3  *ent; #Entidad a la que se refiere.
     EntBC3 &Entidad(void)
public:
    CompBC3(void)
    CompBC3( EntBC3 &e, &fr)
    CompBC3( EntBC3 &e, &f, &r)
    long double Precio(void)
    virtual ppl_precio3 PrecioR(void)
    std.string StrPrecioLtx(void)
    ppl_precio3 PrecioSobre( ppl_precio3 &sobre)
    std.string StrPrecioSobreLtx( ppl_precio3 &sobre)
    virtual tipo_concepto Tipo(void)
     std.string &CodigoEntidad(void)
    bool EsPorcentaje(void)
    void EscribeSpre(std.ostream &os)
    void EscribeBC3(std.ostream &os)
    RegJustPre GetRegJustPre( ppl_precio3 &sobre= 0.0)
    ppl_precio3 ImprLtxJustPre(std.ostream &os, &sobre= 0.0)
    ppl_precio3 ImprLtxCP2(std.ostream &os, &sobre= 0.0)


#endif
