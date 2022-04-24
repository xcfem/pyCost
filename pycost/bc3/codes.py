# -*- coding: utf-8 -*-
#Codigos.py

import logging
from pycost.bc3 import bc3_record

class reg_T(object):
    def __init__(self,c= '',d= None):
        self.cod= c #Codigo.
        self.datos= d

    def Codigo(self):
        return self.cod

    def Datos(self):
        return self.datos

    def CodigoUnidad(self):
        strtk= StrTok(cod)
        return strtk.campos('\\').rbegin()

    def getChapterCode(self):
        strtk= StrTok(cod)
        return strtk.campos('\\').begin()

    def Write(os):
        os.write(cod + '\n')
        datos.Write(os)


class Codigos(dict):

    #Clasificación
    @staticmethod
    def isChapterOrObra(i):
        if(EsMedicion(i)): #Quantities have the code of their chapter.
            return False
        else:
            return es_codigo_capitulo_u_obra((i).first)

    @staticmethod
    def isChapter(i):
        if isChapterOrObra(i):
            return not EsObra(i)
        else:
            return False

    @staticmethod
    def EsObra(i):
        return es_codigo_obra((i).first)

    @staticmethod
    def EsElemento(i):
        return ((i).second.EsElemento())

    @staticmethod
    def EsMedicion(self, i):
        '''Devuelve verdadero si el registro corresponde a una medición.'''
        return ((i).second.EsMedicion())

    @staticmethod
    def EsDescompuesto(i):
        if(EsMedicion(i)): return False
        if(EsElemento(i)): return False
        if(isChapterOrObra(i)): return False
        return True

    def __iadd__(cods):
        InsertaCods(cods)
        return self


    def InsertaCods(self, cods):
        for i in cods:
            (self)[(i).first]= (i).second



    #not  @brief Devuelve los subcapítulos del capitulo que se pasa como parámetro.
    def GetSubCaps(self, ppal):
        retval= None
        desc= ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod= (i).codigo
            if(es_codigo_capitulo(cod)): #Es un capítulo.
                j= findChapter(cod)
                if j:
                    retval[(j).first]= (j).second
                else:
                    lmsg.error("Codigos.GetSubCaps; No se encontró el subcapítulo: " + cod + '\n')

            #else: #partidas del capítulo
            #lmsg.error(u"subcapítulo raro: " + cod + '\n')

        return retval

    def GetSubChapters(self, cods):
        retval= None
        for i in cods:
            retval.InsertaCods(GetSubCaps((i).second))
        return retval

    def GetSubElementos(self, ppal, elementos):
    #Devuelve los precios elementales del capitulo que se pasa como parámetro.
        retval= None
        desc= ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod= (i).codigo
            if(not es_codigo_capitulo(cod)): #No es un capítulo.
                j= elementos.find(cod)
                if j!=end():
                    retval[(j).first]= (j).second


        return retval

    def GetSubDescompuestos(self, ppal, descompuestos):
    #Devuelve los descompuestos del capitulo que se pasa como parámetro.
        retval= None
        desc= ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod= (i).codigo
            if(not es_codigo_capitulo(cod)): #No es un capítulo.
                j= descompuestos.find(cod)
                if j!=end():
                    retval[(j).first]= (j).second


        return retval

    def find(self, cod):
        ''' Find the BC3 record corresponding to the argument key.

        :param cod: key.
        '''
        retval= None
        if(cod in self):
            retval= self[cod]
        else:
            codSharp= cod+'#'
            if(codSharp in self):
                retval= self[codSharp]
            else:
                codSharp2= codSharp+'#'
                if(codSharp2 in self):
                    retval= self[codSharp2]
        return retval
            
    def InsertaReg(self, str_reg, quantities_counter):
        tokens= str_reg.split('|')
        print('tokens: ', tokens)
        tipo= tokens.pop(0)
        cod= tokens.pop(0)
        cod= cod.strip('\\'); # Remove leading backslash.
        print(tipo, cod)

        if(tipo=='V' or tipo=='K' or tipo=='L' or
                tipo=='A' or tipo=='G' or tipo=='E'):
            logging.info("Ignoring '"+tipo+"' record.")
            return

        if(len(cod)>0 and len(tokens)> 0):
            bc3Record= self.find(cod)
            if(bc3Record is None): # Code not found => new record.
                if(tipo == 'M'): #El registro corresponde a una medición.
                    if('\\' in cod): #Sometimes the ~M has the form: ~M|13.3.1#\01.009|1....
                        cod= cod.partition('\\')[2] # remove part 13.3.1#\ of the code.
                    cod= str(quantities_counter) + '@' + cod

                bc3Record= bc3_record.RegBC3() # Constructor.
                (self)[cod]= bc3Record # Update dictionary.

            if(tipo=='C'):
                bc3Record.c= tokens.pop(0)
            elif(tipo=='D'):
                if len(tokens)<2:
                    lmsg.log(u"No components for concept: \'" + cod
                              + "\' decomposition ignored." + '\n')
                else:
                    bc3Record.d= tokens
            elif(tipo=='T'):
                bc3Record.t= tokens
            elif(tipo=='M'):
                bc3Record.m= tokens
            elif(tipo=='Y'):
                bc3Record.y= tokens
            else:
                lmsg.error("Record of type: " + tipo + " unknown." + '\n')

    #not  @brief Devuelve el registro que corresponde a la obra.
    def GetObra(self):
        retval= None
        for i in self:
            if self.EsObra(i):
                retval[(i).first]= (i).second
        if not retval.size():
            lmsg.error("No se encontró el capítulo raíz." + '\n')
        return retval


    #not  @brief Devuelve un iterador al capítulo con el código que se pasa como parámetro.
    def findChapter(self, cod):
        retval= find(cod); #Código
        if retval==end():
            retval= find(cod+'#')
        return retval


    #not  @brief Devuelve el tipo de concepto al que corresponde el registro.
    def GetTipoConcepto(self, i):
        if EsObra(i):
            return obra
        elif EsElemento(i):
            return elemento
        elif EsMedicion(i):
            return medicion
        elif EsDescompuesto(i):
            return descompuesto
        elif isChapter(i):
            return capitulo
        else:
            lmsg.error("No se encontró el tipo del concepto: '" + (i).first + "'\n")
            return sin_tipo



    #not  @brief Devuelve una cadena de caracteres que identifica el
    #not  tipo de concepto al que corresponde el registro.
    def StrTipoConcepto(self, i):
        retval= "sin_tipo"
        tipo= GetTipoConcepto(i)
        if(tipo==obra):
            retval= "obra"
        elif(tipo==elemento):
            retval= "elemento"
        elif(tipo==medicion):
            retval= "medicion"
        elif(tipo==descompuesto):
            retval= "descompuesto"
        elif(tipo==capitulo):
            retval= "capitulo"
        return retval




    #not  @brief Extrae las entidades que corresponden a capitulos
    def GetChapters(self):
        retval= None
        for i in self:
            if isChapter(i):
                retval[(i).first]= (i).second
        logging.info("  leídos " + retval.size() + " capítulos." + '\n')
        return retval


    #not  @brief Devuelve los códigos de los objetos del contenedor
    def GetCodigos(self):
        retval= set()
        for i in self:
            retval.insert((i).first)
        return retval


    #not  @brief Extrae las entidades que corresponden a elementos
    def GetElementos(self):
        retval= None
        for i in self:
            if EsElemento(i):
                retval[(i).first]= (i).second
        logging.info("  leídos " + retval.size() + " precios elementales." + '\n')
        return retval


    #not  @brief Extract quantity entities
    def getQuantities(self):
        retval= None
        for i in self:
            if EsMedicion(i):
                retval[(i).first]= (i).second
        logging.info(retval.size() + " quantities read." + '\n')
        return retval


    #not  @brief Extrae las entidades que corresponden a descompuestos
    def GetDescompuestos(self):
        retval= None
        for i in self:
            if EsDescompuesto(i):
                retval[(i).first]= (i).second
        logging.info(" leídos " + retval.size() + " precios descompuestos." + '\n')
        return retval


    #not  @brief Borra los elementos de self que estan en cods.
    def Borra(self, cods):
        for i in cods:
            j= find((i).first)
            if j: erase(j)



    #not  @brief Extrae las entidades que corresponden a unidades de obra
    def GetUdsObra(self, udsobra):
        retval= None
        for i in udsobra:
            Str= StrTok((i).first)
            scap= Str.get_token('\\')
            codud= Str.resto()
            j= find(codud)
            if j:
                retval[(j).first]= (j).second
            else:
                lmsg.error("GetUdsObra: No se encontro la unidad: \'" + codud
                          + "\' de la medición: " + scap + '\n')

        return retval


    def GetDatosElemento(self, i):
        return reg_elemento((i).first,(i).second.GetDatosElemento())


    def GetDatosUnitPrice(self, i):
        return reg_udobra((i).first,(i).second.GetDatosUnitPrice())


    def getChapterData(self, i):
        return reg_capitulo((i).first,(i).second.getChapterData())


    def GetDatosMedicion(self, i):
        return reg_medicion((i).first,(i).second.GetDatosMedicion())


    def Print(self,os):
        for i in self:
            os.write(u"Código: " + (i).first + '\n'+ (i).second + '\n')
        return os

