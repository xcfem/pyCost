# -*- coding: utf-8 -*-
#Quantities.py


from pycost.utils import EntPyCost as epy
from pycost.measurements import measurement_record

class Quantities(list, epy.EntPyCost):
    '''Quantities de una unidad de obra.'''
    def getTotalUnits(self):
        '''Return the total number of units.'''
        t = 0.0
        for i in self:
            t+=(i).Unidades()
        return t

    def getTotalLength(self):
        '''Return the total length.'''
        t = 0.0
        for i in self:
            t+=(i).Unidades()*(i).Largo()
        return t

    def getTotalWidth(self):
        '''Return the total width.'''
        t = 0.0
        for i in self:
            t+=(i).Unidades()*(i).Ancho()
        return t

    def getTotalHeight(self):
        '''Return the total height.'''
        t = 0.0
        for i in self:
            t+=(i).Unidades()*(i).Ancho()
        return t

    def getTotal(self):
        t = 0.0
        for i in self:
            t+=(i).getTotal()
        return t

    def getTotalR(self):
        t = 0.0
        for i in self:
            t+=(i).getTotalR()
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
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
        for i in self:
          for j in otra:
            (j).ImprLtx(os,"p{1.5cm}")
            os.write(ltx_ampsnd)
            (i).ImprLtx(os,"p{1.5cm}")
            os.write(ltx_fin_reg + '\n')

        # if i:
        #     for(; i!=end(); i+= 1)
        #         os.write(media_linea_en_blanco
        #         os.write(ltx_ampsnd)
        #         (i).ImprLtx(os,"p{1.5cm}")
        #         os.write(ltx_fin_reg + '\n')

        # elif j!=end():
        #     for(; j!=otra.end(); j+= 1)
        #         (j).ImprLtx(os,"p{1.5cm}")
        #         os.write(media_linea_en_blanco + ltx_fin_reg + '\n'

        os.write(linea_en_blanco + '\n')

    def ImprCompLtx(self, os):
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
        for i in self:
            os.write(media_linea_en_blanco)
            (i).ImprLtx(os,"p{1.5cm}")
            os.write(ltx_fin_reg + '\n')

        os.write(linea_en_blanco + '\n')

    def ImprLtx(self, os):
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        for i in self:
            (i).ImprLtx(os,"p{3.5cm}")
            os.write(ltx_fin_reg + '\n')

        os.write(linea_en_blanco + '\n')

    def WriteHCalc(self, os):
        for i in self:
            (i).WriteHCalc(os)
        os.write(",,,,Suma ..." + tab + Total() + '\n' + '\n')

