# -*- coding: utf-8 -*-
#ChapterQuantities.py
#Quantities de un capítulo.




import pylatex
from pycost.structure import unit_price_quantities
from pycost.measurements import measurement_report
#import Pieza
from pycost.utils import EntPyCost as epc

from pycost.utils import pylatex_utils
from pycost.utils import basic_types

class ChapterQuantities(list, epc.EntPyCost):

    def getLtxPriceString(self):
        return basic_types.human_readable(self.getRoundedPrice())

    def getPrice(self):
        t= 0.0
        for i in self:
            t+=(i).getPrice()
        return t

    def getRoundedPrice(self):
        t= basic_types.ppl_price(0.0)
        for i in self:
            t+=(i).getRoundedPrice()
        return t

    def Write(self, os, cod, pos):
        contador= 1
        for i in self:
            pos_med= pos + str(contador) + '\\'
            (i).WriteBC3(os,cod,pos_med)
            contador+= 1

    def WriteDescompBC3(self, os, cod):
        if(len(self)<1):
            return
        else:
            os.write("~D" + '|' #Antes estaba con ~Y (daba problemas)
             + cod + '|')
            for i in self:
                os.write((i).getUnitPriceCode() + "\\1\\" #factor 1
                   + str((i).getRoundedTotal()) + '\\')
            os.write('|' + '\n')

    def ImprCompLtxMed(self, os, otra):
        if len(self):
            doc.append(pylatex_utils.ltx_tiny + '\n')
            doc.append(pylatex_utils.ltx_begin("longtable}{lrrrrr|lrrrrr") + '\n'
               + "\\multicolumn{6}{c|}{\\normalsize\\textbf{Proyecto de construcción}\\tiny} &"
               + "\\multicolumn{6}{c}{\\normalsize\\textbf{Proyecto modificado}\\tiny} \\\\"
               + '\n' + pylatex_utils.ltx_hline + '\n'
               + pylatex_utils.ltx_endhead + '\n'
               + "\\multicolumn{12}{r}{../..}\\\\" + '\n'
               + pylatex_utils.ltx_endfoot + '\n'
               + pylatex_utils.ltx_endlastfoot + '\n')
            for i in self:
                 cod= (i).getUnitPriceCode()
                 for j in otra:
                    if(cod == (j).getUnitPriceCode()): break
                    if(j!=otra.end()): #Found it!
                        (i).ImprCompLtxMed(os,*(j))
                    else:
                        (i).ImprCompLtxMed(os)
            doc.append("\\end{longtable}" + '\n')
            doc.append(pylatex_utils.NormalSizeCommand())

    def writeQuantitiesIntoLatexDocument(self, doc):
        if len(self):
            num_campos= 6
            longTableStr= 'lrrrrr'
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                data_table.add_row((pylatex.table.MultiColumn(num_campos, align='r',data='../..'),))
                data_table.end_table_footer()
                data_table.end_table_last_footer()
                for i in self:
                    (i).writeQuantitiesIntoLatexDocument(data_table)
            doc.append(pylatex.Command('newpage'))

    def ImprCompLtxPre(self, os, tit, otra, tit_otra):
        if size():
            doc.append(pylatex_utils.ltx_tiny + '\n')
            doc.append(pylatex_utils.ltx_begin("longtable}{lrlrr|lrlrr") + '\n'
               + "\\multicolumn{5}{c|}{\\normalsize\\textbf{Proyecto de construcción}\\tiny} &"
               + "\\multicolumn{5}{c}{\\normalsize\\textbf{Proyecto modificado}\\tiny} \\\\"
               + '\n' + pylatex_utils.ltx_hline + '\n'
               + "Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{P. unitario} & Importe & Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{P. unitario} & Importe \\\\" + '\n'
               + pylatex_utils.ltx_hline + '\n'
               + pylatex_utils.ltx_endhead + '\n'
               + "\\multicolumn{10}{r}{../..}\\\\" + '\n'
               + pylatex_utils.ltx_endfoot + '\n'
               + pylatex_utils.ltx_endlastfoot + '\n')
            for i in self:
                 cod= (i).getUnitPriceCode()
                 for j in otra:
                     if(cod == (j).getUnitPriceCode()): break
                 if(j!=otra.end()): #Found it!
                     (i).ImprCompLtxPre(os,*(j))
                 else:
                     (i).ImprCompLtxPre(os)

            doc.append("\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
               + tit_otra + "}} & \\textbf{" + otra.getLtxPriceString() + "} & " + '\n')
            doc.append("\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
               + tit + "}} & \\textbf{" + getLtxPriceString() + "}\\\\" + '\n')
            doc.append("\\end{longtable}" + '\n')
            doc.append(pylatex_utils.NormalSizeCommand())

    def ImprLtxPre(self, doc, tit):
        '''Imprime presupuestos parciales.'''
        if len(self):
            doc.append(pylatex_utils.SmallCommand())
            num_campos= 5
            longTableStr= 'lrlrr'
            header_row= ['Partida','Cantidad',u'Descripción']
            header_row.append(pylatex.table.MultiColumn(1, align=pylatex.utils.NoEscape('p{1.5cm}'),data='Precio unitario'))
            header_row.append('Importe')
                                            
            with doc.create(pylatex_utils.LongTable(longTableStr)) as data_table:
                data_table.add_row(header_row)
                data_table.add_hline()
                data_table.end_table_header()
                data_table.add_row((pylatex.table.MultiColumn(num_campos, align='r',data='../..'),))
                data_table.end_table_footer()
                data_table.end_table_last_footer()
                for i in self:
                    (i).ImprLtxPre(data_table)
                data_table.add_row([pylatex.table.MultiColumn(4, align=pylatex.utils.NoEscape('p{8cm}'),data=pylatex.utils.bold('Total: '+tit)),pylatex.utils.bold(self.getLtxPriceString())])
            doc.append(data_table)
            doc.append(pylatex_utils.NormalSizeCommand())


    def WriteHCalcMed(self, os):
        for i in self:
            (i).WriteHCalcMed(os)

    def WriteHCalcPre(self, os):
        for i in self:
            (i).WriteHCalcPre(os)

    def getQuantitiesReport(self):
        retval= QuantitiesReport()
        for i in self:
            retval.Inserta((i).Informe())
        return retval

