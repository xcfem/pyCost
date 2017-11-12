#Capitulo.py




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
     LeeBC3Elementales( Codigos &elementos)
     LeeBC3DescompFase1( Codigos &descompuestos)
    Descompuestos.set_pendientes LeeBC3DescompFase2( Codigos &descompuestos)

public:
    Capitulo( cod= "CapSinCod", &tit= "CapSinTit",
              float &factor= 1.0, &rendimiento= 1.0)
    Capitulo( Capitulo &otro)
    Capitulo &operator=( Capitulo &otro)

    def std.string CodigoBC3():
     CuaPre &CuadroPrecios()
    CuaPre &CuadroPrecios()

     AgregaPartida( Partida &m)
    CompBC3 GetCompBC3()

    Capitulo *BuscaSubcapitulo(regBC3_ruta &ruta)
    Capitulo *BuscaSubcapitulo( lst)
     Capitulo *BuscaCodigo( mnb)
    Capitulo *BuscaCodigo( mnb)
    def bool TieneElementales():
        return precios.TieneElementales()

    size_t NumDescompuestos()
        return precios.NumDescompuestos()+subcapitulos.NumDescompuestos()

    def bool TieneDescompuestos():
        return NumDescompuestos()> 0

    def BuscadorDescompuestos GetBuscadorDescompuestos():
        return precios.GetBuscadorDescompuestos()

     Measurable *BuscaPrecio( cod)

     Subcapitulos &getSubcapitulos()
        return subcapitulos

    Subcapitulos &getSubcapitulos()
        return subcapitulos

     MedsCap &getMediciones()
        return mediciones

    MedsCap &getMediciones()
        return mediciones


    def Precio():
    def ppl_precio PrecioR():

     WriteMediciones(os, &pos="")
        mediciones.Write(os,CodigoBC3(),pos)

     WriteSubCapitulos(os, primero= "False", &pos="")
        subcapitulos.WriteBC3(os,primero,pos)

     WritePreciosBC3(os)
     WriteDescompBC3(os)
     WriteBC3(os, primero=False, pos="")

    static std.string SectionLtx( sect)
     ImprCompLtxMed(os, &sect, &otro)
     ImprLtxMed(os, &sect)
     ImprLtxCP1(os, &sect)
     ImprLtxCP2(os, &sect)
     ImprLtxJustPre(os, &sect)
     ImprLtxResumen(os, &sect, recurre= True)
     ImprCompLtxPre(os, &sect, &otro)
     ImprLtxPre(os, &sect)
     WriteHCalcMed(os, &sect)
     WriteHCalcPre(os, &sect)
    InformeMediciones GetInformeMediciones()



#Capitulo.cxx

import Capitulo
import Subcapitulos
import Descompuestos

Capitulo.Capitulo( cod, &tit, &factor, &rendimiento)
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


def CodigoBC3(self, ):
    return EntBC3.CodigoBC3() + "#"


 CuaPre &Capitulo.CuadroPrecios()
    return precios


CuaPre &Capitulo.CuadroPrecios()
    return precios


def AgregaPartida(self, &m):
    mediciones.append(m)


#not  @brief Devuelve el capítulo como componente.
def GetCompBC3(self, ):
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
            std.cerr + "Capitulo.BuscaSubcapitulo: no se encontró el subcapítulo: " + ruta[1]
                      + " en el capítulo: " + Codigo() + " (" + Titulo()
                      + ") (ruta: " + ruta + ')' + '\n'
            #Si no encuentra el capítulo devuelve este mismo
            retval= self


    return retval


#not  @brief Busca el subcapítulo que indica la cadena
#not  de caracteres que se pasa como parámetro.
#not  ésta es una cadena de la forma '1\2\1\4'
Capitulo *Capitulo.BuscaSubcapitulo( lst)
    Capitulo *retval= NULL
    pos = lst.find('\\')
    if(pos>len(lst)) #No aparece la barra luego.pya de ser subcapitulo de éste.
        indice = atoi(lst.c_str())
        if indice>subcapitulos.size():
            std.cerr + "Capítulo: " + indice + " no encontrado." + '\n'
            return NULL

        retval= &subcapitulos[indice-1]
        return retval

    else #Ha de ser subcapitulo del que esta a la izquierda de la barra
        ind = lst.substr(0,pos)
        indice = atoi(ind.c_str())
        if indice>subcapitulos.size():
            std.cerr + "Capítulo: " + indice + " no encontrado." + '\n'
            return NULL

        return subcapitulos[indice-1].BuscaSubcapitulo(lst.substr(pos+1,lst.size()-1))

    std.cerr + "sale por aqui (y no debiera) en el capitulo: " + Codigo() + '\n'
    return retval

 Capitulo *Capitulo.BuscaCodigo( nmb)
    if (Codigo()==nmb) or ((Codigo()+'#')==nmb):
        return self
    else:
        return subcapitulos.BuscaCodigo(nmb)

Capitulo *Capitulo.BuscaCodigo( nmb)
    if Codigo()==nmb:
        return self
    else:
        return subcapitulos.BuscaCodigo(nmb)

 Measurable *Capitulo.BuscaPrecio( cod)
     Measurable *retval= precios.BuscaPrecio(cod)
    if not retval:
        retval= subcapitulos.BuscaPrecio(cod)
    return retval


