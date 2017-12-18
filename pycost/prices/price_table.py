# -*- coding: utf-8 -*-
#CuaPre.py




import elementary_price_container
import unit_price_container
from pycost.bc3 import codigos_obra
from pycost.utils import EntPyCost as epc

class CuaPre(epc.EntPyCost):
    def __init__(self):
        self.elementos= elementary_price_container.ElementaryPrices() #Precios elementales.
        self.unidades= unit_price_container.Descompuestos() #Unidades de obra.

    def Elementales(self):
        return self.elementos

    def UdsObra(self):
        return self.unidades

    def TieneElementales(self):
        return (len(self.elementos)>0)

    def NumDescompuestos(self):
        return len(self.unidades)

    def TieneDescompuestos(self):
        return (self.NumDescompuestos()>0)

    def AgregaComponente(self, cod_ud, cod_el, r, f= 1.0):
        self.unidades.AgregaComponente(elementos,cod_ud,cod_el,r,f)


    def LeeBC3Elementales(self, elem):
        self.elementos.LeeBC3(elem)

    def LeeBC3DescompFase1(self, descomp):
        self.unidades.LeeBC3Fase1(descomp)

    def LeeBC3DescompFase2(self, descomp):
        bp= Buscadores()
        b_elem= elementos.GetBuscador()
        bp["elementos"]= b_elem
        b_desc= unidades.GetBuscador()
        bp["ud_obra"]= b_desc
        return unidades.LeeBC3Fase2(descomp,bp)

    def searchForUnitPrice(self, cod):
        return self.unidades.Busca(cod)

    def BuscaElementaryPrice(self, cod):
        return self.elementos.Busca(cod)

    def BuscaPrecio(self, cod):
        retval= self.searchForUnitPrice(cod)
        if not retval:
            retval= self.BuscaElementaryPrice(cod)
        return retval


    def WriteSpre(self):
        self.elementos.WriteSpre()
        ofs_des= std.ofstream("DES001.std",std.ios.out)
        self.unidades.WriteSpre(ofs_des)
        ofs_des.close()

    def WriteBC3(self, os):
        elementos.WriteBC3(os)
        unidades.WriteBC3(os)

    def LeeSpre(self, iS):
        self.elementos.LeeSpre(iS)
        Str=''
        getline(iS,Str,'\n')
        if(Str.find("[DES]")<len(Str)):
            self.unidades.LeeSpre(iS,elementos)


    #not  @brief Write los precios elementales.
    def ImprLtxElementales(self, os):
        self.elementos.printLtx(os)


    #not  @brief Write la justificación de precios.
    def ImprLtxJustPre(self, os):
        self.unidades.ImprLtxJustPre(os)


    #not  @brief Write el cuadro de precios número 1.
    def writePriceTableOneIntoLatexDocument(self, os):
        self.unidades.writePriceTableOneIntoLatexDocument(os)

    #not  @brief Write el cuadro de precios número 2.
    def writePriceTableTwoIntoLatexDocument(self, os):
        self.unidades.writePriceTableTwoIntoLatexDocument(os)

    #not  @brief Write los cuadros de precios números 1 y 2.
    def writePriceTablesIntoLatexDocument(self, os):
        writePriceTableOneIntoLatexDocument(os)
        writePriceTableTwoIntoLatexDocument(os)


    def WriteHCalc(self, os):
        elementos.WriteHCalc(os)
        self.unidades.WriteHCalc(os)


    def SimulaDescomp(self, origen, destino):
        self.unidades.SimulaDescomp(origen,destino)

