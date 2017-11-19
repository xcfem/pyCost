#UnitPriceQuantitiesBase.py
'''Something that can return the quantities for a unit price.'''

from pycost.prices import unit_price_report
from pycost.measurements import measurement_detail
from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc

class UnitPriceQuantitiesBase(epc.EntPyCost):

    def __init__(self,u):
        super(UnitPriceQuantitiesBase,self).__init__()
        self.ud= u

    def getUnitPriceCode(self):
        return self.ud.Codigo()

    def UnidadMedida(self):
        return self.ud.Unidad()

    def PrecioUd(self):
        return self.ud.Precio()

    def PrecioRUd(self):
        return self.ud.PrecioR()

    def Informe(self):
        return self.UnitPriceReport(ud,Total())

    def StrPrecioUd(self):
        return self.ud.StrPrecio()

    def StrPrecioLtxUd(self):
        return self.ud.StrPrecioLtx()

    def Precio(self):
        return self.Total()*ud.Precio()

    def PrecioR(self):
        return ppl_precio(float(self.TotalR())*float(self.PrecioRUd()))

    def StrPrecioLtx(self):
        return self.PrecioR().EnHumano()

    def ImprLtxCabecera(self, os, totalr, ancho):
        '''Imprime la cabecera para la partida.'''
        os.write(ascii2latex(getUnitPriceCode()) + ltx_ampsnd
           + totalr + ' ' + ascii2latex(UnidadMedida()) + ltx_ampsnd
           + ltx_multicolumn(ltx_datos_multicolumn("4",ancho,ascii2latex(self.ud.getLongDescription()()))))


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
        quantities.ImprCompLtx(os,otra.quantities)
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
        quantities.ImprCompLtx(os)
        os.write(media_linea_en_blanco)
        ImprLtxPie(os,totalr)
        os.write(ltx_fin_reg + '\n')
        os.write(ltx_hline + '\n')
        os.write(linea_en_blanco + '\n')


    def ImprLtxCabeceraPre(self, os, totalr, ancho):
        os.write(ascii2latex(getUnitPriceCode()) + ltx_ampsnd
           + totalr + " " + ascii2latex(UnidadMedida()) + ltx_ampsnd
           + ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(self.ud.getLongDescription()()))))

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
        os.write(getUnitPriceCode() + tab
           + en_humano(Total(),3) + tab + ascii2latex(UnidadMedida()) + tab
           + '"' + ascii2latex(self.ud.getLongDescription()()) + '"' + '\n'
           + "Texto" + tab
           + "Unidades" + tab
           + "Largo" + tab
           + "Ancho" + tab
           + "Alto" + tab
           + "Parcial" + '\n')
        quantities.WriteHCalc(os)

    def WriteHCalcPre(self, os):
        os.write(getUnitPriceCode() + tab
           + Total() + tab + UnidadMedida() + tab + self.ud.getLongDescription()() + tab
           + StrPrecioUd() + tab
           + Precio() + '\n')

    def WriteBC3RegM(self, os, cap_padre, pos):
        os.write("~M|" + cap_padre + '\\' + getUnitPriceCode() + '|'
           + pos.write('|'
           + Total() + '|'))

    def WriteBC3(self, os, cap_padre, pos):
        WriteBC3RegM(os,cap_padre,pos)
        quantities.WriteBC3(os)
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
        quantities.ImprLtx(os)
        ImprLtxPie(os,totalr)
        os.write(ltx_fin_reg + '\n')
        os.write(ltx_hline + '\n')
        os.write(linea_en_blanco + '\n')


