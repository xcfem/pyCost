#Obra.h

#ifndef OBRA_H
#define OBRA_H

import Capitulo
import Porcentajes

class CodigoObra
class Codigos

class Obra(Capitulo):
private:
    Porcentajes porcentajes

    inline virtual std.string nombre_clase(void)
        return "Obra"

public:
    Obra( std.string &cod="ObraSinCod", &tit="ObraSinTit")
    virtual std.string CodigoBC3(void)

    void AgregaCapitulo( std.string &cap_padre, &cap)
    void AgregaPartida( std.string &cap_padre, &m)

    void LeeBC3DatosObra( Codigos &obra)
    void EscribeSpre(void)
        precios.EscribeSpre()
        std.cerr << "Exportación de capítulos no implementada." << std.endl

    void EscribeBC3(std.ostream &os, pos="")
    void LeeMedicSpre(std.istream &is)
    void LeeSpre(std.istream &is)
    Capitulo *BuscaCapituloMedicion(regBC3_ruta &ruta)
    void LeeBC3Mediciones( CodigosObra &co)
    void LeeBC3(std.istream &is)

    void ImprLtxPresEjecMat(std.ostream &os)
    void ImprLtxPresContrata(std.ostream &os)
    void ImprLtxPresGen(std.ostream &os)
    void ImprLtxMed(std.ostream &os)
    void ImprCompLtxMed( Obra &otra, &os)
    void ImprLtxCP1(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP(std.ostream &os)
    void ImprLtxPreParc(std.ostream &os)
    void ImprCompLtxPreParc( Obra &otra, &os)
    void ImprLtxResumen(std.ostream &os)
    void ImprCompLtx( Obra &otra, &os)
    void ImprLtx(std.ostream &os)
    void ImprLtxInformeObra(std.ostream &os)

    void EscribeHCalc(std.ostream &os)
    void SimulaDescomp( std.string &origen, &destino)

#endif
#Obra.cxx
import Obra
import CodigosObra

#not  @brief Constructor.
Obra.Obra( std.string &cod, &tit)
    : Capitulo(cod,tit,1,1)
    precios.Elementales().Agrega(Elemento("SINDESCO","Sin descomposición","",1.0,mat))


def CodigoBC3(self, void):
    return Capitulo.CodigoBC3() + "#"


#not  @brief Agrega el capítulo que se pasa como
#not  parámetro al subcapítulo que indica la
#not  cadena de la forma 1\2\1\4.
def AgregaCapitulo(self, &cap_padre, &cap):
    if(cap_padre=="") #Es un capítulo raíz
        subcapitulos.AgregaCapitulo(cap)
    else:
        BuscaSubcapitulo(cap_padre).getSubcapitulos().AgregaCapitulo(cap)


#not  @brief Agrega la partida que se pasa como
#not  parámetro al subcapítulo que indica la
#not  cadena de la forma 1\2\1\4.
def AgregaPartida(self, &cap_padre, &m):
    BuscaSubcapitulo(cap_padre).AgregaPartida(m)


def LeeMedicSpre(self, &is):
    cdg = ""
    while(not is.eof())
        if is.peek()==26:
            std.string resto
            getline(is,resto,'\n')
            continue

        std.string lista
        getline(is,lista,'|')
        if(lista=="") break
        if(lista!=cdg) #capitulo nuevo
            cod = replace(lista,'/','_')
            std.string tit
            getline(is,tit,'\n')
            tit= q_blancos(tit.substr(0,tit.length()-1))
            std.cerr << "Cargando capítulo: " << cod << ' ' << tit << '*' << std.endl
            Capitulo cp(cod,tit)
            ruta = replace(lista,'/','\\')
            pos = ruta.find('\\')
            if(pos>ruta.length()) #Es capítulo raiz.
                AgregaCapitulo("",cp)
            else #es capitulo hijo.
                pos2 = ruta.rfind('\\')
                ruta= ruta.substr(0,pos2)
                AgregaCapitulo(ruta,cp)

            cdg= lista

        else #Medicion
            cod = replace(lista,'/','\\')
            std.string contenido
            getline(is,contenido,'\n')
            pos = contenido.find('|')
            cod_ud_obra = contenido.substr(0,pos)
            contenido= contenido.substr(pos+1,contenido.length())
             UdObra *udo= precios.BuscaUdObra(cod_ud_obra)
            if not udo:
                std.cerr << "Unidad de obra: " << cod_ud_obra
                          << " no encontrada" << std.endl
                return

            Partida muo(*udo)
            while(1)
                pos= contenido.find('|')
                comentario = contenido.substr(0,pos)
                contenido= contenido.substr(pos+1,contenido.length())
                pos= contenido.find('|')
                uds = contenido.substr(0,pos)
                contenido= contenido.substr(pos+1,contenido.length())
                pos= contenido.find('|')
                lng = contenido.substr(0,pos)
                contenido= contenido.substr(pos+1,contenido.length())
                pos= contenido.find('|')
                lat = contenido.substr(0,pos)
                contenido= contenido.substr(pos+1,contenido.length())

                pos= contenido.find('|')
                alt = ""
                if pos>contenido.length():
                    pos= contenido.find('\n')
                    alt= contenido.substr(0,pos-1)
                    RegMedicion rm(comentario,atof(uds),atof(lng),atof(lat),atof(alt))
                    muo.Agrega(rm)
                    break

                else:
                    alt= contenido.substr(0,pos)
                    contenido= contenido.substr(pos+1,contenido.length())
                    RegMedicion rm(comentario,atof(uds.c_str()),atof(lng.c_str()),atof(lat.c_str()),atof(alt.c_str()))
                    muo.Agrega(rm)


            AgregaPartida(cod,muo)




def LeeSpre(self, &is):
    std.string str
    precios.LeeSpre(is)
    getline(is,str,'\n')
    if str.find("[MED]")<str.length()) LeeMedicSpre(is:


Capitulo *Obra.BuscaCapituloMedicion(regBC3_ruta &ruta)
    ruta.pop_back(); #Eliminamos el último elemento que es la posición.
    return self.BuscaSubcapitulo(ruta)


def LeeBC3DatosObra(self, &obra):
    if obra.size()<1:
        std.cerr << "No se encontró la obra." << std.endl
    reg = obra.GetDatosCapitulo(obra.begin())
    Codigo()= reg.Codigo(); #Código
    Titulo()= reg.Datos().Titulo(); #Título
    subcapitulos.AgregaCapitulos(reg.Datos().desc)

def LeeBC3Mediciones(self, &co):
     Codigos &med= co.GetDatosMeds()
    if med.size()<1:
        std.cerr << "No se encontraron mediciones." << std.endl
    for(i = med.begin(); i!=med.end(); i++)
        reg = med.GetDatosMedicion(i)
        # UdObra *ud= precios.BuscaUdObra(reg.CodigoUnidad())
         cod_unidad = copia_desde(reg.CodigoUnidad(),'@')
         Medible *ud= self.BuscaPrecio(cod_unidad)
        if not ud:
            std.cerr << "Obra.LeeBC3Mediciones: No se encontró el precio: \'"
                      << cod_unidad << "\'" << std.endl
            std.cerr << "  El concepto de código: \'" << cod_unidad << "\'"
            if not co.ExisteConcepto(cod_unidad):
                std.cerr << " no existe." << std.endl
            else:
                std.cerr << " existe y está en la tabla: "
                          << co.StrTablaConcepto(cod_unidad) << std.endl


        else:
            Partida m(*ud)
            m.LeeBC3(reg.Datos())
            regBC3_ruta r=reg.Datos().Ruta()
            Capitulo *c= BuscaCapituloMedicion(r)
            if not c:
                c= BuscaCodigo(reg.CodigoCapitulo())
            if c:
                c.AgregaPartida(m)
            else:
                std.cerr << "No se encontró el capítulo: " << reg.CodigoCapitulo() << std.endl



def LeeBC3(self, &is):
    CodigosObra co
    std.clog << "Leyendo registros FIEBDC 3..."
    co.LeeBC3(is,verborrea); #Carga los registros BC3.
    std.clog << "hecho." << std.endl
    std.clog << "Leyendo estructura de capítulos..."
    LeeBC3DatosObra(co.GetDatosObra())
    subcapitulos.LeeBC3Caps(co); #Lee capitulos y precios elementales.
    std.clog << "hecho." << std.endl

    std.clog << "Leyendo precios..."
    precios.LeeBC3Elementales(co.GetDatosElementos()); #Lee los precios elementales fuera de capítulo.

    #LeeBC3DescFase1(co); #Lee descompuestos de capitulos.
    precios.LeeBC3DescompFase1(co.GetDatosUnidades())

    std.clog << "hecho." << std.endl
    Descompuestos.set_pendientes pendientes,tmp
    std.clog << "Leyendo descomposiciones..."

    #pendientes= LeeBC3DescFase2(co); #Lee descomposiciones.
    pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades())

    std.clog << "hecho." << std.endl
    std.clog << "Leyendo precios globales..."
    precios.LeeBC3DescompFase1(co.GetDatosUnidades())
    tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades())
    std.clog << "num. precios= " << precios.NumDescompuestos() << std.endl
    pendientes.insert(tmp.begin(),tmp.end())
    std.clog << "hecho." << std.endl
    if pendientes.size():
        std.clog << "   Leyendo descomposiciones (y 2)..."
        #pendientes= LeeBC3DescFase2(co); #Lee descomposiciones.
        pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades()); #Lee descomposiciones.
        std.clog << "hecho." << std.endl
        std.clog << "   Leyendo precios globales (y 2)..."
        precios.LeeBC3DescompFase1(co.GetDatosUnidades())
        tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades())
        pendientes.insert(tmp.begin(),tmp.end())
        std.clog << "hecho." << std.endl

    std.clog << "Leyendo mediciones..."

    LeeBC3Mediciones(co)
    std.clog << "hecho." << std.endl

