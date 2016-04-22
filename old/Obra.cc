//Obra.cxx
#include "Obra.h"
#include "CodigosObra.h"

//! @brief Constructor.
Obra::Obra(const std::string &cod,const std::string &tit)
    : Capitulo(cod,tit,1,1)
{
    precios.Elementales().Agrega(Elemento("SINDESCO","Sin descomposición","",1.0,mat));
}

std::string Obra::CodigoBC3(void) const
{
    return Capitulo::CodigoBC3() + "#";
}

//! @brief Agrega el capítulo que se pasa como
//! parámetro al subcapítulo que indica la
//! cadena de la forma 1\2\1\4.
void Obra::AgregaCapitulo(const std::string &cap_padre,const Capitulo &cap)
{
    if(cap_padre=="") //Es un capítulo raíz
        subcapitulos.AgregaCapitulo(cap);
    else
        BuscaSubcapitulo(cap_padre)->getSubcapitulos().AgregaCapitulo(cap);
}

//! @brief Agrega la partida que se pasa como
//! parámetro al subcapítulo que indica la
//! cadena de la forma 1\2\1\4.
void Obra::AgregaPartida(const std::string &cap_padre,const Partida &m)
{
    BuscaSubcapitulo(cap_padre)->AgregaPartida(m);
}

void Obra::LeeMedicSpre(std::istream &is)
{
    std::string cdg= "";
    while(!is.eof())
    {
        if(is.peek()==26)
        {
            std::string resto;
            getline(is,resto,'\n');
            continue;
        }
        std::string lista;
        getline(is,lista,'|');
        if(lista=="") break;
        if(lista!=cdg) //capitulo nuevo
        {
            std::string cod= replace(lista,'/','_');
            std::string tit;
            getline(is,tit,'\n');
            tit= q_blancos(tit.substr(0,tit.length()-1));
            std::cerr << "Cargando capítulo: " << cod << ' ' << tit << '*' << std::endl;
            Capitulo cp(cod,tit);
            std::string ruta= replace(lista,'/','\\');
            size_t pos= ruta.find('\\');
            if(pos>ruta.length()) //Es capítulo raiz.
                AgregaCapitulo("",cp);
            else //es capitulo hijo.
            {
                size_t pos2= ruta.rfind('\\');
                ruta= ruta.substr(0,pos2);
                AgregaCapitulo(ruta,cp);
            }
            cdg= lista;
        }
        else //Medicion
        {
            std::string cod= replace(lista,'/','\\');
            std::string contenido;
            getline(is,contenido,'\n');
            size_t pos= contenido.find('|');
            std::string cod_ud_obra= contenido.substr(0,pos);
            contenido= contenido.substr(pos+1,contenido.length());
            const UdObra *udo= precios.BuscaUdObra(cod_ud_obra);
            if(!udo)
            {
                std::cerr << "Unidad de obra: " << cod_ud_obra
                          << " no encontrada" << std::endl;
                return;
            }
            Partida muo(*udo);
            while(1)
            {
                pos= contenido.find('|');
                std::string comentario= contenido.substr(0,pos);
                contenido= contenido.substr(pos+1,contenido.length());
                pos= contenido.find('|');
                std::string uds= contenido.substr(0,pos);
                contenido= contenido.substr(pos+1,contenido.length());
                pos= contenido.find('|');
                std::string lng= contenido.substr(0,pos);
                contenido= contenido.substr(pos+1,contenido.length());
                pos= contenido.find('|');
                std::string lat= contenido.substr(0,pos);
                contenido= contenido.substr(pos+1,contenido.length());

                pos= contenido.find('|');
                std::string alt= "";
                if(pos>contenido.length())
                {
                    pos= contenido.find('\n');
                    alt= contenido.substr(0,pos-1);
                    RegMedicion rm(comentario,atof(uds),atof(lng),atof(lat),atof(alt));
                    muo.Agrega(rm);
                    break;
                }
                else
                {
                    alt= contenido.substr(0,pos);
                    contenido= contenido.substr(pos+1,contenido.length());
                    RegMedicion rm(comentario,atof(uds.c_str()),atof(lng.c_str()),atof(lat.c_str()),atof(alt.c_str()));
                    muo.Agrega(rm);
                }
            }
            AgregaPartida(cod,muo);
        }
    }
}

