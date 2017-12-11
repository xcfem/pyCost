# -*- coding: utf-8 -*-
#ChapterQuantities.py
#Quantities de un capítulo.




from pycost.structure import unit_price_quantities
from pycost.measurements import measurement_report
#import Pieza
from pycost.utils import EntPyCost as epc

import pylatex
from pycost.utils import pylatex_utils

class ChapterQuantities(list, epc.EntPyCost):

    def StrPrecioLtx(self):
        return self.PrecioR().EnHumano()

    def Precio(self):
        t= 0.0
        for i in self:
            t+=(i).Precio()
        return t

    def PrecioR(self):
        t= basic_types.ppl_precio(0.0)
        for i in self:
            t+=(i).PrecioR()
        return t

    def Write(self, os, cod, pos):
        contador= 1
        for i in self:
            pos_med= pos + num2str(contador,0) + '\\'
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
                   + (i).getTotal() + '\\')
            os.write('|' + endl_msdos)

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
            doc.append(pylatex_utils.ltx_normalsize + '\n')

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
               + tit_otra + "}} & \\textbf{" + otra.StrPrecioLtx() + "} & " + '\n')
            doc.append("\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
               + tit + "}} & \\textbf{" + StrPrecioLtx() + "}\\\\" + '\n')
            doc.append("\\end{longtable}" + '\n')
            doc.append(pylatex_utils.ltx_normalsize + '\n')

    def ImprLtxPre(self, os, tit):
        '''Imprime presupuestos parciales.'''
        if(len(self)):
            doc.append(pylatex_utils.SmallCommand())
            doc.append("\\begin{longtable}{lrlrr}" + '\n'
               + "Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{Precio unitario} & Importe \\\\" + '\n'
               + "\\hline" + '\n'
               + "\\endhead" + '\n'
               + "\\multicolumn{5}{r}{../..}\\\\" + '\n'
               + "\\endfoot" + '\n'
               + "\\endlastfoot" + '\n')
            for i in self:
                (i).ImprLtxPre(os)
            doc.append("\\multicolumn{4}{p{8cm}}{\\textbf{Total: " + tit + "}} & \\textbf{" + StrPrecioLtx() + "}\\\\" + '\n')
            doc.append("\\end{longtable}" + '\n')
            doc.append(pylatex_utils.ltx_normalsize + '\n')


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

