//EntFR.cxx

#include "EntFR.h"

EntFR::EntFR(const float &f,const double &r)
    :factor(f),rendimiento(r) {}

double EntFR::Producto(void) const
{
    return factor*rendimiento;
}
double EntFR::ProductoR(void) const
{
    return ppl_precio4(factor*rendimiento);
}
void EntFR::EscribeSpre(std::ostream &os) const
{
    os << rdto2str(Producto()) << '|';
}
void EntFR::EscribeBC3(std::ostream &os) const
{
    os << factor << '\\' << rdto2str(rendimiento) << '\\';
}

