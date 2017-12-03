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
        return ppl_dimension(self.largo)

    def AnchoR(self):
        return ppl_dimension(self.ancho)

    def AltoR(self):
        return ppl_dimension(self.alto)

    def getTotal(self):
        if(self.unidades==0.0) and (self.largo==0.0) and (self.ancho==0.0) and (self.alto==0.0):
            return 0.0
        retval = 1.0
        if(self.unidades!=0.0): retval*= self.unidades
        if(self.largo!=0.0): retval*= self.largo
        if(self.ancho!=0): retval*= self.ancho
        if(self.alto!=0): retval*= self.alto
        return retval


    def getTotalR(self):
        if(self.unidades==0.0) and (self.largo==0.0) and (self.ancho==0.0) and (self.alto==0.0):
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
        self.comentario= m.med.comentario
        self.unidades= m.med.unidades
        self.largo= m.med.largo
        self.ancho= m.med.ancho
        self.alto= m.med.alto

    def WriteBC3(self, os):
        os.write('\\' + self.comentario + '\\'
           + self.unidades + '\\'
           + self.largo + '\\'
           + self.ancho + '\\'
           + self.alto + '\\')


    def Write(self, os):
        os.write(self.comentario + ','
           + self.unidades + ','
           + self.largo + ',' + self.ancho + ',' + self.alto + '\n')


    #not  @brief Imprime la medición en Latex.
    def ImprLtx(self, os, ancho):

        os.write(ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(self.comentario))) + ltx_ampsnd)
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
        os.write('"' + self.comentario + '"' + tab)
        if(self.unidades!=0.0): os.write(self.unidades)
        os.write(tab)
        if(self.largo!=0.0): os.write(self.largo)
        os.write(tab)
        if(self.ancho!=0.0): os.write(self.ancho)
        os.write(tab)
        if(self.alto!=0.0): os.write(self.alto)
        os.write(tab)
        total= self.getTotal()
        if(total!=0.0): os.write(total)
        os.write('\n')

