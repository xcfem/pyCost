# -*- coding: utf-8 -*-
#MeasurementRecord.py



from pycost.prices import unit_price
from pycost.utils import basic_types
from pycost.utils import EntPyCost as epc
import pylatex
from pycost.utils import pylatex_utils

class MeasurementRecord(epc.EntPyCost):

    def __init__(self,c= "", uds= None,l= None,an= None,al= None):
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
        retval= None
        if(self.unidades):
            retval= basic_types.ppl_dimension(self.unidades)
        return retval

    def LargoR(self):
        retval= None
        if(self.largo):
            retval= basic_types.ppl_dimension(self.largo)
        return retval

    def AnchoR(self):
        retval= None
        if(self.ancho):
            retval= basic_types.ppl_dimension(self.ancho)
        return retval

    def AltoR(self):
        retval= None
        if(self.alto):
            retval= basic_types.ppl_dimension(self.alto)
        return retval

    def isNull(self):
        '''Returns true if the measurement result is zero.'''
        retval= False
        if(self.unidades==0.0) and (self.largo==0.0) and (self.ancho==0.0) and (self.alto==0.0):
            retval= True
        else:
            if(self.unidades==None) and (self.largo==None) and (self.ancho==None) and (self.alto==None):
                retval= True
        return retval

    def getTotal(self):
        retval= 0.0
        if(not self.isNull()):
            retval= 1.0
            if(self.unidades): retval*= self.unidades
            if(self.largo): retval*= self.largo
            if(self.ancho): retval*= self.ancho
            if(self.alto): retval*= self.alto
        return retval


    def getTotalR(self):
        retval= basic_types.ppl_dimension(0.0)
        if(not self.isNull()):
            u= self.UnidadesR()
            l= self.LargoR()
            a= self.AnchoR()
            h= self.AltoR()
            zero= basic_types.ppl_dimension(0.0)
            tmp= basic_types.ppl_dimension(1.0)
            if(u): tmp*= u
            if(l): tmp*= l
            if(a): tmp*= a
            if(h): tmp*= h
            retval= tmp.quantize(basic_types.dimensionPlaces)
        return retval

    def LeeBC3(self, m):
        self.comentario= m.med.comentario
        self.unidades= m.med.unidades
        self.largo= m.med.largo
        self.ancho= m.med.ancho
        self.alto= m.med.alto

    def getComponents(self):
        '''Return measurement components: 
           [description,number of units, length, width and height].'''
        retval= [ self.comentario.encode('utf8'), '','','','']
        if(self.unidades): retval[1]= basic_types.human_readable(self.UnidadesR())
        if(self.largo): retval[2]= basic_types.human_readable(self.LargoR())
        if(self.ancho): retval[3]= basic_types.human_readable(self.AnchoR())
        if(self.alto): retval[4]= basic_types.human_readable(self.AltoR())
        return retval
    
    def WriteBC3(self, os):
        components= self.getComponents()
        os.write('\\' + components[0] + '\\'
           + components[1] + '\\'
           + components[2] + '\\'
           + components[3] + '\\'
           + components[4] + '\\')


    def Write(self, os):
        os.write(self.comentario + ','
           + self.unidades + ','
           + str(self.largo) + ',' + str(self.ancho) + ',' + str(self.alto) + '\n')


    #not  @brief Imprime la medición en Latex.
    def printLtx(self, data_table, ancho):
        row= [pylatex.table.MultiColumn(1,align= pylatex.utils.NoEscape(ancho),data= pylatex_utils.ascii2latex(self.comentario))]
        components= self.getComponents()
        zero= basic_types.ppl_dimension(0.0);
        row.append(components[1])
        row.append(components[2])
        row.append(components[3])
        row.append(components[4])
        total= self.getTotalR()
        if(total!=zero): str_t= basic_types.human_readable(total)
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

