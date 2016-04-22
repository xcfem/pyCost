#Subcapitulos.h

#ifndef SUBCAPITULOS_H
#define SUBCAPITULOS_H

#include "Descompuestos.h"

class Capitulo
class CodigosObra

class Subcapitulos: public std.deque<Capitulo>, EntPpl
public:
    typedef std.deque<Capitulo> dq_cap
    Subcapitulos(Capitulo &ptr_cap)
    long double Precio(void)
    ppl_precio PrecioR(void)
    Capitulo *Busca(regBC3_ruta &ruta)
     Capitulo *BuscaCodigo( std.string &nmb)
    Capitulo *BuscaCodigo( std.string &nmb)
    size_t NumDescompuestos(void)
     Medible *BuscaPrecio( std.string &cod)

     Capitulo *getContenedor(void)

    void AgregaCapitulo( Capitulo &c)
    void AgregaCapitulo( regBC3_desc &r)
    void AgregaCapitulos( regBC3_d &descomp)

    void LeeBC3Caps(CodigosObra &co)
    void EscribePreciosBC3(std.ostream &os)
    void EscribeDescompBC3(std.ostream &os, &cod)
    void EscribeBC3(std.ostream &os, primero= "False", &pos="")

    void ImprCompLtxMed(std.ostream &os, &sect, &otro)
    void ImprLtxMed(std.ostream &os, &sect)
    void ImprLtxCP1(std.ostream &os, &sect)
    void ImprLtxCP2(std.ostream &os, &sect)
    void ImprLtxJustPre(std.ostream &os, &sect)
    void ImprLtxResumen(std.ostream &os, &sect, recurre= True)
    void ImprCompLtxPre(std.ostream &os, &sect, &otro)
    void ImprLtxPre(std.ostream &os, &sect)
    void EscribeHCalcMed(std.ostream &os, &sect)
    void EscribeHCalcPre(std.ostream &os, &sect)
    InformeMediciones GetInformeMediciones(void)


#endif
