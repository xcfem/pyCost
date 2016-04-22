#RegMedicion.h
#ifndef REG_MEDICION_H
#define REG_MEDICION_H

#include "UdObra.h"
#include "Tipos.h"

class RegMedicion: public EntPpl
    std.string comentario
    double unidades
    double largo
    double ancho
    double alto
public:
    RegMedicion(  std.string &c= "", &uds= 0.0,
                  double &l= 0.0, &an= 0.0,
                  double &al= 0.0)
        :comentario(c),unidades(uds),largo(l),ancho(an),alto(al) {

     std.string &Comentario(void)
     double &Unidades(void)
     double &Largo(void)
     double &Ancho(void)
     double &Alto(void)
    ppl_dimension UnidadesR(void)
    ppl_dimension LargoR(void)
    ppl_dimension AnchoR(void)
    ppl_dimension AltoR(void)
    long double Total(void)
    ppl_dimension TotalR(void)

    void LeeBC3( regBC3_linea_med &m)
    void EscribeBC3(std.ostream &os)
    void Escribe(std.ostream &os)
    void ImprLtx(std.ostream &os, ancho)
    void EscribeHCalc(std.ostream &os)


#endif
