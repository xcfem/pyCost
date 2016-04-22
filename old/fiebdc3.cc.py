#fiebdc3.cc

#include "fiebdc3.h"
#include "boost/lexical_cast.hpp"

#not  @brief Devuelve verdadero si el código corresponde a una obra.
def es_codigo_obra(self, &c):
     sz = c.size()
    if sz>1:
        return ((c[sz-2]=='#') and (c[sz-1]=='#'))

    else:
        return False


#not  @brief Devuelve verdadero si el código corresponde a un capítulo.
def es_codigo_capitulo(self, &c):
    retval = False
     sz = c.length()
    if es_codigo_capitulo_u_obra(c):
        if sz<2:
            retval= True; #Capítulo sin nombre.
        else:
            retval= (c[sz-2]!='#'); #Si no es obra, capítulo.

    return retval


def es_codigo_capitulo_u_obra(self, &c):
     sz = c.length()
    if sz>0:
        return (c[sz-1]=='#')
    else:
        return False


def limpia_str(self, &str):
    return q_car(q_car(str,char(10)),char(13))


std.ostream &operator<<(std.ostream &os, &r)
    r.Escribe(os)
    return os


def decod_str_bc3(self, &str):
    if not str.empty():
        StrTok strtk(limpia_str(str))
        decod_bc3(strtk)



regBC3_desc.regBC3_desc( std.string &str)
    decod_str_bc3(limpia_str(str))


#not  @brief Decodifica la cadena str
StrTok &regBC3_desc.decod_bc3(StrTok &strtk)
    codigo= strtk.get_token('\\')
    tmp = strtk.get_token('\\')
    if not tmp.empty():
        factor= boost.lexical_cast<float>(tmp)
    if(factor==0.0) factor= 1.0; #Por defecto factor=1.0
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        rendimiento= boost.lexical_cast<float>(tmp)
    return strtk


regBC3_d.regBC3_d( std.string &str)
    decod_str_bc3(limpia_str(str))


StrTok &regBC3_d.decod_bc3(StrTok &strtk)
#La cadena que se pasa es la que queda a la derecha
#de ~D|
    strtk_lista_desc = strtk.get_token('|')
    regBC3_lista_desc.decod_bc3(strtk_lista_desc)
    return strtk


#not  @brief Devuelve verdadero si el registro corresponde a un capítulo.
def EsCapitulo(self, &r, &nombres_capitulo):
    retval = r.EsCapitulo()
    if not retval:
        retval= (nombres_capitulo.find(r.codigo+'#')!= nombres_capitulo.end())
    return retval


#not  @brief Devuelve los elementos de la descomposición que son capítulos.
def FiltraCapitulos(self, &nombres_capitulo):
    regBC3_d retval
    for(i = 0; i<size(); i++)
        if EsCapitulo((*self)[i],nombres_capitulo):
            retval.push_back((*self)[i])
    return retval

#not  @brief Devuelve los elementos de la descomposición que son precios elementales o descompuestos.
def FiltraPrecios(self, &nombres_capitulo):
    regBC3_d retval
    for(i = 0; i<size(); i++)
        if not EsCapitulo((*self)[i],nombres_capitulo):
            retval.push_back((*self)[i])
    return retval



#not  @brief Decodifica la cadena str
StrTok &regBC3_ruta.decod_bc3(StrTok &strtk)
    StrTok.dq_campos.operator=(strtk.campos('\\'))
    return strtk



def Escribe(self, &os):
    str = "Capitulo: "
    for(i = 0; i<Capitulos(); i++)
        os << str << (*self)[i] << std.endl
        str= "Sub" + str

    os << "Posición: " << Posicion()



StrTok &MedArq.decod_bc3(StrTok &strtk)
#Decodifica la cadena str
    unidades= 1
    largo= 1
    ancho= 1
    alto= 1
    comentario= strtk.get_token('\\')
    tmp = strtk.get_token('\\')
    if not tmp.empty():
        unidades= boost.lexical_cast<double>(tmp)
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        largo= boost.lexical_cast<double>(tmp)
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        ancho= boost.lexical_cast<double>(tmp)
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        alto= boost.lexical_cast<double>(tmp)
    return strtk


def Escribe(self, &os):
    os << "Comentario: " << comentario << std.endl
       << "Unidades: " << unidades << std.endl
       << "Largo: " << largo << std.endl
       << "Ancho: " << ancho << std.endl
       << "Alto: " << alto << std.endl


regBC3_linea_med.regBC3_linea_med( std.string &str)
    decod_str_bc3(limpia_str(str))


#not  @brief Decodifica la cadena str
StrTok &regBC3_linea_med.decod_bc3(StrTok &strtk)
     tmp = strtk.get_token('\\')
    if not tmp.empty():
        tipo= boost.lexical_cast<short int>(tmp)
    return med.decod_bc3(strtk)


def Escribe(self, &os):
    os << "Tipo: " << tipo << std.endl
    med.Escribe(os)


regBC3_m.regBC3_m( std.string &str)
    decod_str_bc3(limpia_str(str))


#not  @brief Decodifica un registro de tipo medición (~M).
StrTok &regBC3_m.decod_bc3(StrTok &strtk)
#La cadena que se pasa es la que queda a la derecha
#de ~M|
    strtk_ruta = strtk.get_token('|')
    ruta.decod_bc3(strtk_ruta)
    tmp = strtk.get_token('|')
    if not tmp.empty():
        med_total= boost.lexical_cast<double>(tmp)
    strtk_lista_med = strtk.get_token('|')
    lista_med.decod_bc3(strtk_lista_med)
    return strtk


def Escribe(self, &os):
    os << "Ruta: "
    ruta.Escribe(os)
    os << std.endl << "Total: " << med_total << std.endl
    lista_med.Escribe(os)


regBC3_c.regBC3_c( std.string &str)
    decod_str_bc3(limpia_str(str))


StrTok &regBC3_c.decod_bc3(StrTok &strtk)
#Decodifica la cadena str
    unidad= strtk.get_token('|')
    resumen= strtk.get_token('|')
    tmp = strtk.get_token('|')
    if not tmp.empty():
        precio= boost.lexical_cast<double>(tmp)
    fecha= strtk.get_token('|')
    tmp= strtk.get_token('|')
    if not tmp.empty():
        tipo= boost.lexical_cast<short int>(tmp)
    return strtk


def Escribe(self, &os):
    os << "Unidad: " << unidad << std.endl
       << "Resumen: " << resumen << std.endl
       << "Precio: " << precio << std.endl
       << "Fecha: " << fecha << std.endl
       << "Tipo: " << tipo << std.endl



regBC3_t.regBC3_t( std.string &str)
    decod_str_bc3(limpia_str(str))


StrTok &regBC3_t.decod_bc3(StrTok &strtk)
#Decodifica la cadena str
    texto= strtk.get_token('|')
    return strtk


def Escribe(self, &os):
    os << "Texto: " << texto << std.endl


std.ostream &operator<<(std.ostream &os, &e)
    e.Escribe(os)
    return os


std.ostream &operator<<(std.ostream &os, &rm)
    rm.Escribe(os)
    return os


regBC3_capitulo.regBC3_capitulo( regBC3_c &c, &t, &d)
    : regBC3_udobra(c,t,d) {

def FiltraCapitulos(self, &nombres_capitulo):
    return desc.FiltraCapitulos(nombres_capitulo)

