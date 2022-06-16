# -*- coding: utf-8 -*-
#ElementaryPrice.py

import logging
from pycost.utils import basic_types
from pycost.utils import measurable as m
from decimal import Decimal


class ElementaryPrice(m.Measurable):
    precision= 2
    places= Decimal(10) ** -precision
    formatString= '{0:.'+str(precision)+'f}'

    def __init__(self, cod="", tit="", ud="", p=0.0, tp= basic_types.sin_clasif, long_description= None):
        ''' Constructor.
 
        :param cod: identifier.
        :param tit: short description.
        :param ud: unit of measurement.
        :param p: price
        :param tp: type (basic_types.mdo, basic_types.mat, basic_types.maq or basic_types.sin_clasif)
        :param ld: long description.
        '''
        super(ElementaryPrice,self).__init__(cod= cod, tit= tit, ud=ud, ld= long_description)
        self.precio= p
        self.tipo= tp

    def check_tipo(self):
        if(len(self.Codigo())>0):
            if tipo==sin_clasif and not isPercentage():
                logging.error("El precio elemental de código: " + Codigo()
                          + " no es un porcentaje y su tipo está sin clasificar." + '\n')

    def getType(self):
        return self.tipo

    def getPrice(self):
        return self.precio

    def readBC3(self, r):
        ''' Read data from BC3 record.'''
        if(r):
            super(ElementaryPrice,self).readBC3(r= r)
            self.precio= r.Datos().getPrice()
            self.tipo= basic_types.sint2tipo_concepto(r.Datos().getType())
        else:
            logging.warning('Argument is none.')

    def printLtx(self, data_table):
        row= [pylatex_utils.ascii2latex(self.Codigo())]
        row.append(pylatex_utils.ascii2latex(self.Unidad()))
        row.append(pylatex_utils.ascii2latex(self.getTitle()))
        row.append(self.getLtxPriceString())
        data_table.add_row(row)

    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= super(ElementaryPrice, self).getDict()
        retval['type']= self.tipo
        retval['price']= self.precio
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        self.tipo= dct['type']
        self.precio= dct['price']
        return super(ElementaryPrice, self).setFromDict(dct)

    def appendToChapter(self, chapter):
        ''' Insert this elementary price in the chapter argument.'''
        chapter.precios.elementos.Append(self)

