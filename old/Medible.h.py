#Medible.h

#ifndef MEDIBLE_H
#define MEDIBLE_H

#include <string>
#include "EntBC3.h"
#include "Codigos.h"

#not  @brief Cosa que se mide (en m,kg,h,m2,m3,...)
class Medible: public EntBC3
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
