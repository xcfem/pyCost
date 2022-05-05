# -*- coding: utf-8 -*-
#fiebdc3.py
'''Basic FIE BDC-3 utilities.'''

import logging

def es_codigo_obra(c):
    '''Returns true if c it's the code of a project.'''
    sz= len(c)
    if sz>1:
        return ((c[sz-2]=='#') and (c[sz-1]=='#'))
    else:
        return False

def es_codigo_capitulo(c):
    '''Returns true if c is a chapter code.'''
    retval= False
    sz= len(c)
    if es_codigo_capitulo_u_obra(c):
        if sz<2:
            retval= True; #Chapter without name.
        else:
            retval= (c[-2]!='#'); #Si no es obra, capítulo.
    return retval


def es_codigo_capitulo_u_obra(c):
    sz= len(c)
    if sz>0:
        return (c[-1]=='#')
    else:
        return False


def limpia_str(inputStr):
    retval= ''
    if(inputStr):
        retval= inputStr.replace(chr(10),'')
        retval= retval.replace(chr(13),'')
    return retval

class regBC3(object):
    def decod_bc3(self, strtk):
        logging.error('decod_bc3 not implemented.')
        return None
    def decod_str_bc3(self, Str):
        if(len(Str)>0):
            strtk= limpia_str(Str)
            self.decod_bc3(strtk)
            
    def Write(self, os):
        logging.error('Write not implemented.')


class regBC3_lista_reg(list, regBC3):
    def __init__(self, T, Str):
        ''' Constructor.
        
        :param T: object type.
        :param Str: string to decode.
        '''
        self.T= T
        if not (Str is None):
            self.decod_str_bc3(limpia_str(Str))
        
    def decod_bc3(self, strtk):
        ''' Decode the BC3 string argument.

        :param strtk: string to decode.
        '''
        if not strtk:
            return strtk # empty.
        else:
            lt= self.T(Str= None)
            for token in strtk:
                lt.decod_bc3(token)
                self.append(lt)
        return strtk
    
    def Write(self, os):
        for i in self:
            i.Write(os)

class regBC3_lista_med(regBC3_lista_reg):
        
    def decod_bc3(self, strtk):
        ''' Decode the BC3 string argument.

        :param strtk: string to decode.
        '''
        if not strtk:
            return strtk # empty.
        else:
            lt= self.T(Str= None)
            lt.decod_bc3(strtk)
            self.append(lt)
        return strtk
    
    def Write(self, os):
        for i in self:
            i.Write(os)



class regBC3_desc(regBC3):
    '''Element of a decomposition.

    :ivar codigo: Entity code
    :ivar factor: Entity factor
    :ivar productionRate: Entity output
    '''
    def __init__(self, Str):
        self.codigo= ''
        self.factor= 1.0 # factor defaults to 1.0
        self.productionRate= 0.0
        self.decod_str_bc3(limpia_str(Str))
        
    def decod_bc3(self, strtk):
        ''' decode tokens.'''
        tokens= strtk.split('\\')
        sz= len(tokens)
        if(sz>0): self.codigo= tokens[0]
        if(sz>1):
            token= tokens[1]
            if(len(token)>0): self.factor= float(token)
        if(sz>2):
            token= tokens[2]
            if(len(token)>0): self.productionRate= float(token)
        return strtk

    def isChapterOrObra(self):
        return (self.codigo.find("#")<self.codigo.leng.py())

    def isChapter(self):
        return es_codigo_capitulo(self.codigo)

    def EsObra(self):
        return es_codigo_obra(self.codigo)

    def Write(self, os):
        os.write(u"Código: " + self.codigo + '\n'
           + "Factor: " + str(self.factor) + '\n'
           + "Production rate: " + str(self.productionRate) + '\n')


