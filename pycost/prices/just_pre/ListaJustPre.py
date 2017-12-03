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
      base= ppl_precio3(self.Base())
      if cumulated_percentages:
        percentages.SetBaseAcum(base)
      else:
        percentages.SetBase(base)
    
    def Base(self):
        retval= ppl_precio(mano_de_obra.getTotal(),3)
        retval+= materiales.getTotal()
        retval+= maquinaria.getTotal()
        retval+= otros.getTotal()
        return retval

    def getTotal(self):
        retval= ppl_precio(Base(),3)
        retval+= percentages.getTotal()
        return retval

    def Redondeo(self):
        #return -self.getTotal().Redondeo()
        #XXX Redondeo para 2 decimales.
        tmp= self.getTotal()
        tmp*= 100.0
        rnd= ppl_precio(tmp.Redondeo(),3)
        rnd/=100
        return rnd

    def getTotalRnd(self):
        return self.getTotal() + Redondeo()

    def getTotalCP1(self):
        return ppl_precio2(double(self.getTotalRnd()))

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
            os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Sin descomposición"))
               + " & & " + ltx_fin_reg + '\n' + ltx_fin_reg + '\n')
            #Total
            os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","TOTAL")) + " & "
               + ltx_multicolumn(ltx_datos_multicolumn("2","r","\\textbf{"+total.EnHumano()+"}"))
               + ltx_fin_reg + '\n')

        else:
            mano_de_obra.ImprLtxJust(os)
            materiales.ImprLtxJust(os)
            maquinaria.ImprLtxJust(os)
            otros.ImprLtxJust(os)
            percentages.ImprLtxJust(os)
            #Suma
            os.write(ltx_fin_reg + '\n')
            os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Suma"+ltx_ldots)) + " & "
               + ltx_multicolumn(ltx_datos_multicolumn("2","r",total.EnHumano()))
               + ltx_fin_reg + '\n')
            #Redondeo
            os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Redondeo"+ltx_ldots)) + " & "
               + ltx_multicolumn(ltx_datos_multicolumn("2","r",rnd.EnHumano()))
               + ltx_fin_reg + '\n')
            #Total
            os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","TOTAL")) + " & "
               + ltx_multicolumn(ltx_datos_multicolumn("2","r","\\textbf{"+total_rnd.EnHumano()+"}"))
               + ltx_fin_reg + '\n')


    def ImprLtxCP2(self, os):
        total= self.getTotal()
        rnd= Redondeo()
        total_rnd= self.getTotalRnd()
        if size()<2:
            os.write(" & & " + "Sin descomposición"
               + " & " + ltx_fin_reg + '\n')
            #Total
            os.write(" & & " + ltx_textbf("TOTAL") + " & "
               + "\\textbf{"+total.EnHumano()+"}"
               + ltx_fin_reg + '\n')

        else:
            mano_de_obra.ImprLtxCP2(os)
            materiales.ImprLtxCP2(os)
            maquinaria.ImprLtxCP2(os)
            otros.ImprLtxCP2(os)
            percentages.ImprLtxCP2Porc(os)
            #Suma
            os.write(ltx_fin_reg + '\n')
            os.write(" & & " + "Suma" + ltx_ldots + " & "
               + total.EnHumano() + ltx_fin_reg + '\n')
            #Redondeo
            os.write(" & & " + "Redondeo" + ltx_ldots + " & "
               + rnd.EnHumano() + ltx_fin_reg + '\n')
            #Total
            os.write(ltx_cline("4-4") + '\n')
            os.write(" & & " + ltx_textbf("TOTAL") + " & "
               + "\\textbf{"+total_rnd.EnHumano()+"}"
               + ltx_fin_reg + '\n')



    def ImprLtxCP1(self, os, genero):
        os.write(StrPrecioEnLetra(genero) + " & "
           + StrPrecioLtx())


