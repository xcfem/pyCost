//RegMedicion.cxx

#include "RegMedicion.h"
#include "boost/algorithm/string/trim.hpp"

const std::string &RegMedicion::Comentario(void) const
{
    return comentario;
}
const double &RegMedicion::Unidades(void) const
{
    return unidades;
}
const double &RegMedicion::Largo(void) const
{
    return largo;
}
const double &RegMedicion::Ancho(void) const
{
    return ancho;
}
const double &RegMedicion::Alto(void) const
{
    return alto;
}
ppl_dimension RegMedicion::UnidadesR(void) const
{
    return ppl_dimension(unidades);
}
ppl_dimension RegMedicion::LargoR(void) const
{
    return ppl_dimension(largo);
}
ppl_dimension RegMedicion::AnchoR(void) const
{
    return ppl_dimension(ancho);
}
ppl_dimension RegMedicion::AltoR(void) const
{
    return ppl_dimension(alto);
}


long double RegMedicion::Total(void) const
{
    if( (unidades==0.0) && (largo==0.0)
            && (ancho==0.0) && (alto==0.0))
        return 0.0;
    long double retval= 1.0;
    if(unidades!=0.0) retval*= unidades;
    if(largo!=0.0) retval*= largo;
    if(ancho!=0) retval*= ancho;
    if(alto!=0) retval*= alto;
    return retval;
}

ppl_dimension RegMedicion::TotalR(void) const
{
    if( (unidades==0.0) && (largo==0.0)
            && (ancho==0.0) && (alto==0.0))
        return ppl_dimension(0.0);
    ppl_dimension retval(1.0);
    ppl_dimension u= UnidadesR();
    ppl_dimension l= LargoR();
    ppl_dimension a= AnchoR();
    ppl_dimension h= AltoR();
    const ppl_dimension zero(0.0);
    if(u!=zero) retval*= u;
    if(l!=zero) retval*= l;
    if(a!=zero) retval*= a;
    if(h!=zero) retval*= h;
    return retval;
}

void RegMedicion::LeeBC3(const regBC3_linea_med &m)
{
    comentario= m.med.comentario;
    unidades= m.med.unidades;
    largo= m.med.largo;
    ancho= m.med.ancho;
    alto= m.med.alto;
}

void RegMedicion::EscribeBC3(std::ostream &os) const
{
    os << '\\' << comentario << '\\'
       << unidades << '\\'
       << largo << '\\'
       << ancho << '\\'
       << alto << '\\';
}

void RegMedicion::Escribe(std::ostream &os) const
{
    os << comentario << ','
       << unidades << ','
       << largo << ',' << ancho << ',' << alto << std::endl;
}

//! @brief Imprime la medición en Latex.
void RegMedicion::ImprLtx(std::ostream &os,const std::string ancho) const
{
    std::string str_u,str_l,str_a,str_alt,str_t;

    os << ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(comentario))) << ltx_ampsnd;
    const ppl_dimension zero(0.0);
    if(UnidadesR()!=zero) str_u= UnidadesR().EnHumano();
    if(LargoR()!=zero) str_l= LargoR().EnHumano();
    if(AnchoR()!=zero) str_a= AnchoR().EnHumano();
    if(AltoR()!=zero) str_alt= AltoR().EnHumano();
    ppl_dimension total= TotalR();
    if(total!=zero) str_t= total.EnHumano();
    os << str_u << ltx_ampsnd
       << str_l << ltx_ampsnd << str_a << ltx_ampsnd << str_alt << ltx_ampsnd
       << str_t;
}

void RegMedicion::EscribeHCalc(std::ostream &os) const
{
    os << '"' << comentario << '"' << tab;
    if(unidades!=0.0) os << unidades;
    os << tab;
    if(largo!=0.0) os << largo;
    os << tab;
    if(ancho!=0.0) os << ancho;
    os << tab;
    if(alto!=0.0) os << alto;
    os << tab;
    const double total= Total();
    if(total!=0.0) os << Total();
    os << std::endl;
}
