#Capitulo.h

#ifndef CAPITULO_H
#define CAPITULO_H

import MedsCap
import EntFR
import Subcapitulos
import CuaPre


class Capitulo(EntBC3):
private:
    EntFR fr
    MedsCap mediciones
protected:
    CuaPre precios; #Para precios elementales y descompuestos clasificados por capítulos.
    Subcapitulos subcapitulos

    friend class Subcapitulos
    void LeeBC3Elementales( Codigos &elementos)
    void LeeBC3DescompFase1( Codigos &descompuestos)
    Descompuestos.set_pendientes LeeBC3DescompFase2( Codigos &descompuestos)

public:
    Capitulo( std.string &cod= "CapSinCod", &tit= "CapSinTit",
              float &factor= 1.0, &rendimiento= 1.0)
    Capitulo( Capitulo &otro)
    Capitulo &operator=( Capitulo &otro)

    virtual std.string CodigoBC3(void)
     CuaPre &CuadroPrecios(void)
    CuaPre &CuadroPrecios(void)

    void AgregaPartida( Partida &m)
    CompBC3 GetCompBC3(void)

    Capitulo *BuscaSubcapitulo(regBC3_ruta &ruta)
    Capitulo *BuscaSubcapitulo( std.string &lst)
     Capitulo *BuscaCodigo( std.string &mnb)
    Capitulo *BuscaCodigo( std.string &mnb)
    inline bool TieneElementales(void)
        return precios.TieneElementales()

    size_t NumDescompuestos(void)
        return precios.NumDescompuestos()+subcapitulos.NumDescompuestos()

    inline bool TieneDescompuestos(void)
        return NumDescompuestos()> 0

    inline BuscadorDescompuestos GetBuscadorDescompuestos(void)
        return precios.GetBuscadorDescompuestos()

     Medible *BuscaPrecio( std.string &cod)

     Subcapitulos &getSubcapitulos(void)
        return subcapitulos

    Subcapitulos &getSubcapitulos(void)
        return subcapitulos

     MedsCap &getMediciones(void)
        return mediciones

    MedsCap &getMediciones(void)
        return mediciones


    virtual long double Precio(void)
    virtual ppl_precio PrecioR(void)

    void EscribeMediciones(std.ostream &os, &pos="")
        mediciones.Escribe(os,CodigoBC3(),pos)

    void EscribeSubCapitulos(std.ostream &os, primero= "False", &pos="")
        subcapitulos.EscribeBC3(os,primero,pos)

    void EscribePreciosBC3(std.ostream &os)
    void EscribeDescompBC3(std.ostream &os)
    void EscribeBC3(std.ostream &os, primero=False, pos="")

    static std.string SectionLtx( std.string &sect)
    void ImprCompLtxMed(std.ostream &os, &sect, &otro)
    void ImprLtxMed(std.ostream &os, &sect)
    void ImprLtxCP1(std.ostream &os, &sect)
    void ImprLtxCP2(std.ostream &os, &sect)
    void ImprLtxJustPre(std.ostream &os, &sect)
    void ImprLtxResumen(std.ostream &os, &sect, recurre= True)
    void ImprCompLtxPre(std.ostream &os, &sect, &otro)
    void ImprLtxPre(std.ostream &os, &sect)
    void EscribeHCalcMed(std.ostream &os, &sect)
    void EscribeHCalcPre(std.ostream &os, &sect)
    InformeMediciones GetInformeMediciones(void)


#endif
#Capitulo.cxx

import Capitulo
import Subcapitulos
import Descompuestos

