# -*- coding: utf-8 -*-
#ElementaryPrices.py

import pylatex
import logging
from pycost.prices import elementary_price
from pycost.utils import concept_dict
from pycost.utils import pylatex_utils
from pycost.utils import basic_types
from pycost.prices import component_list
from pycost.bc3 import codes

class ElementaryPrices(concept_dict.ConceptDict):
    ''' Container for elementary prices.'''
    
    def __init__(self):
        super(ElementaryPrices,self).__init__()
        
    def WriteHCalc(os):
        logging.error("ElementaryPrices.WriteHCalc no implementada." + '\n')

    @staticmethod
    def writeLatexHeader(doc, tipo):
        ''' Write the header for the elementary prices table.

        :param doc: pylatex document to write into.
        :param tipo: type of the prices to write (maquinaria, materiales o mano de obra).
        '''
        str_tipo= basic_types.str_tipo(tipo)

        doc.append(pylatex.NoEscape(pylatex_utils.ltx_begin(textStr= "center") + '\n'))
        doc.append(pylatex_utils.LargeCommand())
        doc.append(" Precios elementales de " + str_tipo + ' ')
        doc.append(pylatex_utils.NormalSizeCommand())
        doc.append(pylatex.NoEscape(pylatex_utils.ltx_end("center") + '\n'))
        doc.append(pylatex_utils.SmallCommand())
        # Create LaTeX longtable.
        longTableStr= '|l|l|p{4cm}|r|'
        headerRow= [u'Código','Ud.',u'Denominación',u'Coste directo']
        with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
            data_table.add_hline()
            data_table.add_row(headerRow)
            data_table.add_hline()
            data_table.end_table_header()
            data_table.add_hline()
            data_table.add_row((pylatex.table.MultiColumn(4, align='|r|',data='../..'),))
            data_table.add_hline()
            data_table.end_table_footer()
            data_table.add_hline()
            data_table.end_table_last_footer()
        return data_table

    def LeeMdoSpre(self, iS):
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
                precios= ''
                getline(iS,precios,'\n')
                pre= ''
                pos= precios.find('|')
                if pos<len(precios):
                    pre= precios.substr(0,pos)
                else:
                    pre= precios.substr(0,len(precios)-1)
                elem= elementary_price.ElementaryPrice(cod,tit,ud,atof(pre.c_str()),mdo)
                elem.texto_largo= tit
                self.Append(elem)
                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')

    def LeeMaqSpre(self, iS):
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
                precios= ''
                getline(iS,precios,'\n')
                pre= ''
                pos= precios.find('|')
                if pos<1000:
                    pre= precios.substr(0,pos)
                else:
                    pre= precios.substr(0,len(precios)-1)
                elem= elementary_price.ElementaryPrice(cod,tit,ud,atof(pre.c_str()),maq)
                elem.texto_largo= tit
                self.Append(elem)
                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')

    def LeeMatSpre(self, iS):
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
                precios= ''
                getline(iS,precios,'\n')
                pre= ''
                pos= precios.find('|')
                if pos<1000:
                    pre= precios.substr(0,pos)
                else:
                    pre= precios.substr(0,len(precios)-1)
                elem= elementary_price.ElementaryPrice(cod,tit,ud,atof(pre.c_str()),mat)
                elem.texto_largo= tit
                self.Append(elem)
                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')


    def WriteSpre(self):
        ofs_mdo= std.ofstream("MDO001.std",std.ios.out)
        ofs_maq= std.ofstream("MAQ001.std",std.ios.out)
        ofs_mat= std.ofstream("MAT001.std",std.ios.out)
        for i in self:
            tipo= (i).second.getType()
            if(tipo==mdo):
                (i).second.WriteSpre(ofs_mdo)
                break
            elif(tipo==maq):
                (i).second.WriteSpre(ofs_maq)
                break
            elif(tipo==mat):
                (i).second.WriteSpre(ofs_mat)
                break
            else:
                (i).second.WriteSpre(ofs_mdo)
                break

        ofs_mdo.close()
        ofs_maq.close()
        ofs_mat.close()


    def LeeSpre(self, iS):
        Str= ''
        getline(iS,str,'\n')
        if(Str.find("[MDO]")<len(Str)): LeeMdoSpre(iS)
        getline(iS,Str,'\n')
        if(Str.find("[MAQ]")<len(Str)): LeeMaqSpre(iS)
        getline(iS,Str,'\n')
        if(Str.find("[MAT]")<len(Str)): LeeMatSpre(iS)

    def readBC3(self, els):
        
        if (els and (len(els)>0)):
            logging.info("Reading elementary prices." + '\n')
            sz_inicial= len(self)
            keys= list(self.concepts.keys())
            for key in els.keys():
                data= els.GetDatosElementaryPrice(key)
                el= elementary_price.ElementaryPrice()
                el.readBC3(data)
                self.Append(el)

            num_agregados= len(self)-sz_inicial
            sz= len(els)
            if num_agregados != sz:
                logging.error("¡Errornot , pasaron: " + str(sz)
                          + " precios elementales y se cargaron "
                          + str(num_agregados)+ '\n')
            logging.info("Loaded " + str(sz) + " elementary prices. " + '\n')


    def writeLatexPricesOfType(self, doc, tipo):
        ''' Write the header for the elementary prices table.

        :param doc: pylatex document to write into.
        :param tipo: type of the prices to write (maquinaria, materiales o mano de obra).
        '''
        data_table= self.writeLatexHeader(doc, tipo)
        el= None
        for key in self.concepts:
            el= self.concepts[key]
            if el.getType() == tipo:
                el.writeLatex(data_table)
        doc.append(pylatex_utils.NormalSizeCommand())

    def writeLatex(self, doc, tipos= [basic_types.mdo, basic_types.maq, basic_types.mat]):
        ''' Write the header for the elementary prices table.

        :param doc: pylatex document to write into.
        :param tipos: types of the prices to write (maquinaria, materiales o mano de obra) defaults to all of them.
        '''
        for tp in tipos:
            self.writeLatexPricesOfType(doc, tp)
            # doc.append(pylatex.NoEscape(pylatex_utils.ltx_newpage + '\n'))

    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= super(ElementaryPrices, self).getDict()
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        pendingLinks= list() # Links that cannot be set yet.
        for key in dct:
            p= elementary_price.ElementaryPrice(key)
            itemDict= dct[key]
            pendingLinks.extend(p.setFromDict(itemDict))
            self.Append(p)
        pendingLinks.extend(super(ElementaryPrices, self).setFromDict(dct))
        return pendingLinks

    def clear(self):
        '''removes all items from the chapter.'''
        super(ElementaryPrices, self).clear()
