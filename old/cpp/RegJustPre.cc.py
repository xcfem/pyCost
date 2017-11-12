#RegJustPre.cxx

#include "RegJustPre.h"
#include "bibXCBasica/src/texto/latex.h"

RegJustPre.RegJustPre(void)
    : codigo(""),rdto(0.0),unidad(""),titulo(""),es_porcentaje(False),unitario(0.0),sobre(0.0) {

RegJustPre.RegJustPre( std.string & cod, &rd, &ud, &tit, &esporc, &unit, &b)
    : codigo(cod),rdto(rd),unidad(ud),titulo(tit),es_porcentaje(esporc),unitario(unit),sobre(b) {

def SetBase(self, &b):
    sobre= b

def Total(self, void):
    ppl_precio3 retval(base())
    retval*= rdto
    return retval

def ImprLtxJustPre(self, &os):
    os << ascii2latex(codigo) << " & "
       << rdto.EnHumano() << " & " #Escribe el rendimiento
       << ascii2latex(unidad) << " & "
       << ascii2latex(titulo) << " & "
    if es_porcentaje:
        os << unitario.EnHumano() << ltx_porciento; #Porcentaje
    else:
        os << unitario.EnHumano(); #Precio unitario
    os << " & " << Total().EnHumano() << ltx_fin_reg << std.endl


def ImprLtxCP2(self, &os):
    os << " & & " << ascii2latex(titulo) << " & "
    if(es_porcentaje) os << Total().EnHumano(); #Total.
    os << ltx_fin_reg << std.endl


