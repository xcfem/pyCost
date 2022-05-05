# -*- coding: utf-8 -*-
''' Price tables.'''

from pycost.prices import elementary_price_container
from pycost.prices import unit_price_container
from pycost.bc3 import codigos_obra
from pycost.utils import EntPyCost as epc

class Buscadores(dict):
    def __init__(self):
        super(Buscadores, self).__init__()

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
        ''' Read elementary prices.'''
        self.elementos.readBC3(elem)

    def LeeBC3DescompFase1(self, descomp):
        self.unidades.LeeBC3Fase1(descomp)

    def LeeBC3DescompFase2(self, descomp):
        bp= Buscadores()
        bp["elementos"]= self.elementos
        bp["ud_obra"]= self.unidades
        return self.unidades.LeeBC3Fase2(descomp,bp)

    def searchForUnitPrice(self, cod):
        return self.unidades.Busca(cod)

    def BuscaElementaryPrice(self, cod):
        return self.elementos.Busca(cod)

    def findPrice(self, cod):
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
        self.elementos.WriteBC3(os)
        self.unidades.WriteBC3(os)

    def LeeSpre(self, iS):
        self.elementos.LeeSpre(iS)
        Str=''
        getline(iS,Str,'\n')
        if(Str.find("[DES]")<len(Str)):
            self.unidades.LeeSpre(iS,elementos)


    def ImprLtxElementales(self, os):
        '''Write elementary prices.''' 
        self.elementos.printLtx(os)


    def writePriceJustification(self, doc):
        '''Write price justification.'''
        self.unidades.writePriceJustification(doc)


    def writePriceTableOneIntoLatexDocument(self, os):
        '''Write first price table.'''
        self.unidades.writePriceTableOneIntoLatexDocument(os)

    def writePriceTableTwoIntoLatexDocument(self, os):
        '''Write second prince table.'''
        self.unidades.writePriceTableTwoIntoLatexDocument(os)

    def writePriceTablesIntoLatexDocument(self, os):
        '''Write both price tables.'''
        writePriceTableOneIntoLatexDocument(os)
        writePriceTableTwoIntoLatexDocument(os)


    def WriteHCalc(self, os):
        elementos.WriteHCalc(os)
        self.unidades.WriteHCalc(os)


    def SimulaDescomp(self, origen, destino):
        self.unidades.SimulaDescomp(origen,destino)