void Obra::LeeSpre(std::istream &is)
{
    std::string str;
    precios.LeeSpre(is);
    getline(is,str,'\n');
    if(str.find("[MED]")<str.length()) LeeMedicSpre(is);
}

Capitulo *Obra::BuscaCapituloMedicion(regBC3_ruta &ruta)
{
    ruta.pop_back(); //Eliminamos el último elemento que es la posición.
    return this->BuscaSubcapitulo(ruta);
}

void Obra::LeeBC3DatosObra(const Codigos &obra)
{
    if(obra.size()<1)
        std::cerr << "No se encontró la obra." << std::endl;
    Codigos::reg_capitulo reg= obra.GetDatosCapitulo(obra.begin());
    Codigo()= reg.Codigo(); //Código
    Titulo()= reg.Datos().Titulo(); //Título
    subcapitulos.AgregaCapitulos(reg.Datos().desc);
}
void Obra::LeeBC3Mediciones(const CodigosObra &co)
{
    const Codigos &med= co.GetDatosMeds();
    if(med.size()<1)
        std::cerr << "No se encontraron mediciones." << std::endl;
    for(Codigos::const_iterator i= med.begin(); i!=med.end(); i++)
    {
        Codigos::reg_medicion reg= med.GetDatosMedicion(i);
        //const UdObra *ud= precios.BuscaUdObra(reg.CodigoUnidad());
        const std::string cod_unidad= copia_desde(reg.CodigoUnidad(),'@');
        const Medible *ud= this->BuscaPrecio(cod_unidad);
        if(!ud)
        {
            std::cerr << "Obra::LeeBC3Mediciones: No se encontró el precio: \'"
                      << cod_unidad << "\'" << std::endl;
            std::cerr << "  El concepto de código: \'" << cod_unidad << "\'";
            if(!co.ExisteConcepto(cod_unidad))
                std::cerr << " no existe." << std::endl;
            else
            {
                std::cerr << " existe y está en la tabla: "
                          << co.StrTablaConcepto(cod_unidad) << std::endl;
            }
        }
        else
        {
            Partida m(*ud);
            m.LeeBC3(reg.Datos());
            regBC3_ruta r=reg.Datos().Ruta();
            Capitulo *c= BuscaCapituloMedicion(r);
            if(!c)
                c= BuscaCodigo(reg.CodigoCapitulo());
            if(c)
                c->AgregaPartida(m);
            else
                std::cerr << "No se encontró el capítulo: " << reg.CodigoCapitulo() << std::endl;
        }
    }
}
void Obra::LeeBC3(std::istream &is)
{
    CodigosObra co;
    std::clog << "Leyendo registros FIEBDC 3...";
    co.LeeBC3(is,verborrea); //Carga los registros BC3.
    std::clog << "hecho." << std::endl;
    std::clog << "Leyendo estructura de capítulos...";
    LeeBC3DatosObra(co.GetDatosObra());
    subcapitulos.LeeBC3Caps(co); //Lee capitulos y precios elementales.
    std::clog << "hecho." << std::endl;

    std::clog << "Leyendo precios...";
    precios.LeeBC3Elementales(co.GetDatosElementos()); //Lee los precios elementales fuera de capítulo.

    //LeeBC3DescFase1(co); //Lee descompuestos de capitulos.
    precios.LeeBC3DescompFase1(co.GetDatosUnidades());

    std::clog << "hecho." << std::endl;
    Descompuestos::set_pendientes pendientes,tmp;
    std::clog << "Leyendo descomposiciones...";

    //pendientes= LeeBC3DescFase2(co); //Lee descomposiciones.
    pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades());

    std::clog << "hecho." << std::endl;
    std::clog << "Leyendo precios globales...";
    precios.LeeBC3DescompFase1(co.GetDatosUnidades());
    tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades());
    std::clog << "num. precios= " << precios.NumDescompuestos() << std::endl;
    pendientes.insert(tmp.begin(),tmp.end());
    std::clog << "hecho." << std::endl;
    if(pendientes.size())
    {
        std::clog << "   Leyendo descomposiciones (y 2)...";
        //pendientes= LeeBC3DescFase2(co); //Lee descomposiciones.
        pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades()); //Lee descomposiciones.
        std::clog << "hecho." << std::endl;
        std::clog << "   Leyendo precios globales (y 2)...";
        precios.LeeBC3DescompFase1(co.GetDatosUnidades());
        tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades());
        pendientes.insert(tmp.begin(),tmp.end());
        std::clog << "hecho." << std::endl;
    }
    std::clog << "Leyendo mediciones...";

    LeeBC3Mediciones(co);
    std::clog << "hecho." << std::endl;
}
void Obra::ImprLtxPresEjecMat(std::ostream &os) const
{
    os << "\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución material}" << std::endl;
    os << "\\addcontentsline{toc}{starchapter}{Presupuesto de ejecución material}" << std::endl;
    os << "\\cleardoublepage" << std::endl;
    os << "\\begin{center}" << std::endl;
    os << "\\Large \\textbf{Presupuesto de Ejecución Material} \\large" << std::endl;
    os << "\\end{center}" << std::endl;
    os << "\\vspace{2cm}" << std::endl;
    subcapitulos.ImprLtxResumen(os,"",false);
    os << "\\textbf{Presupuesto de ejecución material:} \\dotfill\\ \\textbf{" << StrPrecioLtx() << '}' << std::endl << std::endl << std::endl;
    os << "\\vspace{0.5cm}" << std::endl;
    os << "Asciende el presente presupuesto de ejecución material a la expresada cantidad de: \\textsc{";
    os << PrecioR().EnLetra(false) << " euros}." << std::endl;
    os << "\\input{firmas}" << std::endl;
}
void Obra::ImprLtxPresContrata(std::ostream &os) const
{
    os << "\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución por contrata}" << std::endl;
    os << "\\addcontentsline{toc}{starchapter}{Presupuesto de ejecución por contrata}" << std::endl;
    os << "\\cleardoublepage" << std::endl;
    os << "\\begin{center}" << std::endl;
    os << "\\Large \\textbf{Presupuesto de Ejecución por Contrata} \\large" << std::endl;
    os << "\\end{center}" << std::endl;
    os << "\\vspace{2cm}" << std::endl;
    porcentajes.ImprLtx(os,PrecioR());
    os << "\\input{firmas}" << std::endl;
}