def ImprLtxPresEjecMat(self, &os):
    os << "\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución material}" << std.endl
    os << "\\addcontentsline{toc}{starchapter}{Presupuesto de ejecución material}" << std.endl
    os << "\\cleardoublepage" << std.endl
    os << "\\begin{center}" << std.endl
    os << "\\Large \\textbf{Presupuesto de Ejecución Material} \\large" << std.endl
    os << "\\end{center}" << std.endl
    os << "\\vspace{2cm}" << std.endl
    subcapitulos.ImprLtxResumen(os,"",False)
    os << "\\textbf{Presupuesto de ejecución material:} \\dotfill\\ \\textbf{" << StrPrecioLtx() << '}' << std.endl << std.endl << std.endl
    os << "\\vspace{0.5cm}" << std.endl
    os << "Asciende el presente presupuesto de ejecución material a la expresada cantidad de: \\textsc{"
    os << PrecioR().EnLetra(False) << " euros}." << std.endl
    os << "\\input{firmas}" << std.endl

def ImprLtxPresContrata(self, &os):
    os << "\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución por contrata}" << std.endl
    os << "\\addcontentsline{toc}{starchapter}{Presupuesto de ejecución por contrata}" << std.endl
    os << "\\cleardoublepage" << std.endl
    os << "\\begin{center}" << std.endl
    os << "\\Large \\textbf{Presupuesto de Ejecución por Contrata} \\large" << std.endl
    os << "\\end{center}" << std.endl
    os << "\\vspace{2cm}" << std.endl
    porcentajes.ImprLtx(os,PrecioR())
    os << "\\input{firmas}" << std.endl


