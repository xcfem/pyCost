#Elemento.cxx

#include "Elemento.h"

Elemento.Elemento( std.string &cod, &tit,
                    std.string &ud, double &p, &tp)
    : Medible(cod,tit,ud), precio(p), tipo(tp) {

def check_tipo(self, void):
    if not Codigo().empty():
        if tipo==sin_clasif and not EsPorcentaje():
            std.cerr << "El precio elemental de código: " << Codigo()
                      << " no es un porcentaje y su tipo está sin clasificar." << std.endl


def Tipo(self, void):
    return tipo

long double Elemento.Precio(void)
    return precio

def LeeBC3(self, &r):
    Medible.LeeBC3(r)
    precio= r.Datos().Precio()
    tipo= sint2tipo_concepto(r.Datos().Tipo())


def ImprLtx(self, &os):
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(Titulo()) << " & "
       << StrPrecioLtx() << "\\\\" << std.endl

