# -*- coding: utf-8 -*-
#ElementaryPrices.py

import logging
from pycost.prices import elementary_price
from pycost.utils import concept_dict
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
    def printLatexHeader(self, tipo, os):
        str_tipo= basic_types.str_tipo(tipo)

        doc.append(pylatex_utils.ltx_begin("center") + '\n')
        doc.append(pylatex_utils.LargeCommand())
        doc.append(" Precios elementales de " + str_tipo + ' ')
        doc.append(pylatex_utils.NormalSizeCommand())
        doc.append(pylatex_utils.ltx_end("center") + '\n')
        doc.append(pylatex_utils.SmallCommand())
        doc.append("\\begin{longtable}{|l|l|p{4cm}|r|}" + '\n'
           + pylatex_utils.ltx_hline + '\n'
           + u"Código & Ud. & Denominación & Precio\\\\" + '\n'
           + pylatex_utils.ltx_hline + '\n'
           + pylatex_utils.ltx_endhead + '\n'
           + pylatex_utils.ltx_hline + '\n'
           + "\\multicolumn{" + 4 + "}{|r|}{../..}\\\\\\hline" + '\n'
           + pylatex_utils.ltx_endfoot + '\n'
           + pylatex_utils.ltx_hline + '\n'
           + pylatex_utils.ltx_endlastfoot + '\n')


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
                Append(elem)
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
                Append(elem)
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
                Append(elem)
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
        if not els.empty():
            logging.info("Reading elementary prices." + '\n')
            sz_inicial= len(self)
            el= elementary_price.ElementaryPrice()
            for i in self:
                el.readBC3(els.GetDatosElementaryPrice(i))
                Append(el)

            num_agregados= len(self)-sz_inicial
            if num_agregados != els.size():
                logging.error("¡Errornot , pasaron: " + els.size()
                          + " precios elementales y se cargaron "
                          + num_agregados+ '\n')
            logging.info("Loaded " + els.size() + " elementary prices. " + '\n')


    def ImprLtxTipo(self, tipo, os):
        printLatexHeader(tipo,os)
        el= None
        for i in self:
            el= ((i).second)
            if el.getType() == tipo:
                el.printLtx(os)

        doc.append("\\end{longtable}" + '\n')
        doc.append(pylatex_utils.NormalSizeCommand())

    def printLtx(self, os):
        ImprLtxTipo(mdo,os)
        doc.append(pylatex_utils.ltx_newpage + '\n')
        ImprLtxTipo(maq,os)
        doc.append(pylatex_utils.ltx_newpage + '\n')
        ImprLtxTipo(mat,os)

