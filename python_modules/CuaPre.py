#CuaPre.h

#ifndef CUAPRE_H
#define CUAPRE_H

import Elementos
import Descompuestos

class CuaPre(EntPyCost):
private:
    Elementos elementos; #Precios elementales.
    Descompuestos unidades; #Unidades de obra.

public:
     Elementos &Elementales(void)
        return elementos

    Elementos &Elementales(void)
        return elementos

     Descompuestos &UdsObra(void)
        return unidades

    inline bool TieneElementales(void)
        return (elementos.size()>0)

    inline size_t NumDescompuestos(void)
        return unidades.size()

    inline bool TieneDescompuestos(void)
        return (unidades.size()>0)

    inline BuscadorDescompuestos GetBuscadorDescompuestos(void)
        return unidades.GetBuscador()

     UdObra *BuscaUdObra( std.string &cod)
     Elemento *BuscaElemento( std.string &cod)
     Medible *BuscaPrecio( std.string &cod)
    void AgregaComponente( std.string &cod_ud, &cod_el, &r, &f= 1.0)
        unidades.AgregaComponente(elementos,cod_ud,cod_el,r,f)


    void EscribeSpre(void)
    void EscribeBC3(std.ostream &os)
    void LeeSpre(std.istream &is)
    inline void LeeBC3Elementales( Codigos &elem)
        elementos.LeeBC3(elem)

    inline void LeeBC3DescompFase1( Codigos &descomp)
        unidades.LeeBC3Fase1(descomp)

    Descompuestos.set_pendientes LeeBC3DescompFase2( Codigos &descomp)
#     inline void LeeBC3Fase1( CodigosObra &c)
##         LeeBC3Elementales(c.GetDatosElementos())
#         LeeBC3DescompFase1(c.GetDatosUnidades())
#
#     inline void LeeBC3Fase2( CodigosObra &c)
#       { LeeBC3DescompFase2(c.GetDatosUnidades());
    void ImprLtxElementales(std.ostream &os)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP1(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void ImprLtxCP(std.ostream &os)
    void EscribeHCalc(std.ostream &os)
    void SimulaDescomp( std.string &origen, &destino)


#endif
#CuaPre.cxx

import CuaPre
import CodigosObra

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

