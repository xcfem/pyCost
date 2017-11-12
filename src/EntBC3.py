#EntBC3.py
#Precio elemental.




#include <string>
#include <iostream>
#import bibXCBasica/src/texto/en_letra
import Codigos
import EntPyCost
import basic_types

tab = char(9)

def precio2str(d):
    return num2str(d,13)



''' TIPO: Tipo de concepto, se reservan los siguientes tipos: '''

''' 0 (Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales). '''

sin_clasif, mdo, maq, mat= range(0, 4)

def str2tipo_concepto(self, Str):
    if(len(Str)<1):
        return sin_clasif
    elif(Str[0]=='0'):
        return sin_clasif
    elif(Str[0]=='1'):
        return mdo
    elif(Str[0]=='2'):
        return maq
    elif(Str[0]=='3'):
        return mat
    else:
        return sin_clasif

def sint2tipo_concepto(self, si):
    if(si==0):
        return sin_clasif
    elif(si==1):
        return mdo
    elif(si==2):
        return maq
    elif(si==3):
        return mat
    else:
        return sin_clasif

def tipo_concepto2str(self, t):
    if(t==0):
        return "sin_clasif"
    elif(t==1):
        return "mdo"
    elif(t==2):
        return "maq"
    elif(t==3):
        return "mat"
    else:
        return "sin_clasif"
    return "sin_clasif"

class EntBC3(EntPyCost):
    static_txtud= ''
    static_texto_largo= ''
    def __init__(self, cod, tit):
      super(EntBC3,self).__init__()
      self.codigo= cod
      self.titulo= tit

    def LeeBC3(self, r):
        if verborrea>4:
            logging.info("Cargando concepto: '" + r.Codigo() + "'\n")
        codigo= r.Codigo()
        titulo= protege_signos(r.Datos().Titulo())

    def Codigo(self):
        return self.codigo

    def CodigoBC3(self):
        return self.Codigo()

    def Unidad(self):
        return self.static_txtud

    def Titulo(self):
        return titulo

    def StrPrecio(self):
        return precio2str(Precio())

    def StrPrecioLtx(self):
        return PrecioR().EnHumano()

    def StrPrecioEnLetra(self, genero):
        return PrecioR().EnLetra(genero)

    def Precio(self):
        return 0.0

    def PrecioR(self):
        return ppl_precio(Precio())

    def Fecha(self):
        return "040400";    # xxx

    def Tipo(self):
        return sin_clasif

    def TextoLargo(self):
        return self.static_texto_largo


    def ChrTipo(self):
        tp= self.Tipo()
        if(tp==sin_clasif):
            return '0'
        elif(tp==mdo):
            return '1'
        elif(tp==maq):
            return '2'
        elif(tp==mat):
            return '3'
        else:
            return '0'


    def EsPorcentaje(self):
        return codigo.find('%')<len(codigo)

    def WriteSpre(self, os):
        os.write(Codigo() + '|'
           + Unidad() + '|'
           + Titulo() + '|'
           + StrPrecio() + '|' + endl_msdos)

    def WriteConceptoBC3(self, os, primero):
        os.write("~C" + '|' + CodigoBC3())
        #if(primero) os.write('#'
        os.write('|' + Unidad() + '|'
           + latin1TOpc850ML(Titulo()) + '|'
           + StrPrecio() + '|'
           + Fecha() + '|'
           + ChrTipo() + '|' + endl_msdos)

    def Write(self, os):
        os.write("Codigo: " + Codigo() + '\n'
           + "Unidad: " + Unidad() + '\n'
           + "Titulo: " + Titulo() + '\n'
           + "Precio: " + StrPrecio() + '\n'
           + "Fecha: "  + Fecha() + '\n'
           + "Tipo: " + ChrTipo() + '\n'
           + "Texto largo: " + TextoLargo() + '\n')

    def Print(self,os):
        self.Write(os)
        return os

