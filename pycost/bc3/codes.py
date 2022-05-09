# -*- coding: utf-8 -*-
#Codigos.py

import logging
from pycost.bc3 import bc3_record
from pycost.bc3 import fiebdc3
from pycost.utils import concept_dict

class reg_T(object):
    def __init__(self, c= '',d= None):
        ''' Constructor.
        :param c: code.
        :param d: data.
        '''
        self.cod= c # code.
        self.datos= d # data.

    def Codigo(self):
        return self.cod

    def Datos(self):
        return self.datos

    def CodigoUnidad(self):
        tokens= self.cod.rpartition('\\')
        return tokens[2]

    def getChapterCode(self):
        tokens= self.cod.partition('\\')
        return tokens[0]

    def Write(os):
        os.write(cod + '\n')
        datos.Write(os)


class Codigos(dict):

    #Clasificación
    def isChapterOrObra(self, i):
        if(self.EsMedicion(i)): #Quantities have the code of their chapter.
            return False
        else:
            return fiebdc3.es_codigo_capitulo_u_obra(i)

    def isChapter(self, i):
        if self.isChapterOrObra(i):
            return not self.EsObra(i)
        else:
            return False

    @staticmethod
    def EsObra(cod):
        return fiebdc3.es_codigo_obra(cod)

    def EsElemento(self, i):
        return ((self)[i].EsElemento())

    def EsMedicion(self, i):
        '''Devuelve verdadero si el registro corresponde a una medición.'''
        return ((self)[i].EsMedicion())

    def EsDescompuesto(self, i):
        if(self.EsMedicion(i)):
            return False
        elif(self.EsElemento(i)):
            return False
        elif(self.isChapterOrObra(i)):
            return False
        else:
            return True

    def __iadd__(cods):
        InsertaCods(cods)
        return self


    def InsertaCods(self, cods):
        self.update(cods)

    def GetSubCaps(self, ppal):
        ''' Devuelve los subcapítulos del capitulo que se pasa 
            como parámetro.'''
        retval= None
        desc= ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod= (i).codigo
            if(fiebdc3.es_codigo_capitulo(cod)): #Es un capítulo.
                j= findChapter(cod)
                if j:
                    retval[(j).first]= (j).second
                else:
                    logging.error("Codigos.GetSubCaps; No se encontró el subcapítulo: " + cod + '\n')

            #else: #partidas del capítulo
            #logging.error(u"subcapítulo raro: " + cod + '\n')

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
            if(not fiebdc3.es_codigo_capitulo(cod)): #No es un capítulo.
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
            if(not fiebdc3.es_codigo_capitulo(cod)): #No es un capítulo.
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
        tipo= tokens.pop(0)
        cod= tokens.pop(0)
        cod= cod.strip('\\'); # Remove leading backslash.

        if(tipo=='V' or tipo=='K' or tipo=='L' or
                tipo=='A' or tipo=='G' or tipo=='E'):
            logging.info("Ignoring '"+tipo+"' record.")
            return

        if(len(cod)>0 and len(tokens)> 0):
            bc3Record= self.find(cod)
            if(bc3Record is None): # Code not found => new record.
                if(tipo == 'M'): #El registro corresponde a una medición.
                    # if('\\' in cod): #Sometimes the ~M has the form: ~M|13.3.1#\01.009|1....
                    #     cod= cod.partition('\\')[2] # remove part 13.3.1#\ of the code.
                    cod= cod+'@'+str(quantities_counter)

                bc3Record= bc3_record.RegBC3() # Constructor.
                (self)[cod]= bc3Record # Update dictionary.

            if(tipo=='C'):
                bc3Record.c= tokens
            elif(tipo=='D'):
                if len(tokens)<2:
                    logging.log(u"No components for concept: \'" + cod
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
                logging.error("Record of type: " + tipo + " unknown." + '\n')

    def GetObra(self):
        ''' Return the record that corresponds to the root chapter.'''
        retval= None
        for key in self:
            if self.EsObra(key):
                retval= Codigos({key: self[key]})
        if(retval is None):
            logging.error("Root chapter not found.")
        return retval


    def findChapter(self, cod):
        ''' Devuelve el capítulo con el código que se pasa como parámetro.'''
        retval = None
        if cod in self:
            retval= self[cod]
        else:
            tmp= cod+'#'
            if(tmp in self):
                retval= self[tmp]
        return retval


    #not  @brief Devuelve el tipo de concepto al que corresponde el registro.
    def GetTipoConcepto(self, i):
        if self.EsObra(i):
            return obra
        elif self.EsElemento(i):
            return elemento
        elif self.EsMedicion(i):
            return medicion
        elif self.EsDescompuesto(i):
            return descompuesto
        elif self.isChapter(i):
            return capitulo
        else:
            logging.error("Type of the concept: '" + str(i) + "' not found.")
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
        retval= Codigos()
        for i in self:
            if self.isChapter(i):
                retval[i]= self[i]
        logging.info("  read " + str(len(retval)) + ' chapters.')
        return retval


    #not  @brief Devuelve los códigos de los objetos del contenedor
    def GetCodigos(self):
        retval= set()
        for key in self:
            retval.add(key)
        return retval


    #not  @brief Extrae las entidades que corresponden a elementos
    def GetElementos(self):
        retval= Codigos()
        for i in self:
            if self.EsElemento(i):
                retval[i]= self[i]
        logging.info("  read " + str(len(retval)) + " elementary prices." + '\n')
        return retval


    #not  @brief Extract quantity entities
    def getQuantities(self):
        retval= Codigos()
        for i in self:
            if EsMedicion(i):
                retval[i]= self[i]
        logging.info(str(len(retval)) + " quantities read." + '\n')
        return retval


    #not  @brief Extrae las entidades que corresponden a descompuestos
    def GetDescompuestos(self):
        retval= Codigos()
        for i in self:
            if self.EsDescompuesto(i):
                retval[i]= self[i]
        logging.info(" read " + str(len(retval)) + " precios descompuestos." + '\n')
        return retval


    def Borra(self, cods):
        '''Removes the elements that are already in the dictionary
           argument.

        :param cods: dictionary with the keys to remove.
        '''
        if(cods):
            keysToRemove= cods.keys()
            for key in keysToRemove:
                del self[key]

    #not  @brief Extrae las entidades que corresponden a unidades de obra
    def GetUdsObra(self, udsobra):
        retval= Codigos()
        for i in udsobra:
            Str= StrTok((i).first)
            scap= Str.get_token('\\')
            codud= Str.resto()
            j= find(codud)
            if j:
                retval[j]= self[j]
            else:
                logging.error("GetUdsObra: No se encontro la unidad: \'" + codud
                          + "\' de la medición: " + scap + '\n')

        return retval


    def GetDatosElementaryPrice(self, key):
        ''' Return the elementary price data.'''
        retval= None
        if(key in self):
            retval= reg_T(c= key, d= self[key].GetDatosElemento())
        # elif(key in concept_dict.ConceptDict.claves):
        #     retval= reg_T(c= key, d= concept_dict.ConceptDict.claves[key].GetDatosElemento())
        else:
            logging.error('elementary price: '+key+' not found.')
        return retval


    def getUnitPriceData(self, key):
        return reg_T(c= key, d= self[key].getUnitPriceData())

    def getChapterData(self, key):
        retval= None
        if key in self:
            retval= reg_T(c= key, d= self[key].getChapterData())
        else:
            tmp= key+'#'
            if(tmp in self):
                retval= reg_T(c= key, d= self[tmp].getChapterData())
        return retval

    def GetDatosMedicion(self, key):
        return reg_T(c= key, d= self[key].GetDatosMedicion())


    def Print(self,os):
        for key in self:
            os.write(u"Código: " + key + '\n'+ self[key] + '\n')
        return os

