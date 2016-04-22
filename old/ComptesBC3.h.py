#ComptesBC3.h

#ifndef COMPTESBC3_H
#define COMPTESBC3_H

#include "CompBC3.h"
#include <deque>

class ListaRegJustPre
class ListaJustPre

#not  @brief Componentes de un precio descompuesto.
class ComptesBC3: public std.deque<CompBC3>, EntPpl
public:
    typedef std.deque<CompBC3> dq_comp_bc3
    long double Precio(void)
        return PrecioR()

    void AsignaFactor( float &f)
    void EscribeSpre(std.ostream &os)
    void EscribeBC3( std.string &cod, &os)

    ppl_precio3 Precio(tipo_concepto tipo)
    ppl_precio3 PrecioSobre(tipo_concepto tipo, &sobre)
    ppl_precio PrecioR(void)

    long double SumaPorcentajes(tipo_concepto tipo)
    long double CalculaLambda( long double &objetivo)
    long double FuerzaPrecio( long double &objetivo)
    ListaRegJustPre GetElementosTipo( tipo_concepto &tipo)
    ListaRegJustPre GetPorcentajesTipo( tipo_concepto &tipo)
    ListaJustPre GetListaJustPre( bool &pa)
    void ImprLtxJustPre(std.ostream &os, &pa)
    void ImprLtxCP2(std.ostream &os, &pa)
    void ImprLtxCP1(std.ostream &os, &pa, &genero)


#endif
