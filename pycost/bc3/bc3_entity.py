#EntBC3.py
#Precio elemental.

from pycost.bc3 import codes
from pycost.utils import EntPyCost as epc
from pycost.utils import basic_types
from decimal import Decimal

class EntBC3(epc.EntPyCost):
    static_txtud= ''
    static_texto_largo= ''
    def __init__(self, cod, tit):
      super(EntBC3,self).__init__()
      self.codigo= cod
      self.title= tit
      # if(type(tit) == str):
      #   self.title= tit.decode(encoding='utf-8')
      # else:
      #   self.title= tit

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

    def getPriceString(self):
        '''Return a string that represents the product.'''
        return self.formatString.format(self.getPrice())

    def getLtxPriceString(self):
        return self.getPriceString()

    def StrPriceToWords(self, genero):
        return basic_types.toWord(self.getRoundedPrice(),genero)

    def getPrice(self):
        return 0.0

    def getRoundedPrice(self):
        return Decimal(self.getPriceString())

    def Fecha(self):
        return "040400";    # xxx

    def getType(self):
        return basic_types.sin_clasif

    def getLongDescription(self):
        return self.static_texto_largo


    def ChrTipo(self):
        return basic_types.tipo_concepto2chr(self.getType())

    def isPercentage(self):
        return self.codigo.find('%')>0

    def WriteSpre(self, os):
        os.write(self.Codigo() + '|'
           + self.Unidad() + '|'
           + self.getTitle() + '|'
           + self.getPriceString() + '|' + '\n')

    def WriteConceptoBC3(self, os):
        os.write("~C" + '|' + self.CodigoBC3())
        os.write('|' + self.Unidad() + '|')
        os.write(self.getTitle() + '|')
        os.write(self.getPriceString() + '|')
        os.write(self.Fecha() + '|')
        os.write(self.ChrTipo() + '|\n')

    def Write(self, os):
        os.write("Codigo: " + Codigo() + '\n'
           + "Unidad: " + Unidad() + '\n'
           + "Title: " + getTitle() + '\n'
           + "Precio: " + getPriceString() + '\n'
           + "Fecha: "  + Fecha() + '\n'
           + "Tipo: " + ChrTipo() + '\n'
           + "Texto largo: " + self.getLongDescription() + '\n')

    def Print(self,os):
        self.Write(os)
        return os

