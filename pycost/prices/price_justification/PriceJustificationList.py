#PriceJustificationList.pyxx




import PriceJustificationRecordContainer
from pycost.utils import basic_types
from decimal import Decimal

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

    def size(self):
        return self.mano_de_obra.size()+self.materiales.size()+self.maquinaria.size()+self.otros.size()+self.percentages.size()


    def ImprLtxJustPre(self, os):
        total= self.getTotal()
        rnd= self.Redondeo()
        total_rnd= self.getTotalRnd()
        if size()<2:
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Sin descomposición"))
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


    def writePriceTableTwoIntoLatexDocument(self, os):
        total= self.getTotal()
        rnd= Redondeo()
        total_rnd= self.getTotalRnd()
        if size()<2:
            doc.append(" & & " + "Sin descomposición"
               + " & " + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(" & & " + pylatex_utils.ltx_textbf("TOTAL") + " & "
               + "\\textbf{"+basic_types.human_readable(total)+"}"
               + pylatex_utils.ltx_fin_reg + '\n')

        else:
            self.mano_de_obra.writePriceTableTwoIntoLatexDocument(os)
            self.materiales.writePriceTableTwoIntoLatexDocument(os)
            self.maquinaria.writePriceTableTwoIntoLatexDocument(os)
            self.otros.writePriceTableTwoIntoLatexDocument(os)
            self.percentages.writePriceTableTwoIntoLatexDocumentPorc(os)
            #Suma
            doc.append(pylatex_utils.ltx_fin_reg + '\n')
            doc.append(" & & " + "Suma" + pylatex_utils.ltx_ldots + " & "
               + basic_types.human_readable(total) + pylatex_utils.ltx_fin_reg + '\n')
            #Redondeo
            doc.append(" & & " + "Redondeo" + pylatex_utils.ltx_ldots + " & "
               + basic_types.human_readable(rnd) + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(pylatex_utils.ltx_cline("4-4") + '\n')
            doc.append(" & & " + pylatex_utils.ltx_textbf("TOTAL") + " & "
               + "\\textbf{"+basic_types.human_readable(total_rnd)+"}"
               + pylatex_utils.ltx_fin_reg + '\n')



    def writePriceTableOneIntoLatexDocument(self, data_table, genero):
        data_table.add_row([self.StrPriceToWords(genero),self.StrPrecioLtx()])


