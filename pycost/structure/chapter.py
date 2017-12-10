# -*- coding: utf-8 -*-
#Chapter.py

from pycost.measurements import measurement_container
from pycost.bc3 import fr_entity
from pycost.bc3 import bc3_entity
from pycost.structure import chapter_container
from pycost.prices import price_table
from pycost.prices import unit_price_container

import pylatex
from pycost.utils import pylatex_utils

class Chapter(bc3_entity.EntBC3):
    def __init__(self, cod= "CapSinCod", tit= "CapSinTit", factor= 1.0, productionRate= 1.0):
      super(Chapter,self).__init__(cod,tit)
      self.fr= fr_entity.EntFR(factor,productionRate)
      self.subcapitulos= chapter_container.Subcapitulos(self)
      self.quantities= measurement_container.ChapterQuantities()
      self.precios= price_table.CuaPre() #Para precios elementales y
                             #descompuestos clasificados por capítulos.
    def TieneElementales():
        return precios.TieneElementales()
    def NumDescompuestos():
        return precios.NumDescompuestos()+subcapitulos.NumDescompuestos()
    def TieneDescompuestos():
        return NumDescompuestos()> 0
    def GetBuscadorDescompuestos():
        return self.precios.GetBuscadorDescompuestos()
    def getSubcapitulos(self):
        return self.subcapitulos
    def getQuantities(self):
        return self.quantities
    def WriteQuantities(os, pos=""):
        self.quantities.Write(os,CodigoBC3(),pos)
    def WriteSubChapters(os, primero= "False", pos=""):
        self.subcapitulos.WriteBC3(os,primero,pos)
    def CodigoBC3(self):
        return EntBC3.CodigoBC3() + "#"
    def CuadroPrecios(self):
        return precios
    def AppendUnitPriceQuantities(self, m):
        self.quantities.append(m)
    def GetBC3Component(self):
        '''Return this chapter as a component.'''
        return BC3Component(self,fr)
    def LeeBC3Elementales(self, elementos):
        '''Appends the elementary prices from argument.'''
        self.precios.LeeBC3Elementales(elementos)
    def LeeBC3DescompFase1(self, descompuestos):
        self.precios.LeeBC3DescompFase1(descompuestos)
    def LeeBC3DescompFase2(self, descompuestos):
        return precios.LeeBC3DescompFase2(descompuestos)
    def BuscaSubcapitulo(self, ruta):
        retval= None
        if ruta:
            retval= subcapitulos.Busca(ruta)
            if not retval:
                lmsg.error("Chapter.BuscaSubcapitulo: no se encontró el subcapítulo: " + ruta[1]
                          + " en el capítulo: " + Codigo() + " (" + getTitle()
                          + ") (ruta: " + ruta + ')' + '\n')
                #Si no encuentra el capítulo devuelve este mismo
                retval= self
        return retval
    def BuscaSubcapitulo(self, lst):
        '''Busca el subcapítulo que indica la cadena
           de caracteres que se pasa como parámetro.
           ésta es una cadena de la forma '1\2\1\4'''
        retval= None
        pos= lst.find('\\')
        if(pos>len(lst)): #No aparece la barra luego.pya de ser subcapitulo de éste.
            indice= atoi(lst.c_str())
            if indice>subcapitulos.size():
                lmsg.error("Capítulo: " + indice + " no encontrado." + '\n')
                return None

            retval= subcapitulos[indice-1]
            return retval

        else: #Ha de ser subcapitulo del que esta a la izquierda de la barra
            ind= lst.substr(0,pos)
            indice= atoi(ind.c_str())
            if indice>subcapitulos.size():
                lmsg.error("Capítulo: " + indice + " no encontrado." + '\n')
                return None

            return subcapitulos[indice-1].BuscaSubcapitulo(lst.substr(pos+1,lst.size()-1))

        lmsg.error("sale por aqui (y no debiera) en el capitulo: " + Codigo() + '\n')
        return retval
    def BuscaCodigo(self, nmb):
        if (Codigo()==nmb) or ((Codigo()+'#')==nmb):
            return self
        else:
            return subcapitulos.BuscaCodigo(nmb)
    def BuscaCodigo(self, nmb):
        if Codigo()==nmb:
            return self
        else:
            return subcapitulos.BuscaCodigo(nmb)
    def BuscaPrecio(self, cod):
        retval= self.precios.BuscaPrecio(cod)
        if not retval:
            retval= self.subcapitulos.BuscaPrecio(cod)
        return retval
    def WritePreciosBC3(self, os):
        precios.WriteBC3(os)
        subcapitulos.WritePreciosBC3(os)
    def WriteDescompBC3(self, os):
        subcapitulos.WriteDescompBC3(os,CodigoBC3())
        self.quantities.WriteDescompBC3(os,CodigoBC3())
    def WriteBC3(self, os, primero, pos):
        WriteConceptoBC3(os,primero)
        WriteDescompBC3(os)
        WriteQuantities(os,pos)
        WriteSubChapters(os,False,pos)
    def Precio(self):
        return (subcapitulos.Precio() + self.quantities.Precio()) * fr.Producto()
    def PrecioR(self):
        retval= subcapitulos.PrecioR() + self.quantities.PrecioR()
        retval*= fr.Producto()
        return retval
    def ImprCompLtxMed(self, os, sect, otro):
        if sect!='root':
            doc.append('\\' + sect + '{' + getTitle() + '}' + '\n')
        self.quantities.ImprCompLtxMed(os, otro.quantities)
        lmsg.error("aqui 1: " + getTitle() + ' ' + subcapitulos.size() + " subcapítulos" + '\n')
        lmsg.error("aqui 2: " + otro.getTitle() + ' ' + otro.subcapitulos.size() + " subcapítulos" + '\n')
        subcapitulos.ImprCompLtxMed(os,pylatex_utils.getLatexSection(sect), otro.subcapitulos)
    def writeQuantitiesIntoLatexDocument(self, doc, sect):
        if sect!='root':
            doc.create(pylatex.section.Section(self.getTitle()))
        self.quantities.writeQuantitiesIntoLatexDocument(doc)
        if len(self.quantities):
            doc.append("\\newpage" + '\n')
        self.subcapitulos.writeQuantitiesIntoLatexDocument(doc,pylatex_utils.getLatexSection(sect))
    def ImprLtxCP1(self, os, sect):
        if(TieneDescompuestos()):
            if sect!='root':
                doc.append('\\' + sect + '{' + getTitle() + '}' + '\n')
            if self.precios.TieneDescompuestos():
                self.precios.ImprLtxCP1(os)
            self.subcapitulos.ImprLtxCP1(os,pylatex_utils.getLatexSection(sect))
    def ImprLtxCP2(self, os, sect):
        if self.precios.TieneDescompuestos():
            if sect!='root':
                doc.append('\\' + sect + '{' + getTitle() + '}' + '\n')
            precios.ImprLtxCP2(os)
        subcapitulos.ImprLtxCP2(os,pylatex_utils.getLatexSection(sect))
    def ImprLtxJustPre(self, os, sect):
        if(sect!='root'):
            doc.append('\\' + sect + '{' + getTitle() + '}' + '\n')
        if self.precios.TieneDescompuestos():
            self.precios.ImprLtxJustPre(os)
        self.subcapitulos.ImprLtxJustPre(os,pylatex_utils.getLatexSection(sect))
    def ImprLtxResumen(self, os, sect, recurre):
        if(sect!='root'):
            doc.append("\\item " + getTitle() + " \\dotfill\\ "
               + StrPrecioLtx() + '\n')
        else:
            doc.append("\\Large\\textbf{Total}\\dotfill\\ \\textbf{"
               + StrPrecioLtx() + "} \\normalsize" + '\n')
        if(recurre):
            self.subcapitulos.ImprLtxResumen(os,pylatex_utils.getLatexSection(sect),recurre)
    def ImprCompLtxPre(self, os, sect, otro):
        if sect!='root':
            doc.append('\\' + sect + '{' + getTitle() + '}' + '\n')
        self.quantities.ImprCompLtxPre(os, getTitle(),otro.quantities,otro.getTitle())
        self.subcapitulos.ImprCompLtxPre(os,pylatex_utils.getLatexSection(sect), otro.subcapitulos)
        if self.subcapitulos:
            doc.append(pylatex_utils.ltx_beg_itemize + '\n')
            doc.append("\\item \\noindent \\textbf{Total " + getTitle()
               + " (P. de construcción): } \\dotfill \\textbf{"
               + otro.StrPrecioLtx() + "} " + '\n' + '\n')
            doc.append("\\item \\noindent \\textbf{Total " + getTitle()
               + " (P. modificado): }\\dotfill \\textbf{"
               + StrPrecioLtx() + "} " + '\n')
            doc.append(pylatex_utils.ltx_end_itemize + '\n')
            doc.append("\\clearpage" + '\n')

        if self.quantities:
            doc.append("\\newpage" + '\n')
    def ImprLtxPre(self, os, sect):
        '''Imprime presupuestos parciales.'''
        if sect!='root':
            doc.append('\\' + sect + '{' + getTitle() + '}' + '\n')
        self.quantities.ImprLtxPre(os,getTitle())
        self.subcapitulos.ImprLtxPre(os,pylatex_utils.getLatexSection(sect))
        if self.subcapitulos:
            doc.append("\\noindent \\large \\textbf{Total: " + getTitle() + "} \\dotfill \\textbf{" + StrPrecioLtx() + "} \\\\ \\normalsize" + '\n')

    def WriteHCalcMed(self, os, sect):
        if sect!='root':
            os.write(getTitle() + '\n')
        self.quantities.WriteHCalcMed(os)
        subcapitulos.WriteHCalcMed(os,sect)

    def WriteHCalcPre(self, os, sect):
        if sect!='root':
            os.write(getTitle() + '\n')
        self.quantities.WriteHCalcPre(os)
        os.write(tab + tab + tab + tab + "Total: " + tab + getTitle() + tab + StrPrecio() + '\n')
        subcapitulos.WriteHCalcPre(os,sect)

    def getQuantitiesReport(self):
        retval= self.quantities.getQuantitiesReport()
        retval.Merge(subcapitulos.getQuantitiesReport())
        return retval