class regBC3_d(regBC3_lista_reg):
    ''' ~D type BC3 record.'''
    def __init__(self, Str):
        ''' Constructor.'''
        super(regBC3_d, self).__init__(T= regBC3_desc, Str= Str)

    def decod_bc3(self, strtk):
        '''La cadena que se pasa es la que queda a la derecha
           #de ~D|'''
        strtk_lista_desc= strtk.split('|')
        super(regBC3_d,self).decod_bc3(strtk= strtk_lista_desc)
        return strtk
    
    def isChapter(r, nombres_capitulo):
        '''Return true if the records is a chapter.'''
        retval= r.isChapter()
        if not retval:
            retval= (nombres_capitulo.find(r.codigo+'#')!= nombres_capitulo.end())
        return retval
    
    def filterChapters(nombres_capitulo):
        '''Devuelve los elementos de la descomposición que son capítulos.'''
        retval= regBC3_d()
        for i in self:
            if isChapter(i,nombres_capitulo):
                retval.append(i)
        return retval
    
    def FiltraPrecios(nombres_capitulo):
        '''Devuelve los elementos de la descomposición que 
           son precios elementales o descompuestos.'''
        retval= regBC3_d()
        for i in self:
            if not isChapter(i,nombres_capitulo):
                retval.append(i)
        return retval


class MedArq(regBC3):
    '''Mensuration lines.

    :ivar lines: mensuration lines
    '''
    def decod_bc3(self, strtk):
        '''String decodification.'''
        self.lines= list()
        tokens= strtk.split('\\')
        while(len(tokens)>0):
            tipo= 0
            comentario= ''
            unidades= 1
            largo= 1
            ancho= 1
            alto= 1
            if(len(tokens)>0):
                tmp= tokens.pop(0)
                if(len(tmp)>0):
                    tipo= int(tmp)
            if(len(tokens)>0):
                comentario= tokens.pop(0)
            if(len(tokens)>0):
                tmp= tokens.pop(0)
                if(len(tmp)>0):
                    unidades= float(tmp)
            if(len(tokens)>0):
                tmp= tokens.pop(0)
                if(len(tmp)>0):
                    largo= float(tmp)
            if(len(tokens)>0):
                tmp= tokens.pop(0)
                if(len(tmp)>0):
                    ancho= float(tmp)
            if(len(tokens)>0):
                tmp= tokens.pop(0)
                if(len(tmp)>0):
                    alto= float(tmp)
            lineData= {'tipo':tipo, 'comentario':comentario, 'unidades':unidades, 'largo':largo, 'ancho':ancho, 'alto':alto}
            self.lines.append(lineData)
        return strtk
    
    def Write(self, os):
        for l in self.lines:
            os.write("Tipo: "+l['tipo']+ '\n'
               + "Comentario: " + l['comentario'] + '\n'
               + "Unidades: " + str(l['unidades']) + '\n'
               + "Largo: " + str(l['largo']) + '\n'
               + "Ancho: " + str(l['ancho']) + '\n'
               + "Alto: " + str(l['alto']) + '\n')


class regBC3_linea_med(regBC3):
    '''Mensuration line.

    :ivar tipo: type
        0 (Vacio en el archivo)
        1 Subtotal parcial
        2 Subtotal acumulado.
        3 El comentario es una fórmula.
    :ivar med: (MedArq) mensuration
    '''
    def __init__(self, Str):
        self.med= MedArq()
        self.decod_str_bc3(limpia_str(Str))
        
    def decod_bc3(self, strtk):
        return self.med.decod_bc3(strtk)
    
    def Write(self,os):
        med.Write(os)


class regBC3_ruta(list, regBC3):
    def decod_bc3(self, strtk):
        '''Decodes string.'''
        self.extend(strtk.split('\\'))
        return strtk
        
    def Chapters():
        return size()-1

    def Posicion(self):
        return self[-1]

    def Write(self,os):
        Str= "Chapter: "
        for i in range(0,Chapters()):
            os.write(Str + self[i] + '\n')
            Str= "Sub" + Str
        os.write(u"Posición: " + Posicion())

