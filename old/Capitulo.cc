//Capitulo.cxx

#include "Capitulo.h"
#include "Subcapitulos.h"
#include "Descompuestos.h"

Capitulo::Capitulo(const std::string &cod,const std::string &tit, const float &factor,const float &rendimiento)
    : EntBC3(cod,tit), fr(factor,rendimiento), subcapitulos(*this) {}

Capitulo::Capitulo(const Capitulo &otro)
    : EntBC3(otro), fr(otro.fr), mediciones(otro.mediciones), subcapitulos(otro.subcapitulos)
{
    subcapitulos.set_owner(this);
}

Capitulo &Capitulo::operator=(const Capitulo &otro)
{
    EntBC3::operator=(otro);
    fr= otro.fr;
    mediciones= otro.mediciones;
    subcapitulos= otro.subcapitulos;
    return *this;
}

std::string Capitulo::CodigoBC3(void) const
{
    return EntBC3::CodigoBC3() + "#";
}

const CuaPre &Capitulo::CuadroPrecios(void) const
{
    return precios;
}

CuaPre &Capitulo::CuadroPrecios(void)
{
    return precios;
}

void Capitulo::AgregaPartida(const Partida &m)
{
    mediciones.push_back(m);
}

//! @brief Devuelve el capítulo como componente.
CompBC3 Capitulo::GetCompBC3(void) const
{
    return CompBC3(*this,fr);
}

//! @brief Agrega los precios elementales que se pasan como parámetro
void Capitulo::LeeBC3Elementales(const Codigos &elementos)
{
    precios.LeeBC3Elementales(elementos);
}
void Capitulo::LeeBC3DescompFase1(const Codigos &descompuestos)
{
    precios.LeeBC3DescompFase1(descompuestos);
}
Descompuestos::set_pendientes Capitulo::LeeBC3DescompFase2(const Codigos &descompuestos)
{
    return precios.LeeBC3DescompFase2(descompuestos);
}

Capitulo *Capitulo::BuscaSubcapitulo(regBC3_ruta &ruta)
{
    Capitulo *retval= NULL;
    if(!ruta.empty())
    {
        retval= subcapitulos.Busca(ruta);
        if(!retval)
        {
            std::cerr << "Capitulo::BuscaSubcapitulo: no se encontró el subcapítulo: " << ruta[1]
                      << " en el capítulo: " << Codigo() << " (" << Titulo()
                      << ") (ruta: " << ruta << ')' << std::endl;
            //Si no encuentra el capítulo devuelve este mismo
            retval= this;
        }
    }
    return retval;
}

//! @brief Busca el subcapítulo que indica la cadena
//! de caracteres que se pasa como parámetro.
//! ésta es una cadena de la forma '1\2\1\4'
Capitulo *Capitulo::BuscaSubcapitulo(const std::string &lst)
{
    Capitulo *retval= NULL;
    size_t pos= lst.find('\\');
    if(pos>lst.length()) //No aparece la barra luego ha de ser subcapitulo de éste.
    {
        size_t indice= atoi(lst.c_str());
        if(indice>subcapitulos.size())
        {
            std::cerr << "Capítulo: " << indice << " no encontrado." << std::endl;
            return NULL;
        }
        retval= &subcapitulos[indice-1];
        return retval;
    }
    else //Ha de ser subcapitulo del que esta a la izquierda de la barra
    {
        std::string ind= lst.substr(0,pos);
        size_t indice = atoi(ind.c_str());
        if(indice>subcapitulos.size())
        {
            std::cerr << "Capítulo: " << indice << " no encontrado." << std::endl;
            return NULL;
        }
        return subcapitulos[indice-1].BuscaSubcapitulo(lst.substr(pos+1,lst.size()-1));
    }
    std::cerr << "sale por aqui (y no debiera) en el capitulo: " << Codigo() << std::endl;
    return retval;
}
const Capitulo *Capitulo::BuscaCodigo(const std::string &nmb) const
{
    if((Codigo()==nmb) || ((Codigo()+'#')==nmb))
        return this;
    else
        return subcapitulos.BuscaCodigo(nmb);
}
Capitulo *Capitulo::BuscaCodigo(const std::string &nmb)
{
    if(Codigo()==nmb)
        return this;
    else
        return subcapitulos.BuscaCodigo(nmb);
}
const Medible *Capitulo::BuscaPrecio(const std::string &cod) const
{
    const Medible *retval= precios.BuscaPrecio(cod);
    if(!retval)
        retval= subcapitulos.BuscaPrecio(cod);
    return retval;
}

void Capitulo::EscribePreciosBC3(std::ostream &os) const
{
    precios.EscribeBC3(os);
    subcapitulos.EscribePreciosBC3(os);
}
void Capitulo::EscribeDescompBC3(std::ostream &os) const
{
    subcapitulos.EscribeDescompBC3(os,CodigoBC3());
    mediciones.EscribeDescompBC3(os,CodigoBC3());
}
void Capitulo::EscribeBC3(std::ostream &os,bool primero,const std::string pos) const
{
    EscribeConceptoBC3(os,primero);
    EscribeDescompBC3(os);
    EscribeMediciones(os,pos);
    EscribeSubCapitulos(os,false,pos);
}

long double Capitulo::Precio(void) const
{
    return (subcapitulos.Precio() + mediciones.Precio()) * fr.Producto();
}

ppl_precio Capitulo::PrecioR(void) const
{
    ppl_precio retval= subcapitulos.PrecioR() + mediciones.PrecioR();
    retval*= fr.Producto();
    return retval;
}

