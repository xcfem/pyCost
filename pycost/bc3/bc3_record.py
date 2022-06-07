# -*- coding: utf-8 -*-
#RegBC3.py


from pycost.bc3 import fiebdc3

elemento, descompuesto, medicion, obra, capitulo, sin_tipo= range(0,6)

class RegBC3(object):
    def __init__(self, code):
        self.code= code # Concept identifier.
        self.c= None #Concepto
        self.d= None #Descomposición.
        self.m= None #Medicion
        self.t= None #Texto
        self.y= None #Descomposición.

    def GetDatosElemento(self):
        return fiebdc3.regBC3_elemento(self.GetConcepto(),self.GetTexto())

    def getUnitPriceData(self):
        return fiebdc3.regBC3_udobra(self.GetConcepto(),self.GetTexto(),self.GetDesc())

    def GetDatosMedicion(self):
        return fiebdc3.regBC3_medicion(self.GetConcepto(),self.GetTexto(),self.GetMed())

    def GetConcepto(self):
        return fiebdc3.regBC3_c(self.c)

    def GetTexto(self):
        return fiebdc3.regBC3_t(self.t)


    def GetDesc(self):
        tmp= None
        if(self.d and self.y):
            tmp= self.d+self.y
        elif(self.d):
            tmp= self.d
        elif(self.y):
            tmp= self.y
        bc3String= ''
        if(tmp): # if it's composed.
            for s in tmp:
                bc3String+= s
        return fiebdc3.regBC3_d(bc3String)


    def GetMed(self):
        return fiebdc3.regBC3_m(self.m)

    def EsElemento(self):
        return ((self.d is None) and (self.y is None) and (self.m is None))


    def EsMedicion(self):
        return not (self.m is None)


    #not  @brief Devuelve verdadero si el concepto corresponde a una obra.
    def EsObra(self):
        return fiebdc3.es_codigo_obra(self.c)


    #not  @brief Devuelve verdadero si el concepto corresponde a un capitulo.
    def isChapter(self):
        return fiebdc3.es_codigo_capitulo(self.c)


    def getChapterData(self):
        return fiebdc3.regBC3_capitulo(self.GetConcepto(), self.GetTexto(), self.GetDesc())


    def Print(self,os):
        os.write("C: " + self.c + ' ' + self.c.size() + '\n'
           + "D: " + self.d + ' ' + self.d.size() + '\n'
           + "M: " + self.m + ' ' + self.m.size() + '\n'
           + "T: " + self.t + ' ' + self.t.size() + '\n'
           + "Y: " + self.y + ' ' + self.y.size() + '\n')
        return os

