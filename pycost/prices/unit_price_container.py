# -*- coding: utf-8 -*-
#Descompuestos.py

import pylatex
import logging
import sys
from pycost.prices import elementary_price_container
from pycost.prices import unit_price
from pycost.utils import concept_dict
from pycost.utils import pylatex_utils

class Descompuestos(concept_dict.ConceptDict):
    '''Unidades de obra.

    :ivar parametricConcepts: parametric concepts dictionary.
    '''
    def __init__(self):
        super().__init__()
        self.parametricConcepts= dict()

    def appendComponent(self, el, cod_ud, cod_el, r, f):
        ''' Append a new component to the container.

        :param el: elementary prices container.
        :param cod_ud: unit price 
        '''
        i= self.Busca(cod_ud)
        j= el.Busca(cod_el)
        if not j:
            logging.error("Elemento: " + cod_el
                      + " no encontrado en unidad de obra: " + cod_ud + '\n')
            exit(1)

        i.Append(j,f,r)

    def LeeBC3Fase1(self, cds):
        '''Read the units whitout its components.'''
        for key in cds:
            if('$' in key): # parametric concept.
                reg= cds.getParametricData(key)
                self.parametricConcepts[key]= reg.datos
            else: # not a parametric concept.
                reg= cds.getUnitPriceData(key)
                ud= unit_price.UnitPrice()
                ud.LeeBC3Fase1(reg)
                self.Append(ud)

    def LeeBC3Fase2(self, cds, rootChapter):
        '''Reads the components of the unit.'''
        ud= None
        error= False
        retval= set()
        for key in cds:
            if(not '$' in key): # not a parametric concept.
                reg= cds.getUnitPriceData(key)
                ud= self.Busca(reg.Codigo())
                error= ud.LeeBC3Fase2(reg, rootChapter= rootChapter)
                if error:
                    retval.add(reg.Codigo())
        return retval

    def WriteSpre(self, os):
        for j in self.concepts:
            self.concepts[j].WriteSpre(os)

    def AsignaFactor(self, f):
        for j in self.concepts:
            self.concepts[j].AsignaFactor(f)

    def LeeSpre(self, iS, elementos):
        if iS.peek()!= 26:
            while(True):
                cod= ''
                getline(iS,cod,'|')
                ud= ''
                getline(iS,ud,'|')
                if ud.find('%')<len(ud):
                    cod= "%" + cod
                    ud= ""

                tit= ''
                getline(iS,tit,'|')
                unidad= UnitPrice(cod,tit,ud)
                unidad.texto_largo= tit
                self.Append(unidad)
                perc= '' #percentage
                getline(iS,perc,'|')
                descomp= '' #descomposición
                getline(iS,descomp,'\n')
                #istrstream istr(descomp.c_str(),descomp.leng.py())
                while(True):
                    pos2= descomp.find('|')
                    cod_el= descomp.substr(0,pos2)
                    descomp.replace(0,pos2+1,"")
                    pos3= descomp.find('|')
                    cantidad= ''
                    if pos3<1000:
                        cantidad= descomp.substr(0,pos3)
                        descomp.replace(0,pos3+1,"")
                    else:
                        cantidad= descomp.substr(0,len(descomp)-1)
                    if(elementos.find("%" + cod_el)!=elementos.end()): #Corresponds to a percentage.
                        cod_el= "%"+cod_el
                    appendComponent(el= elementos, cod_ud= cod, cod_el= cod_el, r= atof(cantidad.c_str()))
                    if(pos3>len(descomp)): break

                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')


    def writePriceTableOneIntoLatexDocument(self, doc):
        ''' Write unit price table one into a latex report.

        :param doc: pylatex document to write into.
        '''
        if(len(self)>=1):
            num_campos= 5
            doc.append(pylatex_utils.SmallCommand())
            longTableStr= '|l|l|p{4cm}|p{3cm}|r|'
            headerRow1= [u'Código','Ud.',u'Denominación',(pylatex.table.MultiColumn(2,align='|c|',data= 'Precio'))]
            headerRow2= ['','','','en letra', 'en cifra']
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                data_table.add_hline()
                data_table.add_row(headerRow1)
                data_table.add_row(headerRow2)
                data_table.add_hline()
                data_table.end_table_header()
                data_table.add_hline()
                data_table.add_row((pylatex.table.MultiColumn(num_campos, align='|r|',data='../..'),))
                data_table.add_hline()
                data_table.end_table_footer()
                data_table.add_hline()
                data_table.end_table_last_footer()
                for j in self.concepts:
                    data_table.add_empty_row()
                    self.concepts[j].writePriceTableOneIntoLatexDocument(data_table)
                    data_table.add_empty_row()

            doc.append(pylatex_utils.NormalSizeCommand())

    def writePriceJustification(self, doc):
        ''' Write price justification into a latex report.

        :param doc: pylatex document to write into.
        '''
        if(len(self)>0):
            doc.append(pylatex_utils.SmallCommand())
            longTableStr= 'l'
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                for j in self.concepts:
                    self.concepts[j].writePriceJustification(data_table)
            doc.append(pylatex_utils.NormalSizeCommand())

    def writePriceTableTwoIntoLatexDocument(self, doc):
        ''' Write unit price table two into a latex report.

        :param doc: pylatex document to write into.
        '''
        if(len(self)>0):
            #doc.append(pylatex_utils.ltx_star_.chapter("Cuadro de precios no. 2") + '\n'
            doc.append(pylatex_utils.SmallCommand())
            longTableStr= 'l'
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                for j in self.concepts:
                    self.concepts[j].writePriceTableTwoIntoLatexDocument(data_table)
            doc.append(pylatex_utils.NormalSizeCommand())

    def WriteHCalc(self, os):
        os.write(u"Código" + tab
           + "Ud." + tab
           + u"Denominación" + tab
           + "Precio en letra" + tab
           + "Precio en cifra" + '\n')
        for j in self.concepts:
            self.concepts[j].WriteHCalc(os)

    def getParametricConceptsKeys(self):
        ''' Return the keys of the parametric concepts.'''
        return list(self.parametricConcepts.keys())

    def getParametricConcept(self, key):
        ''' Return the parametric concept identified by the key.'''
        return self.parametricConcepts[key]

    def writeParametricConcepts(self, os= sys.stdout):
        ''' Writes a report of the parametrics concepts.'''
        for key in self.parametricConcepts:
            pc= self.parametricConcepts[key]
            pc.Write(os)
            
    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= super(Descompuestos, self).getDict()
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        pendingLinks= list() # Links that cannot be set yet.
        for key in dct:
            p= unit_price.UnitPrice(key)
            itemDict= dct[key]
            pendingLinks.extend(p.setFromDict(itemDict))
            self.Append(p)
        pendingLinks.extend(super(Descompuestos, self).setFromDict(dct))
        return pendingLinks

    def clear(self):
        '''removes all items from the container.'''
        # for p in self.concepts:
        #     print('unit price container: ', p)
        #     p.clear()
        super(Descompuestos, self).clear()
        self.parametricConcepts.clear()
