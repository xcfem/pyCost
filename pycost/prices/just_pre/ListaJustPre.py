#ListaJustPre.pyxx




import ListaRegJustPre
import basic_types

class ListaJustPre(object):
    
    def __init__(self,pa, mano, mater, maqui, otr, porc):
      self.cumulated_percentages= pa
      self.mano_de_obra= mano
      self.materiales= mater
      self.maquinaria= maqui
      self.otros= otr
      self.percentages= porc
      base= basic_types.ppl_precio3(self.Base())
      if cumulated_percentages:
        percentages.SetBaseAcum(base)
      else:
        percentages.SetBase(base)
    
    def Base(self):
        retval= basic_types.ppl_precio(mano_de_obra.getTotal(),3)
        retval+= materiales.getTotal()
        retval+= maquinaria.getTotal()
        retval+= otros.getTotal()
        return retval

    def getTotal(self):
        retval= basic_types.ppl_precio(Base(),3)
        retval+= percentages.getTotal()
        return retval

    def Redondeo(self):
        #return -self.getTotal().Redondeo()
        #XXX Redondeo para 2 decimales.
        tmp= self.getTotal()
        tmp*= 100.0
        rnd= basic_types.ppl_precio(tmp.Redondeo(),3)
        rnd/=100
        return rnd

    def getTotalRnd(self):
        return self.getTotal() + Redondeo()

    def getTotalCP1(self):
        return basic_types.ppl_precio2(double(self.getTotalRnd()))

    def StrPrecioLtx(self):
        return self.getTotalCP1().EnHumano()

    def StrPrecioEnLetra(self, genero):
        return self.getTotalCP1().EnLetra(genero)

    def size(self):
        return mano_de_obra.size()+materiales.size()+maquinaria.size()+otros.size()+percentages.size()


    def ImprLtxJustPre(self, os):
        total= self.getTotal()
        rnd= self.Redondeo()
        total_rnd= self.getTotalRnd()
        if size()<2:
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Sin descomposición"))
               + " & & " + pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","TOTAL")) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r","\\textbf{"+total.EnHumano()+"}"))
               + pylatex_utils.ltx_fin_reg + '\n')

        else:
            mano_de_obra.ImprLtxJust(os)
            materiales.ImprLtxJust(os)
            maquinaria.ImprLtxJust(os)
            otros.ImprLtxJust(os)
            percentages.ImprLtxJust(os)
            #Suma
            os.write(pylatex_utils.ltx_fin_reg + '\n')
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Suma"+pylatex_utils.ltx_ldots)) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r",total.EnHumano()))
               + pylatex_utils.ltx_fin_reg + '\n')
            #Redondeo
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","Redondeo"+pylatex_utils.ltx_ldots)) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r",rnd.EnHumano()))
               + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","r","TOTAL")) + " & "
               + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("2","r","\\textbf{"+total_rnd.EnHumano()+"}"))
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
               + "\\textbf{"+total.EnHumano()+"}"
               + pylatex_utils.ltx_fin_reg + '\n')

        else:
            mano_de_obra.writePriceTableTwoIntoLatexDocument(os)
            materiales.writePriceTableTwoIntoLatexDocument(os)
            maquinaria.writePriceTableTwoIntoLatexDocument(os)
            otros.writePriceTableTwoIntoLatexDocument(os)
            percentages.writePriceTableTwoIntoLatexDocumentPorc(os)
            #Suma
            doc.append(pylatex_utils.ltx_fin_reg + '\n')
            doc.append(" & & " + "Suma" + pylatex_utils.ltx_ldots + " & "
               + total.EnHumano() + pylatex_utils.ltx_fin_reg + '\n')
            #Redondeo
            doc.append(" & & " + "Redondeo" + pylatex_utils.ltx_ldots + " & "
               + rnd.EnHumano() + pylatex_utils.ltx_fin_reg + '\n')
            #Total
            doc.append(pylatex_utils.ltx_cline("4-4") + '\n')
            doc.append(" & & " + pylatex_utils.ltx_textbf("TOTAL") + " & "
               + "\\textbf{"+total_rnd.EnHumano()+"}"
               + pylatex_utils.ltx_fin_reg + '\n')



    def writePriceTableOneIntoLatexDocument(self, os, genero):
        doc.append(StrPrecioEnLetra(genero) + " & "
           + StrPrecioLtx())


