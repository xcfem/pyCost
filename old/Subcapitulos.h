//Subcapitulos.h

#ifndef SUBCAPITULOS_H
#define SUBCAPITULOS_H

#include "Descompuestos.h"

class Capitulo;
class CodigosObra;

class Subcapitulos: public std::deque<Capitulo>, public EntPpl
{
public:
    typedef std::deque<Capitulo> dq_cap;
    Subcapitulos(Capitulo &ptr_cap);
    long double Precio(void) const;
    ppl_precio PrecioR(void) const;
    Capitulo *Busca(regBC3_ruta &ruta);
    const Capitulo *BuscaCodigo(const std::string &nmb) const;
    Capitulo *BuscaCodigo(const std::string &nmb);
    size_t NumDescompuestos(void) const;
    const Medible *BuscaPrecio(const std::string &cod) const;

    const Capitulo *getContenedor(void) const;

    void AgregaCapitulo(const Capitulo &c);
    void AgregaCapitulo(const regBC3_desc &r);
    void AgregaCapitulos(const regBC3_d &descomp);

    void LeeBC3Caps(CodigosObra &co);
    void EscribePreciosBC3(std::ostream &os) const;
    void EscribeDescompBC3(std::ostream &os,const std::string &cod) const;
    void EscribeBC3(std::ostream &os,bool primero= "false",const std::string &pos="") const;

    void ImprCompLtxMed(std::ostream &os,const std::string &sect,const Subcapitulos &otro) const;
    void ImprLtxMed(std::ostream &os,const std::string &sect) const;
    void ImprLtxCP1(std::ostream &os,const std::string &sect) const;
    void ImprLtxCP2(std::ostream &os,const std::string &sect) const;
    void ImprLtxJustPre(std::ostream &os,const std::string &sect) const;
    void ImprLtxResumen(std::ostream &os,const std::string &sect,bool recurre= true) const;
    void ImprCompLtxPre(std::ostream &os,const std::string &sect,const Subcapitulos &otro) const;
    void ImprLtxPre(std::ostream &os,const std::string &sect) const;
    void EscribeHCalcMed(std::ostream &os,const std::string &sect) const;
    void EscribeHCalcPre(std::ostream &os,const std::string &sect) const;
    InformeMediciones GetInformeMediciones(void) const;
};

#endif
