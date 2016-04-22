//Descompuestos.cxx

#include "Descompuestos.h"

void Descompuestos::AgregaComponente(const Elementos &el,const std::string &cod_ud,const std::string &cod_el,const float &r, const float &f)
{
    UdObra *i= Busca(cod_ud);
    const Elemento *j= el.Busca(cod_el);
    if(!j)
    {
        std::cerr << "Elemento: " << cod_el
                  << " no encontrado en unidad de obra: " << cod_ud << std::endl;
        exit(1);
    }
    i->Agrega(*j,f,r);
}

BuscadorDescompuestos Descompuestos::GetBuscador(void)
{
    return BuscadorDescompuestos(this);
}

//template<>
//MapaClaves<UdObra> MapaConceptos<UdObra>::claves;

//! @brief Lee las unidades de obra a falta de la descomposición.
void Descompuestos::LeeBC3Fase1(const Codigos &cds)
{
    Codigos::const_iterator i=cds.begin();
    UdObra ud;
    for(; i!=cds.end(); i++)
    {
        Codigos::reg_udobra reg= cds.GetDatosUdObra(i);
        ud.LeeBC3Fase1(reg);
        Agrega(ud);
    }
}
//! @brief Lee la descomposición de las unidades
Descompuestos::set_pendientes Descompuestos::LeeBC3Fase2(const Codigos &cds,Buscadores &bp)
{
    Codigos::const_iterator i=cds.begin();
    UdObra *ud=NULL;
    bool error= false;
    set_pendientes retval;
    for(; i!=cds.end(); i++)
    {
        Codigos::reg_udobra reg= cds.GetDatosUdObra(i);
        ud= Busca(reg.Codigo());
        error= ud->LeeBC3Fase2(reg,bp);
        if(error)
            retval.insert(reg.Codigo());
    }
    return retval;
}
void Descompuestos::EscribeSpre(std::ostream &os) const
{
    const_iterator j= begin();
    for(; j!=end(); j++)
        (*j).second.EscribeSpre(os);
}
void Descompuestos::AsignaFactor(const float &f)
{
    iterator j= begin();
    for(; j!=end(); j++)
        (*j).second.AsignaFactor(f);
}
void Descompuestos::LeeSpre(std::istream &is,const Elementos &elementos)
{
    if(is.peek()!= 26)
        while(1)
        {
            std::string cod;
            getline(is,cod,'|');
            std::string ud;
            getline(is,ud,'|');
            if(ud.find('%')<ud.length())
            {
                cod= "%" + cod;
                ud= "";
            }
            std::string tit;
            getline(is,tit,'|');
            UdObra unidad(cod,tit,ud);
            unidad.TextoLargo()= tit;
            Agrega(unidad);
            std::string porc; //porcentaje
            getline(is,porc,'|');
            std::string descomp; //descomposición
            getline(is,descomp,'\n');
            //istrstream istr(descomp.c_str(),descomp.length());
            while(1)
            {
                size_t pos2= descomp.find('|');
                std::string cod_el= descomp.substr(0,pos2);
                descomp.replace(0,pos2+1,"");
                size_t pos3= descomp.find('|');
                std::string cantidad;
                if(pos3<1000)
                {
                    cantidad= descomp.substr(0,pos3);
                    descomp.replace(0,pos3+1,"");
                }
                else
                    cantidad= descomp.substr(0,descomp.length()-1);
                if(elementos.find("%" + cod_el)!=elementos.end()) //Corresponde a un porcentaje.
                    cod_el = "%"+cod_el;
                AgregaComponente(elementos,cod,cod_el,atof(cantidad.c_str()));
                if(pos3>descomp.length()) break;
            }
            if(is.peek() == 26) break;
        }
    std::string resto;
    getline(is,resto,'\n');
}

void Descompuestos::ImprLtxCP1(std::ostream &os) const
{
    if(size()<1) return;
    const std::string linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg;
    const size_t num_campos= 5;
    os << ltx_small << std::endl;
    os << "\\begin{longtable}{|l|l|p{4cm}|p{3cm}|r|}" << std::endl
       << ltx_hline << std::endl
       << "Código & Ud. & Denominación & \\multicolumn{2}{|c|}{Precio}\\\\"
       << " & & & en letra & en cifra \\\\" << std::endl
       << ltx_hline << std::endl
       << ltx_endhead << std::endl
       << ltx_hline << std::endl
       << "\\multicolumn{" << num_campos << "}{|r|}{../..}\\\\\\hline" << std::endl
       << ltx_endfoot << std::endl
       << ltx_hline << std::endl
       << ltx_endlastfoot << std::endl;
    const_iterator j= begin();
    for(; j!=end(); j++)
    {
        os << linea_en_blanco << std::endl;
        (*j).second.ImprLtxCP1(os);
        os << linea_en_blanco << std::endl;
    }
    os << "\\end{longtable}" << std::endl;
    os << ltx_normalsize << std::endl;
}
void Descompuestos::ImprLtxJustPre(std::ostream &os) const
{
    os << ltx_small << std::endl;
    os << "\\begin{longtable}{l}" << std::endl;
    const_iterator j= begin();
    for(; j!=end(); j++)
    {
        (*j).second.ImprLtxJustPre(os);
        os << ltx_fin_reg << std::endl;
        os << ltx_fin_reg << std::endl;
    }
    os << "\\end{longtable}" << std::endl;
    os << ltx_normalsize << std::endl;
}
void Descompuestos::ImprLtxCP2(std::ostream &os) const
{
    if(size()<1) return;
    //os << ltx_star_chapter("Cuadro de precios no. 2") << std::endl;
    os << ltx_small << std::endl;
    os << "\\begin{longtable}{l}" << std::endl;
    const_iterator j= begin();
    for(; j!=end(); j++)
    {
        (*j).second.ImprLtxCP2(os);
        os << ltx_fin_reg << std::endl;
        os << ltx_fin_reg << std::endl;
    }
    os << "\\end{longtable}" << std::endl;
    os << ltx_normalsize << std::endl;
}
void Descompuestos::EscribeHCalc(std::ostream &os) const
{
    os << "Código" << tab
       << "Ud." << tab
       << "Denominación" << tab
       << "Precio en letra" << tab
       << "Precio en cifra" << std::endl;
    const_iterator j= begin();
    for(; j!=end(); j++)
    {
        (*j).second.EscribeHCalc(os);
    }
}

void const *BuscadorDescompuestos::Busca(const std::string &clave) const
{
    return contenedor->Busca(clave);
}
void *BuscadorDescompuestos::Busca(const std::string &clave)
{
    return contenedor->Busca(clave);
}
