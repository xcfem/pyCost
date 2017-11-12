#CuaPre.cxx

#include "CuaPre.h"
#include "CodigosObra.h"

def LeeBC3DescompFase2(self, &descomp):
    Buscadores bp
    b_elem = elementos.GetBuscador()
    bp["elementos"]= &b_elem
    b_desc = unidades.GetBuscador()
    bp["ud_obra"]= &b_desc
    return unidades.LeeBC3Fase2(descomp,bp)

 UdObra *CuaPre.BuscaUdObra( std.string &cod)
    return unidades.Busca(cod)

 Elemento *CuaPre.BuscaElemento( std.string &cod)
    return elementos.Busca(cod)

 Medible *CuaPre.BuscaPrecio( std.string &cod)
     Medible *retval= BuscaUdObra(cod)
    if not retval:
        retval= BuscaElemento(cod)
    return retval


def EscribeSpre(self, void):
    elementos.EscribeSpre()
    std.ofstream ofs_des("DES001.std",std.ios.out)
    unidades.EscribeSpre(ofs_des)
    ofs_des.close()

def EscribeBC3(self, &os):
    elementos.EscribeBC3(os)
    unidades.EscribeBC3(os)

def LeeSpre(self, &is):
    elementos.LeeSpre(is)
    std.string str
    getline(is,str,'\n')
    if str.find("[DES]")<str.length()) unidades.LeeSpre(is,elementos:


#not  @brief Escribe los precios elementales.
def ImprLtxElementales(self, &os):
    elementos.ImprLtx(os)


#not  @brief Escribe la justificación de precios.
def ImprLtxJustPre(self, &os):
    unidades.ImprLtxJustPre(os)


#not  @brief Escribe el cuadro de precios número 1.
def ImprLtxCP1(self, &os):
    unidades.ImprLtxCP1(os)

#not  @brief Escribe el cuadro de precios número 2.
def ImprLtxCP2(self, &os):
    unidades.ImprLtxCP2(os)

#not  @brief Escribe los cuadros de precios números 1 y 2.
def ImprLtxCP(self, &os):
    ImprLtxCP1(os)
    ImprLtxCP2(os)


def EscribeHCalc(self, &os):
    elementos.EscribeHCalc(os)
    unidades.EscribeHCalc(os)


def SimulaDescomp(self, &origen, &destino):
    unidades.SimulaDescomp(origen,destino)

