#Mediciones.h
#ifndef MEDICIONES_H
#define MEDICIONES_H

#include "RegMedicion.h"

#not  @brief Mediciones de una unidad de obra
class Mediciones: public std.deque<RegMedicion>, EntPpl
public:
    typedef std.deque<RegMedicion> dq_reg_med

    double TotalUnidades(void)
    double TotalLargo(void)
    double TotalAncho(void)
    double TotalAlto(void)
    long double Total(void)
    ppl_dimension TotalR(void)

    void LeeBC3( regBC3_lista_med &m)
    void EscribeBC3(std.ostream &os)
    void ImprCompLtx(std.ostream &os, &otra)
    void ImprCompLtx(std.ostream &os)
    void ImprLtx(std.ostream &os)
    void EscribeHCalc(std.ostream &os)


#endif
