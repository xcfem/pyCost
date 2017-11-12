#Elementos.cxx

#include "Elementos.h"

#template<>
#MapaClaves<Elemento> MapaConceptos<Elemento>.claves

#not  @brief Constructor.
Elementos.Elementos(void)
    : MapaConceptos<Elemento>() {

def GetBuscador(self, void):
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

    os << ltx_begin("center") << std.endl
    os << ltx_large << " Precios elementales de " << str_tipo << ' '
       << ltx_normalsize << std.endl
    os << ltx_end("center") << std.endl
    os << ltx_small << std.endl
    os << "\\begin{longtable}{|l|l|p{4cm}|r|}" << std.endl
       << ltx_hline << std.endl
       << "Código & Ud. & Denominación & Precio\\\\" << std.endl
       << ltx_hline << std.endl
       << ltx_endhead << std.endl
       << ltx_hline << std.endl
       << "\\multicolumn{" << 4 << "}{|r|}{../..}\\\\\\hline" << std.endl
       << ltx_endfoot << std.endl
       << ltx_hline << std.endl
       << ltx_endlastfoot << std.endl


def LeeMdoSpre(self, &is):
    if is.peek()!= 26:
        while(1)
            std.string cod
            getline(is,cod,'|')
            std.string ud
            getline(is,ud,'|')
            if ud.find('%')<ud.length():
                cod= "%" + cod
                ud= ""

            std.string tit
            getline(is,tit,'|')
            std.string precios
            getline(is,precios,'\n')
            std.string pre
            pos = precios.find('|')
            if pos<precios.length():
                pre= precios.substr(0,pos)
            else:
                pre= precios.substr(0,precios.length()-1)
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
            if ud.find('%')<ud.length():
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
                pre= precios.substr(0,precios.length()-1)
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
            if ud.find('%')<ud.length():
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
                pre= precios.substr(0,precios.length()-1)
            Elemento elem(cod,tit,ud,atof(pre.c_str()),mat)
            elem.TextoLargo()= tit
            Agrega(elem)
            if(is.peek() == 26) break

    std.string resto
    getline(is,resto,'\n')


def EscribeSpre(self, void):
    std.ofstream ofs_mdo("MDO001.std",std.ios.out)
    std.ofstream ofs_maq("MAQ001.std",std.ios.out)
    std.ofstream ofs_mat("MAT001.std",std.ios.out)
    const_iterator i
    for(i= begin(); i!=end(); i++)
        switch((*i).second.Tipo())
        case mdo:
            (*i).second.EscribeSpre(ofs_mdo)
            break
        case maq:
            (*i).second.EscribeSpre(ofs_maq)
            break
        case mat:
            (*i).second.EscribeSpre(ofs_mat)
            break
        default:
            (*i).second.EscribeSpre(ofs_mdo)
            break

    ofs_mdo.close()
    ofs_maq.close()
    ofs_mat.close()


def LeeSpre(self, &is):
    std.string str
    getline(is,str,'\n')
    if str.find("[MDO]")<str.length()) LeeMdoSpre(is:
    getline(is,str,'\n')
    if str.find("[MAQ]")<str.length()) LeeMaqSpre(is:
    getline(is,str,'\n')
    if str.find("[MAT]")<str.length()) LeeMatSpre(is:

def LeeBC3(self, &els):
    if not els.empty():
        if verborrea>2:
            std.clog << "Cargando precios elementales." << std.endl
         sz_inicial = size()
        Codigos.const_iterator i=els.begin()
        Elemento el
        for(; i!=els.end(); i++)
            el.LeeBC3(els.GetDatosElemento(i))
            Agrega(el)

         num_agregados = size()-sz_inicial
        if num_agregados != els.size():
            std.cerr << "¡Errornot , pasaron: " << els.size()
                      << " precios elementales y se cargaron "
                      << num_agregados << std.endl
        if verborrea>2:
            std.clog << "Cargados " << els.size() << " precios elementales. " << std.endl


def ImprLtxTipo(self, &tipo, &os):
    ImprLtxCabecera(tipo,os)
     Elemento *el= NULL
    for(i = begin(); i!=end(); i++)
        el= &((*i).second)
        if el.Tipo() == tipo:
            el.ImprLtx(os)

    os << "\\end{longtable}" << std.endl
    os << ltx_normalsize << std.endl

def ImprLtx(self, &os):
    ImprLtxTipo(mdo,os)
    os << ltx_newpage << std.endl
    ImprLtxTipo(maq,os)
    os << ltx_newpage << std.endl
    ImprLtxTipo(mat,os)

