#EntBC3.py
#Precio elemental.




#include <string>
#include <iostream>
#import bibXCBasica/src/texto/en_letra
import Codigos
import EntPyCost
import basic_types

tab = char(9)

def std.string precio2str( long double &d):
    return num2str(d,13)



''' TIPO: Tipo de concepto, se reservan los siguientes tipos: '''

''' 0 (Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales). '''

typedef enum {sin_clasif=0,mdo=1,maq=2,mat=3} tipo_concepto

def str2tipo_concepto(self, str):
def sint2tipo_concepto(self, int &si):
def tipo_concepto2str(self):

class EntBC3(EntPyCost):
private:
    codigo= ''
    titulo= ''
    static  std.string txtud
    static  std.string texto_largo
public:
    EntBC3( cod, tit)

    def Codigo():
    Codigo()
    def std.string CodigoBC3():

    def Unidad():
     Titulo()
    Titulo()

    def std.string StrPrecio():
    std.string StrPrecioLtx()
    std.string StrPrecioEnLetra( bool &genero)
    def Precio():
    def ppl_precio PrecioR():

    def std.string Fecha():
    def tipo_concepto Tipo():
    def TextoLargo():
    def char ChrTipo():
    bool EsPorcentaje()

    template<class T>
     LeeBC3( T &r)
     WriteSpre(os)
     WriteConceptoBC3(os, primero= False)
     Write(os)
    virtual ~EntBC3() {


template<class T>
def LeeBC3(self, r):
    if verborrea>4:
        logging.info("Cargando concepto: '" + r.Codigo() + "'\n")
    codigo= r.Codigo()
    titulo= protege_signos(r.Datos().Titulo())


operator<<(os, e)


#EntBC3.cxx

import EntBC3

 std.string EntBC3.txtud= ""
 std.string EntBC3.texto_largo= ""

EntBC3.EntBC3( cod, tit)
    : codigo(cod), titulo(tit) {
 EntBC3.Codigo()
    return codigo

EntBC3.Codigo()
    return codigo

def CodigoBC3(self):
    return Codigo()

 EntBC3.Unidad()
    return txtud

 EntBC3.Titulo()
    return titulo

EntBC3.Titulo()
    return titulo

def StrPrecio(self):
    return precio2str(Precio())

def StrPrecioLtx(self):
    return PrecioR().EnHumano()

def StrPrecioEnLetra(self, genero):
    return PrecioR().EnLetra(genero)

long double EntBC3.Precio()
    return 0.0

def PrecioR(self):
    return ppl_precio(Precio())

def Fecha(self):
    return "040400";    # xxx

def Tipo(self):
    return sin_clasif

 EntBC3.TextoLargo()
    return texto_largo


def str2tipo_concepto(self, Str):
    if(len(Str)<1) return sin_clasif
    if(Str[0]=='0') return sin_clasif
    if(Str[0]=='1') return mdo
    if(Str[0]=='2') return maq
    if(Str[0]=='3') return mat
    return sin_clasif


def sint2tipo_concepto(self, int &si):
    switch(si)
    case 0:
        return sin_clasif
    case 1:
        return mdo
    case 2:
        return maq
    case 3:
        return mat
    default:
        return sin_clasif



def tipo_concepto2str(self, t):
    switch(t)
    case 0:
        return "sin_clasif"
    case 1:
        return "mdo"
    case 2:
        return "maq"
    case 3:
        return "mat"
    default:
        return "sin_clasif"

    return "sin_clasif"


def ChrTipo(self):
    switch(Tipo())
    case sin_clasif:
        return '0'
    case mdo:
        return '1'
    case maq:
        return '2'
    case mat:
        return '3'
    default:
        return '0'


def EsPorcentaje(self):
    if codigo.find('%')<len(codigo):
        return True
    else:
        return False


def WriteSpre(self, os):
    os.write(Codigo() + '|'
       + Unidad() + '|'
       + Titulo() + '|'
       + StrPrecio() + '|' + endl_msdos

def WriteConceptoBC3(self, os, primero):
    os.write("~C" + '|'
       + CodigoBC3()
    #if(primero) os.write('#'
    os.write('|'
       + Unidad() + '|'
       + latin1TOpc850ML(Titulo()) + '|'
       + StrPrecio() + '|'
       + Fecha() + '|'
       + ChrTipo() + '|' + endl_msdos

def Write(self, os):
    os.write("Codigo: " + Codigo() + '\n'
       + "Unidad: " + Unidad() + '\n'
       + "Titulo: " + Titulo() + '\n'
       + "Precio: " + StrPrecio() + '\n'
       + "Fecha: "  + Fecha() + '\n'
       + "Tipo: " + ChrTipo() + '\n'
       + "Texto largo: " + TextoLargo() + '\n'


operator<<(os, e)
    e.Write(os)
    return os

