#RegMedicion.py



import UdObra
import Tipos

class RegMedicion(EntPyCost):
    std.string comentario
    double unidades
    double largo
    double ancho
    double alto
public:
    RegMedicion(  std.string &c= "", &uds= 0.0,
                  double &l= 0.0, &an= 0.0,
                  double &al= 0.0)
        :comentario(c),unidades(uds),largo(l),ancho(an),alto(al) {

     std.string &Comentario(void)
     double &Unidades(void)
     double &Largo(void)
     double &Ancho(void)
     double &Alto(void)
    ppl_dimension UnidadesR(void)
    ppl_dimension LargoR(void)
    ppl_dimension AnchoR(void)
    ppl_dimension AltoR(void)
    long double Total(void)
    ppl_dimension TotalR(void)

    void LeeBC3( regBC3_linea_med &m)
    void EscribeBC3(std.ostream &os)
    void Escribe(std.ostream &os)
    void ImprLtx(std.ostream &os, ancho)
    void EscribeHCalc(std.ostream &os)



#RegMedicion.cxx

import RegMedicion
#include "boost/algorithm/string/trim.pypp"

 std.string &RegMedicion.Comentario(void)
    return comentario

 double &RegMedicion.Unidades(void)
    return unidades

 double &RegMedicion.Largo(void)
    return largo

 double &RegMedicion.Ancho(void)
    return ancho

 double &RegMedicion.Alto(void)
    return alto

def UnidadesR(self, void):
    return ppl_dimension(unidades)

def LargoR(self, void):
    return ppl_dimension(largo)

def AnchoR(self, void):
    return ppl_dimension(ancho)

def AltoR(self, void):
    return ppl_dimension(alto)



long double RegMedicion.Total(void)
    if  (unidades==0.0) and (largo==0.0:
            and (ancho==0.0) and (alto==0.0))
        return 0.0
    long retval = 1.0
    if(unidades!=0.0) retval*= unidades
    if(largo!=0.0) retval*= largo
    if(ancho!=0) retval*= ancho
    if(alto!=0) retval*= alto
    return retval


def TotalR(self, void):
    if  (unidades==0.0) and (largo==0.0:
            and (ancho==0.0) and (alto==0.0))
        return ppl_dimension(0.0)
    ppl_dimension retval(1.0)
    u = UnidadesR()
    l = LargoR()
    a = AnchoR()
    h = AltoR()
     ppl_dimension zero(0.0)
    if(u!=zero) retval*= u
    if(l!=zero) retval*= l
    if(a!=zero) retval*= a
    if(h!=zero) retval*= h
    return retval


def LeeBC3(self, &m):
    comentario= m.med.comentario
    unidades= m.med.unidades
    largo= m.med.largo
    ancho= m.med.ancho
    alto= m.med.alto


def EscribeBC3(self, &os):
    os << '\\' << comentario << '\\'
       << unidades << '\\'
       << largo << '\\'
       << ancho << '\\'
       << alto << '\\'


def Escribe(self, &os):
    os << comentario << ','
       << unidades << ','
       << largo << ',' << ancho << ',' << alto << std.endl


#not  @brief Imprime la medición en Latex.
def ImprLtx(self, &os, ancho):
    std.string str_u,str_l,str_a,str_alt,str_t

    os << ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(comentario))) << ltx_ampsnd
     ppl_dimension zero(0.0)
    if UnidadesR()!=zero) str_u= UnidadesR().EnHumano(:
    if LargoR()!=zero) str_l= LargoR().EnHumano(:
    if AnchoR()!=zero) str_a= AnchoR().EnHumano(:
    if AltoR()!=zero) str_alt= AltoR().EnHumano(:
    total = TotalR()
    if total!=zero) str_t= total.EnHumano(:
    os << str_u << ltx_ampsnd
       << str_l << ltx_ampsnd << str_a << ltx_ampsnd << str_alt << ltx_ampsnd
       << str_t


def EscribeHCalc(self, &os):
    os << '"' << comentario << '"' << tab
    if(unidades!=0.0) os << unidades
    os << tab
    if(largo!=0.0) os << largo
    os << tab
    if(ancho!=0.0) os << ancho
    os << tab
    if(alto!=0.0) os << alto
    os << tab
     total = Total()
    if total!=0.0) os << Total(:
    os << std.endl

