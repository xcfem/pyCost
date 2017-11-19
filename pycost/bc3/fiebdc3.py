# -*- coding: utf-8 -*-
#fiebdc3.py
'''Basic FIE BDC-3 utilities.'''



def es_codigo_obra(c):
    '''Returns true if c it's the code of a project.'''
    sz= len(c)
    if sz>1:
        return ((c[sz-2]=='#') and (c[sz-1]=='#'))
    else:
        return False

def es_codigo_capitulo(c):
    '''Returns true if c is a chapter code.'''
    retval = False
    sz = len(c)
    if es_codigo_capitulo_u_obra(c):
        if sz<2:
            retval= True; #Chapter without name.
        else:
            retval= (c[sz-2]!='#'); #Si no es obra, capítulo.

    return retval


def es_codigo_capitulo_u_obra(c):
    sz= len(c)
    if sz>0:
        return (c[sz-1]=='#')
    else:
        return False


def limpia_str(Str):
    return q_car(q_car(Str,char(10)),char(13))

class regBC3(object):
    def decod_bc3(self, strtk):
        lmsg.error('decod_bc3 not implemented.')
        return None
    def decod_str_bc3(self, Str):
        if Str:
            strtk= StrTok(limpia_str(Str))
            self.decod_bc3(strtk)
    def Write(self, os):
        lmsg.error('Write not implemented.')


class regBC3_lista_reg(list,regBC3):
    def __init__(self, Str):
        self.decod_str_bc3(limpia_Str(Str))
    def decod_bc3(strtk):
        if not strtk:
            return strtk #Empty.
        else:
            lt= T
            for token in strtk:
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
        self.factor= 1.0
        self.productionRate= 0.0
        self.decod_str_bc3(limpia_str(Str))
    def decod_bc3(self, strtk):
        ''' decode tokens.'''
        codigo= strtk.get_token('\\')
        tmp = strtk.get_token('\\')
        if tmp:
            factor= boost.lexical_cast<float>(tmp)
        if(factor==0.0): factor= 1.0 #As default factor=1.0
        tmp= strtk.get_token('\\')
        if tmp:
            productionRate= float(tmp)
        return strtk

    def isChapterOrObra(self):
        return (self.codigo.find("#")<self.codigo.leng.py())

    def isChapter(self):
        return es_codigo_capitulo(codigo)

    def EsObra(self):
        return es_codigo_obra(codigo)

    def Write(self, os):
        os.write("Código: " + codigo + '\n'
           + "Factor: " + Str(factor) + '\n'
           + "Production rate: " + str(productionRate) + '\n')


class regBC3_d(regBC3_lista_reg):
    ''' ~D type BC3 record.'''
    def __init__(self,Str):
        decod_str_bc3(limpia_str(Str))
    def decod_bc3(strtk):
        '''La cadena que se pasa es la que queda a la dere.pya
           #de ~D|'''
        strtk_lista_desc= strtk.get_token('|')
        regBC3_lista_reg.decod_bc3(strtk_lista_desc)
        return strtk
    def isChapter(r, nombres_capitulo):
        '''Return true if the records is a chapter.'''
        retval = r.isChapter()
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
    '''Mensuration.

    :ivar comentario: comment
    :ivar units: mensuration units
    :ivar largo: length
    :ivar ancho: width
    :ivar alto: height
    '''
    def decod_bc3(self, strtk):
        '''String decodification.'''
        self.comentario= ''
        self.unidades= 1
        self.largo= 1
        self.ancho= 1
        self.alto= 1
        self.comentario= strtk.get_token('\\')
        tmp = strtk.get_token('\\')
        if not tmp.empty():
            unidades= float(tmp)
        tmp= strtk.get_token('\\')
        if not tmp.empty():
            largo= float(tmp)
        tmp= strtk.get_token('\\')
        if not tmp.empty():
            ancho= float(tmp)
        tmp= strtk.get_token('\\')
        if not tmp.empty():
            alto= float(tmp)
        return strtk
    def Write(self, os):
        os.write("Comentario: " + comentario + '\n'
           + "Unidades: " + str(unidades) + '\n'
           + "Largo: " + str(largo) + '\n'
           + "Ancho: " + str(ancho) + '\n'
           + "Alto: " + str(alto) + '\n')


