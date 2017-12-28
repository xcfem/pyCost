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
        return self.UnitPriceReport(ud,getTotal())

    def StrPrecioUd(self):
        return self.ud.StrPrecio()

    def StrPrecioLtxUd(self):
        return self.ud.StrPrecioLtx()

    def Precio(self):
        return self.getTotal()*ud.Precio()

    def PrecioR(self):
        return basic_types.ppl_price(float(self.getTotalR())*float(self.PrecioRUd()))

    def StrPrecioLtx(self):
        return basic_types.human_readable(self.PrecioR())

    def printLatexHeader(self, data_table, totalr, ancho):
        '''Prints header in the quantities table.'''
        row= [pylatex_utils.ascii2latex(self.getUnitPriceCode())]
        row.append(str(totalr))
        row.append(' ' + pylatex_utils.ascii2latex(self.UnidadMedida()))
        row.append((pylatex.table.MultiColumn(3,align= pylatex.utils.NoEscape(ancho),data= pylatex.utils.NoEscape('\\scriptsize '+pylatex_utils.ascii2latex(self.ud.getLongDescription())+ '\\normalsize'))))
        data_table.add_row(row)

    def ImprCompLtxMed(self, doc, otra):
        '''Imprime la partida.'''
        doc.add_empty_row()
        totalr_otra= human_readable(otra.getTotalR())
        otra.printLatexHeader(os,totalr_otra,"p{4.5cm}|")
        doc.append(pylatex_utils.ltx_ampsnd)
        totalr_esta= basic_types.human_readable(getTotalR())
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
        doc.add_empty_row()


    #not  @brief Imprime la partida.
    def ImprCompLtxMed(self, os):
        media_empty_line= ['','', '', '', '', '']
        doc.add_empty_row()
        doc.append(media_empty_line)
        totalr= human_readable(self.getTotalR())
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
        doc.add_empty_row()


    def printLatexHeaderPre(self, data_table, totalr, ancho):
        row= [pylatex_utils.ascii2latex(self.getUnitPriceCode())]
        row.append(totalr+ " " + pylatex_utils.ascii2latex(self.UnidadMedida()))
        row.append(pylatex.table.MultiColumn(3, align=pylatex.utils.NoEscape(ancho),data=self.ud.getLongDescription()))
        data_table.add_row(row)

    def ImprCompLtxPre(self, os, otra):
        doc.add_empty_row()
        totalr_otra= human_readable(otra.getTotalR())
        otra.printLatexHeaderPre(os,totalr_otra,'p{2.5cm}')
        doc.append(pylatex_utils.ltx_ampsnd
           + otra.StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + otra.StrPrecioLtx() + pylatex_utils.ltx_ampsnd)
        totalr_esta= basic_types.human_readable(getTotalR())
        printLatexHeaderPre(os,totalr_esta,"p{2.5cm}")
        doc.append(pylatex_utils.ltx_ampsnd
           + StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + StrPrecioLtx() + pylatex_utils.ltx_fin_reg + '\n')
        doc.add_empty_row()

    def ImprCompLtxPre(self, os):
        media_empty_line= ['','', '', '', '']
        doc.add_empty_row()
        doc.append(empty_line + '\n')
        doc.append(media_empty_line)
        totalr_med= human_readable(self.getTotalR())
        printLatexHeaderPre(os,totalr_med,'p{2.5cm}')
        doc.append(pylatex_utils.ltx_ampsnd
           + StrPrecioLtxUd() + pylatex_utils.ltx_ampsnd
           + StrPrecioLtx() + pylatex_utils.ltx_fin_reg + '\n')
        doc.add_empty_row()

    def ImprLtxPre(self, data_table):
        totalr_med=  basic_types.human_readable(self.getTotalR())
        self.printLatexHeaderPre(data_table,totalr_med,'p{5cm}')
        row= ['','','',self.StrPrecioLtxUd(),self.StrPrecioLtx()]
        data_table.add_row(row)
        data_table.add_empty_row()

    #HCalc
    def WriteHCalcMed(self, os):
        os.write(getUnitPriceCode() + tab
           + en_humano(self.getTotal(),3) + tab + pylatex_utils.ascii2latex(UnidadMedida()) + tab
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
           + self.getTotal() + tab + UnidadMedida() + tab + self.ud.getLongDescription()() + tab
           + StrPrecioUd() + tab
           + Precio() + '\n')

    def WriteBC3RegM(self, os, cap_padre, pos):
        os.write("~M|" + cap_padre + '\\' + getUnitPriceCode() + '|'
           + pos.write('|'
           + self.getTotal() + '|'))

    def WriteBC3(self, os, cap_padre, pos):
        WriteBC3RegM(os,cap_padre,pos)
        quantities.WriteBC3(os)
        os.write('|' + endl_msdos)

    @staticmethod
    def printLtxColumnHeaders(data_table):
        data_table.add_row(["Texto","Unidades", "Largo", "Ancho","Alto","Parcial"])

    @staticmethod
    def ImprLtxPie(data_table, totalr):
        data_table.add_row([pylatex.table.MultiColumn(5,align= 'r',data= pylatex.NoEscape("Suma\\ldots")),pylatex.utils.bold(totalr)])


    def writeQuantitiesIntoLatexDocument(self, data_table):
        data_table.add_empty_row()
        totalr= basic_types.human_readable(self.getTotalR())
        self.printLatexHeader(data_table,totalr,'p{6cm}')
        #data_table.append(pylatex_utils.ltx_fin_reg + '\n')
        self.printLtxColumnHeaders(data_table)
        data_table.add_hline()
        self.quantities.printLtx(data_table)
        self.ImprLtxPie(data_table,totalr)
        data_table.add_hline()
        data_table.add_empty_row()


