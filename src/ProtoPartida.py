#ProtoPartida.py
#Algo capaz de devolver mediciones de una unidad de obra.




import InformeUdObra
import Mediciones
import basic_types
import Obra

class ProtoPartida(EntPyCost):

    def __init__(self,u):
        super(ProtoPartida,self).__init__()
        self.ud= u

    def CodigoUdObra(self):
        return self.ud.Codigo()

    def UnidadMedida(self):
        return self.ud.Unidad()

    def TextoLUdObra(self):
        return self.ud.TextoLargo()

    def PrecioUd(self):
        return self.ud.Precio()

    def PrecioRUd(self):
        return self.ud.PrecioR()

    def Informe(self):
        return self.InformeUdObra(ud,Total())

    def StrPrecioUd(self):
        return self.ud.StrPrecio()

    def StrPrecioLtxUd(self):
        return self.ud.StrPrecioLtx()

    def Precio(self):
        return self.Total()*PrecioUd()

    def PrecioR(self):
        return ppl_precio(float(self.TotalR())*float(self.PrecioRUd()))

    def StrPrecioLtx(self):
        return self.PrecioR().EnHumano()

    def ImprLtxCabecera(self, os, totalr, ancho):
        '''Imprime la cabecera para la partida.'''
        os.write(ascii2latex(CodigoUdObra()) + ltx_ampsnd
           + totalr + ' ' + ascii2latex(UnidadMedida()) + ltx_ampsnd
           + ltx_multicolumn(ltx_datos_multicolumn("4",ancho,ascii2latex(TextoLUdObra()))))


    def ImprCompLtxMed(self, os, otra):
        '''Imprime la partida.'''
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        os.write(linea_en_blanco + '\n')
        totalr_otra= otra.TotalR().EnHumano()
        otra.ImprLtxCabecera(os,totalr_otra,"p{4.5cm}|")
        os.write(ltx_ampsnd)
        totalr_esta = TotalR().EnHumano()
        ImprLtxCabecera(os,totalr_esta,"p{4.5cm}")
        os.write(ltx_fin_reg + '\n')
        ImprLtxLeyenda(os)
        os.write(ltx_ampsnd)
        ImprLtxLeyenda(os)
        os.write(ltx_fin_reg + '\n' + ltx_hline + '\n')
        Meds().ImprCompLtx(os,otra.Meds())
        ImprLtxPie(os,totalr_otra)
        os.write(ltx_ampsnd)
        ImprLtxPie(os,totalr_esta)
        os.write(ltx_fin_reg + '\n')
        os.write(ltx_hline + '\n')
        os.write(linea_en_blanco + '\n')


    #not  @brief Imprime la partida.
    def ImprCompLtxMed(self, os):
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
        os.write(linea_en_blanco + '\n')
        os.write(media_linea_en_blanco)
        totalr= self.TotalR().EnHumano()
        ImprLtxCabecera(os,totalr,"p{4.5cm}")
        os.write(ltx_fin_reg + '\n')
        #ImprLtxLeyenda(os)
        #os.write(ltx_ampsnd
        os.write(media_linea_en_blanco)
        ImprLtxLeyenda(os)
        os.write(ltx_fin_reg + '\n' + ltx_hline + '\n')
        Meds().ImprCompLtx(os)
        os.write(media_linea_en_blanco)
        ImprLtxPie(os,totalr)
        os.write(ltx_fin_reg + '\n')
        os.write(ltx_hline + '\n')
        os.write(linea_en_blanco + '\n')


    def ImprLtxCabeceraPre(self, os, totalr, ancho):
        os.write(ascii2latex(CodigoUdObra()) + ltx_ampsnd
           + totalr + " " + ascii2latex(UnidadMedida()) + ltx_ampsnd
           + ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(TextoLUdObra()))))

    def ImprCompLtxPre(self, os, otra):
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        os.write(linea_en_blanco + '\n')
        totalr_otra = otra.TotalR().EnHumano()
        otra.ImprLtxCabeceraPre(os,totalr_otra,"p{2.5cm}")
        os.write(ltx_ampsnd
           + otra.StrPrecioLtxUd() + ltx_ampsnd
           + otra.StrPrecioLtx() + ltx_ampsnd)
        totalr_esta = TotalR().EnHumano()
        ImprLtxCabeceraPre(os,totalr_esta,"p{2.5cm}")
        os.write(ltx_ampsnd
           + StrPrecioLtxUd() + ltx_ampsnd
           + StrPrecioLtx() + ltx_fin_reg + '\n')
        os.write(linea_en_blanco + '\n')

    def ImprCompLtxPre(self, os):
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
        os.write(linea_en_blanco + '\n')
        os.write(media_linea_en_blanco)
        totalr_med= self.TotalR().EnHumano()
        ImprLtxCabeceraPre(os,totalr_med,"p{2.5cm}")
        os.write(ltx_ampsnd
           + StrPrecioLtxUd() + ltx_ampsnd
           + StrPrecioLtx() + ltx_fin_reg + '\n')
        os.write(linea_en_blanco + '\n')

    def ImprLtxPre(self, os):
        linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        totalr_med= TotalR().EnHumano()
        ImprLtxCabeceraPre(os,totalr_med,"p{5cm}")
        os.write(ltx_ampsnd
           + StrPrecioLtxUd() + ltx_ampsnd
           + StrPrecioLtx() + ltx_fin_reg + '\n')
        os.write(linea_en_blanco + '\n')

    #HCalc
    def WriteHCalcMed(self, os):
        os.write(CodigoUdObra() + tab
           + en_humano(Total(),3) + tab + ascii2latex(UnidadMedida()) + tab
           + '"' + ascii2latex(TextoLUdObra()) + '"' + '\n'
           + "Texto" + tab
           + "Unidades" + tab
           + "Largo" + tab
           + "Ancho" + tab
           + "Alto" + tab
           + "Parcial" + '\n')
        Meds().WriteHCalc(os)

    def WriteHCalcPre(self, os):
        os.write(CodigoUdObra() + tab
           + Total() + tab + UnidadMedida() + tab + TextoLUdObra() + tab
           + StrPrecioUd() + tab
           + Precio() + '\n')

    def WriteBC3RegM(self, os, cap_padre, pos):
        os.write("~M|" + cap_padre + '\\' + CodigoUdObra() + '|'
           + pos.write('|'
           + Total() + '|'))

    def WriteBC3(self, os, cap_padre, pos):
        WriteBC3RegM(os,cap_padre,pos)
        Meds().WriteBC3(os)
        os.write('|' + endl_msdos)

    @staticmethod
    def ImprLtxLeyenda(self, os):
        os.write("Texto" + ltx_ampsnd
           + "Unidades" + ltx_ampsnd
           + "Largo" + ltx_ampsnd
           + "Ancho" + ltx_ampsnd
           + "Alto" + ltx_ampsnd
           + "Parcial")


    @staticmethod
    def ImprLtxPie(self, os, totalr):
        os.write(ltx_multicolumn(ltx_datos_multicolumn("5","r","Suma "+ ltx_ldots)) + ltx_ampsnd
           + ltx_textbf(totalr))


    def ImprLtxMed(self, os):
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        os.write(linea_en_blanco + '\n')
        totalr = TotalR().EnHumano()
        ImprLtxCabecera(os,totalr,"p{6cm}")
        os.write(ltx_fin_reg + '\n')
        ImprLtxLeyenda(os)
        os.write(ltx_fin_reg + '\n'+ ltx_hline + '\n')
        Meds().ImprLtx(os)
        ImprLtxPie(os,totalr)
        os.write(ltx_fin_reg + '\n')
        os.write(ltx_hline + '\n')
        os.write(linea_en_blanco + '\n')


