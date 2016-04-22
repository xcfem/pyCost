#Codigos.h

#ifndef CODIGOS_H
#define CODIGOS_H

#include "bibXCBasica/src/texto/StrTok.h"
#include "bibXCBasica/src/texto/tab_cod.h"
#include "RegBC3.h"
#include <map>
#include <set>

template<class T>
class reg_T
    std.string cod; #Codigo.
    T datos; #chicha.
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


class Codigos: public std.map<std.string,RegBC3>
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
#         if(s.length()<1) return retval
#         StrTok str(s)
#         scap = str.get_token('\\')
#         while(scap.length()>0)
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


#endif
