# -*- coding: utf-8 -*-
#CodigosObra.py

import logging
from pycost.bc3 import codes
from pycost.utils import EntPyCost as epc

class CodigosObra(epc.EntPyCost):
    def __init__(self):
        ''' Constructor.'''
        super(CodigosObra, self).__init__()
        self.caps= codes.Codigos() #capitulos.
        self.elementos= codes.Codigos()
        self.quantities= codes.Codigos()
        self.udsobr= codes.Codigos()
        self.resto= codes.Codigos()
        self.containers= [self.caps,self.elementos,self.quantities,self.udsobr,self.resto]
        self.codigos_capitulos= set()

    def GetDatosElementos(self):
        return elementos


    def GetDatosUnidades(self):
        return udsobr


    def GetDatosObra(self):
        return self.caps.GetObra()


    #not  @brief Devuelve los registros correspondientes a los capítulos
    #not  de la obra.
    def GetDatosCaps():
        return caps


    #not  @brief Devuelve los códigos de los capítulos de la obra.
    def getChapterCodes(self):
        return codigos_capitulos

    def ExisteConcepto(self, cod):
        '''Devuelve verdadero si existe el concepto 
           cuyo código se pasa como parámetro.'''
        retval= False
        for c in containers:
            if c.find(cod) != None:
              retval= True
              break
        return retval


    #not  @brief Devuelve una cadena de caracteres que identifica la
    #not  tabla en la que esta guardado el concepto.
    def StrTablaConcepto(self, cod):
        if self.caps.find(cod) != caps.end():
            return "capitulo"
        elif self.elementos.find(cod) != elementos.end():
            return "elementos"
        elif self.quantities.find(cod) != self.quantities.end():
            return "quantities"
        elif self.udsobr.find(cod) != udsobr.end():
            return "descompuestos"
        elif self.resto.find(cod) != resto.end():
            return "resto"
        else:
            return "ninguna"


    #@ brief Devuelve un iterador al concepto cuyo código se pasa como parámetro.
    def BuscaConcepto(self, cod):
        retval= None
        for c in containers:
            tmp= c.find(cod)
            if(tmp):
                retval= tmp
                break
        return retval

    def Trocea(self):
        '''Separa los registros según sean capítulos, quantities, 
           descompuestos, etc.
        '''
        obra= self.resto.GetObra(); #Obtiene los registros que corresponden a la obra.
        self.caps.InsertaCods(obra)
        #resto.Borra(obra)
        self.caps.update(self.resto.GetChapters())
        self.resto.Borra(self.caps)
        self.elementos= self.resto.GetElementos()
        self.resto.Borra(self.elementos)
        self.udsobr= self.resto.GetDescompuestos()
        self.resto.Borra(self.udsobr)
        if(len(self.resto)>0):
            logging.error("They left " + str(len(self.resto)) + ' not imported concepts.')
            logging.error(str(self.resto) + '\n')


        codigos_capitulos= self.caps.GetCodigos()


    def getChapterData(self, key):
        ''' Return the data of the chapter with the key argument.

        :param key: chapter codename.
        '''
        return self.caps.getChapterData(key)


    def readBC3(self, inputFile):
        ''' Read the remaining lines from BC3 and then calls the "Trocea"
            routine.

        :param inputFile: file to read from.
        '''
        reg= ""
        count= 0
        while(inputFile):
            reg= inputFile.readline()
            print(reg)
            if(len(reg)==0):
                break;
            else:
                if(reg[0]=='~'):
                    reg= reg[1:]
                count+= 1
                logging.info("Reading record: " + str(count) + '\n')
                reg= reg.replace(chr(13),'')
                reg= reg.replace('\n','')
                if len(reg)>2:
                    tipo= reg[0]
                    if(tipo == 'M'): # Quantities are directly inserted.
                        self.quantities.InsertaReg(reg, count)
                    else:
                        self.resto.InsertaReg(reg, count)

        inputFile.close()
        logging.info("  " + str(len(self.quantities)) + " quantities read." + '\n')
        self.Trocea()


    #not  @brief Devuelve los registros de la descomposicion que corresponden a
    #not  precios elementales.
    def FiltraElementales(self, descomp):
        return FiltraPrecios(descomp,elementos)


    #not  @brief Devuelve los registros de la descomposicion que corresponden a
    #not  precios descompuestos.
    def FiltraDescompuestos(self, descomp):
        return FiltraPrecios(descomp,udsobr)


    #not  @brief Devuelve los registros de la descomposicion que corresponden a los
    #not  precios que se pasan como parámetros.
    def FiltraPrecios(self, descomp, precios):
        retval= None
        for d in descomp:
            p= precios.find(d.codigo)
            if(p): #Encontró el precio
                retval[p.first]= p.second

        return retval


    #not  @brief Returns the quantities records.
    def getQuantityData(self):
        return self.quantities


    def BorraElementales(self, els):
        elementos.Borra(els)


    def BorraDescompuestos(self, uds):
        udsobr.Borra(uds)


    def Print(os):
        os.write("Obra: " + '\n' + self.GetDatosObra() + '\n'
           + u"Capítulos: " + '\n' + self.caps + '\n'
           + "Elementos:" + '\n' + '\n'
           + "Descompuestos:" + '\n' + self.udsobr + '\n'
           + basic_types.quantitiesCaption + ':\n' + self.quantities + '\n'
           + "Quedan: " + '\n' + self.resto + '\n')
        return os

