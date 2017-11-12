#RegBC3.py




#include <string>
import fiebdc3

enum TipoConcepto {elemento, descompuesto, medicion, obra, capitulo, sin_tipo

class RegBC3
    c= '' #not  <Concepto
    d= '' #not  <Descomposición.
    m= '' #not  <Medicion
    t= '' #not  <Texto
    y= '' #not  <Descomposición.

    class campos_reg
        StrTok.dq_campos campos_c
        StrTok.dq_campos campos_d
        StrTok.dq_campos campos_m
        StrTok.dq_campos campos_t

    regBC3_c GetConcepto()
    regBC3_t GetTexto()
    regBC3_d GetDesc()
    regBC3_m GetMed()
    bool EsElemento()
    bool EsMedicion()
    bool EsObra()
    bool EsCapitulo()
    regBC3_elemento GetDatosElemento()
        return regBC3_elemento(GetConcepto(),GetTexto())

    regBC3_udobra GetDatosUdObra()
        return regBC3_udobra(GetConcepto(),GetTexto(),GetDesc())

    regBC3_capitulo GetDatosCapitulo()
    regBC3_medicion GetDatosMedicion()
        return regBC3_medicion(GetConcepto(),GetTexto(),GetMed())

    friend operator<<(os, r)


operator<<(os, r)


#RegBC3.cxx

import RegBC3

    def GetConcepto(self):
        return regBC3_c(c)


    def GetTexto(self):
        return regBC3_t(t)


    def GetDesc(self):
        return regBC3_d(d+y)


    def GetMed(self):
        return regBC3_m(m)


    def EsElemento(self):
        return ((len(d)==0) and (len(y)== 0) and (len(m)==0))


    def EsMedicion(self):
        return (m.size()!=0)


    #not  @brief Devuelve verdadero si el concepto corresponde a una obra.
    def EsObra(self):
        return es_codigo_obra(c)


    #not  @brief Devuelve verdadero si el concepto corresponde a un capitulo.
    def EsCapitulo(self):
        return es_codigo_capitulo(c)


    def GetDatosCapitulo(self):
        return regBC3_capitulo(GetConcepto(),GetTexto(),GetDesc())


    operator<<(os, r)
        os.write("C: " + r.c + ' ' + r.c.size() + '\n'
           + "D: " + r.d + ' ' + r.d.size() + '\n'
           + "M: " + r.m + ' ' + r.m.size() + '\n'
           + "T: " + r.t + ' ' + r.t.size() + '\n'
           + "Y: " + r.y + ' ' + r.y.size() + '\n'
        return os

