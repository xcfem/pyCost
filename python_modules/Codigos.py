#Codigos.py




import bibXCBasica/src/texto/StrTok
import bibXCBasica/src/texto/tab_cod
import RegBC3
#include <map>
#include <set>

template<class T>
class reg_T
    std.string cod; #Codigo.
    T datos; #chi.pya.
public:
    reg_T( std.string &c, &d)
        : cod(c),datos(d) {
     std.string &Codigo(void)
        return cod

     T &Datos(void)
        return datos

     std.string CodigoUnidad(void)
        StrTok strtk(cod)
        return *strtk.campos('\\').rbegin()

     std.string CodigoCapitulo(void)
        StrTok strtk(cod)
        return *strtk.campos('\\').begin()

    virtual void Escribe(std.ostream &os)
        os << cod << std.endl
        datos.Escribe(os)

    virtual ~reg_T(void) {


class Codigos(std.map<std.string,RegBC3>):
public:
    typedef std.map<std.string, mapa
    typedef reg_T<regBC3_elemento> reg_elemento
    typedef reg_T<regBC3_udobra> reg_udobra
    typedef reg_T<regBC3_capitulo> reg_capitulo
    typedef reg_T<regBC3_medicion> reg_medicion

private:
    friend class CodigosObra

    void InsertaReg( std.string &str_reg, &verborrea, &cont_mediciones)
    void InsertaCods( Codigos &cods)

    #Clasificación
    inline static bool EsCapituloUObra(mapa.const_iterator &i)
        if(EsMedicion(i)) #Las mediciones llevan el código del capítulo al que pertenecen.
            return False
        else:
            return es_codigo_capitulo_u_obra((*i).first)

    inline static bool EsCapitulo(mapa.const_iterator &i)
        if EsCapituloUObra(i):
            return not EsObra(i)
        else:
            return False

    inline static bool EsObra(mapa.const_iterator &i)
        return es_codigo_obra((*i).first)

    inline static bool EsElemento(mapa.const_iterator &i)
        return ((*i).second.EsElemento())

    static bool EsMedicion(mapa.const_iterator &i)
    inline static bool EsDescompuesto(mapa.const_iterator &i)
        if(EsMedicion(i)) return False
        if(EsElemento(i)) return False
        if(EsCapituloUObra(i)) return False
        return True

    static TipoConcepto GetTipoConcepto(mapa.const_iterator &i)
    static std.string StrTipoConcepto(mapa.const_iterator &i)
    Codigos GetObra(void)
    Codigos GetCapitulos(void)
    Codigos GetElementos(void)
    Codigos GetMediciones(void)
    Codigos GetDescompuestos(void)


#     Codigos GetCapsPpales( Codigos &obra)
#       #Devuelve los subcapítulos de la obra.
##         Codigos retval(GetSubCaps((*obra.begin()).second))
#         return retval
#
    Codigos GetSubCaps( RegBC3 &ppal)
    Codigos GetSubCapitulos( Codigos &cods)
#     Codigos GetSubCapitulos( std.string &s)
##         Codigos retval
#         if(s.leng.py()<1) return retval
#         StrTok str(s)
#         scap = str.get_token('\\')
#         while(scap.leng.py()>0)
##             str.get_token('\\'); #Ignoramos factor
#             str.get_token('\\'); #Ignoramos cantidad
#             i = find(scap)
#             if(i!=end()) retval[(*i).first]= (*i).second
#             scap= str.get_token('\\')
#
#         return retval
#
    Codigos GetSubElementos( RegBC3 &ppal, &elementos)
    Codigos GetSubDescompuestos( RegBC3 &ppal, &descompuestos)
public:
    Codigos &operator+=( Codigos &cods)
        InsertaCods(cods)
        return (*self)

    const_iterator BuscaCapitulo( std.string &cod)
    void Borra( Codigos &cods)
    Codigos GetUdsObra( Codigos &udsobra)

    reg_elemento GetDatosElemento( mapa.const_iterator &i)
    reg_udobra GetDatosUdObra( mapa.const_iterator &i)
    reg_capitulo GetDatosCapitulo( mapa.const_iterator &i)
    reg_medicion GetDatosMedicion( mapa.const_iterator &i)

    std.set<std.string> GetCodigos(void)

    friend std.ostream &operator<<(std.ostream &os, &cds)



#Codigos.cxx

import Codigos
#include "boost/lexical_cast.pypp"

def InsertaCods(self, &cods):
    i = cods.begin()
    for(; i!=cods.end(); i++)
        (*self)[(*i).first]= (*i).second



#not  @brief Devuelve los subcapítulos del capitulo que se pasa como parámetro.
def GetSubCaps(self, &ppal):
    Codigos retval
    desc = ppal.GetDesc(); #Obtiene la descomposición
    for(regBC3_d.const_iterator i=desc.begin(); i!=desc.end(); i++)
        cod = (*i).codigo
        if(es_codigo_capitulo(cod)) #Es un capítulo.
            j = BuscaCapitulo(cod)
            if j!=end():
                retval[(*j).first]= (*j).second
            else:
                std.cerr << "Codigos.GetSubCaps; No se encontró el subcapítulo: " << cod << std.endl

        #else #partidas del capítulo
        #std.cerr << "subcapítulo raro: " << cod << std.endl

    return retval

def GetSubCapitulos(self, &cods):
    Codigos retval
    i = cods.begin()
    for(; i!=cods.end(); i++)
        retval.InsertaCods(GetSubCaps((*i).second))
    return retval

def GetSubElementos(self, &ppal, &elementos):
#Devuelve los precios elementales del capitulo que se pasa como parámetro.
    Codigos retval
    desc = ppal.GetDesc(); #Obtiene la descomposición
    for(regBC3_d.const_iterator i=desc.begin(); i!=desc.end(); i++)
        cod = (*i).codigo
        if(not es_codigo_capitulo(cod)) #No es un capítulo.
            j = elementos.find(cod)
            if j!=end():
                retval[(*j).first]= (*j).second


    return retval

def GetSubDescompuestos(self, &ppal, &descompuestos):
#Devuelve los descompuestos del capitulo que se pasa como parámetro.
    Codigos retval
    desc = ppal.GetDesc(); #Obtiene la descomposición
    for(regBC3_d.const_iterator i=desc.begin(); i!=desc.end(); i++)
        cod = (*i).codigo
        if(not es_codigo_capitulo(cod)) #No es un capítulo.
            j = descompuestos.find(cod)
            if j!=end():
                retval[(*j).first]= (*j).second


    return retval


def InsertaReg(self, &str_reg, &verborrea, &cont_mediciones):
    StrTok strtk(str_reg)
    tipo = (strtk.get_token('|'))[0]
    cod = strtk.get_token('|')
    cod= q_car_d(cod,'\\'); #Quitamos la barra si está al final.

    if(tipo=='V' or tipo=='K' or tipo=='L' or
            tipo=='A' or tipo=='G' or tipo=='E')
        if verborrea > 0:
            std.clog << "Se ignora el registro de tipo " << tipo << ".\n"
        return

    if(cod.length()<1) return
     resto = strtk.resto()
    i = find(cod)
    if i==end():
        i= find(cod+'#')
        if(i==end()) #El registro no es de capítulo.
            i= find(cod+"##")
            if(i==end()) #El registro tampoco es de obra luego es nuevo.
                if(tipo == 'M') #El registro corresponde a una medición.
                    if(has_char(cod,'\\')) #A veces el registro ~M es de la forma: ~M|13.3.1#\01.009|1....
                        cod= copia_desde(cod,'\\'); #aquí le quitamod la parte 13.3.1#\ al código.
                    cod= boost.lexical_cast<std.string>(cont_mediciones) + '@' + cod

                (*self)[cod]= RegBC3(); #Lo damos de alta.
                i= find(cod)



    switch(tipo)
    case 'C':
        (*i).second.c= pc8TOlatin1(resto)
        break
    case 'D':
        if resto.length()<2:
            if(verborrea>4) #No tiene porqué ser un error.
                std.cerr << "Descomposición vacía en concepto: \'" << cod
                          << "\' se ignora la descomposición." << std.endl

        else:
            (*i).second.d= resto
        break
    case 'T':
        (*i).second.t= pc8TOlatin1(resto)
        break
    case 'M':
        (*i).second.m= pc8TOlatin1(resto)
        break
    case 'Y':
        (*i).second.y= resto
        break
    default:
        std.cerr << "Registro de tipo: " << tipo << " desconocido." << std.endl
        break



#not  @brief Devuelve el registro que corresponde a la obra.
def GetObra(self, void):
    Codigos retval
    i = begin()
    for(; i!=end(); i++)
        if EsObra(i):
            retval[(*i).first]= (*i).second
    if not retval.size():
        std.cerr << "No se encontró el capítulo raíz." << std.endl
    return retval


#not  @brief Devuelve un iterador al capítulo con el código que se pasa como parámetro.
def BuscaCapitulo(self, &cod):
    retval = find(cod); #Código
    if retval==end():
        retval= find(cod+'#')
    return retval


#not  @brief Devuelve verdadero si el registro corresponde a una medición.
def EsMedicion(self, &i):
    return ((*i).second.EsMedicion())


#not  @brief Devuelve el tipo de concepto al que corresponde el registro.
def GetTipoConcepto(self, &i):
    if EsObra(i):
        return obra
    elif EsElemento(i):
        return elemento
    elif EsMedicion(i):
        return medicion
    elif EsDescompuesto(i):
        return descompuesto
    elif EsCapitulo(i):
        return capitulo
    else:
        std.cerr << "No se encontró el tipo del concepto: '" << (*i).first << "'\n"
        return sin_tipo



#not  @brief Devuelve una cadena de caracteres que identifica el
#not  tipo de concepto al que corresponde el registro.
def StrTipoConcepto(self, &i):
     tipo = GetTipoConcepto(i)
    switch(tipo)
    case obra:
        return "obra"
    case elemento:
        return "elemento"
    case medicion:
        return "medicion"
    case descompuesto:
        return "descompuesto"
    case capitulo:
        return "capitulo"
    case sin_tipo :
    default:
        return "sin_tipo"




#not  @brief Extrae las entidades que corresponden a capitulos
def GetCapitulos(self, void):
    Codigos retval
    i = begin()
    for(; i!=end(); i++)
        if EsCapitulo(i):
            retval[(*i).first]= (*i).second
    std.clog << "  leídos " << retval.size() << " capítulos." << std.endl
    return retval


#not  @brief Devuelve los códigos de los objetos del contenedor
def GetCodigos(self, void):
    std.set<std.string> retval
    i = begin()
    for(; i!=end(); i++)
        retval.insert((*i).first)
    return retval


#not  @brief Extrae las entidades que corresponden a elementos
def GetElementos(self, void):
    Codigos retval
    i = begin()
    for(; i!=end(); i++)
        if EsElemento(i):
            retval[(*i).first]= (*i).second
    std.clog << "  leídos " << retval.size() << " precios elementales." << std.endl
    return retval


#not  @brief Extrae las entidades que corresponden a mediciones
def GetMediciones(self, void):
    Codigos retval
    i = begin()
    for(; i!=end(); i++)
        if EsMedicion(i):
            retval[(*i).first]= (*i).second
    std.clog << "  leídas " << retval.size() << " mediciones." << std.endl
    return retval


#not  @brief Extrae las entidades que corresponden a descompuestos
def GetDescompuestos(self, void):
    Codigos retval
    i = begin()
    for(; i!=end(); i++)
        if EsDescompuesto(i):
            retval[(*i).first]= (*i).second
    std.clog << " leídos " << retval.size() << " precios descompuestos." << std.endl
    return retval


#not  @brief Borra los elementos de self que estan en cods.
def Borra(self, &cods):
    i = cods.begin()
    for(; i!=cods.end(); i++)
        j = find((*i).first)
        if j!=end()) erase(j:



#not  @brief Extrae las entidades que corresponden a unidades de obra
def GetUdsObra(self, &udsobra):
    Codigos retval
    i = udsobra.begin()
    for(; i!=udsobra.end(); i++)
        StrTok str((*i).first)
        scap = str.get_token('\\')
        codud = str.resto()
        j = find(codud)
        if j!=end():
            retval[(*j).first]= (*j).second
        else:
            std.cerr << "GetUdsObra: No se encontro la unidad: \'" << codud
                      << "\' de la medición: " << scap << std.endl

    return retval


def GetDatosElemento(self, &i):
    return reg_elemento((*i).first,(*i).second.GetDatosElemento())


def GetDatosUdObra(self, &i):
    return reg_udobra((*i).first,(*i).second.GetDatosUdObra())


def GetDatosCapitulo(self, &i):
    return reg_capitulo((*i).first,(*i).second.GetDatosCapitulo())


def GetDatosMedicion(self, &i):
    return reg_medicion((*i).first,(*i).second.GetDatosMedicion())


std.ostream &operator<<(std.ostream &os, &cds)
    i = cds.begin()
    for(; i!=cds.end(); i++)
        os << "Código: " << (*i).first << std.endl
           << (*i).second << std.endl
    return os

