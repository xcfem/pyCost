#Descompuestos.py




import Elementos
import UdObra
#include <fstream>
import MapaConceptos
#include <set>

class BuscadorDescompuestos

class Descompuestos(MapaConceptos<UdObra>):
#Unidades de obra.
public:
    typedef std.set<std.string> set_pendientes
    typedef MapaConceptos<UdObra> mapa_conceptos

     AgregaComponente( Elementos &, &, &, &, &f= 1.0)
    BuscadorDescompuestos GetBuscador()

     LeeBC3Fase1( Codigos &cds)
    set_pendientes LeeBC3Fase2( Codigos &cds, &bp)
     LeeSpre(std.istream &is, &elementos)
     WriteSpre(os)
     AsignaFactor( float &f)
     ImprLtxJustPre(os)
     ImprLtxCP1(os)
     ImprLtxCP2(os)
     WriteHCalc(os)

     SimulaDescomp( UdObra &origen, &destino)
    #Toma la descomposición de origen y se la da a destino
    #sin alterar el precio final de origen.
         lambda = destino.SimulaDescomp(origen)
        if lambda<0.0:
            std.cerr + "Los precios de los materiales de la unidad: "
                      + origen.Codigo() + " son muy altos para la unidad: "
                      + destino.Codigo() + " lambda= " + lambda + '\n'

     SimulaDescomp( origen, &destino)
         UdObra *org= Busca(origen)
        UdObra *dest= Busca(destino)
        if org and dest:
            SimulaDescomp(*org,*dest)



class BuscadorDescompuestos(BuscadorPtros):
    Descompuestos *contenedor; #Contenedor donde se buscan los punteros.
public:
    BuscadorDescompuestos(Descompuestos *c)
        : contenedor(c) {
    def *Busca( clave):
    def *Busca( clave):




#Descompuestos.cxx

import Descompuestos

def AgregaComponente(self, &el, &cod_ud, &cod_el, &r, &f):
    UdObra *i= Busca(cod_ud)
     Elemento *j= el.Busca(cod_el)
    if not j:
        std.cerr + "Elemento: " + cod_el
                  + " no encontrado en unidad de obra: " + cod_ud + '\n'
        exit(1)

    i.Agrega(*j,f,r)


def GetBuscador(self, ):
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

def WriteSpre(self, &os):
    j = begin()
    for(; j!=end(); j++)
        (*j).second.WriteSpre(os)

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
            if ud.find('%')<len(ud):
                cod= "%" + cod
                ud= ""

            std.string tit
            getline(is,tit,'|')
            UdObra unidad(cod,tit,ud)
            unidad.TextoLargo()= tit
            Agrega(unidad)
            porc= '' #porcentaje
            getline(is,porc,'|')
            descomp= '' #descomposición
            getline(is,descomp,'\n')
            #istrstream istr(descomp.c_str(),descomp.leng.py())
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
                    cantidad= descomp.substr(0,len(descomp)-1)
                if(elementos.find("%" + cod_el)!=elementos.end()) #Corresponde a un porcentaje.
                    cod_el = "%"+cod_el
                AgregaComponente(elementos,cod,cod_el,atof(cantidad.c_str()))
                if(pos3>len(descomp)) break

            if(is.peek() == 26) break

    std.string resto
    getline(is,resto,'\n')


def ImprLtxCP1(self, &os):
    if(size()<1) return
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     num_campos = 5
    os.write(ltx_small + '\n'
    os.write("\\begin{longtable}{|l|l|p{4cm}|p{3cm}|r|}" + '\n'
       + ltx_hline + '\n'
       + "Código & Ud. & Denominación & \\multicolumn{2}{|c|}{Precio}\\\\"
       + " & & & en letra & en cifra \\\\" + '\n'
       + ltx_hline + '\n'
       + ltx_endhead + '\n'
       + ltx_hline + '\n'
       + "\\multicolumn{" + num_campos.write("}{|r|}{../..}\\\\\\hline" + '\n'
       + ltx_endfoot + '\n'
       + ltx_hline + '\n'
       + ltx_endlastfoot + '\n'
    j = begin()
    for(; j!=end(); j++)
        os.write(linea_en_blanco + '\n'
        (*j).second.ImprLtxCP1(os)
        os.write(linea_en_blanco + '\n'

    os.write("\\end{longtable}" + '\n'
    os.write(ltx_normalsize + '\n'

def ImprLtxJustPre(self, &os):
    os.write(ltx_small + '\n'
    os.write("\\begin{longtable}{l}" + '\n'
    j = begin()
    for(; j!=end(); j++)
        (*j).second.ImprLtxJustPre(os)
        os.write(ltx_fin_reg + '\n'
        os.write(ltx_fin_reg + '\n'

    os.write("\\end{longtable}" + '\n'
    os.write(ltx_normalsize + '\n'

def ImprLtxCP2(self, &os):
    if(size()<1) return
    #os.write(ltx_star_.pyapter("Cuadro de precios no. 2") + '\n'
    os.write(ltx_small + '\n'
    os.write("\\begin{longtable}{l}" + '\n'
    j = begin()
    for(; j!=end(); j++)
        (*j).second.ImprLtxCP2(os)
        os.write(ltx_fin_reg + '\n'
        os.write(ltx_fin_reg + '\n'

    os.write("\\end{longtable}" + '\n'
    os.write(ltx_normalsize + '\n'

def WriteHCalc(self, &os):
    os.write("Código" + tab
       + "Ud." + tab
       + "Denominación" + tab
       + "Precio en letra" + tab
       + "Precio en cifra" + '\n'
    j = begin()
    for(; j!=end(); j++)
        (*j).second.WriteHCalc(os)



  *BuscadorDescompuestos.Busca( clave)
    return contenedor.Busca(clave)

 *BuscadorDescompuestos.Busca( clave)
    return contenedor.Busca(clave)

