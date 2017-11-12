#Descompuestos.cxx

#include "Descompuestos.h"

def AgregaComponente(self, &el, &cod_ud, &cod_el, &r, &f):
    UdObra *i= Busca(cod_ud)
     Elemento *j= el.Busca(cod_el)
    if not j:
        std.cerr << "Elemento: " << cod_el
                  << " no encontrado en unidad de obra: " << cod_ud << std.endl
        exit(1)

    i.Agrega(*j,f,r)


def GetBuscador(self, void):
    return BuscadorDescompuestos(self)


#template<>
#MapaClaves<UdObra> MapaConceptos<UdObra>.claves

#not  @brief Lee las unidades de obra a falta de la descomposición.
def LeeBC3Fase1(self, &cds):
    Codigos.const_iterator i=cds.begin()
    UdObra ud
    for(; i!=cds.end(); i++)
        reg = cds.GetDatosUdObra(i)
        ud.LeeBC3Fase1(reg)
        Agrega(ud)


#not  @brief Lee la descomposición de las unidades
def LeeBC3Fase2(self, &cds, &bp):
    Codigos.const_iterator i=cds.begin()
    UdObra *ud=NULL
    error = False
    set_pendientes retval
    for(; i!=cds.end(); i++)
        reg = cds.GetDatosUdObra(i)
        ud= Busca(reg.Codigo())
        error= ud.LeeBC3Fase2(reg,bp)
        if error:
            retval.insert(reg.Codigo())

    return retval

def EscribeSpre(self, &os):
    j = begin()
    for(; j!=end(); j++)
        (*j).second.EscribeSpre(os)

def AsignaFactor(self, &f):
    j = begin()
    for(; j!=end(); j++)
        (*j).second.AsignaFactor(f)

def LeeSpre(self, &is, &elementos):
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
            UdObra unidad(cod,tit,ud)
            unidad.TextoLargo()= tit
            Agrega(unidad)
            std.string porc; #porcentaje
            getline(is,porc,'|')
            std.string descomp; #descomposición
            getline(is,descomp,'\n')
            #istrstream istr(descomp.c_str(),descomp.length())
            while(1)
                pos2 = descomp.find('|')
                cod_el = descomp.substr(0,pos2)
                descomp.replace(0,pos2+1,"")
                pos3 = descomp.find('|')
                std.string cantidad
                if pos3<1000:
                    cantidad= descomp.substr(0,pos3)
                    descomp.replace(0,pos3+1,"")

                else:
                    cantidad= descomp.substr(0,descomp.length()-1)
                if(elementos.find("%" + cod_el)!=elementos.end()) #Corresponde a un porcentaje.
                    cod_el = "%"+cod_el
                AgregaComponente(elementos,cod,cod_el,atof(cantidad.c_str()))
                if(pos3>descomp.length()) break

            if(is.peek() == 26) break

    std.string resto
    getline(is,resto,'\n')


def ImprLtxCP1(self, &os):
    if(size()<1) return
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     num_campos = 5
    os << ltx_small << std.endl
    os << "\\begin{longtable}{|l|l|p{4cm}|p{3cm}|r|}" << std.endl
       << ltx_hline << std.endl
       << "Código & Ud. & Denominación & \\multicolumn{2}{|c|}{Precio}\\\\"
       << " & & & en letra & en cifra \\\\" << std.endl
       << ltx_hline << std.endl
       << ltx_endhead << std.endl
       << ltx_hline << std.endl
       << "\\multicolumn{" << num_campos << "}{|r|}{../..}\\\\\\hline" << std.endl
       << ltx_endfoot << std.endl
       << ltx_hline << std.endl
       << ltx_endlastfoot << std.endl
    j = begin()
    for(; j!=end(); j++)
        os << linea_en_blanco << std.endl
        (*j).second.ImprLtxCP1(os)
        os << linea_en_blanco << std.endl

    os << "\\end{longtable}" << std.endl
    os << ltx_normalsize << std.endl

def ImprLtxJustPre(self, &os):
    os << ltx_small << std.endl
    os << "\\begin{longtable}{l}" << std.endl
    j = begin()
    for(; j!=end(); j++)
        (*j).second.ImprLtxJustPre(os)
        os << ltx_fin_reg << std.endl
        os << ltx_fin_reg << std.endl

    os << "\\end{longtable}" << std.endl
    os << ltx_normalsize << std.endl

def ImprLtxCP2(self, &os):
    if(size()<1) return
    #os << ltx_star_chapter("Cuadro de precios no. 2") << std.endl
    os << ltx_small << std.endl
    os << "\\begin{longtable}{l}" << std.endl
    j = begin()
    for(; j!=end(); j++)
        (*j).second.ImprLtxCP2(os)
        os << ltx_fin_reg << std.endl
        os << ltx_fin_reg << std.endl

    os << "\\end{longtable}" << std.endl
    os << ltx_normalsize << std.endl

def EscribeHCalc(self, &os):
    os << "Código" << tab
       << "Ud." << tab
       << "Denominación" << tab
       << "Precio en letra" << tab
       << "Precio en cifra" << std.endl
    j = begin()
    for(; j!=end(); j++)
        (*j).second.EscribeHCalc(os)



void  *BuscadorDescompuestos.Busca( std.string &clave)
    return contenedor.Busca(clave)

void *BuscadorDescompuestos.Busca( std.string &clave)
    return contenedor.Busca(clave)

