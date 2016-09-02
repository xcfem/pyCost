#RegJustPre.pyxx




import ../Tipos
import bibXCLcmd/src/nucleo/EntCmd


class RegJustPre(EntCmd):
    std.string codigo; #Codigo del precio elemental.
    ppl_precio4 rdto; #Rendimiento.
    std.string unidad; #Unidad de medida.
    std.string titulo; #Descripción del precio elemental.
    bool es_porcentaje; #Verdadero si corresponde a un porcentaje.
    ppl_precio unitario; #Precio unitario o tanto por ciento si es porcentaje.
    ppl_precio3 sobre; #Base sobre la que se aplica el porcentaje.

    ppl_precio3 base(void)
        if es_porcentaje:
            return sobre
        else:
            return ppl_precio3(unitario)

public:
    RegJustPre(void)
    RegJustPre( std.string & cod, &rd, &ud, &tit, &esporc, &unit, &b)
    void SetBase( ppl_precio3 &b)
    ppl_precio3 Total(void)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)



#RegJustPre.cxx

import RegJustPre
import bibXCBasica/src/texto/latex

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