def EscribeBC3(self, &os, pos):
    os << "~V|Iturribizia, S.L.|FIEBDC-3/95|ppl 0.1|" << endl_msdos
    EscribePreciosBC3(os)
    EscribeConceptoBC3(os)
    EscribeDescompBC3(os)
    EscribeMediciones(os,pos)
    EscribeSubCapitulos(os,True,pos)


def ImprLtxPresGen(self, &os):
    os << "\\part{Presupuestos Generales}" << std.endl
    ImprLtxPresEjecMat(os)
    ImprLtxPresContrata(os)

def ImprLtxMed(self, &os):
    os << ltx_part("Mediciones") << std.endl
    os << ltx_parttoc << std.endl
    Capitulo.ImprLtxMed(os,"raiz")

def ImprCompLtxMed(self, &otra, &os):
    os << ltx_part("Mediciones") << std.endl
    os << ltx_parttoc << std.endl
    os << ltx_begin("landscape") << std.endl
    Capitulo.ImprCompLtxMed(os,"raiz",otra)
    os << ltx_end("landscape") << std.endl

def ImprLtxCP1(self, &os):
    os << ltx_part("Cuadro de precios no. 1") << std.endl
    os << ltx_parttoc << std.endl
    os << "\\setcounter{chapter}{0}" << std.endl
    Capitulo.ImprLtxCP1(os,"raiz")
    os << "\\input{firmas}" << std.endl

