#EntBC3.py
#Precio elemental.




#include <string>
#include <iostream>
#import bibXCBasica/src/texto/en_letra
from pycost.bc3 import codes
from pycost.utils import EntPyCost as epc
from pycost.utils import basic_types

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

class EntBC3(epc.EntPyCost):
    static_txtud= ''
    static_texto_largo= ''
    def __init__(self, cod, tit):
      super(EntBC3,self).__init__()
      self.codigo= cod
      if(type(tit) == str):
        self.title= unicode(tit,encoding='utf-8')
      else:
        self.title= tit

    def LeeBC3(self, r):
        if verborrea>4:
            logging.info("Cargando concepto: '" + r.Codigo() + "'\n")
        self.codigo= r.Codigo()
        self.title= protege_signos(r.Datos().getTitle())

    def Codigo(self):
        return self.codigo

    def CodigoBC3(self):
        return self.Codigo()

    def Unidad(self):
        return self.static_txtud

    def getTitle(self):
        return self.title

    def StrPrecio(self):
        return precio2str(Precio())

    def StrPrecioLtx(self):
        return basic_types.human_readable(self.PrecioR())

    def StrPriceToWords(self, genero):
        return basic_types.toWord(self.PrecioR(),genero)

    def Precio(self):
        return 0.0

    def PrecioR(self):
        return basic_types.ppl_price(self.Precio())

    def Fecha(self):
        return "040400";    # xxx

    def Tipo(self):
        return sin_clasif

    def getLongDescription(self):
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


    def IsPercentage(self):
        return self.codigo.find('%')<len(self.codigo)

    def WriteSpre(self, os):
        os.write(Codigo() + '|'
           + Unidad() + '|'
           + getTitle() + '|'
           + StrPrecio() + '|' + endl_msdos)

    def WriteConceptoBC3(self, os, primero):
        os.write("~C" + '|' + CodigoBC3())
        #if(primero) os.write('#'
        os.write('|' + Unidad() + '|'
           + latin1TOpc850ML(getTitle()) + '|'
           + StrPrecio() + '|'
           + Fecha() + '|'
           + ChrTipo() + '|' + endl_msdos)

    def Write(self, os):
        os.write("Codigo: " + Codigo() + '\n'
           + "Unidad: " + Unidad() + '\n'
           + "Title: " + getTitle() + '\n'
           + "Precio: " + StrPrecio() + '\n'
           + "Fecha: "  + Fecha() + '\n'
           + "Tipo: " + ChrTipo() + '\n'
           + "Texto largo: " + self.getLongDescription() + '\n')

    def Print(self,os):
        self.Write(os)
        return os

