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
from pycost.utils import basic_types

class Chapter(bc3_entity.EntBC3):
    def __init__(self, cod= "CapSinCod", tit= "CapSinTit", factor= 1.0, productionRate= 1.0):
      super(Chapter,self).__init__(cod,tit)
      self.fr= fr_entity.EntFR(factor,productionRate)
      self.subcapitulos= chapter_container.Subcapitulos(self)
      self.quantities= measurement_container.ChapterQuantities()
      self.precios= price_table.CuaPre() #Para precios elementales y
                             #descompuestos clasificados por capítulos.
    def TieneElementales(self):
        return self.precios.TieneElementales()
    def NumDescompuestos(self):
        return self.precios.NumDescompuestos()+self.subcapitulos.NumDescompuestos()
    def TieneDescompuestos(self):
        return self.NumDescompuestos()> 0
    def GetBuscadorDescompuestos(self):
        return self.precios.GetBuscadorDescompuestos()
    def getSubcapitulos(self):
        return self.subcapitulos
    def getQuantities(self):
        return self.quantities
    def hasQuantities(self):
        retval= False
        if(self.quantities):
            retval= True
        else:
            for s in self.subcapitulos:
                if(s.hasQuantities()):
                    retval= True
                    break
        return retval
    def WriteQuantities(os, pos=""):
        self.quantities.Write(os,CodigoBC3(),pos)
    def WriteSubChapters(os, primero= "False", pos=""):
        self.subcapitulos.WriteBC3(os,primero,pos)
    def CodigoBC3(self):
        return EntBC3.CodigoBC3() + "#"
    def CuadroPrecios(self):
        return self.precios
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
        return self.precios.LeeBC3DescompFase2(descompuestos)
    def BuscaSubcapitulo(self, ruta):
        retval= None
        if ruta:
            retval= self.subcapitulos.Busca(ruta)
            if not retval:
                lmsg.error(u"Chapter.BuscaSubcapitulo: no se encontró el subcapítulo: " + ruta[1]
                          + u" en el capítulo: " + Codigo() + " (" + self.getTitle()
                          + ") (ruta: " + ruta + ')' + '\n')
                #Si no encuentra el capítulo devuelve este mismo
                retval= self
        return retval
    def BuscaSubcapitulo(self, lst):
        '''Search the sub-chapter indicated by
           the string of the form 1\2\1\4'''
        retval= None
        pos= lst.find('\\')
        if(pos>len(lst)): #Not on tht bar so it must be a subchapter of this one.
            indice= atoi(lst.c_str())
            if indice>subcapitulos.size():
                lmsg.error(u"Capítulo: " + indice + " no encontrado." + '\n')
                return None

            retval= self.subcapitulos[indice-1]
            return retval

        else: #Ha de ser subcapitulo del que esta a la izquierda de la barra
            ind= lst.substr(0,pos)
            indice= atoi(ind.c_str())
            if indice>subcapitulos.size():
                lmsg.error(u"Capítulo: " + indice + " no encontrado." + '\n')
                return None

            return self.subcapitulos[indice-1].BuscaSubcapitulo(lst.substr(pos+1,lst.size()-1))

        lmsg.error("sale por aqui (y no debiera) en el capitulo: " + Codigo() + '\n')
        return retval
    def BuscaCodigo(self, nmb):
        if (Codigo()==nmb) or ((Codigo()+'#')==nmb):
            return self
        else:
            return self.subcapitulos.BuscaCodigo(nmb)
    def BuscaCodigo(self, nmb):
        if Codigo()==nmb:
            return self
        else:
            return self.subcapitulos.BuscaCodigo(nmb)
    def BuscaPrecio(self, cod):
        retval= self.precios.BuscaPrecio(cod)
        if not retval:
            retval= self.subcapitulos.BuscaPrecio(cod)
        return retval
    def WritePreciosBC3(self, os):
        self.precios.WriteBC3(os)
        self.subcapitulos.WritePreciosBC3(os)
    def WriteDescompBC3(self, os):
        self.subcapitulos.WriteDescompBC3(os,CodigoBC3())
        self.quantities.WriteDescompBC3(os,CodigoBC3())
    def WriteBC3(self, os, primero, pos):
        WriteConceptoBC3(os,primero)
        WriteDescompBC3(os)
        WriteQuantities(os,pos)
        WriteSubChapters(os,False,pos)
    def Precio(self):
        return (self.subcapitulos.Precio() + self.quantities.Precio()) * self.fr.Producto()
    def PrecioR(self):
        retval= self.subcapitulos.PrecioR() + self.quantities.PrecioR()
        retval*= self.fr.ProductoR()
        return retval
    def ImprCompLtxMed(self, os, sect, otro):
        if sect!='root':
            doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
        self.quantities.ImprCompLtxMed(os, otro.quantities)
        lmsg.error("aqui 1: " + self.getTitle() + ' ' + self.subcapitulos.size() + u" subcapítulos" + '\n')
        lmsg.error("aqui 2: " + otro.getTitle() + ' ' + otro.subcapitulos.size() + u" subcapítulos" + '\n')
        self.subcapitulos.ImprCompLtxMed(os,pylatex_utils.getLatexSection(sect), otro.subcapitulos)
    def writeQuantitiesIntoLatexDocument(self, doc, parentSection):
        if(self.hasQuantities()):
            sectName= pylatex_utils.getLatexSection(parentSection)
            caption= basic_types.quantitiesCaption
            if(sectName!='part'):
              caption= self.getTitle()
            print '**** sectName= ', sectName, ' caption= ', caption
            docPart= pylatex_utils.getPyLatexSection(sectName,caption)
            self.quantities.writeQuantitiesIntoLatexDocument(docPart)
            self.subcapitulos.writeQuantitiesIntoLatexDocument(docPart,sectName)
            doc.append(docPart)
        
    def writePriceTableOneIntoLatexDocument(self, doc, sect):
        if(self.TieneDescompuestos()):
            if sect!='root':
                doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
            if self.precios.TieneDescompuestos():
                self.precios.writePriceTableOneIntoLatexDocument(doc)
            self.subcapitulos.writePriceTableOneIntoLatexDocument(doc,pylatex_utils.getLatexSection(sect))
    def writePriceTableTwoIntoLatexDocument(self, doc, sect):
        if self.precios.TieneDescompuestos():
            if sect!='root':
                doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
            self.precios.writePriceTableTwoIntoLatexDocument(doc)
        self.subcapitulos.writePriceTableTwoIntoLatexDocument(doc,pylatex_utils.getLatexSection(sect))
    def ImprLtxJustPre(self, doc, sect):
        if(sect!='root'):
            doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
        if self.precios.TieneDescompuestos():
            self.precios.ImprLtxJustPre(doc)
        self.subcapitulos.ImprLtxJustPre(doc,pylatex_utils.getLatexSection(sect))
    def ImprLtxResumen(self, doc, sect, recurre= True):
        if(sect!='root'):
            doc.append("\\item " + self.getTitle() + " \\dotfill\\ "
               + self.StrPrecioLtx() + '\n')
        else:
            doc.append("\\Large\\textbf{Total}\\dotfill\\ \\textbf{"
               + self.StrPrecioLtx() + "} \\normalsize" + '\n')
        if(recurre):
            self.subcapitulos.ImprLtxResumen(doc,pylatex_utils.getLatexSection(sect),recurre)
    def ImprCompLtxPre(self, doc, sect, otro):
        if sect!='root':
            doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
        self.quantities.ImprCompLtxPre(doc, self.getTitle(),otro.quantities,otro.getTitle())
        self.subcapitulos.ImprCompLtxPre(doc,pylatex_utils.getLatexSection(sect), otro.subcapitulos)
        if self.subcapitulos:
            doc.append(pylatex_utils.ltx_beg_itemize + '\n')
            doc.append("\\item \\noindent \\textbf{Total " + self.getTitle()
               + " (P. de construcción): } \\dotfill \\textbf{"
               + otro.StrPrecioLtx() + "} " + '\n' + '\n')
            doc.append("\\item \\noindent \\textbf{Total " + self.getTitle()
               + " (P. modificado): }\\dotfill \\textbf{"
               + self.StrPrecioLtx() + "} " + '\n')
            doc.append(pylatex_utils.ltx_end_itemize + '\n')
            doc.append("\\clearpage" + '\n')

        if self.quantities:
            doc.append("\\newpage" + '\n')
    def ImprLtxPre(self, doc, sect):
        '''Imprime presupuestos parciales.'''
        if(sect!='root'):
            doc.append(pylatex.Section(self.getTitle()))
        self.quantities.ImprLtxPre(doc,self.getTitle())
        self.subcapitulos.ImprLtxPre(doc,pylatex_utils.getLatexSection(sect))
        if self.subcapitulos:
            doc.append("\\noindent \\large \\textbf{Total: " + self.getTitle() + "} \\dotfill \\textbf{" + self.StrPrecioLtx() + "} \\\\ \\normalsize" + '\n')

    def WriteHCalcMed(self, os, sect):
        if sect!='root':
            os.write(self.getTitle() + '\n')
        self.quantities.WriteHCalcMed(os)
        self.subcapitulos.WriteHCalcMed(os,sect)

    def WriteHCalcPre(self, os, sect):
        if sect!='root':
            os.write(self.getTitle() + '\n')
        self.quantities.WriteHCalcPre(os)
        os.write(tab + tab + tab + tab + "Total: " + tab + self.getTitle() + tab + self.StrPrecio() + '\n')
        self.subcapitulos.WriteHCalcPre(os,sect)

    def getQuantitiesReport(self):
        retval= self.quantities.getQuantitiesReport()
        retval.Merge(self.subcapitulos.getQuantitiesReport())
        return retval