class regBC3_m(regBC3):
    '''FIEBDC-3 ~M record

    :ivar ruta: path Cap/subcap/subsubcap/.../posicion
    :ivar med: (MedArq) mensuration
    '''
    def __init__(self, strList):
        self.ruta= regBC3_ruta()
        self.ruta.decod_bc3(strList[0])
        self.med_total= float(strList[1])
        self.lista_med= regBC3_lista_med(T= regBC3_linea_med, Str= strList[2])
        #self.decod_str_bc3(limpia_str(strList[2]))

    def decod_bc3(self, strtk):
        '''Decodes string.
           La cadena que se pasa es la que queda a la derecha
           de ~M|
        '''
        strtk_ruta= strtk.get_token('|')
        self.ruta.decod_bc3(strtk_ruta)
        tmp= strtk.get_token('|')
        if(tmp):
            self.med_total= float(tmp)
        strtk_lista_med= strtk.get_token('|')
        self.lista_med.decod_bc3(strtk_lista_med)
        return strtk
    
    def Write(self,os):
        os.write("Ruta: ")
        self.ruta.Write(os)
        os.write('\n' + "Total: " + med_total + '\n')
        lista_med.Write(os)

class regBC3_c(regBC3):
    ''' FIEBDC ~C record.'''
    def __init__(self,Str):
        self.unidad= ''
        self.resumen= ''
        self.precio= 0.0
        self.tipo= 0
        self.decod_str_bc3(limpia_str(Str))
        
    def decod_bc3(self,strtk):
        '''Decodifica la cadena Str'''
        self.unidad= strtk.get_token('|')
        self.resumen= strtk.get_token('|')
        self.tmp= strtk.get_token('|')
        if tmp:
            self.precio= float(tmp)
        self.fecha= strtk.get_token('|')
        tmp= strtk.get_token('|')
        if tmp:
            self.tipo= int(tmp)
        return strtk
    
    def Write(self,os):
        os.write("Unidad: " + unidad + '\n'
           + "Resumen: " + resumen + '\n'
           + "Precio: " + precio + '\n'
           + "Fecha: " + fecha + '\n'
           + "Tipo: " + tipo + '\n')



class regBC3_t(regBC3):
    '''Corresponds to a ~T record of BC3.'''
    def __init__(self,Str):
        self.texto= ''
        if(Str):
            self.decod_str_bc3(limpia_str(Str[0]))
        
    def decod_bc3(self, strtk):
        '''Decodification.'''
        self.texto= strtk.split('|')[0]
        print('****** texto: ', self.texto)
        return strtk
    
    def Write(self,os):
        os.write("Texto: " + self.texto + '\n')

class regBC3_elemento(object):
    def __init__(self, c, t):
        ''' Constructor.

        :param c: concepto.
        :param t: texto.
        '''
        self.ccpto= c #Concepto.
        self.txt= t #Texto.

    def getTitle(self):
        return self.ccpto.resumen

    def Unidad(self):
        return self.ccpto.unidad

    def getPrice(self):
        return self.ccpto.precio

    def getType(self):
        return self.ccpto.tipo

    def Texto(self):
        return self.txt.texto

    def Write(self,os):
        self.ccpto.Write(os)
        self.txt.Write(os)


class regBC3_udobra(regBC3_elemento):
    def __init__(self,c,t,d):
        ''' Constructor.

        :param c: concepto.
        :param t: texto.
        :param d: components.
        '''        
        super(regBC3_udobra,self).__init__(c,t)
        self.desc= d # decompotion.
        
    def Write(self,os):
        super(regBC3_udobra,self).Write(os)
        desc.Write(os)

class regBC3_medicion(regBC3_elemento):
    def __init__(self,c,t,m):
        ''' Constructor.

        :param c: concepto.
        :param t: texto.
        :param m: measurements.
        '''        
        super(regBC3_medicion,self).__init__(c,t)
        self.med= m #Medicion.
        
    def Ruta(self):
        return self.med.ruta
    
    def Write(os):
        super(regBC3_medicion,self).Write(os)
        self.med.Write(os)

class regBC3_capitulo(regBC3_udobra):
    def __init__(self, c, t, d):
        ''' Constructor.

        :param c: concepto.
        :param t: texto.
        :param d: chapter components.
        '''        
        super(regBC3_capitulo,self).__init__(c,t,d)
        
    def filterChapters(self, nombres_capitulo):
        return self.desc.filterChapters(nombres_capitulo)

