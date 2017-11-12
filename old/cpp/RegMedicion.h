//RegMedicion.h
#ifndef REG_MEDICION_H
#define REG_MEDICION_H

#include "UdObra.h"
#include "Tipos.h"

class RegMedicion: public EntPpl
{
    std::string comentario;
    double unidades;
    double largo;
    double ancho;
    double alto;
public:
    RegMedicion( const std::string &c= "",const double &uds= 0.0,
                 const double &l= 0.0,const double &an= 0.0,
                 const double &al= 0.0)
        :comentario(c),unidades(uds),largo(l),ancho(an),alto(al) {}

    const std::string &Comentario(void) const;
    const double &Unidades(void) const;
    const double &Largo(void) const;
    const double &Ancho(void) const;
    const double &Alto(void) const;
    ppl_dimension UnidadesR(void) const;
    ppl_dimension LargoR(void) const;
    ppl_dimension AnchoR(void) const;
    ppl_dimension AltoR(void) const;
    long double Total(void) const;
    ppl_dimension TotalR(void) const;

    void LeeBC3(const regBC3_linea_med &m);
    void EscribeBC3(std::ostream &os) const;
    void Escribe(std::ostream &os) const;
    void ImprLtx(std::ostream &os,const std::string ancho) const;
    void EscribeHCalc(std::ostream &os) const;
};

#endif
