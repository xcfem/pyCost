#EntBC3.h
#Precio elemental.

#ifndef ENTBC3_H
#define ENTBC3_H

#include <string>
#include <iostream>
#include "bibXCBasica/src/texto/en_letra.h"
#include "Codigos.h"
#include "EntPpl.h"
#include "Tipos.h"

 tab = char(9)

inline std.string precio2str( long double &d)
    return num2str(d,13)



''' TIPO: Tipo de concepto, se reservan los siguientes tipos: '''

''' 0 (Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales). '''

typedef enum {sin_clasif=0,mdo=1,maq=2,mat=3} tipo_concepto

def str2tipo_concepto(self, &str):
def sint2tipo_concepto(self, int &si):
def tipo_concepto2str(self, &):

class EntBC3: public EntPpl
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


def LeeBC3(self, r):
    if self.verbosityLevel>4:
        std.clog << "Loading concept: '" << r.Codigo() << "'\n"
    codigo= r.Codigo()
    titulo= protege_signos(r.Datos().Titulo())


std.ostream &operator<<(std.ostream &os, &e)

#endif
