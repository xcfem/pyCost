#Elemento.h

#ifndef ELEMENTO_H
#define ELEMENTO_H

#include "Medible.h"
#include "bibXCBasica/src/texto/latex.h"


class Elemento: public Medible
    long double precio
    tipo_concepto tipo
protected:
    void check_tipo(void)
public:
    Elemento(  std.string &cod="", &tit="",
               std.string &ud="", double &p=0.0,
               tipo_concepto &tp= sin_clasif)
    virtual tipo_concepto Tipo(void)
    long double Precio(void)
    void LeeBC3( Codigos.reg_elemento &r)
    void ImprLtx(std.ostream &os)


#endif
