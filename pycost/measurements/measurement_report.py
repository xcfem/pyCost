# -*- coding: utf-8 -*-
#QuantitiesReport.py


from pycost.prices import unit_price_report as iuo

class QuantitiesReport(dict):

    def Inserta(self, iu):
        i= find(iu.Unidad())
        if i!=end():
            (i).second+= iu.Medicion()
        else:
            (self)[iu.Unidad()]= iu.Medicion()

    def Merge(self, otro):
        for i in otro:
            Inserta(UnitPriceReport((i).first,(i).second))

    def printLtx(self, os):
        if(size()>0):
            longTableStr= '|l|p{4cm}|r|r|'
            headerRow1= ["Código","Descripción.","Medición",'Precio']
            with doc.create(pylatex.table.LongTable(longTableStr)) as data_table:
                data_table.add_hline()
                data_table.add_row(headerRow1)
                data_table.add_hline()
                data_table.end_table_header()
                data_table.add_hline()
                data_table.add_row((MultiColumn(num_campos, align='|r|',
                                    data='../..'),))
                data_table.add_hline()
                data_table.end_table_footer()
                data_table.add_hline()
                data_table.end_table_last_footer()

                for i in self:
                    iu= iuo.UnitPriceReport((i).first,(i).second)
                    iu.printLtx(data_table)

