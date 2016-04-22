//RegBC3.cxx

#include "RegBC3.h"

regBC3_c RegBC3::GetConcepto(void) const
{
    return regBC3_c(c);
}

regBC3_t RegBC3::GetTexto(void) const
{
    return regBC3_t(t);
}

regBC3_d RegBC3::GetDesc(void) const
{
    return regBC3_d(d+y);
}

regBC3_m RegBC3::GetMed(void) const
{
    return regBC3_m(m);
}

bool RegBC3::EsElemento(void) const
{
    return ((d.length()==0) && (y.length()== 0) && (m.length()==0));
}

bool RegBC3::EsMedicion(void) const
{
    return (m.size()!=0);
}

//! @brief Devuelve verdadero si el concepto corresponde a una obra.
bool RegBC3::EsObra(void) const
{
    return es_codigo_obra(c);
}

//! @brief Devuelve verdadero si el concepto corresponde a un capitulo.
bool RegBC3::EsCapitulo(void) const
{
    return es_codigo_capitulo(c);
}

regBC3_capitulo RegBC3::GetDatosCapitulo(void) const
{
    return regBC3_capitulo(GetConcepto(),GetTexto(),GetDesc());
}

std::ostream &operator<<(std::ostream &os,const RegBC3 &r)
{
    os << "C: " << r.c << ' ' << r.c.size() << std::endl
       << "D: " << r.d << ' ' << r.d.size() << std::endl
       << "M: " << r.m << ' ' << r.m.size() << std::endl
       << "T: " << r.t << ' ' << r.t.size() << std::endl
       << "Y: " << r.y << ' ' << r.y.size() << std::endl;
    return os;
}
