#PriceJustificationList.pyxx




import PriceJustificationRecordContainer
from pycost.utils import basic_types
from decimal import Decimal
import pylatex

class PriceJustificationList(object):
    
    def __init__(self,pa, mano, mater, maqui, otr, porc):
      self.cumulated_percentages= pa
      self.mano_de_obra= mano
      self.materiales= mater
      self.maquinaria= maqui
      self.otros= otr
      self.percentages= porc
      base= basic_types.ppl_price(self.Base(),3)
      if self.cumulated_percentages:
        self.percentages.SetBaseAcum(base)
      else:
        self.percentages.SetBase(base)
    
    def Base(self):
        retval= basic_types.ppl_price(self.mano_de_obra.getTotal(),3)
        retval+= self.materiales.getTotal()
        retval+= self.maquinaria.getTotal()
        retval+= self.otros.getTotal()
        return retval

    def getTotal(self):
        retval= basic_types.ppl_price(self.Base(),3)
        retval+= self.percentages.getTotal()
        return retval

    def Redondeo(self):
        #return -self.getTotal().Redondeo()
        #XXX Redondeo para 2 decimales.
        tmp= self.getTotal()
        tmp*= Decimal('100')
        rnd= basic_types.ppl_price(round(tmp),3)
        rnd/= Decimal('100')
        return rnd

    def getTotalRnd(self):
        return self.getTotal() + self.Redondeo()

    def getTotalCP1(self):
        return basic_types.ppl_price(float(self.getTotalRnd()),2)

    def StrPrecioLtx(self):
        return basic_types.human_readable(self.getTotalCP1())

    def StrPriceToWords(self, genero):
        return basic_types.to_words(self.getTotalCP1(),genero)

    def __len__(self):
        return len(self.mano_de_obra)+len(self.materiales)+len(self.maquinaria)+len(self.otros)+len(self.percentages)


    def ImprLtxJustPre(self, os):
        total= self.getTotal()
        rnd= self.Redondeo()
        total_rnd= self.getTotalRnd()
        if(len(self)<2):
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r",basic_types.sin_desc_string))
               + " & & " + pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","TOTAL")) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r","\\textbf{"+basic_types.human_readable(total)+"}"))
               + pylatex_utils.ltx_fin_reg + '\n')

        else:
            self.mano_de_obra.ImprLtxJust(os)
            self.materiales.ImprLtxJust(os)
            self.maquinaria.ImprLtxJust(os)
            self.otros.ImprLtxJust(os)
            self.percentages.ImprLtxJust(os)
            #Suma
            os.write(pylatex_utils.ltx_fin_reg + '\n')
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Suma"+pylatex_utils.ltx_ldots)) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r",basic_types.human_readable(total)))
               + pylatex_utils.ltx_fin_reg + '\n')
            #Redondeo
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Redondeo"+pylatex_utils.ltx_ldots)) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r",basic_types.human_readable(rnd)))
               + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","TOTAL")) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r","\\textbf{"+basic_types.human_readable(total_rnd)+"}"))
               + pylatex_utils.ltx_fin_reg + '\n')


    def writePriceTableTwoIntoLatexDocument(self, data_table):
        total= self.getTotal()
        rnd= self.Redondeo()
        total_rnd= self.getTotalRnd()
        if(len(self)<2):
            row1= ['','',basic_types.sin_desc_string,'']
            data_table.add_row(row1)
            row2= ['','',pylatex.utils.bold('TOTAL'),pylatex.utils.bold(basic_types.human_readable(total))]
            #Total
            data_table.add_row(row2)
        else:
            data_table.add_empty_row()
            self.mano_de_obra.writePriceTableTwoIntoLatexDocument(data_table)
            self.materiales.writePriceTableTwoIntoLatexDocument(data_table)
            self.maquinaria.writePriceTableTwoIntoLatexDocument(data_table)
            self.otros.writePriceTableTwoIntoLatexDocument(data_table)
            self.percentages.writePriceTableTwoIntoLatexDocumentPorc(data_table)
            #Suma
            row1= ['','',pylatex.NoEscape('Suma \ldots'),basic_types.human_readable(total)]
            data_table.add_row(row1)
            #Redondeo
            row2= ['','',pylatex.NoEscape('Redondeo \ldots'),basic_types.human_readable(rnd)]
            data_table.add_row(row2)
            #Total
            data_table.append(pylatex.Command(pylatex.NoEscape('cline{4-4}')))
            row3= ['','',pylatex.NoEscape('TOTAL\ldots'),basic_types.human_readable(total_rnd)]
            data_table.add_row(row3)


    def writePriceTableOneIntoLatexDocument(self, data_table, genero):
        data_table.add_row(['','','',self.StrPriceToWords(genero),self.StrPrecioLtx()])


