#Elementos.py




import Elemento
import bibXCBasica/src/texto/cadena_carac
#include <fstream>
import MapaConceptos
import ComptesBC3
import Codigos
#include "bibXCLcmd/src/base/Buscadores.pyxx"

class BuscadorElementos

#not  @brief Tabla de precios elementales.
class Elementos(MapaConceptos<Elemento>):
protected:
    static  ImprLtxCabecera( tipo_concepto &tipo, &os)
public:
    Elementos()

    BuscadorElementos GetBuscador()

     LeeMdoSpre(std.istream &is)
     LeeMaqSpre(std.istream &is)
     LeeMatSpre(std.istream &is)
     WriteSpre()
     LeeSpre(std.istream &is)
     LeeBC3( Codigos &els)
     ImprLtxTipo( tipo_concepto &tipo, &os)
     ImprLtx(os)
     WriteHCalc(os)
        std.cerr + "Elementos.WriteHCalc no implementada." + '\n'



class BuscadorElementos(BuscadorPtros):
    Elementos *contenedor; #Contenedor donde se buscan los punteros.
public:
    BuscadorElementos(Elementos *c)
        : contenedor(c) {
    def *Busca( clave):
        return contenedor.Busca(clave)

    def *Busca( clave):
        return contenedor.Busca(clave)




#Elementos.cxx

import Elementos

#template<>
#MapaClaves<Elemento> MapaConceptos<Elemento>.claves

#not  @brief Constructor.
Elementos.Elementos()
    : MapaConceptos<Elemento>() {

def GetBuscador(self, ):
    return BuscadorElementos(self)


def ImprLtxCabecera(self, &tipo, &os):
    str_tipo = ""
    switch(tipo)
    case mdo:
        str_tipo= "mano de obra"
        break
    case maq:
        str_tipo= "maquinaria"
        break
    case mat:
        str_tipo= "materiales"
        break
    default:
        str_tipo= "sin clasificar"
        break

    os.write(ltx_begin("center") + '\n'
    os.write(ltx_large + " Precios elementales de " + str_tipo + ' '
       + ltx_normalsize + '\n'
    os.write(ltx_end("center") + '\n'
    os.write(ltx_small + '\n'
    os.write("\\begin{longtable}{|l|l|p{4cm}|r|}" + '\n'
       + ltx_hline + '\n'
       + "Código & Ud. & Denominación & Precio\\\\" + '\n'
       + ltx_hline + '\n'
       + ltx_endhead + '\n'
       + ltx_hline + '\n'
       + "\\multicolumn{" + 4 + "}{|r|}{../..}\\\\\\hline" + '\n'
       + ltx_endfoot + '\n'
       + ltx_hline + '\n'
       + ltx_endlastfoot + '\n'


def LeeMdoSpre(self, &is):
    if is.peek()!= 26:
        while(1)
            std.string cod
            getline(is,cod,'|')
            std.string ud
            getline(is,ud,'|')
            if ud.find('%')<len(ud):
                cod= "%" + cod
                ud= ""

            std.string tit
            getline(is,tit,'|')
            std.string precios
            getline(is,precios,'\n')
            std.string pre
            pos = precios.find('|')
            if pos<len(precios):
                pre= precios.substr(0,pos)
            else:
                pre= precios.substr(0,len(precios)-1)
            Elemento elem(cod,tit,ud,atof(pre.c_str()),mdo)
            elem.TextoLargo()= tit
            Agrega(elem)
            if(is.peek() == 26) break

    std.string resto
    getline(is,resto,'\n')

def LeeMaqSpre(self, &is):
    if is.peek()!= 26:
        while(1)
            std.string cod
            getline(is,cod,'|')
            std.string ud
            getline(is,ud,'|')
            if ud.find('%')<len(ud):
                cod= "%" + cod
                ud= ""

            std.string tit
            getline(is,tit,'|')
            std.string precios
            getline(is,precios,'\n')
            std.string pre
            pos = precios.find('|')
            if pos<1000:
                pre= precios.substr(0,pos)
            else:
                pre= precios.substr(0,len(precios)-1)
            Elemento elem(cod,tit,ud,atof(pre.c_str()),maq)
            elem.TextoLargo()= tit
            Agrega(elem)
            if(is.peek() == 26) break

    std.string resto
    getline(is,resto,'\n')

def LeeMatSpre(self, &is):
    if is.peek()!= 26:
        while(1)
            std.string cod
            getline(is,cod,'|')
            std.string ud
            getline(is,ud,'|')
            if ud.find('%')<len(ud):
                cod= "%" + cod
                ud= ""

            std.string tit
            getline(is,tit,'|')
            std.string precios
            getline(is,precios,'\n')
            std.string pre
            pos = precios.find('|')
            if pos<1000:
                pre= precios.substr(0,pos)
            else:
                pre= precios.substr(0,len(precios)-1)
            Elemento elem(cod,tit,ud,atof(pre.c_str()),mat)
            elem.TextoLargo()= tit
            Agrega(elem)
            if(is.peek() == 26) break

    std.string resto
    getline(is,resto,'\n')


def WriteSpre(self, ):
    std.ofstream ofs_mdo("MDO001.std",std.ios.out)
    std.ofstream ofs_maq("MAQ001.std",std.ios.out)
    std.ofstream ofs_mat("MAT001.std",std.ios.out)
    const_iterator i
    for(i= begin(); i!=end(); i++)
        switch((*i).second.Tipo())
        case mdo:
            (*i).second.WriteSpre(ofs_mdo)
            break
        case maq:
            (*i).second.WriteSpre(ofs_maq)
            break
        case mat:
            (*i).second.WriteSpre(ofs_mat)
            break
        default:
            (*i).second.WriteSpre(ofs_mdo)
            break

    ofs_mdo.close()
    ofs_maq.close()
    ofs_mat.close()


def LeeSpre(self, &is):
    std.string str
    getline(is,str,'\n')
    if str.find("[MDO]")<len(Str)) LeeMdoSpre(is:
    getline(is,Str,'\n')
    if Str.find("[MAQ]")<len(Str)) LeeMaqSpre(is:
    getline(is,Str,'\n')
    if Str.find("[MAT]")<len(Str)) LeeMatSpre(is:

def LeeBC3(self, &els):
    if not els.empty():
        if verborrea>2:
            std.clog + "Cargando precios elementales." + '\n'
         sz_inicial = size()
        Codigos.const_iterator i=els.begin()
        Elemento el
        for(; i!=els.end(); i++)
            el.LeeBC3(els.GetDatosElemento(i))
            Agrega(el)

         num_agregados = size()-sz_inicial
        if num_agregados != els.size():
            std.cerr + "¡Errornot , pasaron: " + els.size()
                      + " precios elementales y se cargaron "
                      + num_agregados.write('\n'
        if verborrea>2:
            std.clog + "Cargados " + els.size() + " precios elementales. " + '\n'


def ImprLtxTipo(self, &tipo, &os):
    ImprLtxCabecera(tipo,os)
     Elemento *el= NULL
    for(i = begin(); i!=end(); i++)
        el= &((*i).second)
        if el.Tipo() == tipo:
            el.ImprLtx(os)

    os.write("\\end{longtable}" + '\n'
    os.write(ltx_normalsize + '\n'

def ImprLtx(self, &os):
    ImprLtxTipo(mdo,os)
    os.write(ltx_newpage + '\n'
    ImprLtxTipo(maq,os)
    os.write(ltx_newpage + '\n'
    ImprLtxTipo(mat,os)