//Devuelve la sección pasándole la del padre.
std::string Capitulo::SectionLtx(const std::string &sect)
{
    if(sect == "raiz")
        return "chapter";
    else if(sect == "chapter")
        return "section";
    else if(sect == "section")
        return "subsection";
    else if(sect == "subsection")
        return "subsubsection";
    else if(sect == "subsubsection")
        return "paragraph";
    else if(sect == "paragraph")
        return "subparagraph";
    else
        return "xxx";
}

void Capitulo::ImprCompLtxMed(std::ostream &os,const std::string &sect,const Capitulo &otro) const
{
    if(sect!="raiz")
        os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
    mediciones.ImprCompLtxMed(os, otro.mediciones);
    std::cerr << "aqui 1: " << Titulo() << ' ' << subcapitulos.size() << " subcapítulos" << std::endl;
    std::cerr << "aqui 2: " << otro.Titulo() << ' ' << otro.subcapitulos.size() << " subcapítulos" << std::endl;
    subcapitulos.ImprCompLtxMed(os,SectionLtx(sect), otro.subcapitulos);
}
void Capitulo::ImprLtxMed(std::ostream &os,const std::string &sect) const
{
    if(sect!="raiz")
        os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
    mediciones.ImprLtxMed(os);
    if(mediciones.size())
        os << "\\newpage" << std::endl;
    subcapitulos.ImprLtxMed(os,SectionLtx(sect));
}
void Capitulo::ImprLtxCP1(std::ostream &os,const std::string &sect) const
{
    if(!TieneDescompuestos()) return;
    if(sect!="raiz")
        os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
    if(precios.TieneDescompuestos()) precios.ImprLtxCP1(os);
    subcapitulos.ImprLtxCP1(os,SectionLtx(sect));
}
void Capitulo::ImprLtxCP2(std::ostream &os,const std::string &sect) const
{
    if(precios.TieneDescompuestos())
    {
        if(sect!="raiz")
            os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
        precios.ImprLtxCP2(os);
    }
    subcapitulos.ImprLtxCP2(os,SectionLtx(sect));
}
void Capitulo::ImprLtxJustPre(std::ostream &os,const std::string &sect) const
{
    if(sect!="raiz")
        os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
    if(precios.TieneDescompuestos()) precios.ImprLtxJustPre(os);
    subcapitulos.ImprLtxJustPre(os,SectionLtx(sect));
}
void Capitulo::ImprLtxResumen(std::ostream &os,const std::string &sect,bool recurre) const
{
    if(sect!="raiz")
        os << "\\item " << Titulo() << " \\dotfill\\ "
           << StrPrecioLtx() << std::endl;
    else
        os << "\\Large\\textbf{Total}\\dotfill\\ \\textbf{"
           << StrPrecioLtx() << "} \\normalsize" << std::endl;
    if(recurre) subcapitulos.ImprLtxResumen(os,SectionLtx(sect),recurre);
}
void Capitulo::ImprCompLtxPre(std::ostream &os,const std::string &sect,const Capitulo &otro) const
{
    if(sect!="raiz")
        os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
    mediciones.ImprCompLtxPre(os, Titulo(),otro.mediciones,otro.Titulo());
    subcapitulos.ImprCompLtxPre(os,SectionLtx(sect), otro.subcapitulos);
    if(subcapitulos.size())
    {
        os << ltx_beg_itemize << std::endl;
        os << "\\item \\noindent \\textbf{Total " << Titulo()
           << " (P. de construcción): } \\dotfill \\textbf{"
           << otro.StrPrecioLtx() << "} " << std::endl << std::endl;
        os << "\\item \\noindent \\textbf{Total " << Titulo()
           << " (P. modificado): }\\dotfill \\textbf{"
           << StrPrecioLtx() << "} " << std::endl;
        os << ltx_end_itemize << std::endl;
        os << "\\clearpage" << std::endl;
    }
    if(mediciones.size())
        os << "\\newpage" << std::endl;
}
void Capitulo::ImprLtxPre(std::ostream &os,const std::string &sect) const
//Imprime presupuestos parciales.
{
    if(sect!="raiz")
        os << '\\' << sect << '{' << Titulo() << '}' << std::endl;
    mediciones.ImprLtxPre(os,Titulo());
    subcapitulos.ImprLtxPre(os,SectionLtx(sect));
    if(subcapitulos.size())
        os << "\\noindent \\large \\textbf{Total: " << Titulo() << "} \\dotfill \\textbf{" << StrPrecioLtx() << "} \\\\ \\normalsize" << std::endl;
}
void Capitulo::EscribeHCalcMed(std::ostream &os,const std::string &sect) const
{
    if(sect!="raiz")
        os << Titulo() << std::endl;
    mediciones.EscribeHCalcMed(os);
    subcapitulos.EscribeHCalcMed(os,sect);
}
void Capitulo::EscribeHCalcPre(std::ostream &os,const std::string &sect) const
{
    if(sect!="raiz")
        os << Titulo() << std::endl;
    mediciones.EscribeHCalcPre(os);
    os << tab << tab << tab << tab << "Total: " << tab << Titulo() << tab << StrPrecio() << std::endl;
    subcapitulos.EscribeHCalcPre(os,sect);
}

InformeMediciones Capitulo::GetInformeMediciones(void) const
{
    InformeMediciones retval= mediciones.GetInformeMediciones();
    retval.Merge(subcapitulos.GetInformeMediciones());
    return retval;
}
