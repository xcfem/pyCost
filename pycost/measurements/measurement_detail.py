# -*- coding: utf-8 -*-
#Quantities.py


import pylatex
from pycost.utils import EntPyCost as epy
from pycost.measurements import measurement_record
from pycost.utils import basic_types
from pycost.utils import pylatex_utils

class Quantities(list, epy.EntPyCost):
    '''Quantities de una unidad de obra.'''
    def getTotalUnits(self):
        '''Return the total number of units.'''
        t= measurement_record.MeasurementRecord.dimension(0.0)
        for i in self:
            t+=(i).Unidades()
        return t

    def getTotalLength(self):
        '''Return the total length.'''
        t= measurement_record.MeasurementRecord.dimension(0.0)
        for i in self:
            t+=(i).Unidades()*(i).Largo()
        return t

    def getTotalWidth(self):
        '''Return the total width.'''
        t= measurement_record.MeasurementRecord.dimension(0.0)
        for i in self:
            t+=(i).Unidades()*(i).Ancho()
        return t

    def getTotalHeight(self):
        '''Return the total height.'''
        t= measurement_record.MeasurementRecord.dimension(0.0)
        for i in self:
            t+=(i).Unidades()*(i).Ancho()
        return t

    def getTotal(self):
        t= 0.0
        for i in self:
            t+=(i).getTotal()
        return t

    def getRoundedTotal(self):
        t= measurement_record.MeasurementRecord.dimension(0.0)
        for i in self:
            t+=(i).getRoundedTotal()
        return t

    #| @brief Read quantities list.
    def LeeBC3(self, m):
        rm= MeasurementRecord()
        for i in m:
            rm.LeeBC3(i)
            append(rm)

    def WriteBC3(self, os):
        for i in self:
            (i).WriteBC3(os)

    def ImprCompLtx(self, os, otra):
        media_empty_line= ['','', '', '', '']
        for i in self:
          for j in otra:
            (j).printLtx(os,"p{1.5cm}")
            doc.append(pylatex_utils.ltx_ampsnd)
            (i).printLtx(os,"p{1.5cm}")
            doc.append(pylatex_utils.ltx_fin_reg + '\n')

        # if i:
        #     for(; i!=end(); i+= 1)
        #         doc.append(media_empty_line
        #         doc.append(pylatex_utils.ltx_ampsnd)
        #         (i).printLtx(os,"p{1.5cm}")
        #         doc.append(pylatex_utils.ltx_fin_reg + '\n')

        # elif j!=end():
        #     for(; j!=otra.end(); j+= 1)
        #         (j).printLtx(os,"p{1.5cm}")
        #         doc.append(media_empty_line + pylatex_utils.ltx_fin_reg + '\n'

        doc.add_empty_row()

    def ImprCompLtx(self, os):
        media_empty_line= ['','', '', '', '', '']
        for i in self:
            doc.append(media_empty_line)
            (i).printLtx(os,"p{1.5cm}")
            doc.append(pylatex_utils.ltx_fin_reg + '\n')
        doc.add_empty_row()

    def printLtx(self, data_table):
        for i in self:
            (i).printLtx(data_table,"p{3.5cm}")
        data_table.add_empty_row()

    def WriteHCalc(self, os):
        for i in self:
            (i).WriteHCalc(os)
        os.write(",,,,Suma ..." + tab + Total() + '\n' + '\n')

