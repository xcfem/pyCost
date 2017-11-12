//UdObra.cxx

#include "UdObra.h"
#include "bibXCBasica/src/texto/en_letra.h"

//! @brief Para unidades de obra sin descomposición de las que
//! sólo se conoce el precio.
ComptesBC3 UdObra::GetSindesco(const double &rendimiento,Buscadores &bp) const
{
    ComptesBC3 retval;
    BuscadorPtros *be= bp["elementos"];
    const EntBC3 &ent= *(const Elemento *)be->Busca("SINDESCO");
    retval.push_back(CompBC3(ent,1.0,rendimiento));
    return retval;
}

//! @brief Obtiene los punteros a los precios de la descomposición.
ComptesBC3 UdObra::ObtienePunteros(const regBC3_d &descBC3,Buscadores &bp,bool &error)
{
    ComptesBC3 retval;
    BuscadorPtros *be= bp["elementos"];
    BuscadorPtros *bd= bp["ud_obra"];
    const EntBC3 *ent= NULL;
    regBC3_d::const_iterator i= descBC3.begin();
    for(; i!=descBC3.end(); i++)
    {
        ent= static_cast<const EntBC3 *>(be->Busca((*i).codigo));
        if(!ent)
            ent= static_cast<const EntBC3 *>(bd->Busca((*i).codigo));
        if(!ent)
        {
            if(verborrea>6) //Puede no ser un error.
                std::cerr << "UdObra::ObtienePunteros; No se encontró la componente: " << (*i).codigo << std::endl;
            error= true;
            continue;
        }
        else
        {
            retval.push_back(CompBC3(*ent,(*i).factor,(*i).rendimiento));
            error= false;
        }
    }
    return retval;
}
bool UdObra::LeeBC3Fase2(const Codigos::reg_udobra &r,Buscadores &bp)
{
    bool error= false;
    if(r.Datos().desc.size())
    {
        ComptesBC3 tmp= ObtienePunteros(r.Datos().desc,bp,error);
        if(!error)
            lista= tmp;
        else
            std::cerr << "Error al leer descomposición de la unidad: " << Codigo() << std::endl;
    }
    else
        lista= GetSindesco(r.Datos().Precio(),bp);
    return error;
}

void UdObra::EscribeSpre(std::ostream &os) const
{
    os << Codigo() << '|'
       << Unidad() << '|'
       << Titulo() << '|';
    lista.EscribeSpre(os);
}

void UdObra::EscribeBC3(std::ostream &os) const
{
    Medible::EscribeBC3(os);
    lista.EscribeBC3(Codigo(),os);
}

//! @brief Toma la descomposición de otra unidad de obra.
//! sin alterar el precio de ésta.
long double UdObra::SimulaDescomp(const UdObra &otra)
{
    const long double objetivo= Precio();
    lista= otra.lista;
    return lista.FuerzaPrecio(objetivo);
}

void UdObra::ImprLtxJustPre(std::ostream &os) const
{
    os << "\\begin{tabular}{l r l p{4cm} r r}" << std::endl;
    //Cabecera
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ltx_multicolumn(ltx_datos_multicolumn("4","p{7cm}",ascii2latex(TextoLargo()))) << ltx_fin_reg << std::endl;
    os << "Código & Rdto. & Ud. & Descripción & Unit. & Total"
       << ltx_fin_reg << std::endl << ltx_hline << std::endl;
    //Descomposición
    lista.ImprLtxJustPre(os,true); //XXX Aqui porcentajes acumulados.
    os << "\\end{tabular}" << std::endl;
}
void UdObra::ImprLtxCP1(std::ostream &os) const
{
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(TextoLargo()) << " & ";
    lista.ImprLtxCP1(os,true,false); //XXX Aqui género.
    os << "\\\\" << std::endl;
}
void UdObra::ImprLtxCP2(std::ostream &os) const
{
    os << "\\begin{tabular}{l r p{5.5cm} r}" << std::endl;
    //Cabecera
    os << "Código & Ud. & Descripción & Importe"
       << ltx_fin_reg << std::endl << ltx_hline << std::endl;
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(TextoLargo()) << " & " << ltx_fin_reg << std::endl << ltx_fin_reg << std::endl;
    //Descomposición
    lista.ImprLtxCP2(os,true); //XXX Aqui porcentajes acumulados.
    os << "\\end{tabular}" << std::endl;
}
void UdObra::EscribeHCalc(std::ostream &os) const
{
    os << Codigo() << tab
       << ascii2latex(Unidad()) << tab
       << '"' << ascii2latex(TextoLargo()) << '"' << tab
       << '"' << StrPrecioEnLetra(true) << '"' << tab
       << StrPrecio() << std::endl;
}