class regBC3_linea_med(regBC3):
    '''Mensuration line.

    :ivar tipo: type
        0 (Vacio en el ar.pyivo)
        1 Subtotal parcial
        2 Subtotal acumulado.
        3 El comentario es una fórmula.
    :ivar med: (MedArq) mensuration
    '''
    def __init__(self, Str):
        self.tipo= 0
        self.med= MedArq()
        self.decod_str_bc3(limpia_str(Str))
    def decod_bc3(strtk):
        tmp = strtk.get_token('\\')
        if tmp:
            tipo= int(tmp)
        return med.decod_bc3(strtk)
    def Write(self,os):
        os.write("Tipo: " + tipo + '\n')
        med.Write(os)


class regBC3_ruta(list,regBC3):
    def decod_bc3(strtk):
        '''Decodes string.'''
        StrTok.dq_campos.operator=(strtk.campos('\\'))
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
        os.write("Posición: " + Posicion())

class regBC3_m(regBC3):
    '''FIEBDC-3 ~M record

    :ivar ruta: path Cap/subcap/subsubcap/.../posicion
    :ivar med: (MedArq) mensuration
    '''
    def __init__(self,Str):
        ruta= regBC3_ruta()
        med_total= 0.0
        lista_med= regBC3_lista_reg
        decod_str_bc3(limpia_str(Str))

    def decod_bc3(strtk):
        '''Decodes string.
           La cadena que se pasa es la que queda a la derecha
           de ~M|
        '''
        strtk_ruta = strtk.get_token('|')
        ruta.decod_bc3(strtk_ruta)
        tmp = strtk.get_token('|')
        if tmp:
            med_total= float(tmp)
        strtk_lista_med = strtk.get_token('|')
        lista_med.decod_bc3(strtk_lista_med)
        return strtk
    def Write(self,os):
        os.write("Ruta: ")
        ruta.Write(os)
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
        self.tmp = strtk.get_token('|')
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



#not  @brief Corresponde a un registro ~T de BC3.
class regBC3_t(regBC3):
    def __init__(self,Str):
        self.texto= ''
        self.decod_str_bc3(limpia_str(Str))
    def decod_bc3(strtk):
        '''Decodification.'''
        self.texto= strtk.get_token('|')
        return strtk                 
    def Write(self,os):
        os.write("Texto: " + self.texto + '\n')

class regBC3_elemento(object):
    def __init__(self,c,t):
      self.ccpto= c #Concepto.
      self.txt= t #Texto.

    def Titulo(self):
        return self.ccpto.resumen

    def Unidad(self):
        return self.ccpto.unidad

    def Precio(self):
        return self.ccpto.precio

    def Tipo(self):
        return self.ccpto.tipo

    def Texto(self):
        return self.txt.texto

    def Write(self,os):
        self.ccpto.Write(os)
        self.txt.Write(os)


class regBC3_udobra(regBC3_elemento):
    def __init__(self,c,t,d):
        super(regBC3_udobra,self).__init__(c,t)
        self.desc= d #Descomposicion.
    def Write(self,os):
        super(regBC3_udobra,self).Write(os)
        desc.Write(os)

class regBC3_medicion(regBC3_elemento):
    def __init__(self,c,t,m):
        super(regBC3_medicion,self).__init__(c,t)
        self.med= m #Medicion.
    def Ruta(self):
        return self.med.ruta
    def Write(os):
        super(regBC3_medicion,self).Write(os)
        self.med.Write(os)

class regBC3_capitulo(regBC3_udobra):
    def __init__(self,c,t,d):
        super(regBC3_capitulo,self).__init__(c,t,d)
    def filterChapters(self,nombres_capitulo):
        return self.desc.filterChapters(nombres_capitulo)

