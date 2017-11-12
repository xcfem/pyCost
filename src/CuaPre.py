#CuaPre.py




import Elementos
import Descompuestos

class CuaPre(EntPyCost):
private:
    Elementos elementos; #Precios elementales.
    Descompuestos unidades; #Unidades de obra.

public:
     Elementos &Elementales()
        return elementos

    Elementos &Elementales()
        return elementos

     Descompuestos &UdsObra()
        return unidades

    def bool TieneElementales():
        return (elementos.size()>0)

    def size_t NumDescompuestos():
        return unidades.size()

    def bool TieneDescompuestos():
        return (unidades.size()>0)

    def BuscadorDescompuestos GetBuscadorDescompuestos():
        return unidades.GetBuscador()

     UdObra *BuscaUdObra( cod)
     Elemento *BuscaElemento( cod)
     Measurable *BuscaPrecio( cod)
     AgregaComponente( cod_ud, &cod_el, &r, &f= 1.0)
        unidades.AgregaComponente(elementos,cod_ud,cod_el,r,f)


     WriteSpre()
     WriteBC3(os)
     LeeSpre(std.istream &is)
    def  LeeBC3Elementales( Codigos &elem):
        elementos.LeeBC3(elem)

    def  LeeBC3DescompFase1( Codigos &descomp):
        unidades.LeeBC3Fase1(descomp)

    Descompuestos.set_pendientes LeeBC3DescompFase2( Codigos &descomp)
#     def  LeeBC3Fase1( CodigosObra &c):
##         LeeBC3Elementales(c.GetDatosElementos())
#         LeeBC3DescompFase1(c.GetDatosUnidades())
#
#     def  LeeBC3Fase2( CodigosObra &c):
#       { LeeBC3DescompFase2(c.GetDatosUnidades());
     ImprLtxElementales(os)
     ImprLtxJustPre(os)
     ImprLtxCP1(os)
     ImprLtxCP2(os)
     ImprLtxCP(os)
     WriteHCalc(os)
     SimulaDescomp( origen, &destino)



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

 UdObra *CuaPre.BuscaUdObra( cod)
    return unidades.Busca(cod)

 Elemento *CuaPre.BuscaElemento( cod)
    return elementos.Busca(cod)

 Measurable *CuaPre.BuscaPrecio( cod)
     Measurable *retval= BuscaUdObra(cod)
    if not retval:
        retval= BuscaElemento(cod)
    return retval


def WriteSpre(self, ):
    elementos.WriteSpre()
    std.ofstream ofs_des("DES001.std",std.ios.out)
    unidades.WriteSpre(ofs_des)
    ofs_des.close()

def WriteBC3(self, &os):
    elementos.WriteBC3(os)
    unidades.WriteBC3(os)

def LeeSpre(self, &is):
    elementos.LeeSpre(is)
    std.string Str
    getline(is,Str,'\n')
    if Str.find("[DES]")<len(Str)) unidades.LeeSpre(is,elementos:


#not  @brief Write los precios elementales.
def ImprLtxElementales(self, &os):
    elementos.ImprLtx(os)


#not  @brief Write la justificación de precios.
def ImprLtxJustPre(self, &os):
    unidades.ImprLtxJustPre(os)


#not  @brief Write el cuadro de precios número 1.
def ImprLtxCP1(self, &os):
    unidades.ImprLtxCP1(os)

#not  @brief Write el cuadro de precios número 2.
def ImprLtxCP2(self, &os):
    unidades.ImprLtxCP2(os)

#not  @brief Write los cuadros de precios números 1 y 2.
def ImprLtxCP(self, &os):
    ImprLtxCP1(os)
    ImprLtxCP2(os)


def WriteHCalc(self, &os):
    elementos.WriteHCalc(os)
    unidades.WriteHCalc(os)


def SimulaDescomp(self, &origen, &destino):
    unidades.SimulaDescomp(origen,destino)

