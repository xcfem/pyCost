# -*- coding: utf-8 -*-
#Chapter.py

import logging
import pylatex
from decimal import Decimal
from pycost.measurements import measurement_container
from pycost.bc3 import fr_entity
from pycost.bc3 import bc3_entity
from pycost.bc3 import bc3_component
from pycost.structure import chapter_container
from pycost.prices import price_table
from pycost.prices import unit_price_container
from pycost.utils import pylatex_utils
from pycost.utils import basic_types

class Chapter(bc3_entity.EntBC3):
    ''' Chapter.

    :ivar fr: factor and production rate values.
    :ivar subcapitulos: sub-chapters.
    :ivar quantities: chapter quantities.
    :ivar precios: chapter price table.
    '''
    precision= 2
    places= Decimal(10) ** -precision
    formatString= '{0:.'+str(precision)+'f}'
    
    def __init__(self, cod= "CapSinCod", tit= "CapSinTit", factor= 1.0, productionRate= 1.0):
        ''' Constructor.

        :param cod: chaper codename.
        :param tit: chapter title.
        :param factor:
        :param productionRate: production rate.
        '''
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
    
    def WriteQuantitiesBC3(self,os, pos=""):
        self.quantities.Write(os,self.CodigoBC3(),pos)
    def WriteSubChaptersBC3(self,os, pos=""):
        self.subcapitulos.WriteBC3(os,pos)
    def CodigoBC3(self):
        return super(Chapter,self).CodigoBC3() + "#"
    def CuadroPrecios(self):
        return self.precios
    def AppendUnitPriceQuantities(self, m):
        self.quantities.append(m)
    def getBC3Component(self):
        '''Return this chapter as a component.'''
        return bc3_component.BC3Component(e= self,fr= self.fr)
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
                logging.error(u"Chapter.BuscaSubcapitulo: no se encontró el subcapítulo: " + ruta[1]
                          + u" en el capítulo: " + self.Codigo() + " (" + self.getTitle()
                          + ") (ruta: " + ruta + ')' + '\n')
                #Si no encuentra el capítulo devuelve este mismo
                retval= self
        return retval
    
    def BuscaSubcapitulo(self, lst):
        '''Search the sub-chapter indicated by
           the list of the form ['1', '2', '1', '4']. '''
        retval= None
        sz= len(lst)
        if(sz>0): # not empty.
            indice= int(lst.pop(0))
            if(indice>len(self.subcapitulos)):
                logging.error(u"Chapter: " + str(indice) + " not found in chapter: "+str(self.Codigo()) + '\n')
                return None
            if(sz==1): # it must be a subchapter of this one.
                retval= self.subcapitulos[indice-1]
                return retval
            elif(sz>1): # still diging.
                return self.subcapitulos[indice-1].BuscaSubcapitulo(lst)
        else:
            logging.error(u"Empty list argument: " + str(lst) + '\n')
            return None

        logging.error("sale por aqui (y no debiera) en el capitulo: " + self.Codigo() + '\n')
        return retval
    
    def BuscaCodigo(self, nmb):
        if (self.Codigo()==nmb) or ((self.Codigo()+'#')==nmb):
            return self
        else:
            return self.subcapitulos.BuscaCodigo(nmb)
        
    def BuscaCodigo(self, nmb):
        if self.Codigo()==nmb:
            return self
        else:
            return self.subcapitulos.BuscaCodigo(nmb)
        
    def findPrice(self, cod):
        retval= self.precios.findPrice(cod)
        if not retval:
            retval= self.subcapitulos.findPrice(cod)
        return retval
    
    def WritePreciosBC3(self, os):
        self.precios.WriteBC3(os)
        self.subcapitulos.WritePreciosBC3(os)
        
    def WriteDescompBC3(self, os):
        self.subcapitulos.WriteDescompBC3(os,self.CodigoBC3())
        self.quantities.WriteDescompBC3(os,self.CodigoBC3())
        
    def WriteBC3(self, os, pos):
        self.WriteConceptoBC3(os)
        self.WriteDescompBC3(os)
        self.WriteQuantitiesBC3(os,pos)
        self.WriteSubChaptersBC3(os,pos)

    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= super(Chapter, self).getDict()
        retval['sub_chapters']= self.subcapitulos.getDict()
        retval['prices']= self.precios.getDict()
        retval['chapter_quantities']= self.quantities.getDict()
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        pendingLinks= self.quantities.setFromDict(dct['chapter_quantities'])
        pendingLinks.extend(self.precios.setFromDict(dct['prices']))
        pendingLinks.extend(self.subcapitulos.setFromDict(dct['sub_chapters']))
        pendingLinks.extend(super(Chapter, self).setFromDict(dct))
        return pendingLinks

    def solvePendingLinks(self, pendingLinks):
        ''' Solve object pending links.

        :param pendingLinks: list of pending links.
        '''
        for link in pendingLinks:
            key= link['key']
            value= self.findPrice(key)
            if(value is None):
                value= self.BuscaCodigo(key)
            if(value):
                obj= link['object']
                attribute= link['attr']
                if(hasattr(obj, attribute)):
                    setattr(obj, attribute, value)
                else:
                    logging.error('attribute: '+attribute+' not found for object: '+str(obj))
            else:
                logging.error('price: '+key+' not found.')
        return pendingLinks
    
    def getPrice(self):
        priceSubC= self.subcapitulos.getPrice()
        priceQuant= self.quantities.getPrice()
        factor= self.fr.getProduct()
        return (priceSubC + priceQuant)*factor 
    
    def getRoundedPrice(self):
        retval= self.subcapitulos.getRoundedPrice() + self.quantities.getRoundedPrice()
        retval*= self.fr.getRoundedProduct()
        return retval
    
    def ImprCompLtxMed(self, os, sect, otro):
        if sect!='root':
            doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
        self.quantities.ImprCompLtxMed(os, otro.quantities)
        logging.error("aqui 1: " + self.getTitle() + ' ' + self.subcapitulos.size() + u" subcapítulos" + '\n')
        logging.error("aqui 2: " + otro.getTitle() + ' ' + otro.subcapitulos.size() + u" subcapítulos" + '\n')
        self.subcapitulos.ImprCompLtxMed(os,pylatex_utils.getLatexSection(sect), otro.subcapitulos)
    def writeQuantitiesIntoLatexDocument(self, doc, parentSection):
        if(self.hasQuantities()):
            sectName= pylatex_utils.getLatexSection(parentSection)
            caption= basic_types.quantitiesCaption
            if(sectName!='part'):
              caption= self.getTitle()
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
    def writePriceJustification(self, doc, sect):
        if(sect!='root'):
            doc.append('\\' + sect + '{' + self.getTitle() + '}' + '\n')
        if self.precios.TieneDescompuestos():
            self.precios.writePriceJustification(doc)
        self.subcapitulos.writePriceJustification(doc,pylatex_utils.getLatexSection(sect))
    def ImprLtxResumen(self, doc, sect, recurre= True):
        if(self.hasQuantities()):
            if(sect!='root'):
                doc.add_item(self.getTitle())
                doc.append(pylatex.Command('dotfill'))
                doc.append(self.getLtxPriceString())
            else:
                doc.append(pylatex_utils.LargeCommand())
                doc.append(pylatex.utils.bold('Total'))
                doc.append(pylatex.Command('dotfill'))
                doc.append(pylatex.utils.bold(self.getLtxPriceString()))
                doc.append(pylatex_utils.NormalSizeCommand())
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
               + otro.getLtxPriceString() + "} " + '\n' + '\n')
            doc.append("\\item \\noindent \\textbf{Total " + self.getTitle()
               + " (P. modificado): }\\dotfill \\textbf{"
               + self.getLtxPriceString() + "} " + '\n')
            doc.append(pylatex_utils.ltx_end_itemize + '\n')
            doc.append("\\clearpage" + '\n')

        if self.quantities:
            doc.append("\\newpage" + '\n')
            
    def hasQuantities(self):
        '''Returns true if the chapter (or its subchapters) have
           quantities.'''
        if(len(self.quantities)):
            return True
        else:
            return self.subcapitulos.hasQuantities()
    def ImprLtxPre(self, doc, sect):
        '''Imprime presupuestos parciales.'''
        if(self.hasQuantities()):
            if(sect!='root'):
                doc.append(pylatex.Section(self.getTitle()))
            self.quantities.ImprLtxPre(doc,self.getTitle())
            self.subcapitulos.ImprLtxPre(doc,pylatex_utils.getLatexSection(sect))
            if self.subcapitulos:
                doc.append(pylatex.Command('noindent'))
                doc.append(pylatex_utils.largeCommand())
                doc.append(pylatex.utils.bold('Total: '+self.getTitle()+' '))
                doc.append(pylatex.Command('dotfill'))
                doc.append(pylatex.utils.bold(self.getLtxPriceString()))
                doc.append(pylatex.NewLine())
                doc.append(pylatex_utils.NormalSizeCommand())

    def WriteHCalcMed(self, os, sect):
        if sect!='root':
            os.write(self.getTitle() + '\n')
        self.quantities.WriteHCalcMed(os)
        self.subcapitulos.WriteHCalcMed(os,sect)

    def WriteHCalcPre(self, os, sect):
        if sect!='root':
            os.write(self.getTitle() + '\n')
        self.quantities.WriteHCalcPre(os)
        os.write(tab + tab + tab + tab + "Total: " + tab + self.getTitle() + tab + self.getPriceString() + '\n')
        self.subcapitulos.WriteHCalcPre(os,sect)

    def getQuantitiesReport(self):
        retval= self.quantities.getQuantitiesReport()
        retval.Merge(self.subcapitulos.getQuantitiesReport())
        return retval

    def clear(self):
        '''removes all items from the chapter.'''
        self.quantities.clear()
        self.subcapitulos.clear()
        self.precios.clear()
