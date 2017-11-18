# -*- coding: utf-8 -*-
#Codigos.py


import bc3_record

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

    def CodigoCapitulo(self):
        strtk= StrTok(cod)
        return strtk.campos('\\').begin()

    def Write(os):
        os.write(cod + '\n')
        datos.Write(os)


class Codigos(dict):

    #Clasificación
    @staticmethod
    def EsCapituloUObra(i):
        if(EsMedicion(i)): #Las mediciones llevan el código del capítulo al que pertenecen.
            return False
        else:
            return es_codigo_capitulo_u_obra((i).first)

    @staticmethod
    def EsCapitulo(i):
        if EsCapituloUObra(i):
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
        if(EsCapituloUObra(i)): return False
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
        desc = ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod = (i).codigo
            if(es_codigo_capitulo(cod)): #Es un capítulo.
                j = BuscaCapitulo(cod)
                if j:
                    retval[(j).first]= (j).second
                else:
                    lmsg.error("Codigos.GetSubCaps; No se encontró el subcapítulo: " + cod + '\n')

            #else: #partidas del capítulo
            #lmsg.error("subcapítulo raro: " + cod + '\n')

        return retval

    def GetSubCapitulos(self, cods):
        retval= None
        for i in cods:
            retval.InsertaCods(GetSubCaps((i).second))
        return retval

    def GetSubElementos(self, ppal, elementos):
    #Devuelve los precios elementales del capitulo que se pasa como parámetro.
        retval= None
        desc = ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod = (i).codigo
            if(not es_codigo_capitulo(cod)): #No es un capítulo.
                j = elementos.find(cod)
                if j!=end():
                    retval[(j).first]= (j).second


        return retval

    def GetSubDescompuestos(self, ppal, descompuestos):
    #Devuelve los descompuestos del capitulo que se pasa como parámetro.
        retval= None
        desc = ppal.GetDesc(); #Obtiene la descomposición
        for i in desc:
            cod = (i).codigo
            if(not es_codigo_capitulo(cod)): #No es un capítulo.
                j = descompuestos.find(cod)
                if j!=end():
                    retval[(j).first]= (j).second


        return retval


    def InsertaReg(self, str_reg, verborrea, cont_mediciones):
        strtk= StrTok(str_reg)
        tipo = (strtk.get_token('|'))[0]
        cod = strtk.get_token('|')
        cod= q_car_d(cod,'\\'); #Quitamos la barra si está al final.

        if(tipo=='V' or tipo=='K' or tipo=='L' or
                tipo=='A' or tipo=='G' or tipo=='E'):
            if verborrea > 0:
                logging.info("Se ignora el registro de tipo " + tipo + ".\n")
            return

        if(len(cod)<1): return
        resto = strtk.resto()
        i = find(cod)
        if(not i):
            i= find(cod+'#')
            if(not i): #El registro no es de capítulo.
                i= find(cod+"##")
                if(not i): #El registro tampoco es de obra luego es nuevo.
                    if(tipo == 'M'): #El registro corresponde a una medición.
                        if(has_char(cod,'\\')): #A veces el registro ~M es de la forma: ~M|13.3.1#\01.009|1....
                            cod= copia_desde(cod,'\\') #aquí le quitamod la parte 13.3.1#\ al código.
                        cod= str(cont_mediciones) + '@' + cod

                    (self)[cod]= RegBC3(); #Lo damos de alta.
                    i= find(cod)

        if(tipo=='C'):
            (i).second.c= pc8TOlatin1(resto)
        elif(tipo=='D'):
            if len(resto)<2:
                if(verborrea>4): #No tiene porqué ser un error.
                    lmsg.error("Descomposición vacía en concepto: \'" + cod
                              + "\' se ignora la descomposición." + '\n')

            else:
                (i).second.d= resto
        elif(tipo=='T'):
            (i).second.t= pc8TOlatin1(resto)
        elif(tipo=='M'):
            (i).second.m= pc8TOlatin1(resto)
        elif(tipo=='Y'):
            (i).second.y= resto
        else:
            lmsg.error("Registro de tipo: " + tipo + " desconocido." + '\n')

    #not  @brief Devuelve el registro que corresponde a la obra.
    def GetObra(self):
        retval= None
        for i in self:
            if EsObra(i):
                retval[(i).first]= (i).second
        if not retval.size():
            lmsg.error("No se encontró el capítulo raíz." + '\n')
        return retval


    #not  @brief Devuelve un iterador al capítulo con el código que se pasa como parámetro.
    def BuscaCapitulo(self, cod):
        retval = find(cod); #Código
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
        elif EsCapitulo(i):
            return capitulo
        else:
            lmsg.error("No se encontró el tipo del concepto: '" + (i).first + "'\n")
            return sin_tipo



    #not  @brief Devuelve una cadena de caracteres que identifica el
    #not  tipo de concepto al que corresponde el registro.
    def StrTipoConcepto(self, i):
        retval= "sin_tipo"
        tipo = GetTipoConcepto(i)
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
    def GetCapitulos(self):
        retval= None
        for i in self:
            if EsCapitulo(i):
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


    #not  @brief Extrae las entidades que corresponden a mediciones
    def GetMediciones(self):
        retval= None
        for i in self:
            if EsMedicion(i):
                retval[(i).first]= (i).second
        logging.info("  leídas " + retval.size() + " mediciones." + '\n')
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
            j = find((i).first)
            if j: erase(j)



    #not  @brief Extrae las entidades que corresponden a unidades de obra
    def GetUdsObra(self, udsobra):
        retval= None
        for i in udsobra:
            Str= StrTok((i).first)
            scap = Str.get_token('\\')
            codud = Str.resto()
            j = find(codud)
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


    def GetDatosCapitulo(self, i):
        return reg_capitulo((i).first,(i).second.GetDatosCapitulo())


    def GetDatosMedicion(self, i):
        return reg_medicion((i).first,(i).second.GetDatosMedicion())


    def Print(self,os):
        for i in self:
            os.write("Código: " + (i).first + '\n'+ (i).second + '\n')
        return os

