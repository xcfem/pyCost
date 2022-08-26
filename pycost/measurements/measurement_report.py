# -*- coding: utf-8 -*-
''' Quantities report.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2017, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import pylatex
from pycost.prices import unit_price_report

class QuantitiesReport(dict):

    def Inserta(self, iu):
        ''' Inserts a unit price in the report.'''
        uPrice= iu.Unidad()
        if(uPrice in self):
            self[uPrice]+= iu.Medicion() # Add to the existing record.
        else:
            (self)[uPrice]= iu.Medicion() # Create new record.

    def Merge(self, otro):
        for key in otro:
            value= otro[key]
            self.Inserta(unit_price_report.UnitPriceReport(key,value))

    def getKeysWithMeasurementGreaterThan(self, lowerMeasurementBound):
        ''' Return the codes of the prices that have a total measurement
            greater than the limit argument.

        :param lowerMeasurementBound: lower bound for the total measurement.
        '''
        retval= list()
        for key in self:
            totalMeasurement= self[key]
            if(totalMeasurement>lowerMeasurementBound):
                retval.append(key.Codigo())
        return retval

    def printLtx(self, doc):
        ''' Write Latex report.

        :param doc: pylatex document to write into.
        '''
        sz= len(self)
        if(sz>0):
            longTableStr= '|l|p{4cm}|r|r|'
            headerRow1= [u"Código",u"Descripción.",u"Medición",'Precio']
            num_campos= 4
            with doc.create(pylatex.table.LongTable(longTableStr)) as data_table:
                data_table.add_hline()
                data_table.add_row(headerRow1)
                data_table.add_hline()
                data_table.end_table_header()
                data_table.add_hline()
                data_table.add_row((pylatex.table.MultiColumn(num_campos, align='|r|',
                                    data='../..'),))
                data_table.add_hline()
                data_table.end_table_footer()
                data_table.add_hline()
                data_table.end_table_last_footer()

                for key in self:
                    value= self[key]
                    iu= unit_price_report.UnitPriceReport(key,value)
                    iu.printLtx(data_table)

