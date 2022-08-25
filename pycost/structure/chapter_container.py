# -*- coding: utf-8 -*-
#Subcapitulos.py

import logging
from decimal import Decimal
import pylatex
from pycost.prices import price_table
from pycost.structure import chapter
from pycost.bc3 import codes
from pycost.bc3 import codigos_obra
from pycost.utils import EntPyCost as epc
from pycost.utils import basic_types
from pycost.measurements import measurement_report

class Subcapitulos(list, epc.EntPyCost):

    def __init__(self,ptr_cap):
        epc.EntPyCost.__init__(self, owner= ptr_cap)

    def getContenedor(self):
        return self

    def NumDescompuestos(self):
        nd= 0
        for j in self:
            nd+= (j).NumDescompuestos()
        return nd

    def getPrice(self):
        p= 0.0
        for j in self:
            p+= (j).getPrice()
        return p


    def getRoundedPrice(self):
        p= Decimal('0.0')
        for j in self:
            p+= (j).getRoundedPrice()
        return p

    def Busca(self,ruta):
        if(len(ruta)==0): return None
        indice= int(ruta[0])-1
        existe= (indice<size())
        if not existe:
            return None
        elif(ruta.size()== 1): #Es subcapitulo de este
            return self[indice]
        else:
            sc= self[indice]
            ruta.pop_front()
            return sc.BuscaSubcapitulo(ruta)
        return None

    def BuscaCodigo(self, nmb):
        retval= None
        for i in self:
            retval= (i).BuscaCodigo(nmb)
            if(retval): return retval

        return retval

    def findPrice(self, cod):
        '''Search a unit price through the chapter tree.'''
        retval= None
        for i in self:
            retval= (i).findPrice(cod)
            if(retval): break
        return retval
    
    def findPricesRegex(self, regex):
        ''' Return the concepts with a code that matches to the regular
            expression argument.

        :param regex: regular expression to match with the concept code.
        '''
        retval= list()
        for chapter in self:
            retval.extend(chapter.findPricesRegex(regex))
        return retval

    def newChapter(self, c):
        self.append(c)
        return c

    def newChapterFromRecord(self, r):
        '''Appends a chapter.'''
        return self.newChapter(chapter.Chapter(r.codigo,"",r.factor,r.productionRate))

    def newChapters(self, descomp):
        '''Append the chapters from the records on the container.'''
        #sz= len(descomp)
        for comp in descomp:
            self.newChapterFromRecord(comp)

    def LeeBC3Caps(self, co):
        ''' Carga los datos de los subcapítulos de (self).'''
        sc= codes.Codigos(co.GetDatosCaps())
        if len(sc)<1:
            logging.error("No se encontraron subcapitulos." + '\n')

        chapterNames= co.getChapterCodes()

        for i in self:
            code= i.Codigo()
            j= sc.findChapter(code)
            if j:
                reg= sc.getChapterData(code)
                if i:
                    logging.info(u"Loading sub-chapter: '" + reg.Datos().getTitle() + "'\n")
                    i.readBC3(reg) # Title

                    #Lee los elementales del capítulo.
                    elementos_capitulo= co.FiltraElementales(reg.Datos().desc)
                    i.LeeBC3Elementales(elementos_capitulo)
                    if(elementos_capitulo):
                      logging.info("  Loaded " + str(len(elementos_capitulo))
                                   + u" elementary prices of the chapter."
                                   + '\n')
                    co.BorraElementales(elementos_capitulo); #Borra los ya leídos.
                    logging.info("  They remain " + str(len(co.GetDatosElementos())) + " elementary prices." + '\n')

                    #Lee los subcapítulos.
                    i.subcapitulos.newChapters(reg.Datos().filterChapters(chapterNames))
                    i.subcapitulos.LeeBC3Caps(co); #Carga los subcapitulos.


            else:
                logging.error(u"LeeBC3Caps; No se encontró el capítulo: " + i.Codigo() + '\n')
                continue




    def WriteDescompBC3(self, os, cod):
        if(len(self)<1): return
        os.write("~D" + '|'
           + cod + '|')
        for i in self:
            (i).getBC3Component().WriteBC3(os)
        os.write('|' + '\n')


    def WritePreciosBC3(self, os):
        for i in self:
            (i).WritePreciosBC3(os)


    def WriteBC3(self, os, pos):
        conta= 1
        for i in self:
            nueva_pos= pos+str(conta)+'\\'
            (i).WriteBC3(os,nueva_pos)
            conta+=1

    def ImprCompLtxMed(self, os, parentSection, otro):
        '''Suponemos que ambos capítulos tienen el 
           mismo número de subcapítulos.'''
        sz= len(otro)
        for k in range(0,sz):
            i= self[k]
            j= otro[k]
            i.ImprCompLtxMed(os,parentSection,j)

    def writeQuantitiesIntoLatexDocument(self, doc, sectName):
        ''' Write quantities in the pylatex document argument.

        :param doc: document to write into.
        :param sectName: section command for the chapter.
        '''        
        for j in self:
            (j).writeQuantitiesIntoLatexDocument(doc,sectName)

    def writePriceTableOneIntoLatexDocument(self, doc, sectName):
        ''' Write unit prices table one in the pylatex document argument.

        :param doc: document to write into.
        :param sectName: section command for the chapter.
        '''
        for j in self:
            (j).writePriceTableOneIntoLatexDocument(doc, sectName)

    def writePriceTableTwoIntoLatexDocument(self, doc, sectName):
        ''' Write unit prices table one in the pylatex document argument.

        :param doc: document to write into.
        :param sectName: section command for the chapter.
        '''
        for j in self:
            (j).writePriceTableTwoIntoLatexDocument(doc, sectName)

    def writeElementaryPrices(self, doc, parentSection, tipos=  [basic_types.mdo, basic_types.maq, basic_types.mat]):
        ''' Write the elementary prices table.

        :param doc: pylatex document to write into.
        :param parentSection: section command for the parent chapter.
        :param tipos: types of the prices to write (maquinaria, materiales o mano de obra) defaults to all of them.
        '''
        for j in self:
            (j).writeElementaryPrices(doc, parentSection, tipos)

    def writePriceJustification(self, data_table, parentSection):
        ''' Write unit prices table one in the pylatex document argument.

        :param data_table: pylatex tabular data to populate.
        :param parentSection: section command for the parent chapter.
        '''
        for j in self:
            (j).writePriceJustification(data_table,parentSection)


    def ImprLtxResumen(self, doc, parentSection, recursive):
        ''' Write summary report.

        :param doc: pylatex document to write into.
        :param parentSection: section command for the parent chapter.
        :param recursive: if true apply recursion through chapters.
        '''
        if len(self):
            with doc.create(pylatex.Itemize()) as itemize:
                for j in self:
                    (j).ImprLtxResumen(itemize,parentSection,recursive)

    def ImprCompLtxPre(self, doc, parentSection, other):
        '''Compare chapters.

        :param doc: pylatex document to write into.
        :param parentSection: section command for the parent chapter.
        :param other: chapter to compare with.
        '''
        for i, j in zip(self, other):
            i.ImprCompLtxPre(doc,parentSection,j)

    def writePartialBudgetsIntoLatexDocument(self, doc, sectName):
        ''' Write partial budgets into the pylatex document argument.

        :param doc: pylatex document to write into.
        :param sectName: section command for the chapter.
        '''
        for j in self:
            (j).writePartialBudgetsIntoLatexDocument(doc,sectName)


    def WriteHCalcMed(self, os, parentSection):
        for j in self:
            (j).WriteHCalcMed(os,parentSection)

    def WriteHCalcPre(self, os, parentSection):
        for j in self:
            (j).WriteHCalcPre(os, parentSection)

    def hasQuantities(self):
        '''Returns true if al least one of the chapters have quantities.'''
        retval= False
        for c in self:
            if c.hasQuantities():
                retval= True
                break
        return retval
    
    def getQuantitiesReport(self):
        retval= measurement_report.QuantitiesReport()
        for j in self:
            retval.Merge((j).getQuantitiesReport())
        return retval

    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= epc.EntPyCost.getDict(self)
        components= dict()
        for chapter in self:
            code= chapter.Codigo()
            components[code]= chapter.getDict()
        retval['components']= components
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        pendingLinks= list() # Links that cannot be set yet.
        components= dct['components']
        for key in components:
            chapterDict= components[key]
            ch= chapter.Chapter(key)
            pendingLinks.extend(ch.setFromDict(chapterDict))
            self.append(ch)
        pendingLinks.extend(epc.EntPyCost.setFromDict(self, dct))
        return pendingLinks

    def clear(self):
        '''removes all items from the chapter.'''
        for sc in self:
            sc.clear()
        super(Subcapitulos,self).clear()
