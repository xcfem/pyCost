#Medible.h

#ifndef MEDIBLE_H
#define MEDIBLE_H

#include <string>
import EntBC3
import Codigos

#not  @brief Cosa que se mide (en m,kg,h,m2,m3,...)
class Medible(EntBC3):
    std.string unidad
    std.string txt_largo
public:
    Medible( std.string &cod, &tit, &ud)
    virtual  std.string &TextoLargo(void)
    std.string &TextoLargo(void)
    virtual  std.string &Unidad(void)
    template<class T>
    void LeeBC3( T &r)
    void EscribeBC3(std.ostream &os)


template<class T>
def LeeBC3(self, &r):
    EntBC3.LeeBC3(r)
    unidad= r.Datos().Unidad()
    txt_largo= protege_signos(r.Datos().Texto())


#endif
#Medible.cxx

import Medible

#not  @brief Constructor.
Medible.Medible( std.string &cod, &tit, &ud)
    : EntBC3(cod,tit), unidad(ud), txt_largo("") {

 std.string &Medible.TextoLargo(void)
    return txt_largo


std.string &Medible.TextoLargo(void)
    return txt_largo


 std.string &Medible.Unidad(void)
    return unidad


def EscribeBC3(self, &os):
    EscribeConceptoBC3(os)
    if TextoLargo().length()>0:
        os << "~T|" << Codigo() << '|' << latin1TOpc850ML(TextoLargo()) << '|' << endl_msdos

