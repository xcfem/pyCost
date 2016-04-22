#RegBC3.cxx

#include "RegBC3.h"

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

