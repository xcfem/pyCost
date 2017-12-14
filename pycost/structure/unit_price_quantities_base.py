#UnitPriceQuantitiesBase.py
'''Something that can return the quantities for a unit price.'''

from pycost.prices import unit_price_report
from pycost.measurements import measurement_detail
from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc
import pylatex
from pycost.utils import pylatex_utils

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
        return self.getTotal()*ud.Precio()

    def PrecioR(self):
        return basic_types.ppl_precio(float(self.TotalR())*float(self.PrecioRUd()))

    def StrPrecioLtx(self):
        return self.PrecioR().EnHumano()

    def printLatexHeader(self, data_table, totalr, ancho):
        '''Imprime la cabecera para la partida.'''
        row= [pylatex_utils.ascii2latex(self.getUnitPriceCode())]
        row.append(str(totalr))
        row.append(' ' + pylatex_utils.ascii2latex(self.UnidadMedida()))
        row.append((pylatex.table.MultiColumn(3,align= pylatex.utils.NoEscape(ancho),data= pylatex_utils.ascii2latex(self.ud.getLongDescription()))))
        data_table.add_row(row)

    def ImprCompLtxMed(self, doc, otra):
        '''Imprime la partida.'''
        empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_fin_reg
        doc.append(empty_line + '\n')
        totalr_otra= otra.TotalR().EnHumano()
        otra.printLatexHeader(os,totalr_otra,"p{4.5cm}|")
        doc.append(pylatex_utils.ltx_ampsnd)
        totalr_esta= TotalR().EnHumano()
        printLatexHeader(os,totalr_esta,"p{4.5cm}")
        doc.append(pylatex_utils.ltx_fin_reg + '\n')
        ImprLtxLeyenda(doc)
        doc.append(pylatex_utils.ltx_ampsnd)
        ImprLtxLeyenda(doc)
        doc.append(pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_hline + '\n')
        quantities.ImprCompLtx(os,otra.quantities)
        ImprLtxPie(os,totalr_otra)
        doc.append(pylatex_utils.ltx_ampsnd)
        ImprLtxPie(os,totalr_esta)
        doc.append(pylatex_utils.ltx_fin_reg + '\n')
        doc.append(pylatex_utils.ltx_hline + '\n')
        doc.append(empty_line + '\n')


    #not  @brief Imprime la partida.
    def ImprCompLtxMed(self, os):
        empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_fin_reg
        media_empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd
        doc.append(empty_line + '\n')
        doc.append(media_empty_line)
        totalr= self.TotalR().EnHumano()
        printLatexHeader(os,totalr,"p{4.5cm}")
        doc.append(pylatex_utils.ltx_fin_reg + '\n')
        #ImprLtxLeyenda(doc)
        #doc.append(pylatex_utils.ltx_ampsnd
        doc.append(media_empty_line)
        ImprLtxLeyenda(doc)
        doc.append(pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_hline + '\n')
        quantities.ImprCompLtx(os)
        doc.append(media_empty_line)
        ImprLtxPie(os,totalr)
        doc.append(pylatex_utils.ltx_fin_reg + '\n')
        doc.append(pylatex_utils.ltx_hline + '\n')
        doc.append(empty_line + '\n')


    def printLatexHeaderPre(self, os, totalr, ancho):
        doc.append(pylatex_utils.ascii2latex(getUnitPriceCode()) + pylatex_utils.ltx_ampsnd
           + totalr + " " + pylatex_utils.ascii2latex(UnidadMedida()) + pylatex_utils.ltx_ampsnd
           + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("1",ancho,pylatex_utils.ascii2latex(self.ud.getLongDescription()()))))

    def ImprCompLtxPre(self, os, otra):
        empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_fin_reg
        doc.append(empty_line + '\n')
        totalr_otra= otra.TotalR().EnHumano()
        otra.printLatexHeaderPre(os,totalr_otra,"p{2.5cm}")
        doc.append(pylatex_utils.ltx_ampsnd
           + otra.StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + otra.StrPrecioLtx() + pylatex_utils.ltx_ampsnd)
        totalr_esta= TotalR().EnHumano()
        printLatexHeaderPre(os,totalr_esta,"p{2.5cm}")
        doc.append(pylatex_utils.ltx_ampsnd
           + StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + StrPrecioLtx() + pylatex_utils.ltx_fin_reg + '\n')
        doc.append(empty_line + '\n')

    def ImprCompLtxPre(self, os):
        empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_fin_reg
        media_empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd
        doc.append(empty_line + '\n')
        doc.append(media_empty_line)
        totalr_med= self.TotalR().EnHumano()
        printLatexHeaderPre(os,totalr_med,"p{2.5cm}")
        doc.append(pylatex_utils.ltx_ampsnd
           + StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + StrPrecioLtx() + pylatex_utils.ltx_fin_reg + '\n')
        doc.append(empty_line + '\n')

    def ImprLtxPre(self, doc):
        empty_line= pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_ampsnd+pylatex_utils.ltx_fin_reg
        totalr_med= TotalR().EnHumano()
        printLatexHeaderPre(os,totalr_med,"p{5cm}")
        doc.append(pylatex_utils.ltx_ampsnd
           + StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + StrPrecioLtx() + pylatex_utils.ltx_fin_reg + '\n')
        doc.append(empty_line + '\n')

    #HCalc
    def WriteHCalcMed(self, os):
        os.write(getUnitPriceCode() + tab
           + en_humano(Total(),3) + tab + pylatex_utils.ascii2latex(UnidadMedida()) + tab
           + '"' + pylatex_utils.ascii2latex(self.ud.getLongDescription()()) + '"' + '\n'
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
    def printLtxColumnHeaders(data_table):
        data_table.add_row(["Texto","Unidades", "Largo", "Ancho","Alto","Parcial"])

    @staticmethod
    def ImprLtxPie(doc, totalr):
        doc.append(pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("5","r","Suma "+ pylatex_utils.ltx_ldots)) + pylatex_utils.ltx_ampsnd
           + pylatex_utils.ltx_textbf(totalr))


    def writeQuantitiesIntoLatexDocument(self, data_table):
        empty_line= ['','','','','','']
        data_table.add_row(empty_line)
        totalr= basic_types.EnHumano(self.getTotalR())
        self.printLatexHeader(data_table,totalr,'p{6cm}')
        #data_table.append(pylatex_utils.ltx_fin_reg + '\n')
        self.printLtxColumnHeaders(data_table)
        data_table.add_hline()
        self.quantities.printLtx(data_table)
        self.ImprLtxPie(data_table,totalr)
        data_table.add_hline()
        data_table.add_row(empty_line)