def ImprLtxCP2(self, &os):
    os << ltx_part("Cuadro de precios no. 2") << std.endl
    os << ltx_parttoc << std.endl
    os << "\\setcounter{chapter}{0}" << std.endl
    Capitulo.ImprLtxCP2(os,"raiz")
    os << "\\input{firmas}" << std.endl

def ImprLtxJustPre(self, &os):
    Capitulo.ImprLtxJustPre(os,"raiz")
    os << "\\input{firmas}" << std.endl

def ImprLtxCP(self, &os):
    ImprLtxCP1(os)
    ImprLtxCP2(os)

def ImprLtxPreParc(self, &os):
    os << ltx_part("Presupuestos parciales") << std.endl
    os << ltx_parttoc << std.endl
    os << "\\setcounter{chapter}{0}" << std.endl
    Capitulo.ImprLtxPre(os,"raiz")

def ImprCompLtxPreParc(self, &otra, &os):
    os << ltx_part("Presupuestos parciales") << std.endl
    os << ltx_parttoc << std.endl
    os << "\\setcounter{chapter}{0}" << std.endl
    os << ltx_begin("landscape") << std.endl
    Capitulo.ImprCompLtxPre(os,"raiz",otra)
    os << ltx_end("landscape") << std.endl

def ImprLtxResumen(self, &os):
    os << ltx_part("Resumen de los presupuestos parciales") << std.endl
       << ltx_star_chapter("Resumen") << std.endl
    Capitulo.ImprLtxResumen(os,"raiz")

def ImprCompLtx(self, &otra, &os):
#Imprime el comparativo con otra obra.
    #ImprCompLtxMed(otra,os)
    ImprCompLtxMed(otra,os)
    precios.ImprLtxCP(os); #Cuadros de precios.
    ImprCompLtxPreParc(otra,os)
    #ImprLtxResumen(os)

def ImprLtx(self, &os):
#Imprime la obra en LaTex.
    ImprLtxMed(os); #Mediciones.
    ImprLtxCP(os); #Cuadros de precios.
    ImprLtxPreParc(os); #Presupuestos parciales.
    ImprLtxResumen(os); #Resument presup. parciales.
    ImprLtxPresGen(os); #Presupuestos generales.

def ImprLtxInformeObra(self, &os):
#Imprime en LaTeX el informe de obra.
    im = GetInformeMediciones()
    im.ImprLtx(os)

def EscribeHCalc(self, &os):
#Imprime la obra en LaTex.
    os << "Mediciones" << std.endl
    Capitulo.EscribeHCalcMed(os,"raiz")
    os << "Cuadros de precios" << std.endl
    precios.EscribeHCalc(os)
    os << "Presupuestos parciales" << std.endl
    Capitulo.EscribeHCalcPre(os,"raiz")

def SimulaDescomp(self, &origen, &destino):
    precios.SimulaDescomp(origen,destino)


