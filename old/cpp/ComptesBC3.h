//ComptesBC3.h

#ifndef COMPTESBC3_H
#define COMPTESBC3_H

#include "CompBC3.h"
#include <deque>

class ListaRegJustPre;
class ListaJustPre;

//! @brief Componentes de un precio descompuesto.
class ComptesBC3: public std::deque<CompBC3>, public EntPpl
{
public:
    typedef std::deque<CompBC3> dq_comp_bc3;
    long double Precio(void) const
    {
        return PrecioR();
    }
    void AsignaFactor(const float &f);
    void EscribeSpre(std::ostream &os) const;
    void EscribeBC3(const std::string &cod,std::ostream &os) const;

    ppl_precio3 Precio(tipo_concepto tipo) const;
    ppl_precio3 PrecioSobre(tipo_concepto tipo,const ppl_precio3 &sobre) const;
    ppl_precio PrecioR(void) const;

    long double SumaPorcentajes(tipo_concepto tipo) const;
    long double CalculaLambda(const long double &objetivo) const;
    long double FuerzaPrecio(const long double &objetivo);
    ListaRegJustPre GetElementosTipo(const tipo_concepto &tipo) const;
    ListaRegJustPre GetPorcentajesTipo(const tipo_concepto &tipo) const;
    ListaJustPre GetListaJustPre(const bool &pa) const;
    void ImprLtxJustPre(std::ostream &os,const bool &pa) const;
    void ImprLtxCP2(std::ostream &os,const bool &pa) const;
    void ImprLtxCP1(std::ostream &os,const bool &pa,const bool &genero) const;
};

#endif
