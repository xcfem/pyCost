//CompBC3.cxx

#include "CompBC3.h"
#include "bibXCLcmd/src/base/Buscadores.hxx"
#include "bibXCBasica/src/texto/StrTok.h"
#include "bibXCBasica/src/texto/latex.h"
#include "just_pre/RegJustPre.h"

CompBC3::CompBC3(void)
    : EntFR(),ent(NULL) {}
CompBC3::CompBC3(const EntBC3 &e,const EntFR &fr)
    : EntFR(fr),ent(&e) {}
CompBC3::CompBC3(const EntBC3 &e,const float &f,const float &r)
    : EntFR(f,r),ent(&e) {}
long double CompBC3::Precio(void) const
{
    return Entidad().Precio()*Producto();
}
ppl_precio3 CompBC3::PrecioR(void) const
{
    ppl_precio3 retval(Entidad().PrecioR());
    retval*= ProductoR();
    return retval;
}
std::string CompBC3::StrPrecioLtx(void) const
{
    return PrecioR().EnHumano();
}

//Para porcentajes.
ppl_precio3 CompBC3::PrecioSobre(const ppl_precio3 &sobre) const
{
    ppl_precio3 d(sobre);
    d*= Producto();
    return d;
}

//Para porcentajes.
std::string CompBC3::StrPrecioSobreLtx(const ppl_precio3 &sobre) const
{
    return PrecioSobre(sobre).EnHumano();
}

tipo_concepto CompBC3::Tipo(void) const
{
    return Entidad().Tipo();
}

const std::string &CompBC3::CodigoEntidad(void) const
{
    return Entidad().Codigo();
}

bool CompBC3::EsPorcentaje(void) const
{
    return Entidad().EsPorcentaje();
}

void CompBC3::EscribeSpre(std::ostream &os) const
{
    if(!((CodigoEntidad()).find('%')))
        os << 0 << '|'
           << CodigoEntidad() << '|';
    EntFR::EscribeSpre(os);
}
void CompBC3::EscribeBC3(std::ostream &os) const
{
    os << Entidad().CodigoBC3() << '\\';
    EntFR::EscribeBC3(os);
}

const EntBC3 &CompBC3::Entidad(void) const
{
    if(ent)
        return *ent;
    else
    {
        std::cerr << "La componente no se refiere a ninguna entidad" << std::endl;
        exit(1);
    }
}

RegJustPre CompBC3::GetRegJustPre(const ppl_precio3 &sobre) const
{
    if(EsPorcentaje())
        return RegJustPre(CodigoEntidad(),ppl_precio4(Producto()),Entidad().Unidad(),Entidad().Titulo(),true,ppl_precio(Producto()*100.0),sobre);
    else
        return RegJustPre(Entidad().Codigo(),ppl_precio4(Producto()),Entidad().Unidad(),Entidad().Titulo(),false,Entidad().PrecioR(),0.0);
}

ppl_precio3 CompBC3::ImprLtxJustPre(std::ostream &os,const ppl_precio3 &sobre) const
{
    RegJustPre r(GetRegJustPre(sobre));
    r.ImprLtxJustPre(os);
    return r.Total();
}

ppl_precio3 CompBC3::ImprLtxCP2(std::ostream &os,const ppl_precio3 &sobre) const
{
    RegJustPre r(GetRegJustPre(sobre));
    r.ImprLtxCP2(os);
    return r.Total();
}

