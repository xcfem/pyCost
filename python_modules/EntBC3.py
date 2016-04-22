#EntBC3.h
#Precio elemental.

#ifndef ENTBC3_H
#define ENTBC3_H

#include <string>
#include <iostream>
import bibXCBasica/src/texto/en_letra
import Codigos
import EntPyCost
import Tipos

 tab = char(9)

inline std.string precio2str( long double &d)
    return num2str(d,13)



''' TIPO: Tipo de concepto, se reservan los siguientes tipos: '''

''' 0 (Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales). '''

typedef enum {sin_clasif=0,mdo=1,maq=2,mat=3} tipo_concepto

def str2tipo_concepto(self, &str):
def sint2tipo_concepto(self, int &si):
def tipo_concepto2str(self, &):

class EntBC3(EntPyCost):
private:
    std.string codigo
    std.string titulo
    static  std.string txtud
    static  std.string txtl
public:
    EntBC3( std.string &cod, &tit)

    virtual  std.string &Codigo(void)
    std.string &Codigo(void)
    virtual std.string CodigoBC3(void)

    virtual  std.string &Unidad(void)
     std.string &Titulo(void)
    std.string &Titulo(void)

    virtual std.string StrPrecio(void)
    std.string StrPrecioLtx(void)
    std.string StrPrecioEnLetra( bool &genero)
    virtual long double Precio(void)
    virtual ppl_precio PrecioR(void)

    virtual std.string Fecha(void)
    virtual tipo_concepto Tipo(void)
    virtual  std.string &TextoLargo(void)
    virtual char ChrTipo(void)
    bool EsPorcentaje(void)

    template<class T>
    void LeeBC3( T &r)
    void EscribeSpre(std.ostream &os)
    void EscribeConceptoBC3(std.ostream &os, &primero= False)
    void Escribe(std.ostream &os)
    virtual ~EntBC3(void) {


template<class T>
def LeeBC3(self, &r):
    if verborrea>4:
        std.clog << "Cargando concepto: '" << r.Codigo() << "'\n"
    codigo= r.Codigo()
    titulo= protege_signos(r.Datos().Titulo())


std.ostream &operator<<(std.ostream &os, &e)

#endif
#EntBC3.cxx

import EntBC3

 std.string EntBC3.txtud= ""
 std.string EntBC3.txtl= ""

EntBC3.EntBC3( std.string &cod, &tit)
    : codigo(cod), titulo(tit) {
 std.string &EntBC3.Codigo(void)
    return codigo

std.string &EntBC3.Codigo(void)
    return codigo

def CodigoBC3(self, void):
    return Codigo()

 std.string &EntBC3.Unidad(void)
    return txtud

 std.string &EntBC3.Titulo(void)
    return titulo

std.string &EntBC3.Titulo(void)
    return titulo

def StrPrecio(self, void):
    return precio2str(Precio())

def StrPrecioLtx(self, void):
    return PrecioR().EnHumano()

def StrPrecioEnLetra(self, &genero):
    return PrecioR().EnLetra(genero)

long double EntBC3.Precio(void)
    return 0.0

def PrecioR(self, void):
    return ppl_precio(Precio())

def Fecha(self, void):
    return "040400";    # xxx

def Tipo(self, void):
    return sin_clasif

 std.string &EntBC3.TextoLargo(void)
    return txtl


def str2tipo_concepto(self, &str):
    if(str.length()<1) return sin_clasif
    if(str[0]=='0') return sin_clasif
    if(str[0]=='1') return mdo
    if(str[0]=='2') return maq
    if(str[0]=='3') return mat
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



def tipo_concepto2str(self, &t):
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


def ChrTipo(self, void):
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


def EsPorcentaje(self, void):
    if codigo.find('%')<codigo.length():
        return True
    else:
        return False


def EscribeSpre(self, &os):
    os << Codigo() << '|'
       << Unidad() << '|'
       << Titulo() << '|'
       << StrPrecio() << '|' << endl_msdos

def EscribeConceptoBC3(self, &os, &primero):
    os << "~C" << '|'
       << CodigoBC3()
    #if(primero) os << '#'
    os << '|'
       << Unidad() << '|'
       << latin1TOpc850ML(Titulo()) << '|'
       << StrPrecio() << '|'
       << Fecha() << '|'
       << ChrTipo() << '|' << endl_msdos

def Escribe(self, &os):
    os << "Codigo: " << Codigo() << std.endl
       << "Unidad: " << Unidad() << std.endl
       << "Titulo: " << Titulo() << std.endl
       << "Precio: " << StrPrecio() << std.endl
       << "Fecha: "  << Fecha() << std.endl
       << "Tipo: " << ChrTipo() << std.endl
       << "Texto largo: " << TextoLargo() << std.endl


std.ostream &operator<<(std.ostream &os, &e)
    e.Escribe(os)
    return os

