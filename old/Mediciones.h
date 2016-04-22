//Mediciones.h
#ifndef MEDICIONES_H
#define MEDICIONES_H

#include "RegMedicion.h"

//! @brief Mediciones de una unidad de obra
class Mediciones: public std::deque<RegMedicion>, public EntPpl
{
public:
    typedef std::deque<RegMedicion> dq_reg_med;

    double TotalUnidades(void) const;
    double TotalLargo(void) const;
    double TotalAncho(void) const;
    double TotalAlto(void) const;
    long double Total(void) const;
    ppl_dimension TotalR(void) const;

    void LeeBC3(const regBC3_lista_med &m);
    void EscribeBC3(std::ostream &os) const;
    void ImprCompLtx(std::ostream &os,const Mediciones &otra) const;
    void ImprCompLtx(std::ostream &os) const;
    void ImprLtx(std::ostream &os) const;
    void EscribeHCalc(std::ostream &os) const;
};

#endif
