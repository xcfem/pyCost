//Elemento.cxx

#include "Elemento.h"

Elemento::Elemento(const std::string &cod,const std::string &tit,
                   const std::string &ud, const long double &p,const tipo_concepto &tp)
    : Medible(cod,tit,ud), precio(p), tipo(tp) {}

void Elemento::check_tipo(void) const
{
    if(!Codigo().empty())
        if(tipo==sin_clasif && !EsPorcentaje())
            std::cerr << "El precio elemental de código: " << Codigo()
                      << " no es un porcentaje y su tipo está sin clasificar." << std::endl;
}

tipo_concepto Elemento::Tipo(void) const
{
    return tipo;
}
long double Elemento::Precio(void) const
{
    return precio;
}
void Elemento::LeeBC3(const Codigos::reg_elemento &r)
{
    Medible::LeeBC3(r);
    precio= r.Datos().Precio();
    tipo= sint2tipo_concepto(r.Datos().Tipo());
}

void Elemento::ImprLtx(std::ostream &os) const
{
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(Titulo()) << " & "
       << StrPrecioLtx() << "\\\\" << std::endl;
}
