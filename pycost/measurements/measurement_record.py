# -*- coding: utf-8 -*-
#MeasurementRecord.py



from pycost.prices import unit_price
from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc

class MeasurementRecord(epc.EntPyCost):

    def __init__(self,c= "", uds= 0.0,l= 0.0,an= 0.0,al= 0.0):
        super(MeasurementRecord,self).__init__()
        self.comentario= c
        self.unidades= uds
        self.largo= l
        self.ancho= an
        self.alto= al

    def Comentario(self):
        return self.comentario

    def Unidades(self):
        return self.unidades

    def Largo(self):
        return self.largo

    def Ancho(self):
        return self.ancho

    def Alto(self):
        return self.alto

    def UnidadesR(self):
        return ppl_dimension(unidades)

    def LargoR(self):
        return ppl_dimension(largo)

    def AnchoR(self):
        return ppl_dimension(ancho)

    def AltoR(self):
        return ppl_dimension(alto)

    def Total(self):
        if(unidades==0.0) and (largo==0.0) and (ancho==0.0) and (alto==0.0):
            return 0.0
        retval = 1.0
        if(unidades!=0.0): retval*= unidades
        if(largo!=0.0): retval*= largo
        if(ancho!=0): retval*= ancho
        if(alto!=0): retval*= alto
        return retval


    def TotalR(self):
        if(unidades==0.0) and (largo==0.0) and (ancho==0.0) and (alto==0.0):
            return ppl_dimension(0.0)
        retval= ppl_dimension(1.0)
        u = self.UnidadesR()
        l = self.LargoR()
        a = self.AnchoR()
        h = self.AltoR()
        zero= ppl_dimension(0.0)
        if(u!=zero): retval*= u
        if(l!=zero): retval*= l
        if(a!=zero): retval*= a
        if(h!=zero): retval*= h
        return retval

    def LeeBC3(self, m):
        comentario= m.med.comentario
        unidades= m.med.unidades
        largo= m.med.largo
        ancho= m.med.ancho
        alto= m.med.alto

    def WriteBC3(self, os):
        os.write('\\' + comentario + '\\'
           + unidades + '\\'
           + largo + '\\'
           + ancho + '\\'
           + alto + '\\')


    def Write(self, os):
        os.write(comentario + ','
           + unidades + ','
           + largo + ',' + ancho + ',' + alto + '\n')


    #not  @brief Imprime la medición en Latex.
    def ImprLtx(self, os, ancho):

        os.write(ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(comentario))) + ltx_ampsnd)
        zero= ppl_dimension(0.0);
        if (self.UnidadesR()!=zero): str_u= UnidadesR().EnHumano()
        if (self.LargoR()!=zero): str_l= LargoR().EnHumano()
        if (self.AnchoR()!=zero): str_a= AnchoR().EnHumano()
        if (self.AltoR()!=zero): str_alt= AltoR().EnHumano()
        total= self.TotalR()
        if(total!=zero): str_t= total.EnHumano()
        os.write(str_u + ltx_ampsnd
           + str_l + ltx_ampsnd + str_a + ltx_ampsnd + str_alt + ltx_ampsnd
           + str_t)


    def WriteHCalc(self, os):
        os.write('"' + comentario + '"' + tab)
        if(unidades!=0.0): os.write(unidades)
        os.write(tab)
        if(largo!=0.0): os.write(largo)
        os.write(tab)
        if(ancho!=0.0): os.write(ancho)
        os.write(tab)
        if(alto!=0.0): os.write(alto)
        os.write(tab)
        total= self.Total()
        if(total!=0.0): os.write(total)
        os.write('\n')

