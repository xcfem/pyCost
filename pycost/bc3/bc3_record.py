# -*- coding: utf-8 -*-
#RegBC3.py


from pycost.bc3 import fiebdc3

elemento, descompuesto, medicion, obra, capitulo, sin_tipo= range(0,6)

class RegBC3(object):
    def __init__(self):
        self.c= '' #Concepto
        self.d= '' #Descomposición.
        self.m= '' #Medicion
        self.t= '' #Texto
        self.y= '' #Descomposición.

    def GetDatosElemento(self):
        return regBC3_elemento(self.GetConcepto(),self.GetTexto())

    def getUnitPriceData(self):
        return regBC3_udobra(self.GetConcepto(),self.GetTexto(),self.GetDesc())

    def GetDatosMedicion(self):
        return regBC3_medicion(self.GetConcepto(),self.GetTexto(),self.GetMed())

    def GetConcepto(self):
        return regBC3_c(c)


    def GetTexto(self):
        return regBC3_t(t)


    def GetDesc(self):
        return regBC3_d(d+y)


    def GetMed(self):
        return regBC3_m(m)


    def EsElemento(self):
        return ((len(d)==0) and (len(y)== 0) and (len(m)==0))


    def EsMedicion(self):
        return (m.size()!=0)


    #not  @brief Devuelve verdadero si el concepto corresponde a una obra.
    def EsObra(self):
        return es_codigo_obra(c)


    #not  @brief Devuelve verdadero si el concepto corresponde a un capitulo.
    def isChapter(self):
        return es_codigo_capitulo(c)


    def getChapterData(self):
        return regBC3_capitulo(GetConcepto(),GetTexto(),GetDesc())


    def Print(self,os):
        os.write("C: " + self.c + ' ' + self.c.size() + '\n'
           + "D: " + self.d + ' ' + self.d.size() + '\n'
           + "M: " + self.m + ' ' + self.m.size() + '\n'
           + "T: " + self.t + ' ' + self.t.size() + '\n'
           + "Y: " + self.y + ' ' + self.y.size() + '\n')
        return os

