# -*- coding: utf-8 -*-
#Mediciones.py


import EntPyCost as epy
import RegMedicion

class Mediciones(list, epy.EntPyCost):
    '''Mediciones de una unidad de obra.'''

    #not  @brief Devuelve el total de unidades de la medición.
    def TotalUnidades(self):
        t = 0.0
        for i in self:
            t+=(i).Unidades()
        return t


    #not  @brief Devuelve el total del largo de la medición.
    def TotalLargo(self):
        t = 0.0
        for i in self:
            t+=(i).Unidades()*(i).Largo()
        return t


    #not  @brief Devuelve el total del an.pyo de la medición.
    def TotalAncho(self):
        t = 0.0
        for i in self:
            t+=(i).Unidades()*(i).Ancho()
        return t


    #not  @brief Devuelve el total del alto de la medición.
    def TotalAlto(self):
        t = 0.0
        for i in self:
            t+=(i).Unidades()*(i).Ancho()
        return t


    def Total(self):
        t = 0.0
        for i in self:
            t+=(i).Total()
        return t

    def TotalR(self):
        t = 0.0
        for i in self:
            t+=(i).TotalR()
        return t


    #| @brief Lee la lista de mediciones.
    def LeeBC3(self, m):
        rm= RegMedicion()
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

