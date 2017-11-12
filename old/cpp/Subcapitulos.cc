//Subcapitulos.cxx

#include "Capitulo.h"
#include "CodigosObra.h"

Subcapitulos::Subcapitulos(Capitulo &ptr_cap)
    : std::deque<Capitulo>(),EntPpl(&ptr_cap) {}

const Capitulo *Subcapitulos::getContenedor(void) const
{
    return dynamic_cast<const Capitulo *>(Owner());
}

size_t Subcapitulos::NumDescompuestos(void) const
{
    size_t nd= 0;
    for(const_iterator j=begin(); j!=end(); j++)
        nd+= (*j).NumDescompuestos();
    return nd;
}

long double Subcapitulos::Precio(void) const
{
    long double p= 0.0;
    for(const_iterator j=begin(); j!=end(); j++)
        p+= (*j).Precio();
    return p;
}

ppl_precio Subcapitulos::PrecioR(void) const
{
    ppl_precio p= 0.0;
    for(const_iterator j=begin(); j!=end(); j++)
        p+= (*j).PrecioR();
    return p;
}

Capitulo *Subcapitulos::Busca(regBC3_ruta &ruta)
{
    if(ruta.size()==0) return NULL;
    size_t indice= atoi(ruta[0])-1;
    bool existe= (indice<size());
    if(!existe)
    {
        return NULL;
    }
    else if(ruta.size()== 1) //Es subcapitulo de este
        return &(*this)[indice];
    else
    {
        Capitulo *sc= &(*this)[indice];
        ruta.pop_front();
        return sc->BuscaSubcapitulo(ruta);
    }
    return NULL;
}
const Capitulo *Subcapitulos::BuscaCodigo(const std::string &nmb) const
{
    const Capitulo *retval= NULL;
    for(const_iterator i= begin(); i!=end(); i++)
    {
        retval= (*i).BuscaCodigo(nmb);
        if(retval) return retval;
    }
    return retval;
}
Capitulo *Subcapitulos::BuscaCodigo(const std::string &nmb)
{
    Capitulo *retval= NULL;
    for(iterator i= begin(); i!=end(); i++)
    {
        retval= (*i).BuscaCodigo(nmb);
        if(retval) return retval;
    }
    return retval;
}

//! @brief Busca una unidad de obra por el árbol de capítulos.
const Medible *Subcapitulos::BuscaPrecio(const std::string &cod) const
{
    const Medible *retval= NULL;
    for(const_iterator i= begin(); i!=end(); i++)
    {
        retval= (*i).BuscaPrecio(cod);
        if(retval) break;
    }
    return retval;
}

void Subcapitulos::AgregaCapitulo(const Capitulo &c)
{
    push_back(c);
}

//! @brief Agrega un capitulo.
void Subcapitulos::AgregaCapitulo(const regBC3_desc &r)
{
    AgregaCapitulo(Capitulo(r.codigo,"",r.factor,r.rendimiento));
}

//! @brief Agrega los capítulos que se pasan como parámetro.
void Subcapitulos::AgregaCapitulos(const regBC3_d &descomp)
{
    size_t sz= descomp.size();
    for(size_t i=0; i<sz; i++)
        AgregaCapitulo(descomp[i]);
}

//! @brief Carga los datos de los subcapítulos de (*this).
void Subcapitulos::LeeBC3Caps(CodigosObra &co)
{
    const Codigos &sc(co.GetDatosCaps());
    if(sc.size()<1)
        std::cerr << "No se encontraron subcapitulos." << std::endl;

    const std::set<std::string> &nombres_capitulos= co.GetCodigosCapitulos();

    for(iterator i= begin(); i!=end(); i++)
    {
        Codigos::const_iterator j= sc.BuscaCapitulo(i->Codigo()); //sc.find(i->Codigo()); //Código
        if(j!=sc.end())
        {
            Codigos::reg_capitulo reg= sc.GetDatosCapitulo(j);
            if(i!=end())
            {
                if(verborrea>4)
                    std::clog << "Cargando el subcapítulo: '" << reg.Datos().Titulo() << "'\n";
                i->Titulo()= reg.Datos().Titulo(); //Título

                //Lee los elementales del capítulo.
                Codigos elementos_capitulo= co.FiltraElementales(reg.Datos().desc);
                i->LeeBC3Elementales(elementos_capitulo);
                if(verborrea>4)
                    std::clog << "  Cargados " << elementos_capitulo.size()
                              << " precios elementales del capítulo." << std::endl;
                co.BorraElementales(elementos_capitulo); //Borra los ya leídos.
                if(verborrea>4)
                    std::clog << "  Quedan " << co.GetDatosElementos().size() << " precios elementales." << std::endl;

                //Lee los subcapítulos.
                i->subcapitulos.AgregaCapitulos(reg.Datos().FiltraCapitulos(nombres_capitulos));
                i->subcapitulos.LeeBC3Caps(co); //Carga los subcapitulos.
            }
        }
        else
        {
            std::cerr << "LeeBC3Caps; No se encontró el capítulo: " << i->Codigo() << std::endl;
            continue;
        }
    }
}
//! @brief Carga los datos de los descompuestos de (*this) a falta de la descomposición.
// void Subcapitulos::LeeBC3DescompFase1(const CodigosObra &co)
//   {
//     const Codigos &sc(co.GetDatosCaps());
//     if(sc.size()<1)
//       std::cerr << "No se encontraron subcapitulos." << std::endl;
//     for(iterator i= begin();i!=end();i++) //Bucle sobre los subcapitulos.
//       {
//         Codigos::const_iterator j= sc.BuscaCapitulo(i->Codigo()); //Busca los datos del subcapitulo.
//         if(j!=sc.end())
//           {
//             Codigos::reg_capitulo reg= sc.GetDatosCapitulo(j);
//             if(i!=end())
//               {
//                 Codigos descompuestos= co.FiltraDescompuestos(reg.Datos().desc);
//                 if(descompuestos.size()>0) i->LeeBC3DescompFase1(descompuestos);
//                 if(verborrea>4)
// 		  std::clog << "  Cargados " << descompuestos.size()
//                             << " precios descompuestos del capítulo." << std::endl;
//                 i->LeeBC3DescFase1(co); //Carga los descompuestos de sus subcapitulos.
//               }
//           }
//         else
//           {
//             std::cerr << "LeeBC3DescompFase1; No se encontró el capítulo: " << i->Codigo() << std::endl;
//             continue;
//           }
//       }
//   }
// //! @brief Carga los datos de los descompuestos de (*this).
// Descompuestos::set_pendientes Subcapitulos::LeeBC3DescompFase2(CodigosObra &co)
//   {
//     Descompuestos::set_pendientes retval;
//     Descompuestos::set_pendientes tmp;
//     const Codigos &sc(co.GetDatosCaps());
//     if(sc.size()<1)
//       std::cerr << "No se encontraron subcapitulos." << std::endl;
//     for(iterator i= begin();i!=end();i++) //Bucle sobre los subcapitulos.
//       {
//         Codigos::const_iterator j= sc.BuscaCapitulo(i->Codigo());
//         if(j!=sc.end())
//           {
//             Codigos::reg_capitulo reg= sc.GetDatosCapitulo(j); //Busca los datos del subcapitulo.
//             if(i!=end())
//               {
//                 Codigos descompuestos= co.FiltraDescompuestos(reg.Datos().desc);
//                 if(descompuestos.size()>0)
//                   {
//                     tmp= i->LeeBC3DescompFase2(descompuestos);
//                     retval.insert(tmp.begin(),tmp.end());
//                   }
//                 co.BorraDescompuestos(descompuestos); //Borra los ya leídos.
//                 tmp= i->LeeBC3DescFase2(co); //Carga los descompuestos de sus subcapitulos.
//                 retval.insert(tmp.begin(),tmp.end());
//               }
//           }
//         else
//           {
//             std::cerr << "LeeBC3DescompFase2; No se encontró el capítulo: " << i->Codigo() << std::endl;
//             continue;
//           }
//       }
//     return retval;
//   }

