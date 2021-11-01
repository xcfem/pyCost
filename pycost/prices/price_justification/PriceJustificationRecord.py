# -*- coding: utf-8 -*-

#PriceJustificationRecord.pyxx

from pycost.utils import basic_types
from pycost.utils import pylatex_utils

class PriceJustificationRecord(object):
    '''Elemental unit cost

    :ivar codigo: code of the elemental unit
    :ivar rdto: production rate
    :ivar unidad: unit of measurement
    :ivar titulo: description of the elemental unit
    :ivar is_percentage: True if it's a percentage
    :ivar unitario: price of the elemental unit (or percentage if isperc==True)
    :ivar sobre: base cost over which to apply percentage
    '''

    def __init__(self, cod= '', rd= 0.0, ud= '', tit= '', isperc= False, unit= 0.0, b= 0.0):
        '''Elemental unit cost

        :param cod: code of the elemental unit
        :param rdto: production rate
        :param ud: unit of measurement
        :param tit: description of the elemental unit
        :param isperc: True if it's a percentage
        :param unit: price of the elemental unit (or percentage if isperc==True)
        :param b: base cost over which to apply percentage
        '''
        self.codigo= cod 
        self.rdto= rd 
        self.unidad= ud 
        self.titulo= tit 
        self.is_percentage= isperc 
        self.unitario= unit 
        self.sobre= b 

    def base(self):
        if self.is_percentage:
            return self.sobre
        else:
            return basic_types.ppl_price(self.unitario)

    def SetBase(self, b):
        ''' Sets the base for percentage calculation.

        :param b: base cost over which to apply percentage
        '''
        self.sobre= b

    def getTotal(self):
        retval= basic_types.ppl_price(self.base())
        retval*= self.rdto
        return retval

    def writePriceJustification(self, data_table):
        row= [pylatex_utils.ascii2latex(self.codigo)]
        row.append(basic_types.human_readable(self.rdto))
        row.append(pylatex_utils.ascii2latex(self.unidad))
        row.append(pylatex_utils.ascii2latex(self.titulo))
        if self.is_percentage:
            row.append(basic_types.human_readable(self.unitario) + pylatex_utils.ltx_porciento); #Percentage
        else:
            row.append(basic_types.human_readable(self.unitario)) #Precio unitario
        row.append(basic_types.human_readable(self.getTotal()))
        data_table.add_row(row)


    def writePriceTableTwoIntoLatexDocument(self, data_table):
        ''' Write row of a percentage price (e.g. indirect costs) in price table number two'''
        if(self.is_percentage): data_table.add_row(['','',pylatex_utils.ascii2latex(self.titulo),basic_types.human_readable(self.getTotal())])

    
 



