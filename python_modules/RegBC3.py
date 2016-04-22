#RegBC3.h

#ifndef RegBC3_H
#define RegBC3_H

#include <string>
import fiebdc3

enum TipoConcepto {elemento, descompuesto, medicion, obra, capitulo, sin_tipo

struct RegBC3
    std.string c; #not  <Concepto
    std.string d; #not  <Descomposición.
    std.string m; #not  <Medicion
    std.string t; #not  <Texto
    std.string y; #not  <Descomposición.

    struct campos_reg
        StrTok.dq_campos campos_c
        StrTok.dq_campos campos_d
        StrTok.dq_campos campos_m
        StrTok.dq_campos campos_t

    regBC3_c GetConcepto(void)
    regBC3_t GetTexto(void)
    regBC3_d GetDesc(void)
    regBC3_m GetMed(void)
    bool EsElemento(void)
    bool EsMedicion(void)
    bool EsObra(void)
    bool EsCapitulo(void)
    regBC3_elemento GetDatosElemento(void)
        return regBC3_elemento(GetConcepto(),GetTexto())

    regBC3_udobra GetDatosUdObra(void)
        return regBC3_udobra(GetConcepto(),GetTexto(),GetDesc())

    regBC3_capitulo GetDatosCapitulo(void)
    regBC3_medicion GetDatosMedicion(void)
        return regBC3_medicion(GetConcepto(),GetTexto(),GetMed())

    friend std.ostream &operator<<(std.ostream &os, &r)


std.ostream &operator<<(std.ostream &os, &r)

#endif
#RegBC3.cxx

import RegBC3

def GetConcepto(self, void):
    return regBC3_c(c)


def GetTexto(self, void):
    return regBC3_t(t)


def GetDesc(self, void):
    return regBC3_d(d+y)


def GetMed(self, void):
    return regBC3_m(m)


def EsElemento(self, void):
    return ((d.length()==0) and (y.length()== 0) and (m.length()==0))


def EsMedicion(self, void):
    return (m.size()!=0)


#not  @brief Devuelve verdadero si el concepto corresponde a una obra.
def EsObra(self, void):
    return es_codigo_obra(c)


#not  @brief Devuelve verdadero si el concepto corresponde a un capitulo.
def EsCapitulo(self, void):
    return es_codigo_capitulo(c)


def GetDatosCapitulo(self, void):
    return regBC3_capitulo(GetConcepto(),GetTexto(),GetDesc())


std.ostream &operator<<(std.ostream &os, &r)
    os << "C: " << r.c << ' ' << r.c.size() << std.endl
       << "D: " << r.d << ' ' << r.d.size() << std.endl
       << "M: " << r.m << ' ' << r.m.size() << std.endl
       << "T: " << r.t << ' ' << r.t.size() << std.endl
       << "Y: " << r.y << ' ' << r.y.size() << std.endl
    return os