void Subcapitulos::EscribeDescompBC3(std::ostream &os,const std::string &cod) const
{
    if(size()<1) return;
    os << "~D" << '|'
       << cod << '|';
    for(const_iterator i=begin(); i!=end(); i++)
        (*i).GetCompBC3().EscribeBC3(os);
    os << '|' << endl_msdos;
}

void Subcapitulos::EscribePreciosBC3(std::ostream &os) const
{
    for(const_iterator i=begin(); i!=end(); i++)
        (*i).EscribePreciosBC3(os);
}

void Subcapitulos::EscribeBC3(std::ostream &os,bool primero,const std::string &pos) const
{
    const_iterator i;
    size_t conta= 1;
    for(i=begin(); i!=end(); i++,conta++)
    {
        std::string nueva_pos= pos+num2str(conta,0)+'\\';
        (*i).EscribeBC3(os,primero,nueva_pos);
    }
}

void Subcapitulos::ImprCompLtxMed(std::ostream &os,const std::string &sect,const Subcapitulos &otro) const
//Suponemos que ambos capítulos tienen el mismo número de subcapítulos.
{
    const_iterator i= begin();
    const_iterator j= otro.begin();
    for(; ((i!=end()) && (j!=otro.end())); i++,j++)
        (*i).ImprCompLtxMed(os,sect,*j);
}
void Subcapitulos::ImprLtxMed(std::ostream &os,const std::string &sect) const
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxMed(os,sect);
}
void Subcapitulos::ImprLtxCP1(std::ostream &os,const std::string &sect) const
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxCP1(os,sect);
}
void Subcapitulos::ImprLtxCP2(std::ostream &os,const std::string &sect) const
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxCP2(os,sect);
}
void Subcapitulos::ImprLtxJustPre(std::ostream &os,const std::string &sect) const
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxJustPre(os,sect);
}

void Subcapitulos::ImprLtxResumen(std::ostream &os,const std::string &sect,bool recurre) const
{
    if(size())
    {
        os << "\\begin{itemize}" << std::endl;
        for(const_iterator j=begin(); j!=end(); j++)
            (*j).ImprLtxResumen(os,sect,recurre);
        os << "\\end{itemize}" << std::endl;
    }
}

void Subcapitulos::ImprCompLtxPre(std::ostream &os,const std::string &sect,const Subcapitulos &otro) const
//Suponemos que ambos capítulos tienen el mismo número de subcapítulos.
{
    const_iterator i= begin();
    const_iterator j= otro.begin();
    for(; ((i!=end()) && (j!=otro.end())); i++,j++)
        (*i).ImprCompLtxPre(os,sect,*j);
}
void Subcapitulos::ImprLtxPre(std::ostream &os,const std::string &sect) const
//Imprime presupuestos parciales.
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxPre(os,sect);
}

void Subcapitulos::EscribeHCalcMed(std::ostream &os,const std::string &sect) const
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).EscribeHCalcMed(os,sect);
}

void Subcapitulos::EscribeHCalcPre(std::ostream &os,const std::string &sect) const
{
    const_iterator j;
    for(j=begin(); j!=end(); j++)
        (*j).EscribeHCalcPre(os,sect);
}

InformeMediciones Subcapitulos::GetInformeMediciones(void) const
{
    InformeMediciones retval;
    for(const_iterator j=begin(); j!=end(); j++)
        retval.Merge((*j).GetInformeMediciones());
    return retval;
}