Capitulo.Capitulo( std.string &cod, &tit, &factor, &rendimiento)
    : EntBC3(cod,tit), fr(factor,rendimiento), subcapitulos(*self) {

Capitulo.Capitulo( Capitulo &otro)
    : EntBC3(otro), fr(otro.fr), mediciones(otro.mediciones), subcapitulos(otro.subcapitulos)
    subcapitulos.set_owner(self)


Capitulo &Capitulo.operator=( Capitulo &otro)
    EntBC3.operator=(otro)
    fr= otro.fr
    mediciones= otro.mediciones
    subcapitulos= otro.subcapitulos
    return *self


def CodigoBC3(self, void):
    return EntBC3.CodigoBC3() + "#"


 CuaPre &Capitulo.CuadroPrecios(void)
    return precios


CuaPre &Capitulo.CuadroPrecios(void)
    return precios


def AgregaPartida(self, &m):
    mediciones.push_back(m)


#not  @brief Devuelve el capítulo como componente.
def GetCompBC3(self, void):
    return CompBC3(*self,fr)


#not  @brief Agrega los precios elementales que se pasan como parámetro
def LeeBC3Elementales(self, &elementos):
    precios.LeeBC3Elementales(elementos)

def LeeBC3DescompFase1(self, &descompuestos):
    precios.LeeBC3DescompFase1(descompuestos)

def LeeBC3DescompFase2(self, &descompuestos):
    return precios.LeeBC3DescompFase2(descompuestos)


Capitulo *Capitulo.BuscaSubcapitulo(regBC3_ruta &ruta)
    Capitulo *retval= NULL
    if not ruta.empty():
        retval= subcapitulos.Busca(ruta)
        if not retval:
            std.cerr << "Capitulo.BuscaSubcapitulo: no se encontró el subcapítulo: " << ruta[1]
                      << " en el capítulo: " << Codigo() << " (" << Titulo()
                      << ") (ruta: " << ruta << ')' << std.endl
            #Si no encuentra el capítulo devuelve este mismo
            retval= self


    return retval


#not  @brief Busca el subcapítulo que indica la cadena
#not  de caracteres que se pasa como parámetro.
#not  ésta es una cadena de la forma '1\2\1\4'
Capitulo *Capitulo.BuscaSubcapitulo( std.string &lst)
    Capitulo *retval= NULL
    pos = lst.find('\\')
    if(pos>lst.length()) #No aparece la barra luego ha de ser subcapitulo de éste.
        indice = atoi(lst.c_str())
        if indice>subcapitulos.size():
            std.cerr << "Capítulo: " << indice << " no encontrado." << std.endl
            return NULL

        retval= &subcapitulos[indice-1]
        return retval

    else #Ha de ser subcapitulo del que esta a la izquierda de la barra
        ind = lst.substr(0,pos)
        indice = atoi(ind.c_str())
        if indice>subcapitulos.size():
            std.cerr << "Capítulo: " << indice << " no encontrado." << std.endl
            return NULL

        return subcapitulos[indice-1].BuscaSubcapitulo(lst.substr(pos+1,lst.size()-1))

    std.cerr << "sale por aqui (y no debiera) en el capitulo: " << Codigo() << std.endl
    return retval

 Capitulo *Capitulo.BuscaCodigo( std.string &nmb)
    if (Codigo()==nmb) or ((Codigo()+'#')==nmb):
        return self
    else:
        return subcapitulos.BuscaCodigo(nmb)

Capitulo *Capitulo.BuscaCodigo( std.string &nmb)
    if Codigo()==nmb:
        return self
    else:
        return subcapitulos.BuscaCodigo(nmb)

 Medible *Capitulo.BuscaPrecio( std.string &cod)
     Medible *retval= precios.BuscaPrecio(cod)
    if not retval:
        retval= subcapitulos.BuscaPrecio(cod)
    return retval


def EscribePreciosBC3(self, &os):
    precios.EscribeBC3(os)
    subcapitulos.EscribePreciosBC3(os)

def EscribeDescompBC3(self, &os):
    subcapitulos.EscribeDescompBC3(os,CodigoBC3())
    mediciones.EscribeDescompBC3(os,CodigoBC3())

def EscribeBC3(self, &os, primero, pos):
    EscribeConceptoBC3(os,primero)
    EscribeDescompBC3(os)
    EscribeMediciones(os,pos)
    EscribeSubCapitulos(os,False,pos)


long double Capitulo.Precio(void)
    return (subcapitulos.Precio() + mediciones.Precio()) * fr.Producto()


def PrecioR(self, void):
    retval = subcapitulos.PrecioR() + mediciones.PrecioR()
    retval*= fr.Producto()
    return retval


#Devuelve la sección pasándole la del padre.
def SectionLtx(self, &sect):
    if sect == "raiz":
        return "chapter"
    elif sect == "chapter":
        return "section"
    elif sect == "section":
        return "subsection"
    elif sect == "subsection":
        return "subsubsection"
    elif sect == "subsubsection":
        return "paragraph"
    elif sect == "paragraph":
        return "subparagraph"
    else:
        return "xxx"


def ImprCompLtxMed(self, &os, &sect, &otro):
    if sect!="raiz":
        os << '\\' << sect << '{' << Titulo() << '}' << std.endl
    mediciones.ImprCompLtxMed(os, otro.mediciones)
    std.cerr << "aqui 1: " << Titulo() << ' ' << subcapitulos.size() << " subcapítulos" << std.endl
    std.cerr << "aqui 2: " << otro.Titulo() << ' ' << otro.subcapitulos.size() << " subcapítulos" << std.endl
    subcapitulos.ImprCompLtxMed(os,SectionLtx(sect), otro.subcapitulos)

def ImprLtxMed(self, &os, &sect):
    if sect!="raiz":
        os << '\\' << sect << '{' << Titulo() << '}' << std.endl
    mediciones.ImprLtxMed(os)
    if mediciones.size():
        os << "\\newpage" << std.endl
    subcapitulos.ImprLtxMed(os,SectionLtx(sect))

def ImprLtxCP1(self, &os, &sect):
    if(not TieneDescompuestos()) return
    if sect!="raiz":
        os << '\\' << sect << '{' << Titulo() << '}' << std.endl
    if precios.TieneDescompuestos()) precios.ImprLtxCP1(os:
    subcapitulos.ImprLtxCP1(os,SectionLtx(sect))

def ImprLtxCP2(self, &os, &sect):
    if precios.TieneDescompuestos():
        if sect!="raiz":
            os << '\\' << sect << '{' << Titulo() << '}' << std.endl
        precios.ImprLtxCP2(os)

    subcapitulos.ImprLtxCP2(os,SectionLtx(sect))

def ImprLtxJustPre(self, &os, &sect):
    if sect!="raiz":
        os << '\\' << sect << '{' << Titulo() << '}' << std.endl
    if precios.TieneDescompuestos()) precios.ImprLtxJustPre(os:
    subcapitulos.ImprLtxJustPre(os,SectionLtx(sect))

def ImprLtxResumen(self, &os, &sect, recurre):
    if sect!="raiz":
        os << "\\item " << Titulo() << " \\dotfill\\ "
           << StrPrecioLtx() << std.endl
    else:
        os << "\\Large\\textbf{Total}\\dotfill\\ \\textbf{"
           << StrPrecioLtx() << "} \\normalsize" << std.endl
    if recurre) subcapitulos.ImprLtxResumen(os,SectionLtx(sect),recurre:

def ImprCompLtxPre(self, &os, &sect, &otro):
    if sect!="raiz":
        os << '\\' << sect << '{' << Titulo() << '}' << std.endl
    mediciones.ImprCompLtxPre(os, Titulo(),otro.mediciones,otro.Titulo())
    subcapitulos.ImprCompLtxPre(os,SectionLtx(sect), otro.subcapitulos)
    if subcapitulos.size():
        os << ltx_beg_itemize << std.endl
        os << "\\item \\noindent \\textbf{Total " << Titulo()
           << " (P. de construcción): } \\dotfill \\textbf{"
           << otro.StrPrecioLtx() << "} " << std.endl << std.endl
        os << "\\item \\noindent \\textbf{Total " << Titulo()
           << " (P. modificado): }\\dotfill \\textbf{"
           << StrPrecioLtx() << "} " << std.endl
        os << ltx_end_itemize << std.endl
        os << "\\clearpage" << std.endl

    if mediciones.size():
        os << "\\newpage" << std.endl

def ImprLtxPre(self, &os, &sect):
#Imprime presupuestos parciales.
    if sect!="raiz":
        os << '\\' << sect << '{' << Titulo() << '}' << std.endl
    mediciones.ImprLtxPre(os,Titulo())
    subcapitulos.ImprLtxPre(os,SectionLtx(sect))
    if subcapitulos.size():
        os << "\\noindent \\large \\textbf{Total: " << Titulo() << "} \\dotfill \\textbf{" << StrPrecioLtx() << "} \\\\ \\normalsize" << std.endl

def EscribeHCalcMed(self, &os, &sect):
    if sect!="raiz":
        os << Titulo() << std.endl
    mediciones.EscribeHCalcMed(os)
    subcapitulos.EscribeHCalcMed(os,sect)

def EscribeHCalcPre(self, &os, &sect):
    if sect!="raiz":
        os << Titulo() << std.endl
    mediciones.EscribeHCalcPre(os)
    os << tab << tab << tab << tab << "Total: " << tab << Titulo() << tab << StrPrecio() << std.endl
    subcapitulos.EscribeHCalcPre(os,sect)


def GetInformeMediciones(self, void):
    retval = mediciones.GetInformeMediciones()
    retval.Merge(subcapitulos.GetInformeMediciones())
    return retval

