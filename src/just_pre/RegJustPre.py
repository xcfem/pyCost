#RegJustPre.pyxx




import basic_types
import bibXCLcmd/src/nucleo/EntCmd


class RegJustPre(EntCmd):
    codigo= '' #Codigo del precio elemental.
    ppl_precio4 rdto; #Rendimiento.
    unidad= '' #Unidad de medida.
    titulo= '' #Descripción del precio elemental.
    bool es_porcentaje; #Verdadero si corresponde a un porcentaje.
    ppl_precio unitario; #Precio unitario o tanto por ciento si es porcentaje.
    ppl_precio3 sobre; #Base sobre la que se aplica el porcentaje.

    ppl_precio3 base()
        if es_porcentaje:
            return sobre
        else:
            return ppl_precio3(unitario)

public:
    RegJustPre()
    RegJustPre(  cod, &rd, &ud, &tit, &esporc, &unit, &b)
     SetBase( ppl_precio3 &b)
    ppl_precio3 Total()
     ImprLtxJustPre(os)
     ImprLtxCP2(os)



#RegJustPre.cxx

import RegJustPre
import bibXCBasica/src/texto/latex

RegJustPre.RegJustPre()
    : codigo(""),rdto(0.0),unidad(""),titulo(""),es_porcentaje(False),unitario(0.0),sobre(0.0) {

RegJustPre.RegJustPre(  cod, &rd, &ud, &tit, &esporc, &unit, &b)
    : codigo(cod),rdto(rd),unidad(ud),titulo(tit),es_porcentaje(esporc),unitario(unit),sobre(b) {

def SetBase(self, &b):
    sobre= b

def Total(self, ):
    ppl_precio3 retval(base())
    retval*= rdto
    return retval

def ImprLtxJustPre(self, &os):
    os.write(ascii2latex(codigo) + " & "
       + rdto.EnHumano() + " & " #Write el rendimiento
       + ascii2latex(unidad) + " & "
       + ascii2latex(titulo) + " & "
    if es_porcentaje:
        os.write(unitario.EnHumano() + ltx_porciento; #Porcentaje
    else:
        os.write(unitario.EnHumano(); #Precio unitario
    os.write(" & " + Total().EnHumano() + ltx_fin_reg + '\n'


def ImprLtxCP2(self, &os):
    os.write(" & & " + ascii2latex(titulo) + " & "
    if(es_porcentaje) os.write(Total().EnHumano(); #Total.
    os.write(ltx_fin_reg + '\n'