void Obra::EscribeBC3(std::ostream &os,const std::string pos) const
{
    os << "~V|Iturribizia, S.L.|FIEBDC-3/95|ppl 0.1|" << endl_msdos;
    EscribePreciosBC3(os);
    EscribeConceptoBC3(os);
    EscribeDescompBC3(os);
    EscribeMediciones(os,pos);
    EscribeSubCapitulos(os,true,pos);
}

void Obra::ImprLtxPresGen(std::ostream &os) const
{
    os << "\\part{Presupuestos Generales}" << std::endl;
    ImprLtxPresEjecMat(os);
    ImprLtxPresContrata(os);
}
void Obra::ImprLtxMed(std::ostream &os) const
{
    os << ltx_part("Mediciones") << std::endl;
    os << ltx_parttoc << std::endl;
    Capitulo::ImprLtxMed(os,"raiz");
}
void Obra::ImprCompLtxMed(const Obra &otra,std::ostream &os) const
{
    os << ltx_part("Mediciones") << std::endl;
    os << ltx_parttoc << std::endl;
    os << ltx_begin("landscape") << std::endl;
    Capitulo::ImprCompLtxMed(os,"raiz",otra);
    os << ltx_end("landscape") << std::endl;
}
void Obra::ImprLtxCP1(std::ostream &os) const
{
    os << ltx_part("Cuadro de precios no. 1") << std::endl;
    os << ltx_parttoc << std::endl;
    os << "\\setcounter{chapter}{0}" << std::endl;
    Capitulo::ImprLtxCP1(os,"raiz");
    os << "\\input{firmas}" << std::endl;
}
void Obra::ImprLtxCP2(std::ostream &os) const
{
    os << ltx_part("Cuadro de precios no. 2") << std::endl;
    os << ltx_parttoc << std::endl;
    os << "\\setcounter{chapter}{0}" << std::endl;
    Capitulo::ImprLtxCP2(os,"raiz");
    os << "\\input{firmas}" << std::endl;
}
void Obra::ImprLtxJustPre(std::ostream &os) const
{
    Capitulo::ImprLtxJustPre(os,"raiz");
    os << "\\input{firmas}" << std::endl;
}
void Obra::ImprLtxCP(std::ostream &os) const
{
    ImprLtxCP1(os);
    ImprLtxCP2(os);
}
void Obra::ImprLtxPreParc(std::ostream &os) const
{
    os << ltx_part("Presupuestos parciales") << std::endl;
    os << ltx_parttoc << std::endl;
    os << "\\setcounter{chapter}{0}" << std::endl;
    Capitulo::ImprLtxPre(os,"raiz");
}
void Obra::ImprCompLtxPreParc(const Obra &otra,std::ostream &os) const
{
    os << ltx_part("Presupuestos parciales") << std::endl;
    os << ltx_parttoc << std::endl;
    os << "\\setcounter{chapter}{0}" << std::endl;
    os << ltx_begin("landscape") << std::endl;
    Capitulo::ImprCompLtxPre(os,"raiz",otra);
    os << ltx_end("landscape") << std::endl;
}
void Obra::ImprLtxResumen(std::ostream &os) const
{
    os << ltx_part("Resumen de los presupuestos parciales") << std::endl
       << ltx_star_chapter("Resumen") << std::endl;
    Capitulo::ImprLtxResumen(os,"raiz");
}
void Obra::ImprCompLtx(const Obra &otra,std::ostream &os) const
//Imprime el comparativo con otra obra.
{
    //ImprCompLtxMed(otra,os);
    ImprCompLtxMed(otra,os);
    precios.ImprLtxCP(os); //Cuadros de precios.
    ImprCompLtxPreParc(otra,os);
    //ImprLtxResumen(os);
}
void Obra::ImprLtx(std::ostream &os) const
//Imprime la obra en LaTex.
{
    ImprLtxMed(os); //Mediciones.
    ImprLtxCP(os); //Cuadros de precios.
    ImprLtxPreParc(os); //Presupuestos parciales.
    ImprLtxResumen(os); //Resument presup. parciales.
    ImprLtxPresGen(os); //Presupuestos generales.
}
void Obra::ImprLtxInformeObra(std::ostream &os) const
//Imprime en LaTeX el informe de obra.
{
    InformeMediciones im= GetInformeMediciones();
    im.ImprLtx(os);
}
void Obra::EscribeHCalc(std::ostream &os) const
//Imprime la obra en LaTex.
{
    os << "Mediciones" << std::endl;
    Capitulo::EscribeHCalcMed(os,"raiz");
    os << "Cuadros de precios" << std::endl;
    precios.EscribeHCalc(os);
    os << "Presupuestos parciales" << std::endl;
    Capitulo::EscribeHCalcPre(os,"raiz");
}
void Obra::SimulaDescomp(const std::string &origen, const std::string &destino)
{
    precios.SimulaDescomp(origen,destino);
}

