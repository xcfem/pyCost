# -*- coding: utf-8 -*-
#Descompuestos.py

import pylatex
import logging
from pycost.prices import elementary_price_container
from pycost.prices import unit_price
from pycost.utils import concept_dict
from pycost.utils import pylatex_utils

class Descompuestos(concept_dict.ConceptDict):
    '''Unidades de obra.'''

    def AgregaComponente(self, el, cod_ud, cod_el, r, f):
        i= Busca(cod_ud)
        j= el.Busca(cod_el)
        if not j:
            logging.error("Elemento: " + cod_el
                      + " no encontrado en unidad de obra: " + cod_ud + '\n')
            exit(1)

        i.Append(j,f,r)

    def LeeBC3Fase1(self, cds):
        '''Read the units whitout its components.'''
        for i in cds:
            reg= cds.getUnitPriceData(i)
            ud= unit_price.UnitPrice()
            ud.LeeBC3Fase1(reg)
            self.Append(ud)


    def LeeBC3Fase2(self, cds, bp):
        '''Reads the components of the unit.'''
        ud= None
        error= False
        retval= set()
        for i in cds:
            reg= cds.getUnitPriceData(i)
            ud= self.Busca(reg.Codigo())
            error= ud.LeeBC3Fase2(reg,bp)
            if error:
                retval.add(reg.Codigo())
        return retval

    def WriteSpre(self, os):
        for j in self.map.keys():
            self.map[j].WriteSpre(os)

    def AsignaFactor(self, f):
        for j in self.map.keys():
            self.map[j].AsignaFactor(f)

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
                Append(unidad)
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
                    AgregaComponente(elementos,cod,cod_el,atof(cantidad.c_str()))
                    if(pos3>len(descomp)): break

                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')


    def writePriceTableOneIntoLatexDocument(self, doc):
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
                for j in self.map.keys():
                    data_table.add_empty_row()
                    self.map[j].writePriceTableOneIntoLatexDocument(data_table)
                    data_table.add_empty_row()

            doc.append(pylatex_utils.NormalSizeCommand())

    def writePriceJustification(self, doc):
        if(len(self)>0):
            doc.append(pylatex_utils.SmallCommand())
            longTableStr= 'l'
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                for j in self.map.keys():
                    self.map[j].writePriceJustification(data_table)
            doc.append(pylatex_utils.NormalSizeCommand())

    def writePriceTableTwoIntoLatexDocument(self, doc):
        if(len(self)>0):
            #doc.append(pylatex_utils.ltx_star_.chapter("Cuadro de precios no. 2") + '\n'
            doc.append(pylatex_utils.SmallCommand())
            longTableStr= 'l'
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                for j in self.map.keys():
                    self.map[j].writePriceTableTwoIntoLatexDocument(data_table)
            doc.append(pylatex_utils.NormalSizeCommand())

    def WriteHCalc(self, os):
        os.write(u"Código" + tab
           + "Ud." + tab
           + u"Denominación" + tab
           + "Precio en letra" + tab
           + "Precio en cifra" + '\n')
        for j in self.map.keys():
            self.map[j].WriteHCalc(os)

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