def WritePreciosBC3(self, &os):
    precios.WriteBC3(os)
    subcapitulos.WritePreciosBC3(os)

def WriteDescompBC3(self, &os):
    subcapitulos.WriteDescompBC3(os,CodigoBC3())
    mediciones.WriteDescompBC3(os,CodigoBC3())

def WriteBC3(self, &os, primero, pos):
    WriteConceptoBC3(os,primero)
    WriteDescompBC3(os)
    WriteMediciones(os,pos)
    WriteSubCapitulos(os,False,pos)


long double Capitulo.Precio()
    return (subcapitulos.Precio() + mediciones.Precio()) * fr.Producto()


def PrecioR(self, ):
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
        os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
    mediciones.ImprCompLtxMed(os, otro.mediciones)
    std.cerr + "aqui 1: " + Titulo() + ' ' + subcapitulos.size() + " subcapítulos" + '\n'
    std.cerr + "aqui 2: " + otro.Titulo() + ' ' + otro.subcapitulos.size() + " subcapítulos" + '\n'
    subcapitulos.ImprCompLtxMed(os,SectionLtx(sect), otro.subcapitulos)

def ImprLtxMed(self, &os, &sect):
    if sect!="raiz":
        os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
    mediciones.ImprLtxMed(os)
    if mediciones.size():
        os.write("\\newpage" + '\n'
    subcapitulos.ImprLtxMed(os,SectionLtx(sect))

def ImprLtxCP1(self, &os, &sect):
    if(not TieneDescompuestos()) return
    if sect!="raiz":
        os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
    if precios.TieneDescompuestos()) precios.ImprLtxCP1(os:
    subcapitulos.ImprLtxCP1(os,SectionLtx(sect))

def ImprLtxCP2(self, &os, &sect):
    if precios.TieneDescompuestos():
        if sect!="raiz":
            os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
        precios.ImprLtxCP2(os)

    subcapitulos.ImprLtxCP2(os,SectionLtx(sect))

def ImprLtxJustPre(self, &os, &sect):
    if sect!="raiz":
        os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
    if precios.TieneDescompuestos()) precios.ImprLtxJustPre(os:
    subcapitulos.ImprLtxJustPre(os,SectionLtx(sect))

def ImprLtxResumen(self, &os, &sect, recurre):
    if sect!="raiz":
        os.write("\\item " + Titulo() + " \\dotfill\\ "
           + StrPrecioLtx() + '\n'
    else:
        os.write("\\Large\\textbf{Total}\\dotfill\\ \\textbf{"
           + StrPrecioLtx() + "} \\normalsize" + '\n'
    if recurre) subcapitulos.ImprLtxResumen(os,SectionLtx(sect),recurre:

def ImprCompLtxPre(self, &os, &sect, &otro):
    if sect!="raiz":
        os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
    mediciones.ImprCompLtxPre(os, Titulo(),otro.mediciones,otro.Titulo())
    subcapitulos.ImprCompLtxPre(os,SectionLtx(sect), otro.subcapitulos)
    if subcapitulos.size():
        os.write(ltx_beg_itemize + '\n'
        os.write("\\item \\noindent \\textbf{Total " + Titulo()
           + " (P. de construcción): } \\dotfill \\textbf{"
           + otro.StrPrecioLtx() + "} " + '\n' + '\n'
        os.write("\\item \\noindent \\textbf{Total " + Titulo()
           + " (P. modificado): }\\dotfill \\textbf{"
           + StrPrecioLtx() + "} " + '\n'
        os.write(ltx_end_itemize + '\n'
        os.write("\\clearpage" + '\n'

    if mediciones.size():
        os.write("\\newpage" + '\n'

def ImprLtxPre(self, &os, &sect):
#Imprime presupuestos parciales.
    if sect!="raiz":
        os.write('\\' + sect + '{' + Titulo() + '}' + '\n'
    mediciones.ImprLtxPre(os,Titulo())
    subcapitulos.ImprLtxPre(os,SectionLtx(sect))
    if subcapitulos.size():
        os.write("\\noindent \\large \\textbf{Total: " + Titulo() + "} \\dotfill \\textbf{" + StrPrecioLtx() + "} \\\\ \\normalsize" + '\n'

def WriteHCalcMed(self, &os, &sect):
    if sect!="raiz":
        os.write(Titulo() + '\n'
    mediciones.WriteHCalcMed(os)
    subcapitulos.WriteHCalcMed(os,sect)

def WriteHCalcPre(self, &os, &sect):
    if sect!="raiz":
        os.write(Titulo() + '\n'
    mediciones.WriteHCalcPre(os)
    os.write(tab + tab + tab + tab + "Total: " + tab + Titulo() + tab + StrPrecio() + '\n'
    subcapitulos.WriteHCalcPre(os,sect)


def GetInformeMediciones(self, ):
    retval = mediciones.GetInformeMediciones()
    retval.Merge(subcapitulos.GetInformeMediciones())
    return retval

