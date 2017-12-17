# -*- coding: utf-8 -*-
#MeasurementRecord.py



from pycost.prices import unit_price
from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc
import pylatex
from pycost.utils import pylatex_utils

class MeasurementRecord(epc.EntPyCost):

    def __init__(self,c= "", uds= 0.0,l= 0.0,an= 0.0,al= 0.0):
        super(MeasurementRecord,self).__init__()
        self.comentario= unicode(c,encoding='utf-8')
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
        return basic_types.ppl_dimension(self.unidades)

    def LargoR(self):
        return basic_types.ppl_dimension(self.largo)

    def AnchoR(self):
        return basic_types.ppl_dimension(self.ancho)

    def AltoR(self):
        return basic_types.ppl_dimension(self.alto)

    def getTotal(self):
        if(self.unidades==0.0) and (self.largo==0.0) and (self.ancho==0.0) and (self.alto==0.0):
            return 0.0
        retval= 1.0
        if(self.unidades!=0.0): retval*= self.unidades
        if(self.largo!=0.0): retval*= self.largo
        if(self.ancho!=0): retval*= self.ancho
        if(self.alto!=0): retval*= self.alto
        return retval


    def getTotalR(self):
        retval= basic_types.ppl_dimension(0.0)
        u= self.UnidadesR()
        l= self.LargoR()
        a= self.AnchoR()
        h= self.AltoR()
        zero= basic_types.ppl_dimension(0.0)
        if(u!=zero) or (l!=zero) or (a!=zero) or (h!=zero):
            retval= basic_types.ppl_dimension(1.0)
            if(u!=zero): retval*= u
            if(l!=zero): retval*= l
            if(a!=zero): retval*= a
            if(h!=zero): retval*= h
        return retval.quantize(basic_types.dimensionPlaces)

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
    def printLtx(self, data_table, ancho):
        row= [pylatex.table.MultiColumn(1,align= pylatex.utils.NoEscape(ancho),data= pylatex_utils.ascii2latex(self.comentario))]
        zero= basic_types.ppl_dimension(0.0);
        str_u= ''
        if (self.UnidadesR()!=zero):
            str_u= basic_types.EnHumano(self.UnidadesR())
        row.append(str_u)
        str_l= ''
        if (self.LargoR()!=zero): str_l= basic_types.EnHumano(self.LargoR())
        row.append(str_l)
        str_a= ''
        if (self.AnchoR()!=zero): str_a= basic_types.EnHumano(self.AnchoR())
        row.append(str_a)
        str_alt= ''
        if (self.AltoR()!=zero): str_alt= basic_types.EnHumano(self.AltoR())
        row.append(str_alt)
        total= self.getTotalR()
        if(total!=zero): str_t= basic_types.EnHumano(total)
        row.append(str_t)
        data_table.add_row(row)

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

