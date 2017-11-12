#RegMedicion.py



import UdObra
import basic_types

class RegMedicion(EntPyCost):
    std.string comentario
    double unidades
    double largo
    double ancho
    double alto
public:
    RegMedicion(  c= "", &uds= 0.0,
                  double &l= 0.0, &an= 0.0,
                  double &al= 0.0)
        :comentario(c),unidades(uds),largo(l),ancho(an),alto(al) {

     Comentario()
     double &Unidades()
     double &Largo()
     double &Ancho()
     double &Alto()
    ppl_dimension UnidadesR()
    ppl_dimension LargoR()
    ppl_dimension AnchoR()
    ppl_dimension AltoR()
    long double Total()
    ppl_dimension TotalR()

     LeeBC3( regBC3_linea_med &m)
     WriteBC3(os)
     Write(os)
     ImprLtx(os, ancho)
     WriteHCalc(os)



#RegMedicion.cxx

import RegMedicion
#include "boost/algorithm/string/trim.pypp"

 RegMedicion.Comentario()
    return comentario

 double &RegMedicion.Unidades()
    return unidades

 double &RegMedicion.Largo()
    return largo

 double &RegMedicion.Ancho()
    return ancho

 double &RegMedicion.Alto()
    return alto

def UnidadesR(self, ):
    return ppl_dimension(unidades)

def LargoR(self, ):
    return ppl_dimension(largo)

def AnchoR(self, ):
    return ppl_dimension(ancho)

def AltoR(self, ):
    return ppl_dimension(alto)



long double RegMedicion.Total()
    if  (unidades==0.0) and (largo==0.0:
            and (ancho==0.0) and (alto==0.0))
        return 0.0
    long retval = 1.0
    if(unidades!=0.0) retval*= unidades
    if(largo!=0.0) retval*= largo
    if(ancho!=0) retval*= ancho
    if(alto!=0) retval*= alto
    return retval


def TotalR(self, ):
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


def WriteBC3(self, &os):
    os.write('\\' + comentario + '\\'
       + unidades + '\\'
       + largo + '\\'
       + ancho + '\\'
       + alto + '\\'


def Write(self, &os):
    os.write(comentario + ','
       + unidades + ','
       + largo + ',' + ancho + ',' + alto + '\n'


#not  @brief Imprime la medición en Latex.
def ImprLtx(self, &os, ancho):
    std.string str_u,str_l,str_a,str_alt,str_t

    os.write(ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(comentario))) + ltx_ampsnd
     ppl_dimension zero(0.0)
    if UnidadesR()!=zero) str_u= UnidadesR().EnHumano(:
    if LargoR()!=zero) str_l= LargoR().EnHumano(:
    if AnchoR()!=zero) str_a= AnchoR().EnHumano(:
    if AltoR()!=zero) str_alt= AltoR().EnHumano(:
    total = TotalR()
    if total!=zero) str_t= total.EnHumano(:
    os.write(str_u + ltx_ampsnd
       + str_l + ltx_ampsnd + str_a + ltx_ampsnd + str_alt + ltx_ampsnd
       + str_t


def WriteHCalc(self, &os):
    os.write('"' + comentario + '"' + tab
    if(unidades!=0.0) os.write(unidades
    os.write(tab
    if(largo!=0.0) os.write(largo
    os.write(tab
    if(ancho!=0.0) os.write(ancho
    os.write(tab
    if(alto!=0.0) os.write(alto
    os.write(tab
     total = Total()
    if total!=0.0) os.write(Total(:
    os.write('\n'

