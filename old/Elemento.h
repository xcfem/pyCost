//Elemento.h

#ifndef ELEMENTO_H
#define ELEMENTO_H

#include "Medible.h"
#include "bibXCBasica/src/texto/latex.h"


class Elemento: public Medible
{
    long double precio;
    tipo_concepto tipo;
protected:
    void check_tipo(void) const;
public:
    Elemento( const std::string &cod="",const std::string &tit="",
              const std::string &ud="", const long double &p=0.0,
              const tipo_concepto &tp= sin_clasif);
    virtual tipo_concepto Tipo(void) const;
    long double Precio(void) const;
    void LeeBC3(const Codigos::reg_elemento &r);
    void ImprLtx(std::ostream &os) const;
};

#endif
